 # From socket library, import everyhing
from socket import *

# Server host address
serverHost = '127.0.0.1' 
# Server port number
serverPort = 8081        
clientSocket = socket(AF_INET, SOCK_STREAM)
# Connect to Host and Port
clientSocket.connect((serverHost, serverPort)) 

# Input filename
filename = input("Masukkan nama file yang ingin dicari: ") 

# Template for file request
request = "GET /" + filename + " HTTP/1.1\r"  
#Send request and encode
clientSocket.send(request.encode()) 

# Blank string to unify message response
response = "" 

while True:
    #Collect data with maximum size 1024 bytes and decode it from client Socket
    data = clientSocket.recv(1024).decode()  
    if not data:
        # if it's not data we looking for then stop the loop
        break       
    # Every data on loop will be merged in response variable
    response += data    

# print string from response variable
print(response)     

# Close client Socket
clientSocket.close()
