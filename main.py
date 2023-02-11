import auctionsearch
import apiteller
import profitcalculator

import PySimpleGUI as sg

client_id = '111111111111111111111111111111111' #Use yours, strongly recommended to save it in a env variable
client_secret = '1111111111111111111111111111111111111' #Use yours, strongly recommended to save it in a env variable
region = "us"
locale = "en_US"
connected_realm_id = 1428 # The id you got from the search

items = auctionsearch.items

token = apiteller.create_access_token(client_id, client_secret)

commodities = apiteller.auction_commodities(token)

# Token price
token_price = int(apiteller.token_price(token)['price']/10000)

calculations_colum = [[sg.Text('Festín')],
                    [sg.Text('-',key='profit_festin')],
                    [sg.Text('Gold available'), sg.Input(key='goldbox')],
                    [sg.Text('Craft '), sg.Text('',key='hm'), sg.Text(' times')],
                    [sg.Push(), sg.Text('Expected profit'), sg.Text('-',key='exprofit')],
                    [sg.Text('Time:'),sg.Text('',key='festin_time'),sg.Push(), sg.Text('',key='festin_gph')],
                    
                    [sg.Text('Shuffle de tailoring/encantamiento')],
                    [sg.Text('-',key='profit_shuffle')],
                    [sg.Text('Gold available'), sg.Input(key='shuffle_goldbox')],
                    [sg.Text('Craft '), sg.Text('',key='shuffle_hm'), sg.Text(' times')],
                    [sg.Push(), sg.Text('Expected profit'), sg.Text('-',key='shuffle_exprofit')],
                    [sg.Text('Time:'),sg.Text('',key='shuffle_time'),sg.Push(), sg.Text('',key='shuffle_gph')],
                    ]

reagents_colum = [
                [sg.Text('Riverside Picnic'), sg.Text('['), sg.Text('',key='qtyriverside'),sg.Text(']')],
                [sg.Text('Gold to craft: '),sg.Text('-',key='griverside'),sg.Text('|'),sg.Text(' Profit: '),sg.Text('-',key='priverside')],

                [sg.Text('Aromatic Seafood Platter'), sg.Text('['), sg.Text('',key='qtyaromatic'),sg.Text(']')],
                [sg.Text('Gold to craft: '),sg.Text('-',key='garomatic'),sg.Text('|'),sg.Text(' Profit: '),sg.Text('-',key='paromatic')],

                [sg.Text('Thousandbone Tongueslicer'), sg.Text('['), sg.Text('',key='qtytongue'),sg.Text(']')],
                [sg.Text('Gold to craft: '),sg.Text('-',key='gtongue'),sg.Text('|'),sg.Text(' Profit: '),sg.Text('-',key='ptongue')],

                [sg.Text('Snow in a Cone'), sg.Text('['), sg.Text('',key='qtycone'),sg.Text(']')],
                [sg.Text('Gold to craft: '),sg.Text('-',key='gcone'),sg.Text('|'),sg.Text(' Profit: '),sg.Text('-',key='pcone')],
]

shopping_colum = [
                [sg.Text('Shopping list festin')],
                [sg.Text('Tuna:'),sg.Text('',key='qtytuna')],
                [sg.Text('Assorted Exotic Spices:'),sg.Text('',key='qtyspice')],
                [sg.Text('Burly Bear Haunch:'),sg.Text('',key='qtybear')],
                [sg.Text('Cerulean Spinefish:'),sg.Text('',key='qtycerulean')],
                [sg.Text('Aileron Seamoth:'),sg.Text('',key='qtyaileron')],
                [sg.Text('Temporal Dragonhead:'),sg.Text('',key='qtytemporal')],
                [sg.Text('Thousandbite Piranha:'),sg.Text('',key='qtypiranha')],
                [sg.Text('Pebbled Rock Salts:'),sg.Text('',key='qtyrocksalt')],
                [sg.Text('Islefin Dorado:'),sg.Text('',key='qtyislefin')],
                [sg.Text('Basilisk Eggs:'),sg.Text('',key='qtybasilisk')],
                [sg.Text('Snowball:'),sg.Text('',key='qtysnowball')],
                [sg.Text('Pastry Packets:'),sg.Text('',key='qtypastry')],
                [sg.Text('Thaldraszian Cocoa Powder:'),sg.Text('',key='qtycocoa')],
]


refresh_colum = [[sg.Text('Token price:'),sg.Text(token_price)],
                [sg.Button("Refresh prices")],
                [sg.Button("How many")],
                [sg.Button('Shuffle calculation')],
                [sg.Button('Refresh AH data')],
                ]

layout = [
    [   
        sg.Column(calculations_colum),
        sg.VSeperator(),
        sg.Column(refresh_colum),
        sg.VSeperator(),
        sg.Column(reagents_colum),
        sg.VSeperator(),
        sg.Column(shopping_colum)
    ]
]

window = sg.Window(title="WoW Profit Calculator by Franman", layout=layout, margins=(100, 150))

craft_price_festin = 0 
profit_festin = 0
qtyfestin = 0
festin_time = (6+6+4+3)*2.3/3600 + 2.3 + (6+6+4+3)*2.3/3600/5

