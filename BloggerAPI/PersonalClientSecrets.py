#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import os
import apiclient
import httplib2
from oauth2client import tools, file

from oauth2client import client

CLIENT_SECRETS = os.path.join(os.path.dirname(__file__), 'client_secrets.json')

# Set up a Flow object to be used for authentication.
# Add one or more of the following scopes. PLEASE ONLY ADD THE SCOPES YOU
# NEED. For more information on using scopes please see
# <https://developers.google.com/+/best-practices>.
FLOW = client.flow_from_clientsecrets(CLIENT_SECRETS,
  scope=[
      'https://www.googleapis.com/auth/drive',
      'https://www.googleapis.com/auth/drive.appdata',
      'https://www.googleapis.com/auth/drive.apps.readonly',
      'https://www.googleapis.com/auth/drive.file',
      'https://www.googleapis.com/auth/drive.metadata.readonly',
      'https://www.googleapis.com/auth/drive.readonly',
      'https://www.googleapis.com/auth/drive.scripts',
      'https://www.googleapis.com/auth/blogger'
    ],
    message=tools.message_if_missing(CLIENT_SECRETS))

def init_google_api():
    storage = file.Storage('sample.dat')
    credentials = storage.get()
    if credentials is None or credentials.invalid:
        # Parser for command-line arguments.
        parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter, parents=[tools.argparser])
        flags = parser.parse_args([])
        credentials = tools.run_flow(FLOW, storage,flags)

    http = httplib2.Http()
    http = credentials.authorize(http)
    return http
