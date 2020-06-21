from comments.models import Site, User, Topic, Comment
from comments.services import ma

from marshmallow import fields, validate
from marshmallow_sqlalchemy import auto_field

class CommentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Comment

    text = auto_field(validate=validate.Length(min=1))

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User

    username = auto_field(validate=validate.Length(min=6))
    email = auto_field(validate=validate.Email())
    url = auto_field(validate=validate.URL(relative=False, require_tld=True))

    comments = fields.List(fields.Nested(CommentSchema))

    _links = ma.Hyperlinks({
        'self': ma.AbsoluteURLFor('user', id='<id>'),
    })

class TopicSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Topic

    _links = ma.Hyperlinks({
        'self': ma.AbsoluteURLFor('topic', id='<id>'),
    })

    comments = fields.List(fields.Nested(CommentSchema))

class SiteSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Site
        include_fk = True

    url = auto_field(validate=validate.URL(relative=False, require_tld=True))

    _links = ma.Hyperlinks({
        'self': ma.AbsoluteURLFor('site', id='<id>'),
        'collection': ma.AbsoluteURLFor('sites'),
    })

    topics = fields.List(fields.Nested(TopicSchema))
    users = fields.List(fields.Nested(UserSchema))