craft_price_shuffle = 0
profit_shuffle = 0
shuffle_time = 6

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        break

    if event == "Refresh prices":
        #Festin
        festin_precios = [auctionsearch.look_com_price(197794,commodities)[0],
                        #frosted tuna
                        auctionsearch.look_com_price(200074,commodities)[0],

                        #Riverside
                        auctionsearch.look_com_price(197789,commodities)[0],
                        auctionsearch.look_com_price(197757,commodities)[0], #Spice 3
                        auctionsearch.look_com_price(197748,commodities)[0], #bear 4
                        auctionsearch.look_com_price(194968,commodities)[0], #cerulean 5
                        #Aromatic
                        auctionsearch.look_com_price(197783,commodities)[0], 
                        auctionsearch.look_com_price(194967,commodities)[0], #Aileron 7
                        auctionsearch.look_com_price(194969,commodities)[0], #Temporal 8
                        #Thousandbone Tongueslicer
                        auctionsearch.look_com_price(197786,commodities)[0],
                        auctionsearch.look_com_price(194966,commodities)[0], #piranha 10
                        auctionsearch.look_com_price(197756,commodities)[0], #salt rock 11
                        auctionsearch.look_com_price(194970,commodities)[0], #islefin dorado 12
                        #Basilisk
                        auctionsearch.look_com_price(197745,commodities)[0],
                        #Snow in a cone
                        auctionsearch.look_com_price(197766,commodities)[0],
                        auctionsearch.look_com_price(17202,commodities)[0], #Snowball 15
                        auctionsearch.look_com_price(197751,commodities)[0],#Pastry packets 16
                        auctionsearch.look_com_price(197753,commodities)[0],#Thldraszian cocoa 17
                        ]

            
        craft_price_festin, profit_festin, profit_individual = profitcalculator.festin(festin_precios)
        text_profit_festin = 'Crafting price '+ str(craft_price_festin) + ' | ' + 'Profit ' + str(profit_festin)
        window['profit_festin'].update(text_profit_festin)

        window['priverside'].update(profit_individual['riverside'])
        window['paromatic'].update(profit_individual['aromatic'])
        window['ptongue'].update(profit_individual['tongue'])
        window['pcone'].update(profit_individual['cone'])

        #Shuffle
        shuffle_precios = [auctionsearch.look_com_price(193922,commodities)[0], 
                            auctionsearch.look_com_price(192096,commodities)[0], 
                            auctionsearch.look_com_price(194123,commodities)[0], 
                            auctionsearch.look_com_price(194124,commodities)[0]]

        craft_price_shuffle, profit_shuffle = profitcalculator.cloth_shuffle(shuffle_precios)
        text_profit_shuffle = 'Crafting price '+ str(craft_price_shuffle) + ' | ' + 'Profit ' + str(profit_shuffle)  
        
        window['profit_shuffle'].update(text_profit_shuffle)

    if event == "Shuffle calculation":
        gold = int(values['shuffle_goldbox'])
        qtyshuffle = int(gold/craft_price_shuffle)
        window['shuffle_hm'].update(qtyshuffle)
        window['shuffle_exprofit'].update(round(qtyshuffle*profit_shuffle,2))
        window['shuffle_time'].update(str(round(shuffle_time*qtyshuffle/3600,2))+'hrs')
        window['shuffle_gph'].update(str(round((qtyshuffle*profit_shuffle)/(shuffle_time*qtyshuffle/3600),2))+' gph')

    if event == "How many":
        gold = int(values['goldbox'])
        qtyfestin = int(gold/craft_price_festin)
        window['hm'].update(qtyfestin)
        window['exprofit'].update(round(qtyfestin*profit_festin,2))
        window['festin_time'].update(round(festin_time*qtyfestin,2))
        window['festin_gph'].update(str(round((qtyfestin*profit_festin)/(festin_time*qtyfestin),2))+' gph')

        #Calculate how many reagents to buy
        qtyriverside = qtyfestin*4
        qtyaromatic = qtyfestin*6
        qtytongue = qtyfestin*6
        qtycone = qtyfestin*3

        window['qtyriverside'].update(qtyriverside)
        window['qtyaromatic'].update(qtyaromatic)
        window['qtytongue'].update(qtytongue)
        window['qtycone'].update(qtycone)

        #Calculate reagents of reagents(?)

        window['qtytuna'].update(qtyfestin*2)
        window['qtybasilisk'].update(qtyfestin*6)

        #Riverside / cerulean tongue
        window['qtyspice'].update(qtyriverside/4)
        window['qtybear'].update(qtyriverside)
        window['qtycerulean'].update(qtyriverside/4+qtytongue/4)

        #Aromatic
        window['qtyaileron'].update(qtyaromatic/4)
        window['qtytemporal'].update(qtyaromatic/4)
        #Tongue
        window['qtypiranha'].update(qtytongue/4)
        window['qtyrocksalt'].update(qtyaromatic*3/4+qtytongue*3/4)
        window['qtyislefin'].update(qtyaromatic/4+qtytongue/4)
        #Cone
        window['qtysnowball'].update(qtycone*3/4)
        window['qtypastry'].update(qtycone/4)
        window['qtycocoa'].update(qtycone*2/4)
    
    if event == "Refresh AH data":
        commodities = apiteller.auction_commodities(token)
                
window.close()
