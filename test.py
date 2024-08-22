import socket             
s = socket.socket()         
print ("Socket successfully created")
 
port = 12345               
 
s.bind(('192.168.18.155', port))         
print ("socket binded to %s" %(port)) 
 
s.listen(5)     
print ("socket is listening")            
 
while True: 
  c, addr = s.accept()     
  print ('Got connection from', addr )
 
  c.send('Thank you for connecting'.encode()) 

  temp = int(c.recv(1024).decode())
  y = [int(d) for d in str(temp)]
  print (y)
  sum = 0

  while (len(y) != 1):
    for i in range(len(y)):
        sum = sum + y[i]

    y.clear()
    y = [int(d) for d in str(sum)]

    print (sum)
    ans = sum
    print (y)
    sum = 0

  c.send(str(ans).encode())

  c.close()
   
  break