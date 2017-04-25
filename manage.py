#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/24 17:45
# @Author  : ljtyzhr
# @Site    : 
# @File    : manage.py
# @Software: PyCharm Community Edition

from instagram import app
from instagram import db
from flask_script import Manager

from instagram.models import User

manager = Manager(app)


# 根据命令行来，初始化数据库信息
@manager.command
def init_database():
    db.drop_all()
    db.create_all()

    # 创建 10 用户
    for i in range(0, 10):
        db.session.add(User('牛客' + str(i), 'a' + str(i)))

    db.session.commit()

if __name__ == '__main__':
    manager.run()