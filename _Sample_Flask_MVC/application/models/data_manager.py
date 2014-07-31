import json, os

def save_account(list) :

	fw = open("users.txt", 'w')
	fw.write(json.dumps(list))
	if not fw.closed :
		fw.close()

def load_account() :
	if os.path.exists('users.txt'):
		fr = open("users.txt", 'r')
		data = fr.read()
		if data == "":
			users = []
		else:
			users = json.loads(data)
		if not fr.closed:
			fr.close()
	else:
		users = []
	return users 
