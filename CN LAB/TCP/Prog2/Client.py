# Using TCP/IP sockets, write a client-server program to make client sending the file name
# and a word and the server to search for the presence of the word in the file and return the
# number of times the word being repeated in the file contents back to client.


from socket import *
serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
sentence = input("\nEnter file name: ")
word= input("\nEnter word: ")
clientSocket.send(sentence.encode())
clientSocket.send(word.encode())
wordtimes = clientSocket.recv(1024).decode()
print ('\nWord Occured : ')
print(wordtimes)
clientSocket.close()