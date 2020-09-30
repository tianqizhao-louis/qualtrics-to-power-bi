'''
    This file is used to get credentials from Azure.
    It requires the admin to add premissions.
'''

import adal
import requests

def get_access_token(clientId ,clientSecret):

    parameters = {
    "resource": "https://analysis.windows.net/powerbi/api",
    "tenant" : "#",
    "authorityHostUrl" : "https://login.windows.net",
    "clientId" : clientId,
    "clientSecret" : clientSecret,
     "username" : "#",
    "password" : "#,"
    }

    authority_url = (parameters['authorityHostUrl'] + '/' +
                 parameters['tenant'])

    GRAPH_RESOURCE = '00000002-0000-0000-c000-000000000000'
    RESOURCE = parameters.get('resource', GRAPH_RESOURCE)

    context = adal.AuthenticationContext(
        authority_url, validate_authority=True)

    token = context.acquire_token_with_username_password(RESOURCE,parameters['username'],parameters['password'],parameters['clientId'])

    #just an indication that that token obtained
    if 'accessToken' in token.keys():print('TOKEN OBTAINED')

    return token


# returns a token dictionary
token = get_access_token(clientId = '#',
                         clientSecret = '#')

# extracts access token
accessToken = token['accessToken']

'''

# headers dictionary
headers = {'Authorization': 'Bearer ' + accessToken, 'Content-Type': 'application/json'}

# sends request to refresh a dataset
requests.post(f'https://api.powerbi.com/v1.0/myorg/groups/{group_id}/datasets/{dataset_id}/refreshes',headers = headers)

'''