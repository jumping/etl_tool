#!/usr/bin/env python
# -*- coding:utf-8 -*-


import sys
import os
import codecs


def remove_wrapping_lines(filePath, fromCode='utf_8_sig', toCode='utf-8'):
    """
    将csv文件中的内容中换行符转为\n，并转换编码保存
    常用编码类型:
    gb18030: 中文编码
    utf_8: 常用的utf8编码
    utf_8_sig: utf8 with bom
    """

    fr = codecs.open(filePath, 'rb', fromCode)
    fw = codecs.open(filePath+'.'+'csv', 'wb', toCode)
    # 当前行是否未结束的标记，默认False代表正常结束
    needAppend = False
    # 完整行内容变量
    res = ''
    while True:
        # 读取一行
        line = fr.readline()

        # 如果文件内容结束
        if not line:
            if needAppend:
                fw.write(res+'\n')
            break
        
        # 去除前后空格和行尾换行符
        line = line.strip()

        if needAppend:
            # 如果上一次循环标记行未结束，则把本次循环读取行内容附加到上一行后面
            res += line+'\\n'
        else:
            # 否则正常读取本行内容
            res = line
        
        if res[-1:] == '"':
            # 如果当前行尾最后一个字符是双引号，认为是正常结束，标记符设置为False，并写入文件
            needAppend = False
            print(res)
            fw.write(res+'\n')
        else:
            # 否则标记行未完成，等待下一个循环附加下一行内容
            needAppend = True


def read_dir(dir_path, ext, fromCode='utf-8', toCode='utf-8'):
    for (root, dirs, files) in os.walk(dir_path):
        print(dirs)

        for filename in files:
            if filename[-len(ext):] == ext:
                remove_wrapping_lines(os.path.join(root, filename),
                                      fromCode, toCode)
        for dir_name in dirs:
            remove_wrapping_lines(os.path.join(root, dir_name), ext,
                                  fromCode, toCode)


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("usage: removern.py dirpath ext fromCode toCode ")
        exit(1)
    read_dir(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    print("done")
