#!/usr/bin/env python

from bottle import route, run, error

@route('/app/<myid:int>')
def provide(myid):
    return "Object with id {} returned".format(myid)

@error(404)
def error404(error):
    return '404 - the requested page could not be found'   

run(host='localhost', port=8080, debug=True)
