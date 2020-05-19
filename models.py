import os
from flask_sqlalchemy import SQLAlchemy

# database for local development
# db_name = 'notebook'
# database_path = 'postgres://postgres:123456@{}/{}'.format('localhost:5432', db_name)

# database for production
database_path = os.environ['DATABASE_URL']

db = SQLAlchemy()

# setting up SQLALchemy
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


class Category(db.Model):
    __tablename__ = "category"
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(50), nullable=False)
    note = db.relationship('Note', backref="category", lazy=True)

    def __init__(self, description):
        self.description = description

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def format(self):
        return({
            'id': self.id,
            'description': self.description,
        })



class Note(db.Model):
    __tablename__ = "note"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True)
    description = db.Column(db.String, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)


    def __init__(self, title, description, category):
        self.title = title
        self.description = description
        self.category_id = category
    
    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def format(self):
        return{
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'category': self.category_id
        }
