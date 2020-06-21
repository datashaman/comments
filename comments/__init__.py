import flask
import os
import re

from dotenv import load_dotenv
load_dotenv()

from comments.models import Site, User, Topic, Comment
from comments.schemas import SiteSchema, UserSchema, TopicSchema, CommentSchema
from comments.services import db, ma

from marshmallow import ValidationError

def update_config_from_env(app):
    prefix = '%s_' % app.name.upper()
    for key, value in os.environ.items():
        match = re.match(r'^%s(.*)' % prefix, key)
        if match:
            app.config[match.group(1)] = value

app = flask.Flask(__name__)
update_config_from_env(app)

with app.app_context():
    db.init_app(app)
    db.create_all()
    ma.init_app(app)

@app.route('/')
def home():
    return flask.redirect(flask.url_for('sites'))

@app.route('/sites')
def sites():
    return SiteSchema(many=True, exclude=('topics', 'users')).jsonify(Site.query.all())

@app.route('/sites/<id>')
def site(id):
    return SiteSchema(exclude=('topics.comments', 'users.comments')).jsonify(Site.query.get(id))

@app.route('/sites', methods=['POST'])
def new_site():
    json_input = flask.request.get_json()
    if not json_input:
        return {'message': 'No input data'}, 400

    site_schema = SiteSchema(exclude=('topics.comments', 'users.comments'))

    try:
        data = site_schema.load(json_input)
    except ValidationError as err:
        return err.messages, 422
    site = Site(**data)
    db.session.add(site)
    db.session.commit()

    return site_schema.jsonify(Site.query.get(site.id))

@app.route('/sites/<id>', methods=['PUT'])
def update_site(id):
    json_input = flask.request.get_json()
    if not json_input:
        return {'message': 'No input data'}, 400

    site_schema = SiteSchema(exclude=('topics.comments', 'users.comments'))

    try:
        data = site_schema.load(json_input)
    except ValidationError as err:
        return err.messages, 422
    site = Site.query.get(id)
    site.url = data['url']
    db.session.add(site)
    db.session.commit()

    return site_schema.jsonify(Site.query.get(site.id))

@app.route('/sites/<id>/topics')
def site_topics(id):
    return TopicSchema(many=True, exclude=('comments',)).jsonify(Site.query.get(id).topics)

@app.route('/sites/<id>/users')
def site_users(id):
    return UserSchema(many=True).jsonify(Site.query.get(id).users)

@app.route('/comments/<id>')
def comment(id):
    return CommentSchema().jsonify(Comment.query.get(id))

@app.route('/topics/<id>')
def topic(id):
    return TopicSchema().jsonify(Topic.query.get(id))

@app.route('/topics/<id>/comments')
def topic_comments(id):
    return CommentSchema(many=True).jsonify(Topic.query.get(id).comments)

@app.route('/users/<id>')
def user(id):
    return UserSchema().jsonify(User.query.get(id))

@app.route('/users/<id>/comments')
def user_comments(id):
    return CommentSchema(many=True).jsonify(User.query.get(id).comments)
