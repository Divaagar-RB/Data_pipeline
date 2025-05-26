from scripts.extract import read_file_from_csv
from scripts.transform import transform_data
from scripts.load import load_data
import logging
logging.basicConfig(filename="logs/pipeline.log" ,level=logging.INFO)
file_path = r"C:\Users\kombu\OneDrive\Documents\Data Engineer\Project 1\Data Pipeline\data\data.csv"

def runPipeLine():
    try:
        logging.info("Pipeline Started")
        data_frame = read_file_from_csv(file_path=file_path)
        data_frame_cleaned=transform_data(data_frame)
        load_data("sqlite:///data_pipeline.db",data_frame_cleaned,"cleaned_table")
        logging.info("Pipeline completed successfully")
    

    except Exception  as e:
        logging.info("Pipeline Failed ,{str{e}}")

if __name__ =="__main__":
    runPipeLine()
