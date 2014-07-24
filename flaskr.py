import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
import re
import json

#create our little application
app = Flask(__name__)
app.config.from_object(__name__)

#Load default config and override config
app.config.update(dict(
	DATABASE=os.path.join(app.root_path, 'flaskr.db'),
	DEBUG=True,
	SECRET_KEY='development key',
	USERNAME='admin',
	PASSWORD='default'
	))
app.config.from_envvar('FLASK_SETTINGS', silent=True)

def connect_db() :
	"""Connects to the specific database."""
	rv = sqlite3.connect(app.config['DATABASE'])
	rv.row_factory = sqlite3.Row
	return rv

	# if __name__ == '__main__':
	# 	app.run()

def get_db():
	"""Opens a new database connection if there is none yet for the current application context.
	"""
	if not hasattr(g, 'sqlite_db'):
		g.sqlite_db = connect_db()
	return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
	"""Close the database again at the end of the request."""
	if hasattr(g, 'sqlite_db'):
		g.sqlite_db.close()

def init_db():
	with app.app_context():
		db = get_db()
		with app.open_resource('schema.sql', mode ='r') as f:
			db.cursor().executescript(f.read())
		db.commit()

from flaskr import init_db
init_db()

@app.route('/')
def show_entries():
	db = get_db()
	cur = db.execute('select title, text from entries order by id desc')
	entries = cur.fetchall()
	return render_template('show_entries.html', entries=entries)

@app.route('/add', methods=['POST'])
def add_entry():
	if not session.get('logged_in'):
		abort(401)
	db = get_db()
	db.execute('insert into entries (title, text) values (?,?)', [request.form['title'], request.form['text']])
	db.commit()
	flash('New entry was successfully posted')
	return redirect(url_for('show_entries'))

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
		if os.path.isfile('users.txt') == True:
			fr = open("users.txt", 'r')
			data = fr.read()
		
			users = json.loads(data)
	
			
			if check_list(users, request.form['username']) == False:
				error = "Invalid email"
			elif check_list(users, request.form['username']) == True:
				info = check_id_password(users, request.form['username'], request.form['password'])
				if info == False:
					error = "Invalid password"
				else :
					if info['admin'] == True:
						session['admin'] = True
						session['logged_in'] = True
						session['email'] = request.form['username']
						flash('You were logged in')
						return redirect(url_for('show_entries'))
					else:
						fr.close()
						session['logged_in'] = True
						session['email'] = request.form['username']
						flash('You were logged in')
						return redirect(url_for('show_entries'))

		else :
			error = "Invalid Email. Join"

		#if request.form['username'] != app.config['USERNAME']:
		# 	error = 'Invalid username'
		# elif request.form['password'] != app.config['PASSWORD']:
		# 	error = 'Invalid password'
		# else:
		# 	session['logged_in'] = True
		# 	flash('You were logged in')
		# 	return redirect(url_for('show_entries'))
	return render_template('login.html', error=error)

@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	flash('You were logged out')
	return redirect(url_for('show_entries'))

@app.route('/user_page')
def user_page():
	if os.path.isfile('users.txt') == True:
		fr = open("users.txt", 'r')
		data = fr.read()
		users = json.loads(data)
	return render_template('user_page.html',result = users)

	

@app.route('/signup', methods=['GET','POST'])
def signup():
	message = None

	if 'admin' in request.form:
		admin_temp = True
	else :
		admin_temp = False	

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
				if os.path.isfile('users.txt') == True:
					fr = open("users.txt", 'r')
					data = fr.read()
					users = json.loads(data)
					if check_list(users, request.form['email']) == True:
						fr.close()
						message = "This e-mail is already used"
					else:
						fr.close()
						fw = open("users.txt", 'w')
						info = {
						'email' : request.form['email'],
						'password' : request.form['password'],
						'admin' : admin_temp
						}
						users.append(info)
						fw.write(json.dumps(users))
						fw.close()
						message = "Sign up successful"
				else:
					f = open("users.txt", 'w')
					info = {
						'email' : request.form['email'],
						'password' : request.form['password'],
						'admin' : admin_temp
						}
					f.write(json.dumps([info]))
					f.close()

	return render_template('signup.html', message = message)


if __name__ == '__main__':
	init_db()
	app.run()


