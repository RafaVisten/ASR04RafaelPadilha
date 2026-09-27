from socket import *
from constCS import *

import threading
import time
from datetime import timedelta

def parseCompute(data, conn):
    # convert data back to expression
    expr = bytes.decode(data).split()

    # parse and compute expression
    try:
        num1 = int(expr[0])
        num2 = int(expr[1])

        if expr[2] == 'add':
            ans = num1 + num2
        elif expr[2] == 'sub':
            ans = num1 - num2
        elif expr[2] == 'mult':
            ans = num1 * num2
        elif expr[2] == 'div':
            ans = num1 / num2
        else:
            raise ValueError
    except:
        ans = 'faulty expression. try again'

    print("answer provided: " + str(ans))

    # return answer
    conn.sendall(str.encode(str(ans)))

    # close the connection
    conn.close()


s = socket(AF_INET, SOCK_STREAM)

s.bind((HOST, PORT))
s.listen(MAX_REQUESTS)

threads = []
start = time.time()

# start one thread for each request
for i in range(MAX_REQUESTS):

    conn, addr = s.accept()

    t = threading.Thread(
        target=parseCompute,
        args=(conn.recv(1024), conn)
    )

    threads.append(t)
    t.start()

# wait for all threads to finish
for t in threads:
    t.join()

end = time.time()
elapsed = end - start

print("Tempo processamento e resposta: "+str(timedelta(seconds=elapsed)))

s.close()