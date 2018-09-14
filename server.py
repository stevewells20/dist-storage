import socket
import os

class FileServer:

    def __init__(self):

        rootDir = '.'
        for dirName, subdirList, fileList in os.walk(rootDir):
            print('Found directory: %s' % dirName)
            for fname in fileList:
                print('\t%s' % fname)

        try:
            self.port = PORT
        except:
            print("PORT not defined, setting port to 5999")
            self.port = 5999

        self.s = socket.socket()             # Create a socket object
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.host = socket.gethostname()     # Get local machine name
        self.s.bind((self.host, self.port))            # Bind to the port
        self.s.listen(5)                     # Now wait for client connection.
        print ('Server listening....')


    def run(self):

        while True:
            self.conn, self.addr = self.s.accept()     # Establish connection with client.
            print ('Got connection from', self.addr)
            self.data = self.conn.recv(1024)
            print('Server received', repr(self.data))

            self.filename='mytext.txt'
            self.f = open(self.filename,'rb')
            l = self.f.read(1024)
            while (l):
               self.conn.send(l)
               print('Sent ',repr(l))
               l = self.f.read(1024)
            self.f.close()

            print('Done sending')
            self.conn.send('Thank you for connecting'.encode('utf-8'))
            self.conn.close()

print("Done")
