'''
    This file is used to get a token from Azure.
    It didn't work for the power bi access.
'''



#27e9fb9e-9de4-4abc-9209-ae4f98cbad53 :application ID



import json
import logging
import os
import sys
import adal
from msrestazure.azure_active_directory import AADTokenCredentials


def authenticate_client_key():
    """
    Authenticate using service principal w/ key.
    """
    authority_host_uri = '#'
    tenant = '#'
    authority_uri = authority_host_uri + '/' + tenant
    resource_uri = 'https://analysis.windows.net/powerbi/api'
    client_id = '#'
    client_secret = '#'

    context = adal.AuthenticationContext(authority_uri, api_version=None)
    mgmt_token = context.acquire_token_with_client_credentials(resource_uri, client_id, client_secret)
    credentials = AADTokenCredentials(mgmt_token, client_id)

    return credentials

a = authenticate_client_key()
print(a)