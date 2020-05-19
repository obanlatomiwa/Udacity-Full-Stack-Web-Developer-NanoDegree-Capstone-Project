import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from models import Note, Category, setup_db
from app import create_app
from models import db


class NotebookTestCase(unittest.TestCase):

    def setUp(self):
        '''define test variables and initialize app'''

        self.app = create_app()
        self.client = self.app.test_client
        setup_db(self.app)
        db.create_all()

        self.new_category = {
            'description': 'Personal',
        }

        self.new_note = {
            'title': 'My Experience',
            'description': 'It began 5 years ago..',
            'category_id': 1
        }

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        pass

    def test_get_categories(self):
        res = self.client().get('/categories')
        self.assertEqual(res.status_code, 200)

    def test_get_categories_fail(self):
        res = self.client().get('/categoriess')
        self.assertEqual(res.status_code, 404)

    def test_get_notes(self):
        res = self.client().get('/notes')
        self.assertEqual(res.status_code, 200)

    def test_get_notes(self):
        res = self.client().get('/notess')
        self.assertEqual(res.status_code, 404)

    def test_create_category(self):
        res = self.client().post('/categories', json=self.new_category)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['new_category']['description'], 'Personal')

    def test_create_note(self):
        res = self.client().post('/notes', json=self.new_note)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['new_note']['title'], 'My Experience')

    def test_patch_category(self):
        res = self.client().patch('/categories/1', json=self.new_category)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_patch_category_fail(self):
        res = self.client().patch('/categories/1000', json=self.new_category)
        self.assertEqual(res.status_code, 404)

    def test_patch_note(self):
        res = self.client().patch('/notes/1', json=self.new_note)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_patch_note_fail(self):
        res = self.client().patch('/notes/1000', json=self.new_note)
        self.assertEqual(res.status_code, 404)

    def test_delete_category(self):
        res = self.client().delete('/categories/1')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_delete_category_fail(self):
        res = self.client().delete('/categories/100')
        self.assertEqual(res.status_code, 404)

    def test_delete_note(self):
        res = self.client().delete('/notes/1')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_delete_note_fail(self):
        res = self.client().delete('/notes/100')
        self.assertEqual(res.status_code, 404)


if __name__=="__main__":
    unittest.main()