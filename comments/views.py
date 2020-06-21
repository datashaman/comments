from flask_resty import GenericModelView

from . import models, schemas

class SiteViewBase(GenericModelView):
    model = models.Site
    schema = schemas.SiteSchema()

class SiteListView(SiteViewBase):
    def get(self):
        return self.list()

    def post(self):
        return self.create()

class SiteView(SiteViewBase):
    def get(self, id):
        return self.retrieve(id)

    def patch(self, id):
        return self.update(id, partial=True)

    def delete(self, id):
        return self.destroy(id)

class UserViewBase(GenericModelView):
    model = models.User
    schema = schemas.UserSchema()

class UserListView(UserViewBase):
    def get(self):
        return self.list()

    def post(self):
        return self.create()

class UserView(UserViewBase):
    def get(self, id):
        return self.retrieve(id)

    def patch(self, id):
        return self.update(id, partial=True)

    def delete(self, id):
        return self.destroy(id)

class TopicViewBase(GenericModelView):
    model = models.Topic
    schema = schemas.TopicSchema()

class TopicListView(TopicViewBase):
    def get(self):
        return self.list()

    def post(self):
        return self.create()

class TopicView(TopicViewBase):
    def get(self, id):
        return self.retrieve(id)

    def patch(self, id):
        return self.update(id, partial=True)

    def delete(self, id):
        return self.destroy(id)

class CommentViewBase(GenericModelView):
    model = models.Comment
    schema = schemas.CommentSchema()

class CommentListView(CommentViewBase):
    def get(self):
        return self.list()

    def post(self):
        return self.create()

class CommentView(CommentViewBase):
    def get(self, id):
        return self.retrieve(id)

    def patch(self, id):
        return self.update(id, partial=True)

    def delete(self, id):
        return self.destroy(id)
