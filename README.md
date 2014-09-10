flask-blitzdb
=============

An extension to allow the integrated use of the [blitzdb](https://github.com/adewes/blitzdb) platform by [Andreas Dewes](http://www.andreas-dewes.de/en/)

Currently this plugin only support 'FileBackend' backend. 

Using flask-blitzdb
--------------------

flask-blitzdb can be installed using pip

	pip install flask-blitzdb

flask-blitzdb allows your Flask based application to interact with your blitzdb file based datastore.

	import flask
	from flask_blitzdb import BlitzDB

	BLITZDB_DATABASE = r'./blitz_test.db'

	app = flask.Flask(__name__)
	app.config.from_object(__name__)

	db = BlitzDB(app)

via the `db` object you can now access your BlitzDB datastore

apps model:

from blitzdb import Document

	class MyDocument(Document):
		pass

flask app: 

	@app.route('/dbsave/<name>/<one>/<two>/<three>')
	def index():
		test_dict = {
			'name': name,
			'one': one,
			'two': two,
			'three': three
		}
		test_doc = test_model.TestDoc(test_dict)
		db.save(test_doc)
		if not len(db.filter(test_model.TestDoc, {})) => 1:
			abort(500)

	@app.route('/get/<name>')
	def index():
		get_query = db.get(test_model.TestDoc, {'name': name})
		if not len(get_query) == 1:
			abort(500)

		return json.dumps(dict(get_query))