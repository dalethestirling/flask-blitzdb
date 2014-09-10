import flask
from flask_blitzdb import BlitzDB
import test_model

BLITZDB_DATABASE = r'./test_app.db'

app = flask.Flask(__name__)
app.config.from_object(__name__)


db = BlitzDB(app)


@app.route('/docsave/<name>/<one>/<two>/<three>')
def index():
	test_dict = {
		'name': name,
		'one': one,
		'two': two,
		'three': three
	}
	test_doc = test_model.TestDoc(test_dict)
	test_doc.save(db)
	if not len(db.filter(test_model.TestDoc, {})) => 1:
		abort(500)


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

app.route('/getall')
def index():
	get_all_len = len(db.filter(test_model.TestDoc, {}))
	if not get_all_len => 1:
		abort(500)
	
	return str(get_all_len)

# application execution 
if __name__ == '__main__': 
    app.run()
