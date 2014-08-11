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

def get_comments(_id):
	comments = Comment.query.filter(Comment.post_id == _id).all()
	return comments

