import apiteller

items = {'197794': 'Grand Banquet of the Kaluak',

        '200074': 'Frosted Rimefin Tuna',

        '197789': 'Riverside Picnic',
        '197757': 'Assorted Exotic Spices',
        '197748': 'Burly Bear Haunch',
        '194968': 'Cerulean Spinefish',

        '197783': 'Aromatic Seafood Platter',
        '194967': 'Aileron Seamoth',
        '194969': 'Temporal Dragonhead',

        '197786': 'Thousandbone Tongueslicer',
        '194966' : 'Thousandbite Piranha',
        '194968' : 'Cerulean Spinefish',
        '197756' : 'Pebbled Rock Salts',
        '194970' : 'Islefin Dorado',

        '197745': 'Basilisk Eggs',
        '197766': 'Snow in a Cone',
        '17202' : 'Snowball',
        '197751' : 'Pastry Packets',
        '197753' : 'Thaldraszian Cocoa Powder',
        #Shuffle
        '193922': 'Wildercloth',
        '193050': 'Tattered Wildercloth',
        '194123': 'Chromatic Dust',
        '194124': 'Vibrant Shard',
        '192096': 'Spool of Wilderthread',
        }

def look_com_price(com_id,commodities):
    prices = []
    for auction in commodities['auctions']:
        if auction['item']['id'] == com_id:
            prices.append(round(auction['unit_price']/10000,2))

    price = min(prices)
    name = items[str(com_id)]
    return price,name

#token = apiteller.create_access_token(client_id, client_secret)

#commodities = apiteller.auction_commodities(token)

#print(look_com_price(200074))



'''
https://develop.battle.net/documentation/guides/using-oauth/client-credentials-flow
https://medium.com/quick-code/absolute-beginners-guide-to-slaying-apis-using-python-7b380dc82236#:~:text=To%20interact%20with%20an%20API,in%20an%20organized%2C%20logical%20manner.
https://sqqihao.github.io/trillworks.html
https://develop.battle.net/documentation/guides/getting-started

https://github.com/lockwooddev/python-wowapi/blob/master/wowapi/api.py
'''

''''auctions': [{'id': 643126172, 'item': {'id': 186131, 'context': 5, 'bonus_lists': [7452, 1691], 'modifiers': [{'type': 9, 'value': 60}, {'type': 28, 'value': 2105}]}, 'buyout': 408098800, 'quantity': 1, 'time_left': 'SHORT'}, {'id': 640862186, 'item': {'id': 24671, 'context': 1, 'bonus_lists': [6654, 1681], 'modifiers': [{'type': 9, 'value': 30}, {'type': 28, 'value': 225}]}, 'buyout': 2527700, 'quantity': 1, 'time_left': 'VERY_LONG'}, {'id': 640996640, 'item': {'id': 198243, 'context': 13, 'bonus_lists': [8841, 8842, 8807], 'modifiers': [{'type': 28, 'value': 2164}, {'type': 38, 'value': 8}, {'type': 39, 'value': 47430}, {'type': 40, 'value': 620}, {'type': 41, 'value': 14}, {'type': 42, 'value': 162}]}, 'buyout': 3589900, 'quantity': 1, 'time_left': 'VERY_LONG'}, {'id': 640215338, 'item': {'id': 87455, 'bonus_lists': [6658], 'modifiers': [{'type': 9, 'value': 35}, {'type': 28, 'value': 58}]}, 'buyout': 824467100, 'quantity': 1, 'time_left': 'LONG'}, {'id': 642491332, 'item': {'id': 7611, 'context': 1, 'bonus_lists': [6655]'''