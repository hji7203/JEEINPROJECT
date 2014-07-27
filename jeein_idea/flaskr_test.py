import os
import flaskr
import unittest
import tempfile

class FlaskTestCase(unittest.TestCase):

	def setUp(self):
		self.db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
		flaskr.app.config['TESTING'] = True
		self.app = flaskr.app.test_client()
		flaskr.init_db()

	def tearDown(self):
		os.close(self.db_fd)
		os.unlink(flaskr.app.config['DATABASE'])

if __name__ == '__main__':
	unittest.main()

class FlaskrTestCase(unittest.TestCase):

	def setUp(self):
		self.db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
		self.app = flaskr.app.test_client()
		flaskr.init_db()
	
	def tearDown(self):
		os.close(self.db_fd)
		os.unlink(flask.app.config['DATABASE'])

	def test_empty_db(self):
		rv = self.app.get('/')
		assert 'No entries here so far' in rv.data

	def login(self, username, password):
		return self.app.post('/login', data=dict(username=username, password=password), follow_redirect=True)

	def logout(self):
		return self.app.get('/logout', follow_redirects=True)

	def test_login_logout(self):
		rv = self.login('admin', 'default')
		assert 'You were logged in' in rv.data
		rv = self.logout()
		assert 'You were logged out' in rv.data
		rv = self.login('adminx', 'default')
		assert 'Invalid username' in rv.data
		rv = self.login('admin', 'defaultx')
		assert 'Invalid password' in rv.data

	def test_messages(self):
		self.login('admin', 'default')
		rv = self.app.post('/add' , data=dict(
			title = '<Hello>',
			text='<strong>HTML</strong> allowed here'
			), follow_redirects = True)
		assert 'No entries here so far' not in rv.data
		assert '&lt;Hello&gt;' in rv.data
		assert '<strong>HTML</strong> allowed here' in rv.data

app = flask.Flask(__name__)
with app.test_request_context('/?name=Peter'):
	assert flask.request.path == '/'
	assert flask.request.args['name'] == 'Peter'

def get_user():
	user = getattr(g, 'user', None)
	if user is None:
		user = fetch_current_user_from_database()
		g.user = user
	return user

from contextlib import contextmanager
from flask import appcontext_pushed

@contextmanager
def user_set(app, user):
	def handler(sender, **kwargs):
		g.user = user
	with appcontext_pushed.connected_to(handler, app):
		yield

from flask import json, jsonity
@app.route('/users/me')
def users_me():
	return jsonity(username=g.user.username)

with user_set(app, my_user):
	with app.test_client() as c:
		resp = c.get('/users/me')
		data = json.loads(resp.data)
		self.assert_equal(data['username'], my_user.username)

app = flask.flask(__name__)

with app.test_client() as c:
	rv = c.get('/?tequila=42')
	assert request.args['tequila'] == '42'

with app.test_client() as c:
	rv = c.get('/')
	assert flask.session['foo'] == 42

with app.test_client() as c:
	with c.session_transaction() as sess:
		sess['a_key'] = 'a value'

	#once this is reached the session was stored
