# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client # pip3 install twilio


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
def free_sms(to_num, message):
	account_sid = 'AC52b7fd8a233b1de41723648a583964b3'
	auth_token = 'e167a0df16bc679163489cdd9a8e38e5'
	client = Client(account_sid, auth_token)

	message = client.messages \
	                .create(
	                     body=message,
	                     from_='+14702357804',
	                     to=to_num
	                 )

	return f"Your msg is in process, current status: {message.status}"

