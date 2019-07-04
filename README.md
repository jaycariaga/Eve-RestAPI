# Eve-RestAPI
contains code that is supposed to run REST API commands POST, GET, PUT, and DELETE

# Current State
so far client.py works but currently trying to get mongodb to work properly to get the localhost to run.

# Begin by setting up Eve
$ pip install eve

# Set up MongoDB (via linux)
follow instructions on 'https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/'.
<br> Next step is to start it. <br> Use: $ sudo service mongod start 
<br> Then $ mongo


# Development version of Eve
$ git clone http://github.com/pyeve/eve.git
Initialized empty Git repository in ~/dev/eve/.git/
To activate Eve:
$ . venv/bin/activate

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
  Within that terminal, an output should contain a JSON of the resources mentioned in settings.py

# Info on client.py
Client.py is a seperate file that contains code that works with another server.  This code manages to
HTTP delete the original resources and POST a new set of resources. In the meantime, this server also allows the user to use
curl to GET the resources as well.
