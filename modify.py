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
def delitem(resource, ident, etag): 
    url_ = "%s%s/" % (endpoint(resource), ident)
    print url_ 
    return requests.delete(url_, headers = {"IF-MATCH": etag}) #can use global configs in headers

#works and returns whole endpoint
def get_people(resource):
    print '%s' % (requests.get(endpoint(resource)).json()) #we need .json() for formatting

#works when we use .json()
def get_person(resource, ident):
    print '%s' % ((requests.get(endpoint(resource)+ident)).json())

	


if __name__ == '__main__':
    delitem('people','5d2e37d85d1da9dedaae26aa', '7a5a701ee5a0acba6bf27ca1a3094ee6effdca6d')
    #get_people('people')
    #get_person('people', 'Doe') #can use either lastname 'Doe' or the id of that item

    #from previous known code
    #delete()
    #ids = post_people()
    #post_works(ids)
