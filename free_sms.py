# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client # pip3 install twilio
import os


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
def free_sms(to_num, message):
#	print(os.environ)
	account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
	auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
	client = Client(account_sid, auth_token)

	message = client.messages \
	                .create(
	                     body=message,
	                     from_='+14702357804',
	                     to=to_num
	                 )

	return f"Your msg is in process, current status: {message.status}"

