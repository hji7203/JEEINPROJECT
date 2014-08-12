#-*- coding:utf-8 -*-
from application import app
from application.models import user_manager, post_manager, comment_manager
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
    wall_user = user_manager.get_user_by(wall_id)
    wall_name = wall_user.username
    wall_posts = post_manager.get_posts(session['wall_id'])

    return render_template('posts.html', wall_name = wall_name, wall_posts = wall_posts)

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
        return redirect(url_for('posts', wall_id = session['wall_id']))
    else:

        return render_template('write.html')

@app.route('/comments/<int:post_id>', methods = ['GET','POST'])
def comments(post_id):
    if request.method =='POST':
        comment_manager.add_comment(request.form, post_id, session['user_id'])
        return redirect(url_for('read', post_id = post_id))
    else:
        return redirect(url_for('read', post_id = post_id))

@app.route('/read/<int:post_id>', methods = ['GET','POST'])
def read(post_id):
    post = post_manager.get_post_by(post_id)
    return render_template('read.html', wall_id =session['wall_id'], post = post)

@app.route('/post_edit/<int:post_id>')
def post_edit(post_id):
    post = post_manager.get_post_by(post_id)
    return render_template('edit.html', post = post)

@app.route('/edit/<int:post_id>', methods = ['GET','POST'])
def edit(post_id):
    if request.method =='POST':
        post_manager.edit_post(post_id, request.form)
    return redirect(url_for('read' ,post_id = post_id))


@app.route('/delete/<int:post_id>')
def delete(post_id):
    post = post_manager.get_post_by(post_id)
    if session['user_id'] == post.user_id:
        post_manager.del_post(post_id)
    else:
        pass

    return redirect(url_for('posts', wall_id =session['wall_id']))

@app.route('/delele_comment/<int:comment_id>')
def delete_comment(comment_id):
    comment = comment_manager.get_comment_by(comment_id)
    post_id = comment.post_id
    if session['user_id'] == comment.user_id:
        comment_manager.del_comment(comment_id)
    else:
        pass

    return redirect(url_for('read', post_id = post_id))



@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404