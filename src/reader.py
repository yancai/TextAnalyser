# -*- coding: utf-8 -*-
#!/usr/bin/python
# Author = 'yancai'
# Date = '13-4-14'

import codecs
import simplejson
import datetime
import chardet
import copy
import os
from model.model_copy import characters, table


class Reader():

    def __init__(self):
        self.table = copy.deepcopy(table)

    def get_id(self, character):
        return characters.get(character, "")

    def process_line(self, line):
        for i in range(len(line) - 1):
            id_cur = self.get_id(line[i])
            id_next = self.get_id(line[i + 1])
            if id_cur and id_next:
                cur_count = self.table[id_cur].get(id_next, 0)
                self.table[id_cur][id_next] = cur_count + 1

    def get_now_str(self):
        now = datetime.datetime.now()
        now_str = str(now).replace("-", "_").replace(" ", "_").replace(":", "_").replace(".", "_")
        return now_str

    def detect_coding(self, file_path):
        f = open(file_path, "r")
        result = chardet.detect(f.read())
        return result.get("encoding", "gbk")

    def reader(self, file_path):
        text_file = codecs.open(file_path, "r", self.detect_coding(file_path))

        line = text_file.readline()
        while line != "":
            self.process_line(line)
            line = text_file.readline()

        for key, value in self.table.items():
            if value == {}:
                self.table.pop(key)


        file_result = open("./result/" + self.get_now_str() + "_result.json", "w")
        simplejson.dump(self.table, file_result)
        file_result.close()
