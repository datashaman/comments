import faker
import flask

from comments.factories import SiteFactory
from comments.models import Site
from flask_resty.testing import assert_response, assert_shape
from unittest.mock import ANY

def test_list(client):
    count = 10
    sites = SiteFactory.create_batch(count)
    response = client.get('/sites/')
    assert_response(response, 200, [{'id': site.id, 'url': site.url, 'origins': None} for site in sites])

def test_create(client):
    data = vars(SiteFactory.stub())
    response = client.post('/sites/', data=data)
    assert_response(response, 201, data)

def test_create_with_origin(client):
    data = vars(SiteFactory.stub(origins=['http://example.com']))
    response = client.post('/sites/', data=data)
    assert_response(response, 201, data)

def test_create_with_origins(client):
    data = vars(SiteFactory.stub(origins=['http://example.com', 'https://example.com']))
    response = client.post('/sites/', data=data)
    assert_response(response, 201, data)

def test_retrieve(client):
    site = SiteFactory.create()
    response = client.get('/sites/%s' % site.id)
    assert_response(response, 200, {'id': site.id, 'url': site.url, 'origins': None})

def test_update(client):
    site = SiteFactory.create()
    data = {
        'id': site.id,
        'url': 'http://example.com',
    }
    response = client.patch('/sites/%s' % site.id, data=data)
    assert_response(response, 200, {'id': site.id, 'url': 'http://example.com'})
