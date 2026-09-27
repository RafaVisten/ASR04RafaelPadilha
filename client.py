from socket  import *
from constCS import *

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT))                                 # connect to server (block until accepted)

data_to_send = input("int int add/sub/mult/div: ")      # expression to send

s.send(str.encode(data_to_send))                        # send some data
data = s.recv(1024)                                     # receive the response
print (bytes.decode(data))                              # print the result
s.close()                                               # close the connection
