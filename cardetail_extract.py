
def cardetail(df):
    
    import pandas as pd
    import json 
    
    #replace single quote with double quote to make everything as json and replace none with 1
    df.new_car_detail=df['new_car_detail'].apply(lambda x : json.loads(x.replace("'",'"').replace('None',"1")))
    
    cars_detail = {'it': [], 'ft': [], 'bt': [], 'km': [], 'transmission': [], 'ownerNo': [], 'owner': [],
                  'oem': [], 'model': [], 'modelYear': [], 'centralVariantId': [], 'variantName': [],
                  'price': [], 'priceActual': [], 'priceSaving': [],
                  'priceFixedText': [], 'trendingText': [] } #dict.fromkeys(unique_detail_keys, [])

    #taking out all the values and appending them in cars_detail
    for detail in df['new_car_detail']:

        for key in cars_detail.keys():
            
            if key in detail.keys():
                cars_detail[key].append(detail[key])
        
    return pd.DataFrame(cars_detail)


