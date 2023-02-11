'''
Here we calculate the different profits and the maths behind everything
'''
multicraft_cocina = 3.2
resourceful_cocina = 9.9
proc = 1 - multicraft_cocina/100 - resourceful_cocina/100

def festin(precios):
    '''
    Prices are an iterable list in the following order: ,'Grand Banquet of the Kaluak','Frosted Rimefin Tuna','Riverside Picnic', and its reagents,'Aromatic Seafood Platter',and its reagents,'Thousandbone Tongueslicer', and its reagents,'Basilisk Eggs','Snow in a Cone', and its reagents
    '''
    c_festin = precios[0]
    c_craft_riverside = 4 * precios[4] + precios[5] + precios[3]
    c_craft_aromatic = precios[7] + precios[8] + 3 * precios[11] + precios[12]
    c_craft_tongue = precios[10] + precios[5] + 3 * precios[11] + precios[12]
    c_craft_cone = 3 * precios[15] + 2 * precios[17] + precios[16]
    c_basilisk = precios[13]
    c_tuna = precios[1]

    costo_total_crafteo = round(c_craft_riverside + 6 * c_craft_aromatic/4 + 6 * c_craft_tongue/4 + 3 * c_craft_cone/4 + 2 * c_tuna + 6 * c_basilisk,2)
    costo_total_crafteo_procs = round(((c_craft_riverside + 6 * c_craft_aromatic/4 + 6 * c_craft_tongue/4 + 3 * c_craft_cone/4)*proc + 2 * c_tuna + 6 * c_basilisk)*proc,2)

    profit = round(c_festin * 2 - costo_total_crafteo,2)
    profit_procs = round(c_festin * 2 - costo_total_crafteo_procs,2)
    
    profit_individual = {
                        'riverside':round(4*precios[2]-c_craft_riverside*proc,2),
                        'aromatic':round(4*precios[6]-c_craft_aromatic*proc,2),
                        'tongue':round(4*precios[9]-c_craft_tongue*proc,2),
                        'cone':round(4*precios[14]-c_craft_cone*proc,2),
    }
    return costo_total_crafteo, profit, profit_individual


def cloth_shuffle(precios):
    '''
    Prices are an iterable list in the following order: ,'Tattered Wildercloth','Wildercloth','Dust','Shard'
    '''

    dust_qty = 1.9
    shard_qty = 0.86
    costo_per_item = round(4 * precios[0] + 4 * precios [1],2)
    ganancia_per_item = dust_qty * precios[2] + shard_qty * precios[3]
    profit = round(ganancia_per_item - costo_per_item,2)
    
    return costo_per_item, profit
