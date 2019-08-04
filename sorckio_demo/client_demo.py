# coding: utf-8
"""
__auter__ == 'blx'
"""
import socketio
print(socketio.__version__)

sio = socketio.Client()

@sio.event
def connection():
    print('connect established')

@sio.event
def my_message(data):
    print('message received with ', data)
    sio.emit('my response', {'response': 'my response'})

@sio.event
def disconnect():
    print('disconnected from server')


sio.connect('http://localhost:5000')
sio.wait()






