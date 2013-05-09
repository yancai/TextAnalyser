#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author:   'yancai'
# Date:     '13-5-9'

"""Documentation"""

from distutils.core import setup
import py2exe

setup(
    console=["run.py"],
    data_files=[
        ("model", ["model/__init__.py",
                   "model/characters.py",
                   "model/model_copy.py",
                   "model/table.py"]),
        ("", ["./__init__.py",
              "./__init__.py",
              "./reader.py",
              u"./ReadMe说明.txt"]),
        ("files", ""),
    ],
    install_requires=[
        "chardet",
        "simplejson"
    ],
)
