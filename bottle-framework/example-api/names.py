import re
import json

from bottle import request
from bottle import response
from bottle import post, get, put, delete

_names = set()
namepattern = re.compile(r'^[a-zA-Z\d]{1,64}$')

@post('/names')
def creation_handler():
    '''Handles name creation'''

    try:
        #parse input data
        try:
            data = request.json
        except:
            raise ValueError

        if data is None:
            raise ValueError
            
        #extract and validate the name
        try:
            if namepattern.match(data['name']) is None:
                raise ValueError
            name = data['name']
        except (TypeError, KeyError):
            raise ValueError

        #check if the name exists on our list
        if name in _names:
            raise KeyError

    except ValueError:
        #bad data, return 400
        response.status = 400
        return
    except KeyError:
        #name exists, return 409
        response.status = 409
        return
    #add the name
    _names.add(name)
    #return a 200 success status
    response.headers['Content-Type'] = 'application/json'
    return json.dumps({'name': name})

@get('/names')
def listing_handler():
    '''Handles name listing'''
    
    response.headers['Content-Type'] = 'application/json'
    response.headers['Cache-Control'] = 'no-cache'
    return json.dumps({'names': list(_names)})

@put('/names/<oldname>')
def update_handler(oldname):
    '''Handles name updates'''
    
    try:
        try:
            data = request.json
            #data = json.load(utf8reader(request.body))
        except:
            raise ValueError

        #extract and validate the new name
        try:
            if namepattern.match(data['name']) is None:
                raise ValueError
            newname = data['name']
        except (TypeError, KeyError):
            raise ValueError

        #if the name updating doesn't exist
        if oldname not in _names:
            raise KeyError(404)
        #if the newname already exists
        if newname in _names:
            raise KeyError(409)

    except ValueError:
        response.status = 400
        return
    except KeyError as e:
        response.status = e.args[0]
        return
    #remove the old name and add the new name
    _names.remove(oldname)
    _names.add(newname)
    #return 200 success
    response.headers['Content-Type'] = 'application/json'
    return json.dumps({'name': newname})

@delete('/names/<name>')
def delete_handler(name):
    '''Handles name deletions'''
    try:
        #check if name exists
        if name not in _names:
            raise KeyError
    except:
        response.status = 404
        return
    
    #remove the name
    _names.remove(name)
    #returning nothing presents a 200 status
    return
