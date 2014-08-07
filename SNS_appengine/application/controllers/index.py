#-*- coding:utf-8 -*-
from application import app
from application.models import user_manager, post_manager
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from application.models.schema import *

@app.route('/')
def layout():
	return render_template('layout.html')

@app.route('/login', methods = ['GET','POST'])
def login():
    error= None
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if user_manager.login_check(email, password) == True:
            session['logged_in'] = True
            session['email'] = email
            users = user_manager.get_user(email)
            session['user_id'] = users[0].id  
            flash('You were logged_in')
            return redirect(url_for('posts'))
        else :
            error = "There is no information."
    else :
        pass
    return render_template('login.html', error = error)

@app.route('/signup', methods = ['GET','POST'])
def signup():
    if request.method == 'POST':
        user_manager.add_user(request.form)
    return render_template('signup.html')


@app.route('/post', defaults = {'wall_id':0})
@app.route('/post/<int:wall_id>')
def posts(wall_id):
    if wall_id == 0 :
        wall_id = session['user_id']
    
    session['wall_id'] = wall_id
    return render_template('posts.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('email', None)
    session.pop('user_id', None)
    return redirect(url_for('layout'))

@app.route('/write', methods = ['GET','POST'])
def write():
    if request.method == 'POST': 
        if 'secret' in request.form:
            secret_temp = 1
        else :
            secret_temp = 0  
        post_manager.add_post(request.form, secret_temp, session['user_id'], session['wall_id'])
        return redirect(url_for('posts'))
    else:
        return render_template('write.html')

@app.route('/read')
def read():
    return render_template('read.html')


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404