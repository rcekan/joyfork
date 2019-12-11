# joyfork
Github fork service for Healthjoy coding assessment. 


GOAL ==================================================

Write a web service which provides an endpoint that a user can trigger from within a web browser.
Endpoint should respond only to safe HTTP methods. (i.e., POST/PUT/PATCH)
Please explain your decision of choosing a HTTP method.
By triggering the endpoint service, a user can fork it's own Github repo to the user’s account.


Solution ==============================================

Will use PUT. Idempotent in nature. Eg, we can call many times, if it times out, no problem. Just call again.
Note: Github API docs specify using POST to create a fork. https://developer.github.com/v3/repos/forks/
However after testing, there are no additional side-effects when called multiple times. 
While it is possible the Github API may change at any time and doesn't guarantee idempotent behavior for forking, 
I feel PUT more accurately reflects the current nature of the service. 

Also note, Idempotent is not the same as safe. A safe method has no side-effects. This service however, most certainly has a side-effect (forking a repo). 


Deploy Instructions ====================================

Code requires the following environment variables to be defined:
FLASK_SECRET, GITHUB_CLIENT_ID, and GITHUB_CLIENT_SECRET (instructions below, don't worry)
Refer to fork.py for more details on their usage.
Deployment is otherwise straightforward.

Heroku Deployment --------------------------------------
Below are instruction for deploying to a free tier Heroku account.

0) Checkout this code to your local machine if you haven't done so already

1) Create a new app at Heroku

2) Register your new app for Github oauth
Here: https://github.com/settings/applications/new

  Use following
  homepage: https://APPNAME.herokuapp.com/
  callback: https://APPNAME.herokuapp.com/login/github/authorized

  For local testing use:
  callback: http://127.0.0.1:5000/login/github/authorized

Where APPNAME refers to the name of the Heroku app in step #1.
Save the client_id, and client_secret for step #5.

3) Install Heroku CLI
Instructions here: https://devcenter.heroku.com/articles/heroku-cli

4) Initialize Heroku CLI
$ heroku login

5) Set Heroku config vars
Using the oauth registration from step #2, along with the Heroku app name from step #1:
$ heroku config:set FLASK_SECRET=anything_you_want GITHUB_CLIENT_ID=xxxxxxxxxxxxxxxxxxx GITHUB_CLIENT_SECRET=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx -app your_heroku_appname

For local testing, don't forget to set environment variables locally!
Oh yes, and you must add this tricky variable as well for local testing (without https): 
$ export OAUTHLIB_INSECURE_TRANSPORT=true

6) Push code to Heroku
$ git push heroku master
