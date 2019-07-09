# Eve-RestAPI
contains code that is supposed to run REST API commands POST, GET, PUT, and DELETE
<br>Main site that helped the most: https://docs.python-eve.org/en/stable/quickstart.html
<br>The most important part of this is to make sure three terminals run: <b>for mongod, for python run.py, and the last to complete API commands (POST, GET, DELETE, PATCH ...) <b>

# References to Possible Questions
1) So far client.py works but currently trying to get mongodb to work properly to get the localhost to run. 
<br>Problem: once running a GET command on the localhost to return a JSON on a resource, an "Internal Server Error occurs".
Mongodb has been solved in a way that an instance running to a data/db folder
<br>SOLUTION: Fix the authentication in Settings.py by removing the lines involving usernames and passwords and setting authentication on the dbname.
2) If the mongod --dbpath ~/path/.../ command does not work: create a data/db/ within ur target path and rerun.
3) For API commands besides GET, it is better to use "http://127.0.0.1:5000/" for the url.


# Begin by setting up Eve
$ pip install eve

# Set up MongoDB (via linux)
follow instructions on 'https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/'.
<br> //Next step is to start it. <br> Use: $ sudo service mongod start 
<br> $ mongodb --dbpath ~/path/to/.../data/db    

# Installing Development version of Eve
$ git clone http://github.com/pyeve/eve.git
Initialized empty Git repository in ~/dev/eve/.git/
<br>To activate Eve:
<br>$ . venv/bin/activate
<br>$ cd eve
<br>$ virtualenv venv
<br>New python executable in venv/bin/python
<br>$ . venv/bin/activate
<br>$ python setup.py install
<br>...
Finished processing dependencies for Eve


# Run GET
Make sure an INSTANCE of mongod (for linux) is running in one terminal.
<br>In another terminal, type: "python run.py". This records successes/failures of accessing API's.
<br>In another terminal, type: "curl -i http://localhost:5000/", or "curl -i http://127.0.0.1:5000/".
<br>Within that terminal, an output should contain a JSON of the list of resources mentioned in settings.py
<br>To create a specific list of the objects' schema details, do "curl -i http://localhost:5000/resource"

# Info on client.py
Client.py is a seperate file that contains code that works with another server that is NOT a localhost.  This code manages to
use Eve and utilize API's like DELETE for ridding of the original resources and POST to create a new object of that specific resources. In the meantime, this server also allows the user to use curl commands on another linux terminal to GET the resources as well.
