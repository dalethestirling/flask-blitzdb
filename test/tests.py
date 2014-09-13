import unittest
import blitzdb
import requests
import test_model

import os
import sys
import time

# Add parent dir to sys.path so that flask-blitzdb can be imported 
sys.path.append(
        os.path.abspath('../')
    )

class TestFlaskBlitzDB(unittest.TestCase):
    '''Tests for flask-blitzdb'''

    def test_import(self):
        '''Test import is not broken'''
        import flask_blitzdb

    def test_document_save(self):
        '''
Test that data can be added to document with a documnet based save 

my_blitzdb.begin()
my_doc = MyDocument({'a':'a', 'b':'b'})
my_doc.save(my_blitsdb)
my_blitzdb.commit()
        '''

        r = requests.get('http://127.0.0.1:5000/docsave/docsave/a/b/c')
        
        if r.status_code == 200:
            # Get JSON fron request
            request_json = r.json()

            # Connect to db and get record
            file_backend = blitzdb.FileBackend('./test_app.db')
            db_query = dict(
                file_backend.get(test_model.TestDoc, {'name': 'docsave'})
            )

            self.assertEqual(request_json, db_query)
        else:
            raise Exception

        r.close()

    def test_db_save(self):
        '''
Test that data can be added to document with a backend based save 

my_blitzdb.begin()
my_doc = MyDocument({'a':'a', 'b':'b'})
my_blitsdb.save(my_doc)
my_blitzdb.commit()
        '''

        r = requests.get('http://127.0.0.1:5000/dbsave/dbsave/a/b/c')

        if r.status_code == 200:
            # Get JSON from request
            request_json = r.json()

            # Connect to db and get record
            file_backend = blitzdb.FileBackend('./test_app.db')
            db_query = dict(file_backend.get(test_model.TestDoc, {'name': 'dbsave'}))
            self.assertEqual(request_json, db_query)
        else:
            raise Exception

        r.close()

if __name__ == '__main__':
    import pdb
    pdb.run('unittest.main()')