from app import app
from flask import request, abort, jsonify

@app.route('/<string:name>/')
@app.route('/')
def index(name ="world"):
    return "Hello,{}".format(name)

@app.route('/form/', methods=['GET', 'POST'])
def form():
	if request.method == 'GET':
		return """"<html><head></head><body>
		<form method="POST" action='/form/'>
		<input name="first_name">
		<input name="last_name">
		<input type="submit">
		</form> </body></html>"""
	else:
		rv = jsonify(request.form)
		return rv

class Obj:
    int status_code 
    int mimetype
    str result

    def form():
	if request.method == 'GET':
		return """"<html><head></head><body>
		<form method="POST" action='/form/'>
		<input name="first_name">
		<input name="last_name">
		<input type="submit">
		</form> </body></html>"""
	else:
		rv = jsonify(request.form)
		return rv

