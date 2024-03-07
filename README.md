# sqlalchemy-challenge

This ReadMe serves to:
   1. Certify that this work is my own,
   2. Specify code source and its location in my 'sqlalchemy-challenge' repository,
   3. Clarify the reason for the assignment,

1. 
My name is Brittney Watts, and I am in the UNCC/EdX Data Analytics Bootcamp. Currently, we 
are working on Module 10 of our exploration into the SQLAlchemy ORM, Flask, and APIs.

2. 
The source code is my interpretation of the information we have learned in class with some debugging help from forums, and here
is a breakdown of the locations of each element of my assignment:

    sqlalchemy-challenge
        SurfsUp
            Resources
                app.py
                hawaii.sqlite
                hawaii_measurements.csv
                hawaii_stations.csv
            climate_starter.ipynb
         README.md

3. 
This assignment serves to track my understanding of the SQLAlchemy ORM, data exploration, Flask, and SQLite.

SQLAlchemy Challenge:
   My task was to read the data from the hawaii.sqlite file and perform queries on the datasets! In climate_starter.ipynb, we made graphs base on our queries to analyze our retrieved data. In app.py, I designed a Flask API containing routes with different functions. These functions returned data based on the queries made within them. 
   The hawaii.sqlite file contained measurement and station data for different weather stations in Hawaii for a certain collection of dates.  
   
   My Steps: 

    - First, I had to connect to the SQLite database, reflect the tables into classes, save the references to the classes, and link python to the database all using SQLAlchemy.

    - PART 1: ANALYZE AND EXPLORE THE CLIMATE DATA
        - Precipitation Analysis
            - Find the most recent date in the dataset, query the previous 12 months of data, load the results for the "date" and "prcp" into a Pandas DataFrame, sort the values by date, and plot the results into a bar graph using the "plot" method.
            - Print the summary statistics for the precipitation data using Pandas.
        - Station Analysis
            - Query the total number of stations, design a query to find the most active stations and list them in order taking note of the most active station overall, and design a query that calculates the max, min, and avg temperatures for that station.
            - Design a query to get the temperature information for the last 12 months for the most active station, and plot the results as a histogram with 12 bins for each month.
    
    - PART 2: DESIGN THE CLIMATE APP
        - Create a route for the homepage that lists all of the available routes.
        - Create a route that queries the last 12 months of data for all stations, their dates, and their precipitation values and return the JSON representation of that dictionary.
        - Create a stations route that just returns a list of stations in the dataset.
        - Create a route that queries the dates and temperature observations of the most active station for the previous year of data and return is as a JSON list.
        - Create two routes that return the min, max, and avg temperature for a specified date range. For the specified start date, calculate the stats for all dates greater than the date specified. For the specified start and end date, calculate the statistics from the start date to the end date inclusively. 


      
THANK YOU!!!!!


