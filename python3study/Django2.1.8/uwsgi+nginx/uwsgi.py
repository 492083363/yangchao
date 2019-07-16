#/bin/python
#conding=utf-8

def application(env,start_response):
    start_response('200 ok'm[('Content-Type','text/html')])
    return [b"Hello World"]
    