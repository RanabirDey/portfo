# Password_hack_check

import requests as req
import hashlib

def req_api_data(hashkey):
	url = 'https://api.pwnedpasswords.com/range/' + hashkey
	res = req.get(url)
	if res.status_code != 200:
		err_msg = 'error while fetching API data, error code ' + res.status_code + '. Please check url'
		raise RuntimeError(err_msg)
	return res

def password_leak_count(response, hash_tail):
	password_hack = False
	for multi_res in response.text.splitlines():
		if multi_res.split(":")[0] == hash_tail:
			ret_msg = 'Oops!! your password has been hacked ' + multi_res.split(":")[1] + ' times. Please change your password now.'
			return ret_msg
			password_hack = True
	if password_hack == False:
		return 'Congratulations! Your password is still secure'

def gen_hash(password):
	hashkey = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
	hash_tail = hashkey[5:]
	response = req_api_data(hashkey[:5])
	return password_leak_count(response, hash_tail)
