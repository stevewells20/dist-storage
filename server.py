import socket
import os
import pickle


class FileServer:

    def __init__(self, ):

        # rootDir = '.'
        # for dirName, subdirList, fileList in os.walk(rootDir):
        #     print('Found directory: %s' % dirName)
        #     for fname in fileList:
        #         print('\t%s' % fname)


        print("Setting port to 5999")
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

    def getIP(self):
        import socket
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        self.IP = s.getsockname()[0]
        return self.IP

    def getMAC(self):
        from subprocess import Popen, PIPE
        import re
        # IP = "1.2.3.4"
        IP = self.IP
        # The time between ping and arp check must be small, as ARP may not cache long
        pid = Popen(["arp", "-n"], stdout=PIPE)
        s = pid.communicate()[0].decode()
        mac = re.search(r"(([a-f\d]{1,2}\:){5}[a-f\d]{1,2})", s).groups()[0]
        self.MAC = mac
        return self.MAC

    def addFolder(folderPath):


    # def save(self, dirName, Object):
        # with open('company_data.pkl', 'wb') as output:
        #     company1 = DirTracker('banana', 40)
        #     pickle.dump(company1, output, pickle.HIGHEST_PROTOCOL)
        #
        #     company2 = DirTracker('spam', 42)
        #     pickle.dump(company2, output, pickle.HIGHEST_PROTOCOL)
        #
        # del company1
        # del company2

    # def load(self, dirName):
        # with open(dirName + '.pkl', 'rb') as input:
        #     tracker = pickle.load(input)
        #     print(company1.name)  # -> banana
        #     print(company1.value)  # -> 40
        #
        #     company2 = pickle.load(input)
        #     print(company2.name) # -> spam
        #     print(company2.value)  # -> 42


print("Done")
