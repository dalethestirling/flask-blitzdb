import unittest
import blitzdb
import requests
import test_model
import json

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

        import flask_test_app

        test_app = flask_test_app.app.test_client()
        test_response = test_app.get('/docsave/docsave/a/b/c', follow_redirects=True)

        if test_response.status == '200 OK':
            # Get JSON fron request
            response_data = json.loads(test_response.data)

            # Connect to db and get record
            file_backend = blitzdb.FileBackend('./test_app.db')
            db_query = dict(
                file_backend.get(test_model.TestDoc, {'name': 'docsave'})
            )

            self.assertEqual(response_data, db_query)
        else:
            raise Exception

    def test_db_save(self):
        '''
Test that data can be added to document with a backend based save 

my_blitzdb.begin()
my_doc = MyDocument({'a':'a', 'b':'b'})
my_blitsdb.save(my_doc)
my_blitzdb.commit()
        '''

        import flask_test_app

        test_app = flask_test_app.app.test_client()
        test_response = test_app.get('/dbsave/dbsave/a/b/c', follow_redirects=True)

        if test_response.status == '200 OK':
            # Get JSON from request
            response_data = json.loads(test_response.data)

            # Connect to db and get record
            file_backend = blitzdb.FileBackend('./test_app.db')
            db_query = dict(file_backend.get(test_model.TestDoc, {'name': 'dbsave'}))
            self.assertEqual(response_data, db_query)
        else:
            raise Exception

    def test_direct_get(self):
        '''
A direct test of a get from a document class

my_blitzdb.get(MyDocument, {'name': 'docsave'})
        '''

        import flask_test_app

        test_app = flask_test_app.app.test_client()
        test_response = test_app.get('/get/dbsave')

        if test_response.status == '200 OK':
            # Get JSON from request
            response_data = json.loads(test_response.data)

            file_backend = blitzdb.FileBackend('./test_app.db')
            db_query = dict(file_backend.get(test_model.TestDoc, {'name': 'dbsave'}))
            self.assertEqual(response_data, db_query)
        else:
            raise Exception

    def test_filter_basic(self):
            '''
    A direct test of a basic filter query

    my_blitzdb.filter(MyDocument, {})
            '''

            import flask_test_app

            test_app = flask_test_app.app.test_client()
            test_response = test_app.get('/getall')

            if test_response.status == '200 OK':
                # Get JSON from request
                response_data = int(test_response.data)

                file_backend = blitzdb.FileBackend('./test_app.db')
                db_query = len(file_backend.filter(test_model.TestDoc, {}))
                self.assertEqual(response_data, db_query)
            else:
                raise Exception




if __name__ == '__main__':
    unittest.main()