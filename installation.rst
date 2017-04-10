============
Installation
============
1. Install git::

	$ yum install git

2. Install dependency softwares::

        $ yum install gcc libffi-devel python-devel

3. Install http://github.com/skyrings/skyring-tools from the source code::

	$ git clone https://github.com/skyrings/skyring-tools.git

4. Install skyring-tools::

	$ cd skyring-tools
	$ python setup.py install

5. Run::

	$ skyring-password-reset

6. Restart skyring server::

 	$  service skyring restart
