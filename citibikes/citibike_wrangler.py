# -*- coding: utf-8 -*-
"""
Created on Wed Oct 07 14:48:00 2015

"""

# required libs and source data
import pandas as pd
import numpy as np
import urllib2
import json
from geopy.distance import vincenty
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
from statsmodels.graphics.api import abline_plot
import scipy.stats.mstats as ms

source_path = 'C:/Users/mu03179/Desktop/NYU/PUI_project/201509-citibike-tripdata.csv'
my_api_key = 'AIzaSyDyk0ENB_gn2r8yhogXYXpD5mux6Gc7n68'

# this reads from CSVs the data that we already wrangled in the commented-out code below
unique_stations = pd.read_csv('C:/Users/mu03179/Desktop/NYU/PUI_project/unique_stations.csv')
station_combos = pd.read_csv('C:/Users/mu03179/Desktop/NYU/PUI_project/station_combos.csv')
bikedata = pd.read_csv(source_path)

# commented-out code that only needed to be run once (to minimize use of APIs)
"""
# Create a dataframe of unique combinations of start/end station coordinates.
# This is required for distance calculation.
station_combos = bikedata.drop_duplicates(subset=['start station latitude',
                                                  'start station longitude',
                                                  'end station latitude',
                                                  'end station longitude'])\
                                                  [['start station latitude',
                                                  'start station longitude',
                                                  'end station latitude',
                                                  'end station longitude']]
# Create a dataframe just of unique stations.  Needed for County lookups.
unique_stations = bikedata.drop_duplicates(subset=['start station id'])\
                                                  [['start station id',
                                                  'start station latitude',
                                                  'start station longitude']]
# Rename columns and add an empty one to house the County names.
unique_stations.columns = ['station id','station latitude','station longitude']
unique_stations['County'] = ""

for i in unique_stations.index:  
    try:
        countylookupurl = ('https://maps.googleapis.com/maps/api/geocode/json?' +
            'latlng=%s,%s&key=%s' % (unique_stations.loc[i,'station latitude'],
                                    unique_stations.loc[i,'station longitude'],
                                    my_api_key))
        request = urllib2.urlopen(countylookupurl)
        locationdata = json.loads(request.read())
        unique_stations.loc[i,'County'] = str(locationdata['results'][0]\
                                        ['address_components'][4]['long_name'])
    except:
        continue
    
print 'Done with API loop'

# calculate the distance for each unique station combination
station_combos['distance'] = ""
for i in station_combos.index:
    x = station_combos.loc[i,'start station latitude']
    y = station_combos.loc[i,'start station longitude']
    z = station_combos.loc[i,'end station latitude']
    t = station_combos.loc[i,'end station longitude']
    e = (x, y)
    c = (z, t)
    station_combos.loc[i,'distance'] = (vincenty(e,c).miles)

# for any combos that didn't get a result, fill in 0.0
station_combos.ix[(station_combos['distance'] == ''),'distance'] = 0.0    

print 'Done with distance calculation'
"""

# Add the county names as a new column onto the original dataframe
joined_bikedata = pd.merge(bikedata, unique_stations, how='left', 
                           left_on='start station id', right_on='station id')
joined_bikedata.rename(columns = {'County':'start County'}, inplace=True)
# get rid of the duplicate columns that were created by the join
del joined_bikedata['station id']
del joined_bikedata['station latitude']
del joined_bikedata['station longitude']

# now do the same thing for the end station
joined_bikedata = pd.merge(joined_bikedata, unique_stations, how='left', 
                           left_on='end station id', right_on='station id')
joined_bikedata.rename(columns = {'County':'end County'}, inplace=True)
# again get rid of the duplicate columns that were created by the join
del joined_bikedata['station id']
del joined_bikedata['station latitude']
del joined_bikedata['station longitude']

# Create a new column and populate with category variable
joined_bikedata['CountyCombo'] = ""
joined_bikedata.ix[(joined_bikedata['start County'] == 'New York') & \
    (joined_bikedata['end County'] == 'New York'),'CountyCombo'] = 1
joined_bikedata.ix[(joined_bikedata['start County'] == 'Kings County') & \
    (joined_bikedata['end County'] == 'Kings County'),'CountyCombo'] = 2
joined_bikedata.ix[(joined_bikedata['start County'] == 'Queens County') & \
    (joined_bikedata['end County'] == 'Queens County'),'CountyCombo'] = 3
joined_bikedata.ix[(joined_bikedata['CountyCombo'] == ''),'CountyCombo'] = 4


# now merge the calculated distances into the main dataframe and esimate speed
final_bikedata = pd.merge(joined_bikedata, station_combos, 
                          on=['start station latitude','start station longitude',
                              'end station latitude', 'end station longitude'])
final_bikedata['trip_speed'] = final_bikedata['distance']\
    /(final_bikedata['tripduration'].astype('float')/3600.0)
    

final_bikedata = final_bikedata.convert_objects(convert_dates=False,convert_numeric=True,convert_timedeltas=False)
final_bikedata = final_bikedata[ms.zscore(final_bikedata.tripduration) < 3]
final_bikedata = final_bikedata[final_bikedata.distance > 0]
%pylab inline
plt.figure()
final_bikedata['trip_speed'].hist(bins = 50)

linearmodel = smf.ols(formula = 'trip_speed ~ C(gender) + C(CountyCombo) + distance', data = final_bikedata).fit()

print(linearmodel.summary())
