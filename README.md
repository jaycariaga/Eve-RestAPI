# Eve-RestAPI
contains code that is supposed to run REST API commands POST, GET, PUT, and DELETE
<br>Main site that helped the most: https://docs.python-eve.org/en/stable/quickstart.html

# Current State
so far client.py works but currently trying to get mongodb to work properly to get the localhost to run. 
<br>Problem: once running a GET command on the localhost to return a JSON on a resource, an "Internal Server Error occurs".
Mongodb has been solved in a way that an instance running to a data/db folder
<br>
# Begin by setting up Eve
$ pip install eve

# Set up MongoDB (via linux)
follow instructions on 'https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/'.
<br> //Next step is to start it. <br> Use: $ sudo service mongod start 
<br> $ mongodb --dbpath ~/path/to/.../data/db    

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
<br>Within that terminal, an output should contain a JSON of the resources mentioned in settings.py
<br>To create a specific list of the schema details of a resource, do "curl -i http://localhost:5000/resource"

# Info on client.py
Client.py is a seperate file that contains code that works with another server that is NOT a localhost.  This code manages to
use Eve and utilize API's like DELETE for ridding of the original resources and POST to create a new object of that specific resources. In the meantime, this server also allows the user to use curl commands on another linux terminal to GET the resources as well.
