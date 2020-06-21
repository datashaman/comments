import uuid

from sqlalchemy.sql import func
from sqlalchemy_utils import ScalarListType, Timestamp, UUIDType

from comments.services import db

class Site(db.Model, Timestamp):
    id = db.Column(UUIDType(binary=False), default=uuid.uuid4, primary_key=True)

    url = db.Column(db.String(120), unique=True, nullable=False)
    origins = db.Column(ScalarListType())

    def __repr__(self):
        return '<Site %r>' % self.url

    def __json__(self):
        return self.__dict__

class User(db.Model, Timestamp):
    id = db.Column(UUIDType(binary=False), default=uuid.uuid4, primary_key=True)

    site_id = db.Column(UUIDType(binary=False), db.ForeignKey('site.id'), nullable=False)
    site = db.relationship('Site', backref=db.backref('users', lazy=True))

    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True)
    url = db.Column(db.String)

    def __repr__(self):
        return '<User %r>' % self.username

    def __json__(self):
        return self.__dict__

class Topic(db.Model, Timestamp):
    id = db.Column(UUIDType(binary=False), default=uuid.uuid4, primary_key=True)

    site_id = db.Column(UUIDType(binary=False), db.ForeignKey('site.id'), nullable=False)
    site = db.relationship('Site', backref=db.backref('topics', lazy=True))

    url = db.Column(db.String, nullable=False)

class Comment(db.Model, Timestamp):
    id = db.Column(UUIDType(binary=False), default=uuid.uuid4, primary_key=True)

    topic_id = db.Column(UUIDType(binary=False), db.ForeignKey('topic.id'), nullable=False)
    topic = db.relationship('Topic', backref=db.backref('comments', lazy=True))

    parent_id = db.Column(UUIDType(binary=False), db.ForeignKey('comment.id'))
    replies = db.relationship('Comment', backref=db.backref('parent', remote_side=[id]))

    user_id = db.Column(UUIDType(binary=False), db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('comments', lazy=True))

    text = db.Column(db.Text(), nullable=False)
    status = db.Column(db.String(20), default='pending', nullable=False)

    def __repr__(self):
        return '<Comment %r>' % self.text

    def __json__(self):
        return self.__dict__
