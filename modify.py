import sys

import json
import random
import requests

#entry point variable represents the url WITHOUT the 'http://'
ENTRY_POINT = '127.0.0.1:5000'


def post_people():
    people = [
	#examples of adding an object(s) to a resource       
	{
            'firstname': 'John',
            'lastname': 'Doe',
            'role': ['author'],
            'location': {'address': '422 South Gay Street', 'city': 'Auburn'},
            'born': 'Thu, 27 Aug 1970 14:37:13 GMT'
        },
        {
            'firstname': 'Serena',
            'lastname': 'Love',
            'role': ['author'],
            'location': {'address': '363 Brannan St', 'city': 'San Francisco'},
            'born': 'Wed, 25 Feb 1987 17:00:00 GMT'
        },
        {
            'firstname': 'Mark',
            'lastname': 'Green',
            'role': ['copy', 'author'],
            'location': {'address': '4925 Lacross Road', 'city': 'New York'},
            'born': 'Sat, 23 Feb 1985 12:00:00 GMT'
        },
        {
            'firstname': 'Julia',
            'lastname': 'Red',
            'role': ['copy'],
            'location': {'address': '98 Yatch Road', 'city': 'San Francisco'},
            'born': 'Sun, 20 Jul 1980 11:00:00 GMT'
        },
        {
            'firstname': 'Anne',
            'lastname': 'White',
            'role': ['contributor', 'copy'],
            'location': {'address': '32 Joseph Street', 'city': 'Ashfield'},
            'born': 'Fri, 25 Sep 1970 10:00:00 GMT'
        },
    ]

    r = perform_post('people', json.dumps(people))
    print "'people' posted", r.status_code

    valids = []
    if r.status_code == 201:
        response = r.json()
        if response['_status'] == 'OK':
            for person in response['_items']:
                if person['_status'] == "OK":
                    valids.append(person['_id'])

    return valids


def post_works(ids):
    works = []
    for i in range(28):
        works.append(
            {
                'title': 'Book Title #%d' % i,
                'description': 'Description #%d' % i,
                'owner': random.choice(ids),
            }
        )

    r = perform_post('works', json.dumps(works))
    print "'works' posted", r.status_code


def perform_post(resource, data):
    headers = {'Content-Type': 'application/json'}
    return requests.post(endpoint(resource), data, headers=headers)

#below function essentially WIPES OUT all items from the collection
def delete():
    r = perform_delete('people')
    print "'people' deleted", r.status_code
    r = perform_delete('works')
    print "'works' deleted", r.status_code


def perform_delete(resource):
    return requests.delete(endpoint(resource))


def endpoint(resource):
    return 'http://%s/%s/' % (
        ENTRY_POINT if not sys.argv[1:] else sys.argv[1], resource)

#works
def checkdeleteitem(resource, ident, etag):
    r = delitem(resource, ident, etag)
    print r.status_code

def delitem(resource, ident, etag): 
    url_ = "%s%s/" % (endpoint(resource), ident)
    print url_ #checking for correct url
    return requests.delete(url_, headers = {"IF-MATCH": etag}) #can use global configs in headers

#works and returns whole endpoint
def get_people(resource):
    print '%s' % (requests.get(endpoint(resource)).json()) #we need .json() for formatting

#works when we use .json()
def get_person(resource, ident):
    print '%s' % ((requests.get(endpoint(resource)+ident)).json())

#works
def patching(resource, ident, etag, change):
    url_ = "%s%s/" % (endpoint(resource), ident)
    return requests.patch(url_, json=change , headers = {"IF-MATCH": etag})
#json={"firstname" : "blah"} is an example of second param

def checkput(resource, ident, etag, changes):
    out = put(resource, ident, etag, changes)
    print "'put' status: ", out.status_code

def put(resource, ident, etag, changes):
    url_ = "%s%s/" % (endpoint(resource), ident)
    
    return requests.put(url_, json = changes, headers = {"IF-MATCH": etag})

#REMEMBER: patch and put is an updater, so the etag always changes after!
""" The running code below contain samples of my function calls that involve 
multiple important REST API's: POST, GET, DELETE, PATCH, and PUT.
The get_people function prints all items of a resource, while get_person gets a specific person based on 
specifying identification. Delete, Patch, and Put work differently in that they require an IF-MATCH header."""
if __name__ == '__main__':
    #checkdeleteitem('people','5d2e37d85d1da9dedaae26ab', 'c7844155ef09f7ff5a957c45eb75955f650fc8bb') 
    #deleting an item REQUIRES id and not the unique variable of 'lastname'!

    #get_people('people')

    #get_person('people', 'Doe') #can use either lastname 'Doe' or the id of that item

    #patching('people', '5d2e37d85d1da9dedaae26ab', '5ef1599d4b66578d6f2c76ae0f0dbfc3027bfe7f', {"firstname": 'chance'})

    #checkput('people', '5d2e37d85d1da9dedaae26ad', '2b32dd3a178770f28e78876d4e922965490ec1fc', {
    #        'firstname': 'Mark',
    #        'lastname': 'Red', #lastname is a unique-schema so it CANT be changed...must specify that it stays the same or put wont work
    #        'role': ['copy', 'author'],
    #        'location': {'address': '4925 Lacross Road', 'city': 'New York'},
    #        'born': 'Sat, 23 Feb 1985 12:00:00 GMT'
    #    })
    #get_people('people')
    
    #code below came from a tutorial that deletes both resources and replaces it with defaults using DELETE and POSTS...
    delete()
    ids = post_people()
    post_works(ids)
