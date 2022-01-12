# 5. Create two process which can exchange messages and interact with each other. 
# Implement the code for connection-oriented service where the client sends the 
# filename to the server. Server searches for the file and sends back the count 
# of lines and words in that file along with the contents of the file. Display 
# the same on the client terminal.


from socket import *
serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
sentence = input("\nEnter file name: ")
clientSocket.send(sentence.encode())
lines = clientSocket.recv(1024).decode()
words = clientSocket.recv(1024).decode()
contents = clientSocket.recv(1024).decode()
print("The number of lines : ")
print(lines)
print("The number of words : ")
print(words)
print("Contents of file \n ")
print(words)
clientSocket.close()