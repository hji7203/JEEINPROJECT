from application import app
from application.models import user_manager
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

@app.route('/follow', methods = ['GET','POST'])
def follow():
	return render_template('follow.html')

@app.route('/follow_user', methods = ['GET','POST'])
def follow_user():
	if request.method == "POST":
		follow = request.form['follow']
		users = user_manager.follow_user(follow)

		return render_template('follow_ajax.html', users = users)
