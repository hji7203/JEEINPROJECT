from application import db
from schema import *
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

def add_comment(data, post_id, comment_user_id):
	comment = Comment(
		body = data['comments'],
		post_id = post_id,
		user_id = comment_user_id
    )
	db.session.add(comment)
	db.session.commit()
	return comment

def get_comment_by(_id):
	comment = Comment.query.get(_id)
	return comment

def del_comment(_id):
	comment = Comment.query.get(_id)

	db.session.delete(comment)
	db.session.commit()

	return comment