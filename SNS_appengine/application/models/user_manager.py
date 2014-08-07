from application import db
from schema import *
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash


def add_user(data):
	user = User(
		email = data['email'],
		username = data['username'],
		password = db.func.md5(data['password']),
		gender = data['gender'],
		phone = data['mobile'],
		birthday = data['birthday']
    )

	db.session.add(user)
	db.session.commit()
	return user

def get_user(email):
	user = User.query.filter(User.email == email).all()
	return user

def login_check(email, password):
	return User.query.filter(User.email == email,
		User.password == db.func.md5(password)).count() != 0