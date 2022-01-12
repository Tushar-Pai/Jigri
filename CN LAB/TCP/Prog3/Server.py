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
    contents = open(sentence,"r")
    l=contents.read()
    number_of_lines = 0
    number_of_words = 0
    with open(sentence, "r") as f:
        for line in f:
            line = line.strip("\n")
            words = line.split()
            number_of_lines += 1
            number_of_words += len(words)
    connectionSocket.send(str(number_of_lines).encode())
    connectionSocket.send(str(number_of_words).encode())
    connectionSocket.send(l.encode())
    print ('\nCount Send')
    connectionSocket.close()

