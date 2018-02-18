import socket, threading, ssl

class ClientThread(threading.Thread):
    
    def __init__(self, clientAddress, clientSocket):
        threading.Thread.__init__(self)
        self.csocket = clientSocket
        self.caddress = clientAddress
        print("New connection added: ", clientAddress)


    def run(self):

        print("Connection from a client: {}".format(self.caddress))
        msg = ''

        while True:

            data = self.csocket.recv(1024)
            msg = data.decode('ascii')

            if msg=='exit':
                break

            print("Clients at address: {}, message is: {}".format(self.caddress, msg))
            self.csocket.send(bytes('Hi {} you are connected to the MTserver!'.format(self.caddress), 'ascii'))

        print("client at {} disconnected".format(self.caddress))


def main():
    LH = "127.0.0.1"
    port = 8000
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((LH, port))
    print("The server has been started")
    print("Waiting to connect with a client")

    while True:
        server.listen(1)
        clientSock, clientAddr = server.accept()
        #wrap the socket in SSL

        #ssl_client_sock = ssl.wrap_socket(clientSock,
        #                                 server_side=True,
        #                                certfile='server.crt',
        #                               keyfile='server.key')
        
        newThread = ClientThread(clientAddr, clientSock)
        newThread.start()


if __name__ in '__main__':
    main()
