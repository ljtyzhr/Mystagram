#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/24 17:45
# @Author  : ljtyzhr
# @Site    : 
# @File    : manage.py
# @Software: PyCharm Community Edition

from instagram import app
from flask_script import Manager


manager = Manager(app)

if __name__ == '__main__':
    manager.run()