import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from models import setup_db, db_path, Category, Note
from auth import AuthError, requires_auth


def create_app(test_config=None, database_path=db_path):
    # create and configure the app
    app = Flask(__name__)
    app.config["SQLAlCHEMY_DATABASE_URI"] = database_path
    setup_db(app, database_path)
    CORS(app)

    # ROUTES
    # GET /categories
    @app.route('/categories')
    @requires_auth(permission='get:categories')
    def get_categories(permission):
        categories = Category.query.all()
        return jsonify({'success': True}), 200

    # GET /notes
    @app.route('/notes')
    @requires_auth(permission='get:notes')
    def get_notes(permission):
        notes = Note.query.all()
        return jsonify({'success': True}), 200

    # POST /notes
    @app.route('/notes', methods=['POST'])
    @requires_auth(permission='post:notes')
    def post_notes(permission):
        title = request.json.get('title')
        description = request.json.get('description')
        if not title or not description:
            abort(400)
        description_string = str(description).replace("\'", "\"")
        new_note = Note(title=title, description=description_string)
        new_note.insert()
        return jsonify({'success': True}), 200

    # POST /categories
    @app.route('/categories', methods=['POST'])
    @requires_auth(permission='post:catagories')
    def post_categories(permission):
        description = request.json.get('description')
        if not description:
            abort(400)
        description_string = str(description).replace("\'", "\"")
        new_category = Category(description=description_string)
        new_category.insert()
        return jsonify({'success': True}), 200

    # PATCH /notes/<id>
    # if id not found return 404 error
    @app.route('/notes/<int:note_id>', methods=['PATCH'])
    @requires_auth(permission='patch:notes')
    def patch_notes(permission, note_id):
        note = Note.query.filter(Note.id == note_id).one_or_none()
        if not note:
            abort(404)
        title = request.json.get('title')
        if title:
            note.title = title
        description = request.json.get('description')
        if description:
            description_string = str(description).replace("\'", "\"")
            note.description = description_string
        note.update()
        return jsonify({'success': True, 'modify': note_id}), 200

    # PATCH /categories/<id>
    # if id not found return 404 error
    @app.route('/categories/<int:category_id>', methods=['PATCH'])
    @requires_auth(permission='patch:categories')
    def patch_categories(permission, category_id):
        category = Category.query.filter(
            Category.id == category_id).one_or_none()
        if not category:
            abort(404)
        description = request.json.get('description')
        if description:
            description_string = str(description).replace("\'", "\"")
            category.description = description_string
        description.update()
        return jsonify({'success': True, 'modify': note_id}), 200

    # DELETE /notes/<id>
    # if id not found return 404 error
    @app.route('/notes/<int:note_id>', methods=['DELETE'])
    @requires_auth(permission='delete:notes')
    def delete_notes(permission):
        note = Note.query.filter(Note.id == note_id).one_or_none()
        if not note:
            abort(404)
        note.delete()
        return jsonify({'success': True, 'delete': note_id}), 200


    # DELETE /categories/<id>
    # if id not found return 404 error
    @app.route('/categories/<int:category_id>', methods=['DELETE'])
    @requires_auth(permission='delete:categories')
    def delete_categories(permission):
        category = Category.query.filter(
            Category.id == category_id).one_or_none()
        if not category:
            abort(404)
        category.delete()
        return jsonify({'success': True, 'delete': category_id}), 200

    # search note
    @app.route('/notes')
    @requires_auth(permission='get:notes')
    def search_notes(permission):
        search = request.json.get('searchTerm')
        if search:
            options = Note.query.filter(Note.title.ilike(f'%{search}%'))
            search_count = options.count()
            current_search = [option.format() for option in options]
        return jsonify({
            'success': True, 'search': current_search,
            'result': search_count}), 200


    # ERROR HANDLING
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            'success': False, 'error': 400, 'message': 'BAD REQUEST'})

    @app.errorhandler(403)
    def forbidden(error):
        return jsonify({
            'success': False, 'error': 403, 'message': 'FORBIDDEN'})

    @app.errorhandler(404)
    def request_not_found(error):
        return jsonify({
            'success': False, 'error': 404, 'message': 'REQUEST NOT FOUND'})

    @app.errorhandler(422)
    def request_unprocessable(error):
        return jsonify({
            'success': False, 'error': 422, 'message': 'REQUEST CAN NOT BE PROCESSED'})

    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({
            'success': False, 'error': 500, 'message': 'INTERNAL SERVER ERROR'})

    @app.errorhandler(AuthError)
    def authorization_error(error):
        return jsonify({
            'success': False,
            'error': error.status_code,
            'message': 'YOU ARE NOT AUTHORIZED TO ACCESS THIS PAGE'}), error.status_code

    return app

APP = create_app()

if __name__ == '__main__':
    APP.run(debug=True)