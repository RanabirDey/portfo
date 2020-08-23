############################################ send email########################################### 
import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

#email = EmailMessage()
#html = Template(Path('Index.html').read_text())

def send_mail(name,emailid,amount,due_date):
	email = EmailMessage()
	html = Template(Path('Index.html').read_text())

	email['from'] = 'ABC Corp'
	email['to'] = emailid
	email['subject'] = 'Monthly mobile bill'

	email.set_content(html.substitute({'name': name, 'amount': amount, 'date': due_date}),'html')

	with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
		smtp.ehlo()
		smtp.starttls()
#		smtp.login('sendmailthrupython@gmail.com', 'Sendmailthrupython01')
		smtp.login('sendmailthrupython@gmail.com', 'pukpzkluobskyeyb')    # the password was set by Google only for accessing the mail account from Python
		smtp.send_message(email)
		print('mail sent to', emailid)

cust_list = [
{'name': 'Ranabir Dey', 'emailid': 'ranabir4u@gmail.com', 'amount': 20},
{'name': 'Nabanita Dey', 'emailid': 'nabanitadastidar@gmail.com', 'amount': 30},
{'name': 'Anonymous Nameless', 'emailid': 'anonymous.nameless09@gmail.com', 'amount': 10}
]

for customer in cust_list:
	send_mail(customer['name'],customer['emailid'],customer['amount'],'2/20/2020')
