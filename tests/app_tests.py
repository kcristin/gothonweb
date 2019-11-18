from nose.tools import *
from gothonweb.app import app

app.config['TESTING'] = True
web = app.test_client()

def test_index():
    rv = web.get('/', follow_redirects=True)
    ok_(rv.status_code, 404)

    rv = web.get('/game', follow_redirects=True)
    ok_(rv.status_code, 200)

def test_game():
    rv = web.get('/game', follow_redirects=True)
    
