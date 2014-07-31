from application import app
from application.models import data_manager
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

@app.route('/')
def show_entries():
	return render_template('show_entries.html')

@app.route('/add', methods=['POST'])
def add_entry():
	if not session.get('logged_in'):
		abort(401)
	flash('New entry was successfully posted')
	return redirect(url_for('show_entries'))
