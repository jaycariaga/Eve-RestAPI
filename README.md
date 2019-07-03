# Eve-RestAPI
contains code that is supposed to run REST API commands POST, GET, PUT, and DELETE

# Begin by setting up Eve
$ pip install eve

# Development version of Eve
$ git clone http://github.com/pyeve/eve.git
Initialized empty Git repository in ~/dev/eve/.git/

$ cd eve
$ virtualenv venv
New python executable in venv/bin/python

$ . venv/bin/activate
$ python setup.py install
...
Finished processing dependencies for Eve

# Run GET
In one terminal, type: "python run.py".
In another terminal, type: "curl -i http://localhost:5000/". 

