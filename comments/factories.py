import factory

from comments.models import db, Site, User, Topic, Comment
from factory.alchemy import SESSION_PERSISTENCE_COMMIT

class SiteFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Site
        sqlalchemy_session = db.session
        sqlalchemy_session_persistence = SESSION_PERSISTENCE_COMMIT

    url = factory.Faker('url')

class UserFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = User
        sqlalchemy_session = db.session
        sqlalchemy_session_persistence = SESSION_PERSISTENCE_COMMIT

    email = factory.Faker('email')
    site = factory.SubFactory(SiteFactory)
    username = factory.Faker('user_name')
    url = factory.Faker('url')

class TopicFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Topic
        sqlalchemy_session = db.session
        sqlalchemy_session_persistence = SESSION_PERSISTENCE_COMMIT

    url = factory.Faker('url')

class CommentFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Comment
        sqlalchemy_session = db.session
        sqlalchemy_session_persistence = SESSION_PERSISTENCE_COMMIT

    text = factory.Faker('text')
    topic = factory.SubFactory(TopicFactory)
    user = factory.SubFactory(UserFactory)
