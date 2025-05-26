import pandas as pd

def transform_data(data_frame):
    data_frame=data_frame.drop_duplicates()
    data_frame= data_frame.fillna({'Gender':'Unknown'})
    data_frame['Date']=pd.to_datetime(data_frame['Date'],errors='coerce')
    data_frame['Birthdate']=pd.to_datetime(data_frame['Birthdate'],errors='coerce')
    
    return data_frame
