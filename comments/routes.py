import flask_resty
flask_resty.api.DEFAULT_ID_RULE = '<int:id>'

from . import app, views

api = flask_resty.Api(app)

api.add_ping('/ping/')
api.add_resource('/comments/', views.CommentListView, views.CommentView)
api.add_resource('/sites/', views.SiteListView, views.SiteView)
api.add_resource('/topics/', views.TopicListView, views.TopicView)
api.add_resource('/users/', views.UserListView, views.UserView)
