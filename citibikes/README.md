# Citibikes HW 3

## citibikes_group.ipynb
## data: Sept. 2015

# IDEA
## Riders are likely to ride faster in longer distances

# NULL HYPOTHESIS
## The average speed for riders are the same during long distance trips rather than short distance trips

# ALTERNATIVE HYPOTHESIS

## The average speed for riders are higher in long distances rather than short distances

Significance level : α=0.05

First we tried to figure out calculating distance using coordinates from longitude and latitude using the vincenty function. Then calculated speed using distance divded by tripduration column. We originally wanted to combine all the boroughs and to see whether riders ride faster in certain boroughs, ex: Brooklyn (faster) than Manhattan. We also wanted to see if riders are likely to ride faster during rush hours (morning and evening). So I came up with the values for rush hours. 

Because we don't need combos nor rush hours anymore, we then formed a linear regression model, comparing our distance t-value to the t-tables chart. I plotted a scatter plot to see speed (mph) vs distance. According to the t-table and the values we get, we reject the null hypothesis, which shows that there is a relationship between the two variables. If the distance increases 1 unit, the average speed will increase by 0.6540 units. 
