from sqlalchemy import create_engine
import logging
def load_data(database_url,data_frame,table):
    engine = create_engine(database_url)
    data_frame.to_sql(table,con=engine,if_exists='append',index=False)
    logging.info("Inserted into Database Successfully")
    