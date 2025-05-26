# Data_pipeline
This project is all about extracting data from the csv and doing transformation of data and loading into a sqlite database.
It is used to learn how a data pipeline works

Data has been stored in data directory
# Scripts
Extract.py -> loads data from csv

Transform.py -> Removes null values and duplicate values

Load.py -> Stores the cleaned dataframe to the sqlite database using sqlalchemy 

# Database
data_pipeline.db -> The database of stored values

