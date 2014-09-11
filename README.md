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

Configuring flask-blitzdb
-------------------------

flask-blitzdb can be configured in several ways. this allows flask-blitzdb to be able to perform in a wider range of application senarios. 

Currently flask-blitzdb only supports `blitzdb.FileBackend` datastores, the path of this is defined through the config variable BLITZDB_DATABASE.

	app.config[’BLITZDB_DATABASE’] = '/path/to/db'

By default flask-blitzdb will instansiate the transactions on your behalf using the `app.before_request` to create a transaction for your blitzdb datastore and `app.teardown_appcontext` to commit to the database. 

This behaviour can be toggled using the folloing flask config variables:

* `BLITZDB_BEGIN` is the flag to tell flask-blitzdb to handle commits for you 
	enable:

		app.config[’BLITZDB_BEGIN’] = True

	disable:

		app.config[’BLITZDB_BEGIN’] = False

* `BLITZDB_COMMIT` is the flag for commit management
	enable:

		app.config[`BLITZDB_COMMIT`] = True

	disable:

		app.config[`BLITZDB_COMMIT`] = False
