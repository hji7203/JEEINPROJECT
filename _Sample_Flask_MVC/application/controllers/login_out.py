from application import app
from application.models import data_manager
import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
import re
import json

@app.route('/login', methods=['GET','POST'])
def login():
	error = None
	
	def check_id_password(users_list, user_id, user_ps):
		for info in users_list:
			if info['email'] == user_id:
				if info['password'] == user_ps:
					return info
		return False
	
	def check_list(users_list, user_id):
		for info in users_list:
			if info['email'] == user_id:
				return True
		return False
	
	if request.method == 'POST':
		# if os.path.isfile('users.txt') == True:
		# 	fr = open("users.txt", 'r')
		# 	data = fr.read()
		
		# 	users = json.loads(data)
		users = data_manager.load_account()
				
		if check_list(users, request.form['username']) == False:
			error = "Invalid email"
		elif check_list(users, request.form['username']) == True:
			info = check_id_password(users, request.form['username'], request.form['password'])
			if info == False:
				error = "Invalid password"
			else :
			
				session['admin'] = info['admin']
				session['logged_in'] = True
				session['email'] = request.form['username']
				flash('You were logged in')
				return redirect(url_for('show_entries'))
				
	else :
		error = "Invalid Email. Join"


	return render_template('login.html', error=error)

@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	flash('You were logged out')
	return redirect(url_for('show_entries'))