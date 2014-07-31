from application import app
from application.models import data_manager
import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
import re
import json

@app.route('/user_page')
def user_page():
	# if os.path.isfile('users.txt') == True:
	# 	fr = open("users.txt", 'r')
	# 	data = fr.read()
	# 	users = json.loads(data)
	users = data_manager.load_account();
	return render_template('user_page.html',result = users)