

def read_file(): #reading files inside the folders
    
    import glob
    csv_path = r"D:\scrapped_jobs\cardekho_data\Scrapped_Cars_Data" #

    # filenames = glob.glob(path + "\*.xlsx")
    path_filenames = glob.glob(csv_path + "/*.csv")
    path_filenames.sort()
#     print('File names:', csv_filenames)
    
    return path_filenames


def create_frames(path_filenames): #getting file names
    import pandas as pd
    files = []
    
    dict_data = {'new_car_detail': [], 'new_car_overview': [], 'new_car_feature': [],
                      'new_car_specs': [], 'car_links': [], 'place': []}
    
    main_frame = pd.DataFrame(dict_data)
    
    
    for index,file in enumerate(path_filenames):
        
        #print(file.split("D:\\GUVI\\Assessments\\")[1].split(".csv")[0])
        df = pd.read_csv(file)
      
        f = file.split("D:\\scrapped_jobs\\cardekho_data\\Scrapped_Cars_Data\\")[1].split(".csv")[0]
        files.append(f'{index},{f}')
        
        city_name = f.split("_")[0]
        df['place'] = city_name

        main_frame = pd.concat([main_frame,df],axis = 0)
        
    return files,main_frame