#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys
import os
import codecs


def check_file(file_path, read_code='utf_8_sig'):
    dir_name = os.path.dirname(file_path)
    new_file_name = os.path.splitext(os.path.basename(file_path))[0] \
                    + '_error.csv'
    new_file_path = dir_name + os.sep + new_file_name
    print(new_file_path)

    with codecs.open(file_path, 'rb', read_code) as fr, \
            codecs.open(new_file_path, 'w', read_code) as fw:

        fw.write("start check " + file_path)
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
            if len(line) < 16:
                # 如果是空行，或者当前行最后一个字符不是双引号
                error_line = error_line + 1
                print(file_path + " line: " + str(i))
                fw.write(file_path + '  line:' + str(i) + '\n')
                print(line)
                fw.write(line + '\n')

            i = i + 1
        fw.write('Total error line: ' + str(error_line))


def read_dir(dir_path, ext, read_code):
    for (root, dirs, files) in os.walk(dir_path):
        print(dirs)

        for filename in files:
            if filename[-len(ext):] == ext:
                check_file(os.path.join(root, filename), read_code)
        for dir_name in dirs:
            read_dir(os.path.join(root, dir_name), ext, read_code)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("usage: idfa_imei_quality dir_path ext read_code")
        exit(1)
    read_dir(sys.argv[1], sys.argv[2], sys.argv[3])
    print("done")
