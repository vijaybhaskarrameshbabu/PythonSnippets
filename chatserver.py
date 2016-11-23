import socket
import time

host = '127.0.0.1'
port = 8080

clients = []

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host,port))
s.setblocking(0)

quitting = False

print ("Server started")

while not quitting:
    try:
        data, addr = s.recvfrom(1024)
        modifiedMessage,server = s.recvfrom(message.decode('utf-8'))
        if "Quit" in str(data):
            quitting = True
        if addr not in Clients:
            clients.append(addr)

        print (time.ctime(time.time())+ str(addr)+ "::" + str(data))

        for client in clients:
            s.sendto(data,client)

    except:
        pass

s.close()

