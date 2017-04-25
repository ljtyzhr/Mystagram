#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/24 17:46
# @Author  : ljtyzhr
# @Site    : 
# @File    : views.py
# @Software: PyCharm Community Edition

from flask import render_template, redirect

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