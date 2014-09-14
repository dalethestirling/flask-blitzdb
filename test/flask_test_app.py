import flask
import test_model

import os
import sys

sys.path.append(
		os.path.abspath('../')
	)

from flask_blitzdb import BlitzDB

import json

DEBUG = True
BLITZDB_DATABASE = r'./test_app.db'

app = flask.Flask(__name__)
app.config.from_object(__name__)


db = BlitzDB(app)
# conn = db.connection
# more_conn = db.connect()
# print dir(db)
# print conn


@app.route('/docsave/<name>/<one>/<two>/<three>')
def docsave(name, one, two, three):
	conn = db.connection
	test_dict = {
		'name': name,
		'one': one,
		'two': two,
		'three': three
	}
	test_doc = test_model.TestDoc(test_dict)
	test_doc.save(conn)

	return flask.redirect(flask.url_for('get_one', name=name))

@app.route('/dbsave/<name>/<one>/<two>/<three>')
def dbsave(name, one, two, three):
	conn = db.connection
	test_dict = {
		'name': name,
		'one': one,
		'two': two,
		'three': three
	}
	test_doc = test_model.TestDoc(test_dict)
	conn.save(test_doc)

	return flask.redirect(flask.url_for('get_one', name=name))

@app.route('/get/<name>')
def get_one(name):
	conn = db.connection
	try:
		get_query = conn.get(test_model.TestDoc, {'name': name})
		return json.dumps(dict(get_query))
	except:
		flask.abort(500)

	

@app.route('/getall')
def get_all():
	conn = db.connection
	get_all_len = len(conn.filter(test_model.TestDoc, {}))
	if not get_all_len >= 1:
		flask.abort(500)
	
	return str(get_all_len)

# application execution 
if __name__ == '__main__': 
    app.run()
