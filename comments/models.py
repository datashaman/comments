import os
import uuid

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from sqlalchemy_utils import ScalarListType, Timestamp, UUIDType, generic_repr

from . import app

db = SQLAlchemy(app)

with app.app_context():
    db.init_app(app)
    db.create_all()

@generic_repr
class Site(db.Model, Timestamp):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(UUIDType(binary=False), default=uuid.uuid4, nullable=False)

    url = db.Column(db.String(120), unique=True, nullable=False)
    origins = db.Column(ScalarListType())

@generic_repr
class User(db.Model, Timestamp):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(UUIDType(binary=False), default=uuid.uuid4, nullable=False)

    site_id = db.Column(db.Integer, db.ForeignKey('site.id'), nullable=False)
    site = db.relationship('Site', backref=db.backref('users', lazy=True))

    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True)
    url = db.Column(db.String)

@generic_repr
class Topic(db.Model, Timestamp):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(UUIDType(binary=False), default=uuid.uuid4, nullable=False)

    site_id = db.Column(db.Integer, db.ForeignKey('site.id'), nullable=False)
    site = db.relationship('Site', backref=db.backref('topics', lazy=True))

    url = db.Column(db.String, nullable=False)

@generic_repr
class Comment(db.Model, Timestamp):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(UUIDType(binary=False), default=uuid.uuid4, nullable=False)

    topic_id = db.Column(db.Integer, db.ForeignKey('topic.id'), nullable=False)
    topic = db.relationship('Topic', backref=db.backref('comments', lazy=True))

    parent_id = db.Column(db.Integer, db.ForeignKey('comment.id'))
    replies = db.relationship('Comment', backref=db.backref('parent', remote_side=[id]))

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('comments', lazy=True))

    text = db.Column(db.Text(), nullable=False)
    status = db.Column(db.String(20), default='pending', nullable=False)
