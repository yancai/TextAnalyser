# -*- coding: utf-8 -*-
#!/usr/bin/python
# Author = 'yancai'
# Date = '13-4-14'

import codecs
import simplejson
import datetime
from model.model_copy import characters, table

table = table


def get_id(character):
    return characters.get(character, "")


def process_line(line):
    global table
    for i in range(len(line) - 1):
        id_cur = get_id(line[i])
        id_next = get_id(line[i + 1])
        if id_cur and id_next:
            cur_count = table[id_cur].get(id_next, 0)
            table[id_cur][id_next] = cur_count + 1


def get_now_str():
    now = datetime.datetime.now()
    now_str = str(now).replace("-", "_").replace(" ", "_").replace(":", "_").replace(".", "_")
    return now_str


def reader(file_path):
    global table
    text_file = codecs.open(file_path, "r", "gb2312")

    line = text_file.readline()
    while line != "":
        process_line(line)
        line = text_file.readline()

    for key, value in table.items():
        if value == {}:
            table.pop(key)
    file_result = open("./" + get_now_str() + "_result.json", "w")
    simplejson.dump(table, file_result)
    file_result.close()

reader("./text.txt")
