from application import app
from application.models import user_manager, follow_manager
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

@app.route('/follow')
def follow():
	my_followees = user_manager.get_user_by(session['user_id']).followees.all()
	my_followers = user_manager.get_user_by(session['user_id']).followers.all()
	return render_template('follow.html', my_followees = my_followees, my_followers = my_followers)

@app.route('/follow_user', methods = ['GET','POST'])
def follow_user():
	if request.method == "POST":
		follow = request.form['follow']
		users = user_manager.follow_user(follow)

		return render_template('follow_ajax.html', users = users)

@app.route('/click_follow/<int:followee_id>')
def click_follow(followee_id):
	follow_manager.add_follow(session['user_id'], followee_id)
	return redirect(url_for('follow'))
