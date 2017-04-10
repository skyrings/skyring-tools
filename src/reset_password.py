import bcrypt
import getpass
import pymongo
import json
import traceback
from bson.binary import Binary

CONF_FILE = "/etc/skyring/skyring.conf"

def read_config_file():
    json_data=open(CONF_FILE).read()
    data = json.loads(json_data)
    return data["dbconfig"]

def connect_db(dbconfig):
    client = pymongo.MongoClient(dbconfig['hostname'])
    db = getattr(client, dbconfig['database'])
    db.authenticate(dbconfig['user'], dbconfig['password'])
    return db

def main():
    try:
        dbconfig = read_config_file()
        db = connect_db(dbconfig)
        password = getpass.getpass('Enter new password:')
        password_hashed = bcrypt.hashpw(password, bcrypt.gensalt())
        hash = Binary(password_hashed)
        db.skyring_session_store.remove()
        db.skyringusers.update_one(
            {"username": "admin"},
            {
                "$set": {
                    "hash": hash,
                }
            }
        )
        print "Password is changed successfully"
    except(IOError,
           ValueError,
           KeyError,
           pymongo.errors.OperationFailure) as ex:
        traceback.print_exc('nn')
        print "Unable to change password"

if __name__ == "__main__":
    main()

