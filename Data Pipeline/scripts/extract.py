import pandas as pd

def read_file_from_csv(file_path):
    data_frame = pd.read_csv(file_path)
    return data_frame
   