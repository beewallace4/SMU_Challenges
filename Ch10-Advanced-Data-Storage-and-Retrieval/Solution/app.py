from flask import Flask, jsonify
import pandas as pd
from sqlHelper import sql_helper

# Flask Setup
# -----------------------------------------------------------
app = Flask(__name__)
sqlHelper = sql_helper()


# Flask Routes
# -----------------------------------------------------------
@app.route("/")
def welcome():
    return (
        f"Welcome to the Hawaii Weather API!<br>"
        
        f"Available Routes:<br/>"

        f"<a href='/api/v1.0/precipitation'>/api/v1.0/precipitation</a><br/>"
        f"<a href='/api/v1.0/stations'>/api/v1.0/stations</a><br/>"
        f"<a href='/api/v1.0/<start>'>/api/v1.0/start/</a><br/>"
        f"<a href='/api/v1.0/<start>/<end>'>/api/v1.0/start/end/<end></a><br/>"

        f"<p>'start' and 'end' date should be in the format MMDDYYYY.</p>"
    )


@app.route("/api/v1.0/precipitation")
def get_precipitation():
    df = sqlHelper.get_precipitation()
    data = df.to_dict(orient="records")
    return(jsonify(data))


@app.route("/api/v1.0/stations")
def get_stations():
    df = sqlHelper.get_stations()
    data = df.to_dict(orient="records")
    return(jsonify(data))


@app.route("/api/v1.0/<start>")
def get_temp_data_for_year(start):
    df = sqlHelper.get_temp_data_for_year(start)
    data = df.to_dict(orient="records")
    return(jsonify(data))


@app.route("/api/v1.0/<start>/<end>")
def get_temp_data_for_date_range(start, end):
    df = sqlHelper.get_temp_data_for_date_range(start, end)
    data = df.to_dict(orient="records")
    return(jsonify(data))

if __name__ == "__main__":
    app.run(debug=True)