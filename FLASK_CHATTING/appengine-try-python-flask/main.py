from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

import pusher

app = Flask(__name__)
app.config['DEBUG'] = True
p = pusher.Pusher(
	app_id = '83092',
	key = '136fb99306188ba55ed3',
	secret = 'a6f4e910b38e7fb79566'
	)
app.secret_key = 'tlzmfltzl1234'

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.

@app.route('/')
def index():
	if 'username' in session:
		return render_template('index.html')
	else:
		return redirect(url_for('login'))

@app.route('/chat_box', methods=['GET','POST'])
def chat_box():
	if request.method == 'POST':
		p['syg'].trigger('chatting', {"chat_box" : request.form['chat_box'],"username" : session['username']})
	return render_template('index.html')
	# return render_template("index.html")
		
	



@app.route('/login', methods=['GET','POST'])
def login():
	if request.method == 'POST':
		session['username'] = request.form['username']
		p['syg'].trigger('notification', {"username":session['username']})
		return redirect(url_for('index'))
	else:
		return render_template("login.html")


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404

    

