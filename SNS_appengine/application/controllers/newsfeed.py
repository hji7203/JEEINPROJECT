from application import app
from application.models import user_manager, follow_manager, post_manager
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

@app.route('/newsfeed')
def newsfeed():
	# wall_id = session['wall_id']
	# user_id = session['user_id']
	# list = [user_id]
	# my_followers = user_manager.get_user_by(user_id).followers.all()
	# for follower in my_followers:
	# 	list.append(follower.id)
	# user_id_posts = post_manager.get_user_id_posts(list)
	# wall_id_posts = post_manager.get_wall_id_posts(list)
	return render_template('newsfeed.html')

@app.route('/load_newsfeed', methods = ['GET','POST'])
def newsfeed_data():
	if request.method == 'POST':
		num = request.form['num']
		wall_id = session['wall_id']
		user_id = session['user_id']
		list = [user_id]
		my_followers = user_manager.get_user_by(user_id).followers.all()
		for follower in my_followers:
			list.append(follower.id)
		news_posts = post_manager.get_news_posts(list, num)
		return render_template('newsfeed_ajax.html', news_posts = news_posts)