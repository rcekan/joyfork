# joyfork
Github fork service for Healthjoy coding assessment. 

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

6) Push code to Heroku
$ git push heroku master
