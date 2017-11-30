from . import auth
import os

import flask
import requests
from flask_login import current_user, login_user, logout_user
from apiclient import discovery
from oauth2client import client
from oauth2client.client import Storage
import httplib2
from ..utils import User

from kogo.general import email_utils
from kogo.process import order


# This variable specifies the name of a file that contains the OAuth 2.0
# information for this authlication, including its client_id and client_secret.
CLIENT_SECRETS_FILE = "client_secret.json"

# This OAuth 2.0 access scope allows for full read/write access to the
# authenticated user's account and requires requests to use an SSL connection.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
API_SERVICE_NAME = 'gmail'
API_VERSION = 'v1'

@auth.route('/signin')
def signin():
 #Create flow instance to manage the OAuth 2.0 Authorization Grant Flow steps.
	flow = client.flow_from_clientsecrets(CLIENT_SECRETS_FILE, scope=SCOPES, redirect_uri=flask.url_for('.oauth2callback', _external=True))
	auth_uri = flow.step1_get_authorize_url()

	return flask.redirect(auth_uri)

@auth.route('/signout')
def signout():
	pass

@auth.route('/oauth2callback')
def oauth2callback():
    flow = client.flow_from_clientsecrets(CLIENT_SECRETS_FILE, scope=SCOPES, redirect_uri=flask.url_for('.oauth2callback', _external=True))
     #TODO:error = flask.request.args.get('error')
    code = flask.request.args.get('code')

    # Store credentials in the session.
    # ACTION ITEM: In a production auth, you likely want to save these
    #              credentials in a persistent database instead.

    credentials = flow.step2_exchange(code)

    flask.session['credentials'] = credentials.to_json()

    gmail_svc = discovery.build(API_SERVICE_NAME, API_VERSION, credentials=credentials)
    #TODO: store it in a database
    emailAddress = gmail_svc.users().getProfile(userId='me').execute().get('emailAddress', 'unknown')

    #TODO, hack, use use LoginManager
    user = User()
    user.username = emailAddress
    user.id =2

    login_user(user)

    next = flask.request.args.get('next')

    print(current_user.is_authenticated)
    return flask.redirect(flask.url_for('main.index'))


@auth.route('/test')
def test_api_request():
    if 'credentials' not in flask.session:
      return flask.redirect('authorize')

    # Load credentials from the session.
    credentials = client.OAuth2Credentials.from_json(flask.session['credentials'])

    http_auth = credentials.authorize(httplib2.Http())
    gmail_svc = discovery.build(
      API_SERVICE_NAME, API_VERSION, credentials=credentials)
    #TODO: store it in a database
    emailAddress = gmail_svc.users().getProfile(userId='me').execute().get('emailAddress', 'unknown')
  
    results = gmail_svc.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])

    # Save credentials back to session in case access token was refreshed.
    # ACTION ITEM: In a production auth, you likely want to save these
    #              credentials in a persistent database instead.

    return flask.jsonify(*labels)


@auth.route('/list_order')
def list_order():
    if 'credentials' not in flask.session:
        return flask.redirect('authorize')

    # Load credentials from the session.
    credentials = client.OAuth2Credentials.from_json(flask.session['credentials'])

    gmail_svc = discovery.build(API_SERVICE_NAME, API_VERSION, credentials=credentials)

    # Get email ids
    response = gmail_svc.users().messages().list(userId="me", maxResults=100).execute()
    message_ids = []
    if 'messages' in response:
        message_ids.extend(response['messages'])

    # Use userId and email id to retrieve emails
    order_infos = []
    for message_id in message_ids:
        message = gmail_svc.users().messages().get(userId="me", id=message_id['id'], format="raw").execute()
        mime_message_summary = email_utils.get_mime_message(message)
        # Find and add order information
        order_info = order.find_order_info(mime_message_summary)
        if order_info.get("is_order"):
            order_infos.append(order_info)

    return flask.jsonify(*order_infos)

'''
@auth.route('/revoke')
def revoke():
  if 'credentials' not in flask.session:
    return ('You need to <a href="/authorize">authorize</a> before ' +
            'testing the code to revoke credentials.')

  credentials = google.oauth2.credentials.Credentials(
    **flask.session['credentials'])

  revoke = requests.post('https://accounts.google.com/o/oauth2/revoke',
      params={'token': credentials.token},
      headers = {'content-type': 'authlication/x-www-form-urlencoded'})

  status_code = getattr(revoke, 'status_code')
  if status_code == 200:
    return('Credentials successfully revoked.')
  else:
    return('An error occurred.')


@auth.route('/clear')
def clear_credentials():
  if 'credentials' in flask.session:
    del flask.session['credentials']
  return ('Credentials have been cleared.<br><br>')
'''
