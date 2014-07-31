import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
import re
import json
from application import app
from application.models import data_manager

@app.route('/email_check', methods=['GET','POST'])
def email_check():
	email = request.form['email']
	result = {}
	# fr = open("users.txt", 'r')
	# data = fr.read()
	# users = json.loads(data)
	# fr.close()
	users = data_manager.load_account()
	if check_list(users, request.form['email']):
		result['message'] = "used"
		
	else :
		result['message']= "new"
	return json.dumps(result)

def check_list(users_list, user_id):
	for info in users_list:
		if info['email'] == user_id:
			return True
	return False