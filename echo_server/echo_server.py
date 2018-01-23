
import socket
import threading

SERVER_HOST = '0.0.0.0'
SERVER_PORT = 4760 # use one of your assigned ports instead
SERVER_ADDR = (SERVER_HOST, SERVER_PORT)

class HandlerThread(threading.Thread):
    """TODO write docstring!"""

    def __init__(self, client, address):
        """constructor"""
        threading.Thread.__init__(self)
        self.client = client
        self.address = address

    def run(self):
        """thread code"""
        print('executing thread for client {}'.format(address))
        data = self.client.recv(4096)
        print('received {} of length {}'.format(data, len(data)))
        self.client.send(data)
        print('sent echo back')
        self.client.shutdown(socket.SHUT_RDWR)
        self.client.close()

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
connection.bind(SERVER_ADDR)
connection.listen(10)

while True:
    client, address = connection.accept()
    th = HandlerThread(client, address)
    th.start()

