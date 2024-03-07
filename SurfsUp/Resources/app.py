# Import the dependencies.
import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# # reflect the tables
# #Base.prepare(engine, reflect = True)
Base.prepare(autoload_with = engine)
Base.classes.keys()

# # Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

session = Session(engine)
#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def home():
    """List all available api routes."""
    return (
        f"Available Routes:<br/><br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/temp/2017-12-01<br/>"
        f"/api/v1.0/temp/2017-12-01/2017-12-31"
    )


@app.route("/api/v1.0/precipitation")
def precip():
    # Create session (link) from Python to the DB
    session = Session(engine)

    print("Server received request for 'precipitation' page...")
    print("Returning the last 12 months of precipitation data...")
    results = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= '2016-08-23').all()
    
    session.close()

    precip_dict = {date: prcp for date, prcp in results}
    return jsonify(precip_dict)


@app.route("/api/v1.0/stations")
def stations():
    # Create session (link) from Python to the DB
    print("Server received request for 'stations' page...")
    print("Returning a list of stations...")
    session = Session(engine)

    results = session.query(Station.station).all()

    session.close()

    stations_list = [result[0] for result in results]
    return jsonify(stations_list)


@app.route("/api/v1.0/tobs")
def tobs():
    # Create session (link) from Python to the DB
    session = Session(engine)

    print("Server received request for 'tobs' page...")
    print("Returning temperature observations for the most active station...")

    # Query most active station
    most_active = session.query(Measurement.station).\
        group_by(Measurement.station).\
        order_by(func.count(Measurement.station).desc()).first()[0]

    query_date = (dt.date(2017, 8, 23) - dt.timedelta(days=365))
    
    results = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.station == most_active).\
        filter(Measurement.date >= query_date).all()
    
    session.close()

    tobs_list = []
    for date, tobs in results:
        tobs_list.append({"Date" : date, "Temperature" : tobs})

    return jsonify(tobs_list)


@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start=None, end=None):
    # Create session (link) from Python to the DB
    session = Session(engine)
    select = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    print("Server received request for 'passengers' page")
    print("Returning temperature stats for <start> to <end>")

    start = dt.datetime.strptime(start, "%Y-%m-%d")

    if not end:
        results = session.query(*select).\
            filter(Measurement.date >= start).all()

    else:
        end = dt.datetime.strptime(end, "%Y-%m-%d")
        results = session.query(*select).\
            filter(Measurement.date >= start).\
            filter(Measurement.date <= end).all()

    session.close()

    if not results:
        return jsonify({"error": 'No data found'})
    
    stats = {
        'Minimum Temperature' : results[0][0],
        'Average Temperature' : results[0][1],
        'Maximum Temperature' : results[0][2],
    }

    return jsonify(stats)

if __name__ == '__main__':
    app.run(debug=True)

