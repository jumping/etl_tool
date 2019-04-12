#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File: mysql_connection.py
Author: Gene Jiang
Email: genejiang2012@outlook.com
Github: https://github.com/genejiang2012
Description: python class to access the mysql
"""

from collections import OrderedDict
from pymysql import connect, cursors


class MySQL(object):
    """
        Python class for connecting with mysql server and accelerate development
        project using mysql, 
        Extremely easy to learn and use, friendly construction.
    """

    def __init__(self, host='localhost', port=3306, user='root',
                 password='', database=''):
        self.__host = host
        self.__port = port
        self.__user = user
        self.__password = password
        self.__database = database

    def __open(self):
        try:
            cnn = connect(self.__host,
                          self.__user,
                          self.__password,
                          self.__database)
            self.__connection = cnn
            self.__session = cnn.cursor()
        except Exception as e:
            print("Error connection %d: %s" % (e.args[0], e.args[1]))

    def __close(self):
        self.__session.close()
        self.__connection.close()

    def select(self, table, where=None, *args, **kwargs):
        """
        query the data from table with only one condition
        :param table: the table name
        :param where: condition
        :param args: show the columns
        :param kwargs: condition prameters
        :return:

        Example:
            conditional_query = 'car_make = %s '
            result = connect_mysql.select('car', conditional_query,
            'id_car', 'car_text', car_make='nissan')
        """
        result = None
        query = 'SELECT '
        keys = args
        values = tuple(kwargs.values())
        length = len(keys) - 1

        for i, key in enumerate(keys):
            query += "`" + key + "`"
            if i < length:
                query += ","

        query += ' FROM {}'.format(table)

        if where:
            query += " WHERE {}".format(where)

        print(query)

        self.__open()
        self.__session.execute(query, values)
        number_rows = self.__session.rowcount
        number_columns = len(self.__session.description)

        if number_rows >= 1 and number_columns > 1:
            result = [item for item in self.__session.fetchall()]
        else:
            result = [item[0] for item in self.__session.fetchall()]

        self.__close()

        return result

    def select_advanced(self, sql, *args):
        """
        query the data with more than one condition
        :param sql: the sql sentence
        :param args: the condition
        :return: one list with query data

        Example:
        sql_query = 'SELECT C.cylinder FROM car C WHERE C.car_make = %s
            AND C.car_model = %s'
        result = connect_mysql.select_advanced(sql_query,
            ('car_make', 'nissan'),('car_model','altima'))
        """
        od = OrderedDict(args)
        query = sql
        values = tuple(od.values())
        self.__open()
        self.__session.execute(query, values)
        number_rows = self.__session.rowcount
        number_columns = len(self.__session.description)

        if number_rows >= 1 and number_columns > 1:
            result = [item for item in self.__session.fetchall()]
        else:
            result = [item[0] for item in self.__session.fetchall()]

        self.__close()
        return result


if __name__ == '__main__':
    web_dev2 = MySQL(host='rm-bp1613192u3673jr7to.mysql.rds.aliyuncs.com',
                     password='RyNXMfigZhtkt3ti',
                     database='tasks')
    print(web_dev2.__dict__)

    conditional_query = 'segment_id = %s '
    # print(web_dev2.select("das_object_tasks_tracking", None,
    # "*"))

    sql_query = 'select upload_file_s3_path ' \
                'FROM das_object_tasks_tracking ' \
                'WHERE object_name = %s and process_start_datetime > %s ' \
                'and status=%s order by process_start_datetime asc'

    temp_list = web_dev2.select_advanced(sql_query, ('object_name', "csm_css_enduser"),
                                 ('process_start_datetime',
                                  "2019-04-07 00:00:00"),
                                 ('status', 6))

    with open("test.txt", "a") as file:
        for i in range(len(temp_list)):
            new_line = 'hfs -cp '+ temp_list[i] + '* '+ temp_list[0] + "\n"
            file.write(new_line)
