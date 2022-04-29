from flask import Flask
import json, time

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
	data_set = {'Page': 'Home', 'Msg': 'Hello, World!', 'Timestamp': time.time()}
	json_dump = json.dump(data_set)
	return json.dump
