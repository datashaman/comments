from flask_resty import Api

from . import app, views

api = Api(app)

api.add_resource('/comments/', views.CommentListView, views.CommentView, id_rule='<int:id>')
api.add_resource('/sites/', views.SiteListView, views.SiteView, id_rule='<int:id>')
api.add_resource('/topics/', views.TopicListView, views.TopicView, id_rule='<int:id>')
api.add_resource('/users/', views.UserListView, views.UserView, id_rule='<int:id>')

api.add_ping('/ping/')
