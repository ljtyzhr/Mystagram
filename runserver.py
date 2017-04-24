#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/24 17:45
# @Author  : ljtyzhr
# @Site    : 
# @File    : runserver.py
# @Software: PyCharm Community Edition


from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)