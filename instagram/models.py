#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/24 17:46
# @Author  : ljtyzhr
# @Site    : 
# @File    : models.py
# @Software: PyCharm Community Edition

import random

from instagram import db


# 用户model
class User(db.Model):
    #__tablename__ = 'myuser' 指定表名字
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(32))
    salt = db.Column(db.String(32))
    head_url = db.Column(db.String(256))

    def __init__(self, username, password, salt=''):
        self.username = username
        self.password = password  # 暂时明文，下节课讲解加密
        self.salt = salt
        self.head_url = 'http://images.nowcoder.com/head/' + str(random.randint(0, 1000)) + 't.png'