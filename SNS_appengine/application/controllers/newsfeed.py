from application import app
from application.models import user_manager, follow_manager, post_manager
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

@app.route('/newsfeed')
def newsfeed():
	wall_id = session['wall_id']
	user_id = session['user_id']
	list = [user_id]
	my_followers = user_manager.get_user_by(user_id).followers.all()
	for follower in my_followers:
		list.append(follower.id)
	user_id_posts = post_manager.get_user_id_posts(list)
	wall_id_posts = post_manager.get_wall_id_posts(list)


	return render_template('newsfeed.html', user_id_posts = user_id_posts, wall_id_post = wall_id_posts)
