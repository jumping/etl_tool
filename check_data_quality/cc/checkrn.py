#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
import os
import codecs

# gbk gb18030


def checkFile(filePath, readCode='utf_8_sig'):
    dir_name = os.path.dirname(filePath)
    new_file_name = os.path.splitext(os.path.basename(filePath))[0] \
                    + '_error.csv'
    new_file_path = dir_name + os.sep+new_file_name
    print(new_file_path)

    with codecs.open(filePath, 'rb', readCode) as fr, \
        codecs.open(new_file_path, 'w', readCode) as fw:

        fw.write("start check " + filePath)
        i = 0
        error_line = 0
        while True:
            # 读取一行
            line = fr.readline()
            # 如果文件内容结束
            if not line:
                break
            # 去除前后空格和行尾换行符
            line = line.strip()

            # if not line or line[-1:] != '"':
            if not line:
                # 如果是空行，或者当前行最后一个字符不是双引号
                error_line = error_line + 1
                print(filePath+" line: "+str(i))
                fw.write(filePath + '  line:' + str(i) + '\n')
                print(line)
                fw.write(line + '\n')

            i = i+1
        fw.write('Total error line: ' + str(error_line))


def readDir(dirPath, ext, readCode):
    for (root, dirs, files) in os.walk(dirPath):
        print(dirs)

        for filename in files:
            if filename[-len(ext):] == ext:
                checkFile(os.path.join(root, filename),readCode)
        for dirname in dirs:
            readDir(os.path.join(root, dirname),ext,readCode)


if __name__ == "__main__":
    if len(sys.argv) != 4 :
        print("usage: checkrn.py dirpath ext readcode")
        exit(1)
    readDir(sys.argv[1], sys.argv[2], sys.argv[3])
    print("done")
