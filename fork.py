from flask import Flask, Response, session, redirect, request, flash, url_for
from flask_dance.contrib.github import make_github_blueprint, github 
import json, os

app = Flask(__name__)
app.secret_key = os.environ['FLASK_SECRET'] 

# setup oauth access for Github
blueprint = make_github_blueprint(
    client_id=os.environ['GITHUB_CLIENT_ID'], 
    client_secret=os.environ['GITHUB_CLIENT_SECRET'],
    scope='repo',
)
app.register_blueprint(blueprint, url_prefix='/login')

@app.route('/')
def index():
    """Display an html form to trigger the fork process. 
    Requires login via Github oauth."""
    
    if not github.authorized:
        return redirect(url_for('github.login'))

    try:
        response = github.get('/user')
        username = response.json()['login']
    except: 
        # If github_authorized, with scope='repo', username should always be defined
        username = 'oauth_error'

    html = """
        <h1>Hello. So you want to fork?</h1>
        <p>You are @{uname} on GitHub.</p>
        <form method="PUT" action="/fork">
        <p>Please enter the username and repository that you would like to fork.</p>
        <label for="username">Username: <input type="input" name="username">
        <label for="repository">Repository: <input type="input" name="repository">
        <input type="submit" value="Fork">
        </form>
        """
    return html.format(uname=username)

@app.route('/fork', methods=['PUT']) 
def fork():
    """Endpoint for fork service. 
    Service is idempotent; can be called multiple times in the event of a time-out or transmission error."""
    try:
        uname = request.form.get('username')
        repos = request.form.get('repository')
        response = github.post('/repos/%s/%s/forks'%(uname, repos))  
        if not response.ok:
            raise Exception(response.raise_for_status())
        data = {'success':True}
    except Exception as e:
        data = {'success':False,'error':str(e)}

    return Response(json.dumps(data), mimetype='application/json')
