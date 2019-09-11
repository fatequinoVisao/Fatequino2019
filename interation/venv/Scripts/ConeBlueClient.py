import sys
from bluetooth import *


def client(host, port):
    s = BluetoothSocket(RFCOMM)

    s.connect((host, port))

    while True:
        message = raw_input('Send:')
        if not message: return
        s.send(message)
        data = s.recv(1024)
        print
        'Received', (data)
    s.close()

client(sys.argv[1], 8888)