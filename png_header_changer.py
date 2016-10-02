#!/usr/bin/env python
# -*- coding: utf-8 -*-
import mmap
import sys


__author__ = 'namh'
__version__ = '1.0.0'
__contact__ = 'gaedduck@gmail.com'


class PngHeaderModifier:


    def __init__(self, image_path):

        """

        @type image_path: path
        """
        self.image = image_path

        self.__change_mark__(image_path)

    def __change_mark__(self, fname):
        with open(fname, 'r+b') as fd:
            self.__data__ = mmap.mmap(fd.fileno(), 0, access=mmap.ACCESS_WRITE)

            existing_name = "Photoshop"
            sidx = 0x3d
            eidx = sidx + len(existing_name)
            #self.__data__[sidx:eidx].replace(existing_name, "namhunhop");
            self.__data__[sidx:eidx] = "namhunhop";







if __name__ == '__main__':

    if len(sys.argv) < 2:
        print "file name is needed"
    else:
        filename = sys.argv[1]
        PngHeaderModifier(filename)




