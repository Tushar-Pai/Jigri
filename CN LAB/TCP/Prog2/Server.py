from socket import *
serverName="127.0.0.1"
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind((serverName,serverPort))
serverSocket.listen(2)
while 1:
    print('Server is ready to receive : ')
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()
    print('File Name received')
    word = connectionSocket.recv(1024).decode()
    print('Word name is received')
    count=0
    with open(sentence, "r") as f:
        for line in f:
            w=line.split()
            for i in w:
                if(i==word):
                    count=count+1
    connectionSocket.send(str(count).encode())
    print ('\nCount Send')
    connectionSocket.close()