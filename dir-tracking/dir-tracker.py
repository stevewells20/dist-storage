# import cPickle
import pickle
import os
import zlib

# filelist = os.listdir()
# for el in filelist:
#     file = open(el).read().encode()
#     # print(file)
#     # checksum = zlib.adler32()
#     print(el, os.path.getmtime(el), zlib.adler32(file))


class DirTracker(object):
    def __init__(self, path):
        self.path = path
        self.files = {}

    def scan(self):
        os.chdir(self.path)
        filelist = os.listdir()
        for el in filelist:
            if not (os.path.isfile(el)): continue

            creation_time = os.path.getmtime(el)

            file = open(el).read().encode()
            checksum = zlib.adler32(file)

            self.files[el] = (creation_time, checksum)

        print(self.files.keys())

d = DirTracker("./")
d.scan()

    # def save(self):

# with open('company_data.pkl', 'wb') as output:
#     company1 = DirTracker('banana', 40)
#     pickle.dump(company1, output, pickle.HIGHEST_PROTOCOL)
#
#     company2 = DirTracker('spam', 42)
#     pickle.dump(company2, output, pickle.HIGHEST_PROTOCOL)
#
# del company1
# del company2
#
# with open('company_data.pkl', 'rb') as input:
#     company1 = pickle.load(input)
#     print(company1.name)  # -> banana
#     print(company1.value)  # -> 40
#
#     company2 = pickle.load(input)
#     print(company2.name) # -> spam
#     print(company2.value)  # -> 42
