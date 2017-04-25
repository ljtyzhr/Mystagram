#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/24 17:46
# @Author  : ljtyzhr
# @Site    : 
# @File    : __init__.py
# @Software: PyCharm Community Edition

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# 简单的配置 app
app = Flask(__name__)
app.jinja_env.add_extension('jinja2.ext.loopcontrols')
app.config.from_pyfile('app.conf')
app.secret_key = 'nowcoder'
db = SQLAlchemy(app)

# 导入 view 和 model，构建基本的 mvc 模型
from instagram import views, models