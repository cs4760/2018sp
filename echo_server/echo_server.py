
import socket

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
connection.bind(('0.0.0.0', 4760))
connection.listen(10)

while True:
    client, address = connection.accept()
    data = client.recv(4096)
    print('received {} of length {}'.format(data, len(data)))
    client.send(data)
    print('sent echo back')
    client.shutdown(socket.SHUT_RDWR)
    client.close()


