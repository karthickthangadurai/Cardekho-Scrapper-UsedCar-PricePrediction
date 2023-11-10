
def carspec(df):
    
    import json
    import pandas as pd
    
    df['new_car_specs'] = df['new_car_specs'].apply(lambda x : json.loads(x.replace("'",'"')))

    print("1st car spec row----->",df['new_car_specs'].to_list()[0])
    
    def spec_dict_creater(sub_dict):

        dictionary = { sub_dict['heading']:[{i['key']:i['value']} for i in sub_dict['top']] }

        for subcat_dict in sub_dict['data']:
            catdict = { subcat_dict['heading']:[{i['key']:i['value']} for i in subcat_dict['list']] }
            dictionary.update(catdict)

        return dictionary

    df.new_car_specs = df.new_car_specs.apply(lambda sub_dict : spec_dict_creater(sub_dict))

    print("1st car spec row after extraction----->",df.new_car_specs.to_list()[0])
    
    #putting all spec into one
    def all_spec_dict(specifi):
        all_spec = {}

        for value in specifi.values():
            for spec in value:
                for key,value in spec.items():
                    all_spec.update({key:value})
        return all_spec

    df.new_car_specs = df.new_car_specs.apply( lambda specifi : all_spec_dict(specifi) )
    print("Making all spec into one dictionary----->",df.new_car_specs.to_list()[0])
    
    #unique specs

    unique_spec_keys = []

    for specs in df.new_car_specs:
        for key in specs.keys():
            if key not in unique_spec_keys:
                unique_spec_keys.append(key)
    print("unique spec keys------->",unique_spec_keys)
    print("length of unique spec keys------->",len(unique_spec_keys))
    
    specs_dict = { 'Engine': [], 'Max Power': [], 'Torque': [], 'Wheel Size': [], 'Seats': [], 'Color': [],
                  'Engine Type': [], 'Displacement': [], 'Max Torque': [], 'No of Cylinder': [],
                  'Values per Cylinder': [], 'Fuel Suppy System': [], 'Turbo Charger': [], 'Length': [],
                  'Width': [], 'Height': [], 'Wheel Base': [], 'Kerb Weight': [], 'Gear Box': [],
                  'Drive Type': [], 'Seating Capacity': [], 'Steering Type': [], 'Front Brake Type': [],
                  'Rear Brake Type': [], 'Tyre Type': [], 'Alloy Wheel Size': [], 'No Door Numbers': [],
                  'Cargo Volumn': [], 'Mileage': [], 'Value Configuration': [], 'Compression Ratio': [],
                  'Super Charger': [], 'Front Tread': [], 'Rear Tread': [], 'Gross Weight': [],
                  'Turning Radius': [], 'Top Speed': [], 'Acceleration': [], 'BoreX Stroke': [],
                  'Ground Clearance Unladen': [] }

    for dictionary in df.new_car_specs:
        for key in specs_dict:
            if key in dictionary:
                specs_dict[key].append(dictionary[key])
            else:
                specs_dict[key].append(None)


    return pd.DataFrame(specs_dict) #returning dataframe of specs
