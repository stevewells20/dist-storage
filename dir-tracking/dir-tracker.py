#!/usr/bin/python3
# import cPickle

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
        # normpath strips any trailing slashes, basename returns dirname
        self.dirName = os.path.basename(os.path.normpath(path))
        self.files = {}

    def scan(self):
        os.chdir(self.path)
        filelist = os.listdir()
        for el in filelist:

            if not (os.path.isfile(el)): continue

            modified_time = os.path.getmtime(el)

            file = open(el).read().encode()
            checksum = zlib.adler32(file)

            self.files[el] = (modified_time, checksum)

        print(self.files.keys())
        print(self.files)

if __name__ == "__main__":
    d = DirTracker("./")
    d.scan()
