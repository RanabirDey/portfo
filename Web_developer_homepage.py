from flask import Flask, render_template, request, url_for, redirect # to set debug mode ON, type in command line "set FLASK_ENV=development"
import csv
from password_hack import gen_hash
from custom_hackernews import cust_hackernews
from generate_news import generate_news
from password_validation import password_check

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

@app.route('/password_hack', methods=['POST', 'GET'])
def password_hack():
	if request.method == 'POST':
		try:
			password = request.form.to_dict()
			return gen_hash(password['password'])
		except:
			return 'password not entered'
	else:
		return 'Something went wrong. Please try again!'

@app.route('/hacker_news', methods=['POST', 'GET'])
def hacker_news():
	if request.method == 'POST':
		try:
			vote_count = request.form.to_dict()
			generate_news(cust_hackernews(vote_count['vote_count']))
			return redirect('/cust_news.html')
		except:
			return 'Please enter vote count for your reading pleasure'
	else:
		return 'Something went wrong. Please try again!'

@app.route('/password_validation', methods=['POST', 'GET'])
def password_validation():
	if request.method == 'POST':
		try:
			password = request.form.to_dict()
			return password_check(password['password'])
		except:
			return 'Please re-enter your new password for validation'
	else:
		return 'Something went wrong. Please try again!'
