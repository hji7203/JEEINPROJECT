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


def get_posts(_id):
	posts = Post.query.filter(Post.wall_id == _id).all()
	return posts

def get_post_by(_id):
	post = Post.query.get(_id)
	return post

def del_post(_id):
	post = Post.query.get(_id)
	db.session.delete(post)
	db.session.commit()
	return post

def edit_post(_id, data):
	post = Post.query.get(_id)
	post.body = data['content']
	db.session.commit()
	