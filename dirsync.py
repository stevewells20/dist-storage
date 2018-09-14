from server import FileServer



s = FileServer()

# s.run()
print(s.getIP())
print(s.getMAC())
print(s.IP)
print(s.MAC)

# while True:
#     conn, addr = s.accept()     # Establish connection with client.
#     print ('Got connection from', addr)
#     data = conn.recv(1024)
#     print('Server received', repr(data))
#
#     filename='mytext.txt'
#     f = open(filename,'rb')
#     l = f.read(1024)
#     while (l):
#        conn.send(l)
#        print('Sent ',repr(l))
#        l = f.read(1024)
#     f.close()
#
#     print('Done sending')
#     conn.send('Thank you for connecting'.encode('utf-8'))
#     conn.close()
