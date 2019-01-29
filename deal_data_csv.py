#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File: deal_data_csv.py
Author: Gene Jiang
Email: zhengrong.jiang@chiefclouds.com
Github: https://github.com/yourname
Description: 
"""

import csv
import os


def access_files(file_path):
    for temp_file_path, dirs, files in os.walk(file_path):
        csv_files = [file for file in files if file.split('.')[-1] == 'csv']
        file_w_path = [os.path.join(file_path, file) for file in files]
        print(csv_files)
        print(file_w_path)


def deal_with_csv_file(csv_file, dst_file, error_file, delimiter_counter):
    data_set = []
    data_set_error = []

    with open(csv_file, 'r', encoding='utf-8', newline='') as fi, \
         open(dst_file, 'w', encoding='utf-8', newline='')as fo, \
         open(error_file, 'w', encoding='utf-8', newline='') as fe:

        reader = csv.reader(fi, delimiter=',')

        for line in reader:
            print(line)
            new_line = [item for item in line]
            if len(line) >= delimiter_counter:
                data_set.append(new_line)
            else:
                data_set_error.append(new_line)

        for sub_item in data_set:
            writer = csv.writer(fo)
            writer.writerow(sub_item)

        for sub_item_error in data_set_error:
            print(sub_item_error)
            writer = csv.writer(fe)
            writer.writerow(sub_item_error)


if __name__ == "__main__":
    access_files(r'D:\genejiang2012_baidu\000_BigData\000_Testing\002_Proj_Qinyuan\Data\DataCleaning\sript')

    # csv_file = 'twechat.csv'
    # dst_file = 'twechat_correct.csv'
    # error_file = 'twechat_error.csv'
    # delimiter_counter = 21
    # deal_with_csv_file(csv_file, dst_file, error_file, delimiter_counter)
    # print('Done....')






