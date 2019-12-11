import json
from fork import app
from unittest.mock import Mock, patch

client = app.test_client()

@patch('fork.github')
def test_index_not_authorized(mock_github):
    mock_github.authorized = False
    resp = client.get('/')
    assert resp.status_code == 302 # Redirect

@patch('fork.github')
def test_index_authorized(mock_github):
    mock_github.authorized = True
    mock_github.get.return_value.json.return_value="username"
    resp = client.get('/')
    assert resp.status_code == 200 # OK

@patch('fork.github')
def test_fork_invalid_github_request(mock_github):
    mock_github.post.return_value.ok = False
    mock_github.post.return_value.raise_for_status.return_value = 'invalid request'
    resp = client.post('/fork')
    data = json.loads(resp.data)
    assert data['success'] == False
    assert data['error'] == 'invalid request'
    assert resp.status_code == 200 # OK

@patch('fork.github')
def test_fork_valid_github_request(mock_github): 
    mock_github.post.return_value.ok = True
    resp = client.post('/fork')
    data = json.loads(resp.data)
    assert data['success'] == True
    assert resp.status_code == 200 # OK


