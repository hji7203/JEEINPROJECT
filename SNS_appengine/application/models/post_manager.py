from application import db
from schema import *
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

def add_post(data, temp, post_user_id, post_wall_id):
	post = Post(
		body 		= data['content'],
		is_secret 	= temp,
		user_id 	= post_user_id,
		wall_id		= post_wall_id
    )

	db.session.add(post)
	db.session.commit()
	return post

def get_post(content):
	pass
