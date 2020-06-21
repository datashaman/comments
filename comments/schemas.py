import marshmallow as ma

class CommentSchema(ma.Schema):
    id = ma.fields.Integer()
    uuid = ma.fields.UUID(dump_only=True)
    topic_id = ma.fields.Integer(required=True)
    parent_id = ma.fields.Integer()
    user_id = ma.fields.Integer(required=True)
    text = ma.fields.String(required=True, validate=ma.validate.Length(min=1))
    status = ma.fields.String(dump_only=True)
    created_at = ma.fields.DateTime(dump_only=True)
    updated_at = ma.fields.DateTime(dump_only=True)

class UserSchema(ma.Schema):
    id = ma.fields.Integer()
    uuid = ma.fields.UUID(dump_only=True)
    site_id = ma.fields.Integer(required=True)
    username = ma.fields.String(required=True, validate=ma.validate.Length(min=6))
    email = ma.fields.Email()
    url = ma.fields.URL()
    created_at = ma.fields.DateTime(dump_only=True)
    updated_at = ma.fields.DateTime(dump_only=True)

    comments = ma.fields.List(ma.fields.Nested(CommentSchema))

class TopicSchema(ma.Schema):
    id = ma.fields.Integer()
    uuid = ma.fields.UUID(dump_only=True)
    site_id = ma.fields.Integer(required=True)
    url = ma.fields.URL(required=True)
    created_at = ma.fields.DateTime(dump_only=True)
    updated_at = ma.fields.DateTime(dump_only=True)

    comments = ma.fields.List(ma.fields.Nested(CommentSchema))

class SiteSchema(ma.Schema):
    id = ma.fields.Integer()
    uuid = ma.fields.UUID(dump_only=True)
    url = ma.fields.URL(required=True)
    origins = ma.fields.List(ma.fields.URL(required=True))
    created_at = ma.fields.DateTime(dump_only=True)
    updated_at = ma.fields.DateTime(dump_only=True)

    topics = ma.fields.List(ma.fields.Nested(TopicSchema))
    users = ma.fields.List(ma.fields.Nested(UserSchema))
