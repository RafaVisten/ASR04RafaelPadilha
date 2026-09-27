from socket import *
from constCS import *
import threading

import random
import time
from datetime import timedelta

def generateData():
    num1 = random.randint(0, 100)
    num2 = random.randint(1, 100) # to avoid division by zero
    op = random.choice(["add", "sub", "mult", "div"])
    
    return str(num1) + " " + str(num2) + " " + op

def request(data):
    # open connection
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((HOST, PORT))

    # send data
    s.sendall(str.encode(data))

    # obtain and print response
    response = s.recv(1024)
    print(bytes.decode(response))

    # close connection
    s.close()

threads = []
start = time.time()

# start one thread for each request
for i in range(MAX_REQUESTS):
    data_to_send = generateData()

    t = threading.Thread(target=request, args=(data_to_send,))

    threads.append(t)
    t.start()

# wait for all threads to finish
for t in threads:
    t.join()

end = time.time()
elapsed = end - start

print("Tempo total cliente: "+str(timedelta(seconds=elapsed)))