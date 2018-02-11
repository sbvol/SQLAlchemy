from matplotlib import dates
from datetime import datetime
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sqlalchemy
from sqlalchemy import asc, and_
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func
import matplotlib.patches as mpatches
from flask import Flask, jsonify


engine = create_engine("sqlite:///hawaii.sqlite", echo=False)
# Reflect an existing database into a new model
Base = automap_base()
# Reflect the tables
Base.prepare(engine, reflect=True)
# Save reference to the table
Measure = Base.classes.measure
Station = Base.classes.stations
# Create our session (link) from Python to the DB
session = Session(engine)
# Flask Setup
app = Flask(__name__)

# Flask Routes
start_date='2017-02-01'
end_date='2018-02-01'

@app.route("/")
def welcome1():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.1/precipitation<br/>"
        f"/api/v1.1/stations<br/>"
        f"/api/v1.1/tobs<br>"
        f"/api/v1.1/<start_date> & /api/v1.1/<end_date>")


@app.route("/api/v1.1/precipitation")
def date_tob():
	"""Return a list of all dates and temps from last year"""
	# Query all dates and temps
	results = session.query(Measure.date, Measure.tobs).filter(Measure.date > '2017-02-01').order_by(Measure.date).all()
	# Convert list of tuples into normal list
	data = list(np.ravel(results))

	return jsonify(data)

@app.route("/api/v1.1/stations")
def station():
    """Return a list of all stations"""
    # Query all stations
    results = session.query(Station.station).all()

    return jsonify(results)

@app.route("/api/v1.1/tobs")
def temp():
    """Return a list of all dates and temps from last year"""
    # Query all temps
    results = session.query(Measure.tobs).\
    filter(Measure.date > '2017-02-01').\
    order_by(Measure.date).all()

    # Convert list of tuples into normal list
    data = list(np.ravel(results))

    return jsonify(data)

@app.route("/api/v1.1/<start_date> and /api/v1.1/<end_date>")
def temp_tob():
    """Return a list of all dates and temps from last year"""
    # Query all dates and temps
    results_start_end = session.query(Measure.date, Measure.tobs).\
    filter(and_(Measure.date >= start_date, Measure.date <= end_date)).all()
    results_start_end_df = pd.DataFrame(results_start_end)
    
    range_min_tob = results_start_end_df['tobs'].min()
    range_max_tob = results_start_end_df['tobs'].max()
    range_mean_tob = results_start_end_df['tobs'].mean()

    results_start = results_start_end[results_start_end['date'] == start_date]
    results_end = results_start_end[results_start_end['date'] == end_date]
    
    results_start_min = results_start['tobs'].min()
    results_start_max = results_start['tobs'].max()
    results_start_mean = results_start['tobs'].mean()
    
    results_end_min = results_start['tobs'].min()
    results_end_max = results_start['tobs'].max()
    results_end_mean = results_start['tobs'].mean()

    return jsonify(results_start_min, results_start_max, results_start_mean,\
                  results_end_min, results_end_max, results_end_mean,\
                  range_min_tob, range_max_tob, range_mean_tob)
