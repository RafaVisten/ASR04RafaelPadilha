from socket  import *
from constCS import * 

s = socket(AF_INET, SOCK_STREAM) 
s.bind((HOST, PORT))  
s.listen(1)           

(conn, addr) = s.accept()                       # returns new socket and addr. client 

while True:

  data = conn.recv(1024)                        # receive data from client
  if not data: break                            # stop if client stopped

  expr = bytes.decode(data).split()             # convert data back to expression

                                                # parse and compute expression
  try:
    num1, num2 = int(expr[0]), int(expr[1])

    if expr[2] == 'add': ans = num1 + num2
    elif expr[2] == 'sub': ans = num1 - num2
    elif expr[2] == 'mult': ans = num1 * num2
    elif expr[2] == 'div': ans = num1 / num2
    else: raise ValueError
  except:
    ans = 'faulty expression. try again'

  print("answer provided: "+str(ans))

  conn.send(str.encode(str(ans)))               # return answer

conn.close()                                    # close the connection
