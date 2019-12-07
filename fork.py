from flask import Flask, session, redirect, flash, url_for
from flask_dance.contrib.github import make_github_blueprint, github 

app = Flask(__name__)
app.secret_key = 'expialadocious'
blueprint = make_github_blueprint(
    client_id='a79f2f917eaff7383909',
    client_secret='2228fffc207476054bb8cd7c54eefffc8ce0b989',
)
app.register_blueprint(blueprint, url_prefix='/login')

@app.route('/fork/<username>/<repo>')
def fork(username, repo):
    if not github.authorized:
        return redirect(url_for('github.login'))
    resp = github.get('/user')
    assert resp.ok
    return 'You are @{login} on GitHub'.format(login=resp.json()['login'])

@app.route('/')
def index():
	return 'Try: /fork/username/repo-to-fork'
