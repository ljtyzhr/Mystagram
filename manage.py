#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/24 17:45
# @Author  : ljtyzhr
# @Site    : 
# @File    : manage.py
# @Software: PyCharm Community Edition

import random

from instagram import app
from instagram import db
from flask_script import Manager

from instagram.models import User, Image, Comment

manager = Manager(app)

def get_image_url():
    return 'http://images.nowcoder.com/head/' + str(random.randint(0, 1000)) + 'm.png'

# 根据命令行来，初始化数据库信息
@manager.command
def init_database():
    db.drop_all()
    db.create_all()

    # 创建 10 用户
    for i in range(0, 10):
        db.session.add(User('牛客' + str(i), 'a' + str(i)))
        for j in range(0, 10):  # 每人发十张图
            db.session.add(Image(get_image_url(), i + 1))
            for k in range(0, 3):
                db.session.add(Comment('这是一条评论' + str(k), 1 + 10 * i + j, i + 1))

    db.session.commit()

# 查询用户的命令
@manager.command
def research():
    print 1, User.query.all()
    print 2, User.query.get(3)  # primary key = 3
    print 3, User.query.filter_by(id=2).first()
    print 4.1, User.query.order_by(User.id.desc()).offset(1).limit(2).all()
    print 4.2, User.query.order_by(db.asc('id')).offset(1).limit(2).all()

if __name__ == '__main__':
    manager.run()