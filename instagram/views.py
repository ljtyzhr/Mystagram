#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/24 17:46
# @Author  : ljtyzhr
# @Site    : 
# @File    : views.py
# @Software: PyCharm Community Edition


from instagram import app

@app.route('/')
def index():
    return "Hello Index!"