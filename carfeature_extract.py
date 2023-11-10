
def carfeature(df): #returns carfeatures counts dataframe
    
    import pandas as pd
    import json
    
    #replace single quote with double quote to make everything as json and replace none with 1
    df.new_car_feature = df['new_car_feature'].apply(lambda x : json.loads(x.replace("'",'"')))
    
    #feature dictionary creator
    #creates and returns like { "Features":["value 1","value 2"],"Comfort & Convenience":["value 1","value 2"],
    # 'Interior':["value 1","value 2"],'Exterior':["value 1","value 2"],"safety": ["value 1","value 2"],
    # 'Entertainment & Media':["value 1","value 2"] }
    
    def feature_dict_creater(feature_dict): 
        
        dictionary = {}
        dictionary.update({feature_dict['heading']:[i['value'] for i in feature_dict['top']]})
        
        for sub_dict in feature_dict['data']:
            
            element_list = []
            
            for element in sub_dict['list']:
                
                element_list.append(element['value'])
            dictionary.update({sub_dict['heading']:element_list})
            element_list = []
        return dictionary

    df.new_car_feature = df.new_car_feature.apply(lambda feature_dict : feature_dict_creater(feature_dict))
    
    #print 1st row value of feature
    print("First row feature------------->",df.new_car_feature.to_list()[0])
    
    unique_feature_keys = []

    for feature in df.new_car_feature:
        for i in feature.keys():
            if i not in unique_feature_keys:
                unique_feature_keys.append(i)
    print("Unique feature keys----->",unique_feature_keys) #unique_feature_keys
    #print unique feature keys
    
    #dict.fromkeys(unique_feature_keys, [])
    #getting total counts of the individual features
    feature_count_dict = {'Features': [],
    'Comfort & Convenience': [],
    'Interior': [],
    'Exterior': [],
    'Safety': [],
    'Entertainment & Communication': []}

    for feature_dict in df.new_car_feature:
        for key in feature_count_dict.keys():
            if key in feature_dict:
                feature_count_dict[key].append(len(feature_dict[key]))
            else:
                feature_count_dict[key].append(0)
    #print(feature_count_dict)

    return pd.DataFrame(feature_count_dict) #returns dataframe of features counts