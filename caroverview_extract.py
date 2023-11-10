
def caroverview(df):
    
    import pandas as pd
    import json
    
    #replace single quote with double quote to make everything as json and replace none with 1
    df.new_car_overview=df['new_car_overview'].apply(lambda x : json.loads(x.replace("'",'"').replace('None',"1")))
    
    #dictionary creator for overview column
    def overview_dict_creater(overview):
        all_overviews = {}
        
        for dictionary in overview['top']:
            all_overviews.update({dictionary['key']:dictionary['value']})

        return all_overviews

    df.new_car_overview = df.new_car_overview.apply(lambda overview: overview_dict_creater(overview))
    
    print("converted dictionary---->",df.new_car_overview.to_list()[0])

    #find unique keys
    unique_overview_keys =  [ ]
    for dictionary in df.new_car_overview:
        for key in dictionary:
            if key not in unique_overview_keys:
                unique_overview_keys.append(key)

    print('all overview keys---->',unique_overview_keys)
    
    #dict.fromkeys(unique_overview_keys, [])
    overview_dict = {'Registration Year': [], 'Insurance Validity': [],'Fuel Type': [], 'Seats': [], 
                     'Kms Driven': [], 'RTO': [],'Ownership': [], 'Engine Displacement': [],'Transmission': [],
                     'Year of Manufacture': []}

    for view in df.new_car_overview:
        for key in overview_dict:
            if key in view.keys():
                overview_dict[key].append(view[key])
            else:
                overview_dict[key].append(None)
    
    
    return pd.DataFrame(overview_dict)
