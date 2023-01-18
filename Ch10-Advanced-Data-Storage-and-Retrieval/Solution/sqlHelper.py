from sqlalchemy import create_engine
import pandas as pd
import datetime as dt

class sql_helper():
    def __init__(self):
        self.database_path = "Resources/hawaii.sqlite"
        self.connection_str = f"sqlite:///{self.database_path}"
        self.engine = create_engine(self.connection_str)

    def execute_query(self, query):
        df = pd.read_sql(query, self.engine)
        return(df)

    def get_precipitation(self):
        query = """Select
                        date,
                        station,
                        prcp
                    From
                        measurement
                    Where
                        date >= '2016-08-23' and prcp is not null
                    Order By
                        date asc, 
                        station asc;
                """
        return(self.execute_query(query))

    def get_stations(self):
        query = """Select * 
                    From station 
                    Order By id asc
                """
        return(self.execute_query(query))
    
    def get_temp_data_for_year(self, start):
        # start = dt.datetime.strptime(start, "%m%d%Y")
        query = f"""Select
                        min(tobs) as min_temp_observation_data,
                        avg(tobs) as avg_temp_observation_data,
                        max(tobs) as max_temp_observation_data
                    From
                        measurement
                    Where
                        date >= '{start}';
                """
        return(self.execute_query(query))

    def get_temp_data_for_date_range(self, start, end):
        # start = dt.datetime.strptime(start, "%m%d%Y")
        # end = dt.datetime.strptime(end, "%m%d%Y")
        query = f"""Select
                        min(tobs) as min_temp_observation_data,
                        avg(tobs) as avg_temp_observation_data,
                        max(tobs) as max_temp_observation_data
                    From
                        measurement
                    Where
                        date >= '{start}' and date <= '{end}';
                """
        return(self.execute_query(query))