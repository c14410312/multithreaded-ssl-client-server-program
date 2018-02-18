import socket, ssl

def main():
    
    SERVERIP = "127.0.0.1"
    PORT = 8000

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SERVERIP, PORT))

    #ssl_sock = ssl.wrap_socket(client, 
    #                           ca_certs="server.crt",
    #                           cert_reqs=ssl.CERT_REQUIRED)
    #ssl_sock.connect((SERVERIP, PORT))
    #print(repr(ssl_sock.getpeername()))
    #ssl_sock.write(bytes('Hello from client', 'ascii'))

    client.sendall(bytes("This is from the client", 'ascii'))

    while True:
        
        inc_data = client.recv(1024)
        #inc_data = ssl_sock.read()
        print("Server says {}".format(inc_data.decode()))
        print("enter any key to stay connected or enter 'exit' to disconnect)")
        out_data = input()
        #ssl_sock.write(bytes(out_data, 'ascii'))
        client.sendall(bytes(out_data, 'ascii'))
        if out_data == 'exit':
            break
    client.close()


if __name__ in '__main__':
    main()
