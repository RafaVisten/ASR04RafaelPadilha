# experimento original (single-threaded)

from socket  import *
from constCS import *

import random
import time
from datetime import timedelta

def generateData():
    num1 = random.randint(0, 100)
    num2 = random.randint(1, 100) # to avoid division by zero
    op = random.choice(["add", "sub", "mult", "div"])
    
    return str(num1) + " " + str(num2) + " " + op

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT))                                 # connect to server (block until accepted)

start = time.time()

for i in range(MAX_REQUESTS):
    data_to_send = generateData()                       # expression to send
    s.send(str.encode(data_to_send))                    # send some data
    data = s.recv(1024)                                 # receive the response
    print (bytes.decode(data))                          # print the result

end = time.time()
elapsed = end - start

print("Tempo total cliente: "+str(timedelta(seconds=elapsed)))
    
s.close()                                               # close the connection
