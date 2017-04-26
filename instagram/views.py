#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/24 17:46
# @Author  : ljtyzhr
# @Site    : 
# @File    : views.py
# @Software: PyCharm Community Edition
import hashlib
import random

from flask import render_template, redirect
from flask import request, flash, get_flashed_messages

from instagram import app, db

from instagram.models import Image, User


# 首页的展示内容：首页根据图片展示，每张图片都是由哪个用户发上来的
@app.route('/')
def index():
    images = Image.query.order_by(db.desc(Image.id)).limit(10).all()
    return render_template('index.html', images=images)


# 显示 Image 的具体信息
@app.route('/image/<int:image_id>/')
def image(image_id):
    image = Image.query.get(image_id)
    if image == None:
        return redirect('/')
    return render_template('pageDetail.html', image = image)

# 个人信息界面
@app.route('/profile/<int:user_id>/')
def profile(user_id):
    user = User.query.get(user_id)
    if user == None:
        return redirect('/')
    return render_template('profile.html', user = user)


# 应用的登录操作
@app.route('/regloginpage/')
def regloginpage(msg=''):
    for m in get_flashed_messages(with_categories=False, category_filter=['reglogin']):
        msg = msg + m
    return render_template('login.html',msg=msg)


# 跳转
def redirect_with_msg(target, msg, category):
    if msg != None:
        flash(msg, category=category)
    return redirect(target)


# 这里是注册的入口，接收 GET 和 POST 方法
@app.route('/reg/', methods={'get', 'post'})
def reg():
    username = request.values.get('username').strip()
    password = request.values.get('password').strip()

    # 校验（还有其他更多的边界问题）
    if username == '' or password == '':
        print u'用户名和密码不能为空'
        return redirect_with_msg('/regloginpage', u'用户名和密码不能为空', 'reglogin')
    user = User.query.filter_by(username = username).first()
    if user != None:
        return redirect_with_msg('/regloginpage', u'用户名已存在', 'reglogin')

    # 请大家考虑更多边界问题