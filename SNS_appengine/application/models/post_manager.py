from application import db
from schema import *
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

def add_post(data):
	post = Post(
		body 		= data['content'],
		is_secret 	= data['secret'],
		user_id 	= session['email'],
		wall_id		= 0
    )

	db.session.add(post)
	db.session.commit()
	return post