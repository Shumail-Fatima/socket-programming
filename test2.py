import socket             
 
s = socket.socket()         
 
port = 12345               
 
s.connect(('192.168.18.155', port)) 
 
print (s.recv(1024).decode())

msg = str(input("enter string = "))
s.send(msg.encode()) 

print (s.recv(1024).decode())

s.close()  