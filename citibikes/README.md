# Citibikes HW 3 & HW 4.1, 4.3

citibikes_group.ipynb

## Assignment 3

Data: 
> [Sept. 2015](https://drive.google.com/file/d/0B8EwoI-cGyuZY0QwWlFmNjlnMms/)

> [station_combos.csv](https://github.com/livenlulu/PUI2015_lkang/blob/master/citibikes/station_combos.csv)

> [unique_stations.csv](https://github.com/livenlulu/PUI2015_lkang/blob/master/citibikes/unique_stations.csv)

### IDEA
Riders are likely to ride faster in longer distances

### NULL HYPOTHESIS
The average speed for riders are the same during long distance trips rather than short distance trips

### ALTERNATIVE HYPOTHESIS

The average speed for riders are higher in long distances rather than short distances

Significance level : α=0.05

There's a total of 3 csv files. We used Sept.2015 for the main data. Then cleaned the data for station_combos.csv and unique_stations.csv.

First we tried to figure out calculating distance using coordinates from longitude and latitude using the vincenty function. Then calculated speed using distance divded by tripduration column. We originally wanted to combine all the boroughs and to see whether riders ride faster in certain boroughs, ex: Brooklyn (faster) than Manhattan. We also wanted to see if riders are likely to ride faster during rush hours (morning and evening). So I came up with the values for rush hours. 

Because we don't need combos nor rush hours anymore, we then formed a linear regression model, comparing our distance t-value to the t-tables chart. I plotted a scatter plot to see speed (mph) vs distance. According to the t-table and the values we get, we reject the null hypothesis, which shows that there is a relationship between the two variables. If the distance increases 1 unit, the average speed will increase by 0.6540 units. 


# HW #4

## Assignment 1 : Distributions 

HW4-Assignment1.ipynb copy

Data: 
> [June 2015](https://s3.amazonaws.com/tripdata/201506-citibike-tripdata.zip)

I tested the correlation of the age distribution of Male vs Female riders and Day vs Night riders using June 2015 citibikes dataset.

### Male vs Female riders
> Pearson's test: It implies no linear relationship correlation because it is between -1 and +1 with 0, therefore we accept the null hypothesis.

> Spearman's test: Since it is between -1 and +1 with 0, implies that there's no monotonic correlation relationship.

> K-S test: Using a = .05, we reject the null hypothesis that these samples are drawn from the same distribution

### Day vs Night riders
> Pearson's test: It implies no linear relationship correlation because it is between -1 and +1 with 0, therefore we accept the null hypothesis.

> Spearman's test: Since it is between -1 and +1 with 0, implies that there's no monotonic correlation relationship.

> K-S test: Using a = .05, we reject the null hypothesis that these samples are drawn from the same distribution