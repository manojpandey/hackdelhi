from flask import request
from flask import jsonify
import time

class Shake(object):
	"""docstring for Shake"""
	def __init__(self, user_id, location, timestamp):
		super(Shake, self).__init__()
		self.user_id = user_id
		self.location = location
		self.timestamp = timestamp
	

def get_time_in_sec():
	return int(round(time.time()))

def db_insert_shake(shake): ##TODO
	pass

def get_matching_shake(shake): ##TODO
	pass

#Note only one the shakes should call the api
def start_transaction(shake1, shake2): ##TODO
	pass

# /shake params-user_id, location, timestamp, amount
# 	
@app.route('/shake', methods=['GET'])
def shake_func():
	user_id = request.args.get('user_id')
	location = request.args.get('location')
	timestamp = request.args.get('timestamp')
	amount = request.args.get('amount') ##This will be none for one of the shakes
	shake = Shake(user_id, location, timestamp, amount)
	db_insert_shake(shake)
	initial_time_sec = get_time_in_sec()
	num_seconds_retry = 5
	while get_time_in_sec() - initial_time_sec < num_seconds_retry:
		matching_shake = get_matching_shake(shake)
		if matching_shake:
			return start_transaction(shake, matching_shake)
	response = {'success' : false, 'message' : 'No opposite device found'}
	return jsonify(**response)