#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File: remove_CR_LF.py
Author: Gene Jiang
Email: zhengrong.jiang@chiefclouds.com
Github: https://github.com/yourname
Description: 
"""
import codecs
import csv

dst_file = r"C:\Users\Administrator\Desktop\CSS_ENDUSER\CSS_ENDUSER_20180630_0.dat"
test_file = r"C:\Users\Administrator\Desktop\CSS_ENDUSER\CSS_ENDUSER_20180630_fix.dat"

with codecs.open(dst_file, 'r', encoding='utf-8') as fo,\
     codecs.open(test_file, 'w', encoding='utf-8') as fnew:
    reader = csv.reader(fo, delimiter=',')
    dataset = []

    for line in reader:
        new_line = []
        for item in line:
            mid_item = item.replace("\n", "")
            new_line.append(mid_item)
        dataset.append(new_line)
        print(new_line)
    for sub_list in dataset:
        writer = csv.writer(fnew, quoting=csv.QUOTE_ALL)
        writer.writerow(sub_list)

