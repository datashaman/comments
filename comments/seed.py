import random

from comments import app
from comments.factories import SiteFactory, UserFactory, TopicFactory, CommentFactory
from comments.models import db

with app.app_context():
    db.create_all()

    for site in SiteFactory.create_batch(3):
        topics = TopicFactory.create_batch(random.randint(3, 10), site=site)
        for user in UserFactory.create_batch(random.randint(1, 10), site=site):
            for topic in topics:
                CommentFactory.create_batch(random.randint(0, 5), topic=topic, user=user)
