#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/24 17:46
# @Author  : ljtyzhr
# @Site    : 
# @File    : __init__.py
# @Software: PyCharm Community Edition

from flask import Flask

app = Flask(__name__)

from instagram import views, models