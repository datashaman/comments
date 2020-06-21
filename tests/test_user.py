from comments.factories import SiteFactory, UserFactory
from flask_resty.testing import assert_response

def test_list(client):
    site = SiteFactory.create()
    count = 10
    users = UserFactory.create_batch(count, site=site)
    response = client.get('/users/')
    assert_response(response, 200, [{'id': user.id, 'url': user.url} for user in users])

def test_create(client):
    site = SiteFactory.create()
    data = {'site_id': site.id, 'username': 'JoeSoap', 'email': 'joesoap@example.com', 'url': 'https://joesoap.example.com/'}
    response = client.post('/users/', data=data)
    assert_response(response, 201, data)

def test_retrieve(client):
    user = UserFactory.create()
    response = client.get('/users/%s' % user.id)
    assert_response(response, 200, {'id': user.id, 'url': user.url})

def test_update(client):
    user = UserFactory.create()
    data = {'id': user.id, 'url': 'http://example.com'}
    response = client.patch('/users/%s' % user.id, data=data)
    assert_response(response, 200, data)

def test_destroy(client):
    user = UserFactory.create()
    response = client.delete('/users/%s' % user.id)
    assert_response(response, 204)
