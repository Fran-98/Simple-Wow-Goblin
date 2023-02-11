from blizzardapi import BlizzardApi
''' 
Just a tool for looking the realm id and connected realm id from the api

ONLY USED WHEN YOU WANT TO SEARCH FOR YOUR IDs
'''
client_id = '111111111111111111111111111111' #Use yours, strongly recommended to save it in a env variable
client_secret = '1111111111111111111111111111111111' #Use yours, strongly recommended to save it in a env variable
region = "us"
locale = "en_US"
connected_realm_id = 1

api_client = BlizzardApi(client_id, client_secret)
# Unprotected API endpoint
index = api_client.wow.game_data.get_connected_realms_index(region, locale)
realmlist = []

for CR in index['connected_realms']:
  x = CR['href'].replace('https://us.api.blizzard.com/data/wow/connected-realm/','')
  x = x.replace('?namespace=dynamic-us','')
  realmlist.append(int(x))
print(realmlist)

for i in realmlist:
  connected_realms = api_client.wow.game_data.get_connected_realm(region,locale,i)
  print(connected_realms)
  if len(connected_realms) == 3:
    print('{} no'.format(i))
  else:
    for realm in connected_realms['realms']:
      print(realm['name'])
'''
https://develop.battle.net/documentation/guides/using-oauth/client-credentials-flow
https://medium.com/quick-code/absolute-beginners-guide-to-slaying-apis-using-python-7b380dc82236#:~:text=To%20interact%20with%20an%20API,in%20an%20organized%2C%20logical%20manner.
https://sqqihao.github.io/trillworks.html
https://develop.battle.net/documentation/guides/getting-started

https://github.com/lockwooddev/python-wowapi/blob/master/wowapi/api.py
'''

