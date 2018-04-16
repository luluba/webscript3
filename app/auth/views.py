from . import auth
import os

import flask
import requests
from flask_login import current_user, login_user, logout_user
from apiclient import discovery
from oauth2client import client
from oauth2client.client import Storage
import httplib2
from json2html import *
from ..utils import User

import sys

lib_path = os.path.abspath("../../../../kogo")
sys.path.append(lib_path)
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
    pass

@auth.route('/signout')
def signout():
    pass

@auth.route('/authorize')
def authorize():
    #Create flow instance to manage the OAuth 2.0 Authorization Grant Flow steps.
    flow = client.flow_from_clientsecrets(CLIENT_SECRETS_FILE, scope=SCOPES, redirect_uri=flask.url_for('.oauth2callback', _external=True))
    auth_uri = flow.step1_get_authorize_url()

    return flask.redirect(auth_uri)


@auth.route('/oauth2callback')
def oauth2callback():
    flow = client.flow_from_clientsecrets(CLIENT_SECRETS_FILE, scope=SCOPES, redirect_uri=flask.url_for('.oauth2callback', _external=True))
    error = flask.request.args.get('error')
    if error is not None:
        return ("Failed to get credentials with error = ", error)

    code = flask.request.args.get('code')

    # Store credentials in the session.
    # ACTION ITEM: In a production auth, you likely want to save these
    #              credentials in a persistent database instead.

    credentials = flow.step2_exchange(code)
    flask.session['credentials'] = credentials.to_json()

    return flask.redirect('list')


@auth.route('/revoke')
def revoke():
    if 'credentials' not in flask.session:
        return ('You need to <a href="/authorize">authorize</a> before ' +
                'testing the code to revoke credentials.')

    credentials = client.OAuth2Credentials.from_json(flask.session['credentials'])
    if not credentials.refresh_token:
        try:
            credentials.revoke(httplib2.Http())
        except Exception:
            response = requests.get(
                  credentials.revoke_uri + '?token=' + credentials.access_token)
 
    #clear the session
    clear_credentials()
    return ("Credentials have been revoked.<br><br>")

@auth.route('/clear')
def clear_credentials():
    if 'credentials' in flask.session:
        del flask.session['credentials']
    return ('Credentials have been cleared.<br><br>')

@auth.route('/list')
def list():
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
            del order_info["is_order"]
            order_infos.append(order_info)

    input = {
        "your orders": order_infos
    } 
    output = json2html.convert(json=input)
    return output 


