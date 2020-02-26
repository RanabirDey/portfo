from flask import Flask, render_template, request, url_for, redirect # to set debug mode ON, type in command line "set FLASK_ENV=development"
import csv
import requests as req
import hashlib

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/<string:page_name>')
def web_pages(page_name):
    return render_template(page_name)

@app.route('/thankyou/<name>')
def thankyou_page(name):
    return render_template('thankyou.html',name=name)

def write_to_txtdb(data):
	with open('database.txt', mode='a') as text_db:
		name = data['name']
		email = data['email']
		subject = data['subject']
		message = data['message']
		file = text_db.write(f'\n{name},{email},{subject},{message}')

def write_to_csvdb(data):
	with open('database.csv', newline='', mode='a') as csv_db:
		name = data['name']
		email = data['email']
		subject = data['subject']
		message = data['message']
		csv_writer = csv.writer(csv_db, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([name,email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		try:
			data = request.form.to_dict()
			write_to_csvdb(data)
			return redirect(url_for('thankyou_page', name=data['name']))
		except:
			return 'data not saved in database'
	else:
		return 'Something went wrong. Please try again!'

def req_api_data(hashkey):
	url = 'https://api.pwnedpasswords.com/range/' + hashkey
	res = req.get(url)
	if res.status_code != 200:
		raise RuntimeError(f'error while fetching API data, error code {res.status_code}. Please check url')
	return res

def password_leak_count(response, hash_tail):
	password_hack = False
	for multi_res in response.text.splitlines():
		if multi_res.split(":")[0] == hash_tail:
			return f'Oops!! your password has been hacked {multi_res.split(":")[1]} times. Please change your password now.'
			password_hack = True
	if password_hack == False:
		return 'Congratulations! Your password is still secure'

def gen_hash(password):
	print('************************* password in gen_hash:', password)
	hashkey = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
	hash_tail = hashkey[5:]
	response = req_api_data(hashkey[:5])
	return password_leak_count(response, hash_tail)

@app.route('/password_hack', methods=['POST', 'GET'])
def password_hack():
	if request.method == 'POST':
		try:
			password = request.form.to_dict()
			print(password)
			return gen_hash(password['password'])
		except:
			return 'password not entered'
	else:
		return 'Something went wrong. Please try again!'