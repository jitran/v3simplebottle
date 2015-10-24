__author__ = 'spousty'


from bottle import route, run
import socket

@route('/')
def index():
    return "<h1>[%]: hello OpenShift Ninja</h1>" % (socket.gethostname())

if __name__ == '__main__':
    run(host='0.0.0.0', port=8080)
