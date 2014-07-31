from application import app
from application.models import data_manager
import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
import re
import json

@app.route('/signup', methods=['GET','POST'])
def signup():
	message = None

	admin_temp = 'admin' in request.form
	# if 'admin' in request.form:
	# 	admin_temp = True
	# else :
	# 	admin_temp = False	

	def check_list(users_list, user_id):
		for info in users_list:
			if info['email'] == user_id:
				return True
		return False

	if request.method == 'POST':
		if request.form['email'] == "":
			message = "Email is empty"
		elif bool(re.search("[\w_]+@\w+(\.com|\.net|\.ac\.kr)", request.form['email']))== False:
			message = "Email form is wrong"
		elif request.form['password'] == "":
			message = "Password is empty"
		elif request.form['password'] != "":
			if bool(re.search("^.{8,20}$", request.form['password'])) == False:
				message = "Password is wrong"
			elif bool(re.search("[A-Z]+", request.form['password'])) == False:
				message = "Password is wrong"
			elif bool(re.search("[a-z]+", request.form['password'])) == False:
				message = "Password is wrong"
			elif bool(re.search("[0-9]+", request.form['password'])) == False:
				message = "Password is wrong"
			elif bool(re.search("\W+", request.form['password'])) == False:
				message = "Password is wrong"

			elif request.form['password_check'] != request.form['password']:
				message = "Password check again"

			else:
				users = data_manager.load_account()
				if check_list(users, request.form['email']):

					message = "This e-mail is already used"
				else :
					info = {
					'email' : request.form['email'],
					'password' : request.form['password'],
					'admin' : admin_temp
					}
					users.append(info)
					data_manager.save_account(users)
					message = "Sign up successful"
				
					

	return render_template('signup.html', message = message)