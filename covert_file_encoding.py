#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File: covert_file_encoding.py
Author: Gene Jiang
Email: zhengrong.jiang@chiefclouds.com
Github: https://github.com/yourname
Description: 
"""
import sys
import codecs


def covert_file_encode(src_file, dst_file,
                       src_file_encoding='gb18030', dst_file_encoding='utf-8'):
    """
    covert the encoding of file from chinese to utf-8
    :param src_file: file name with whole path
    :param dst_file: file name with whole path
    :param src_file_encoding: encoding of the src_file
    :param dst_file_encoding: encoding of the dst_file
    :return:
    """

    with codecs.open(src_file, 'r', src_file_encoding) as fi,\
            codecs.open(dst_file, 'w', dst_file_encoding)as fo:

        while 1:
            line = fi.readline()
            if line == '':
                print('end')
                break
            fo.write(line)


if __name__ == '__main__':
    if len(sys.argv) !=5:
        print("Usage: convert_file_encoding.py "
              "src_file dst_file src_file_encoding dst_file_encoding")
        print("Example: convert_file_encoding.py test.csv new.csv gb18030 utf-8")
        exit(1)
    covert_file_encode(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    print('Done')
