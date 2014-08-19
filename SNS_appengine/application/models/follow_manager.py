from application import db
from schema import *
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

def add_follow(follower_id, followee_id):
	follow = Follow(
		follower_id 	=  follower_id,
		followee_id		=  followee_id
    )
	db.session.add(follow)
	db.session.commit()
	return follow