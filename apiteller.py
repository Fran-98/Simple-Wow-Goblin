import requests
'''
Api calls
'''
def create_access_token(client_id, client_secret, region = 'us'):
    data = { 'grant_type': 'client_credentials' }
    token = requests.post('https://%s.battle.net/oauth/token' % region, data=data, auth=(client_id, client_secret))
    return token.json()

def token_price(access_token, region = 'us', locale = 'en_US'):

    headers = {
        'Authorization': "Bearer {}".format(access_token['access_token']),
    }

    params = {
        'namespace': 'dynamic-us',
        'region': region,
        'locale': locale,
    }

    response = requests.get('https://us.api.blizzard.com/data/wow/token/index', params=params, headers=headers)
    return response.json()

def auction_commodities(access_token, region = 'us', locale = 'en_US'):

    headers = {
        'Authorization': "Bearer {}".format(access_token['access_token']),
    }

    params = {
        'namespace': 'dynamic-us',
        'region': region,
        'locale': locale,
    }

    response = requests.get('https://us.api.blizzard.com/data/wow/auctions/commodities', params=params, headers=headers)
    return response.json()

