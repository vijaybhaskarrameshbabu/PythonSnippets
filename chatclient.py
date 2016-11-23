import socket
import threading

import time

tlock = threading.Lock()
shutdown = False #Tells the thread to shutdown when the program exits



def receiving(name,sock):
 while not shutdown:
     try:
         tlock.acquire()
         while True:
             data, addr = s.recvfrom(1024)
             
             print (str(data))

     except:
        pass

     finally:
        tlock.release()

host = '127.0.0.1'
port = 0

server = ('127.0.0.1','8080')

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((host,port))
s.setblocking(0)

rT = threading.Thread(target=receiving, args=("RecvThread", s))
rT.start()

alias = input("Enter your name:")
message = input(alias +"->")
messageencoded = message.encode('utf-8')

while message != 'q':
    if message!= '':
        data = alias + ":"+ message
        s.sendto(data.encode('utf-8'),server)
    tlock.acquire()
    message = input(alias + "->")
    tlock.release()
    time.sleep(0.2)

shutdown = True

rT.join()
s.close()

