from application import app
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from application.models import file_manager, user_manager

@app.route('/profile')
def profile():
	user = user_manager.get_user_by(session['user_id'])

	return render_template('profile.html', profile_image = user.profile_image)

@app.route('/upload_image', methods = ['POST'])
def upload_image():
	image_file = request.files['profile-image']
	
	filename = image_file.filename
	
	extention = filename.split('.')[-1]
	new_file_name = str(session['user_id'])+ '.'+extention
	directory = '/gs/likelionpro/profile/'
	filepath = directory + new_file_name

	file_manager.save_file(image_file, filepath)

	user_manager.add_profile_image(session['user_id'], new_file_name)

	return redirect(url_for('profile'))


@app.route('/image/profile/<filename>')
def get_profile_image(filename):
	directory = '/gs/likelionpro/profile/'
	filepath = directory + filename
	return file_manager.read_file(filepath)
