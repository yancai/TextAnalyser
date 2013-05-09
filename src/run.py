#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author:   'yancai'
# Date:     '13-5-9'

"""Documentation"""

import os
from reader import Reader
import logging

if not os.path.exists("./result"):
    os.mkdir("./result")

if not os.path.exists("./files"):
    os.mkdir("./files")

logging.basicConfig(
    filename=os.path.join(os.getcwd(), "./result/TextAnalyser.log"),
    level=logging.NOTSET)


def scan_folder():
    return [os.path.realpath(item) for item in os.listdir(os.getcwd() + "/files") if os.path.splitext(item)[1] == ".txt"]

for item in scan_folder():
    try:
        reader = Reader()
        reader.reader(item)
    except Exception as e:
        logging.error(
            "read file error!\n"
            "filename: " + item +
            "ERROR MESSAGE: " + e.message)

raw_input("Thanks!\ninput any key to continue...")
