#-*- coding:utf-8 -*-
from application import app
from flask import render_template, url_for

@app.route('/')
def layout():
	return render_template('layout.html')

@app.route('/login')
def login():
    """Return a friendly HTTP greeting."""
    return render_template('login.html')

@app.route('/signup')
def signup():
    """Return a friendly HTTP greeting."""
    return render_template('signup.html')

@app.route('/posts')
def posts():
    """Return a friendly HTTP greeting."""
    return render_template('posts.html')

@app.route('/write')
def write():
    """Return a friendly HTTP greeting."""
    return render_template('write.html')

@app.route('/read')
def read():
    """Return a friendly HTTP greeting."""
    return render_template('read.html')


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404