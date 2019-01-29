#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys,codecs

#gbk gb18030
def covertFile(filePath,fromCode='gb18030',toCode='utf-8'):

    """
    文件编码转换
    常用编码类型:
    gb18030: 中文编码
    utf_8: 常用的utf8编码
    utf_8_sig: utf8 with bom
    """

    fr = codecs.open(filePath,'rb',fromCode)
    fw = codecs.open(filePath+'.'+toCode,'wb',toCode)
    while True:
        line = fr.read(4096)
        if not line:
            break
        fw.write(line)

if __name__ == "__main__":
    if len(sys.argv)==1:
        print("usage: gb2utf8.py file1path")
        exit(1)
    covertFile(sys.argv[1])