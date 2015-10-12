#PUI 2015 HW #3 Assignment 1 - Distributions

Generate 100 samples of different sizes N (N>10 & N<2000).
For 6 different distributions, I chose Normal, Poisson, Binomial, Chi-Squared, Rayleigh and Logistic.

Population: mean = 100
Binomial: p = 0.5
Log: scale = 1
Gaus: sd = 10

Results: The larger the sample size, the closer the sample value to the population mean

#PUI 2015 HW#3 Assignment 2 - Hypothesis testing

We compared two variables using the Z-score Normal Distribution data and percentage points of the Chi-Square Distribution. 

alpha = 0.05

Results: Since the result for employment for >6 consecutive months is 1.589, less than the critical value of 3.84, which has a higher p=0.25. Therefore we cannot reject the null hypothesis, meaning that the percentage for former prisoners employed for 6+ years after release is higher for candidates who participated in the program as for the control group. Significance level p=0.25>p=0.05.

# PUI 2015 HW #4 Assignment 1 - Distributions
HW4-Assignment1.ipynb copy

## Assignment 1 : Distributions 

I tested the correlation of the age distribution of Male vs Female riders and Day vs Night riders using June 2015 citibikes dataset.

### Male vs Female riders
> Pearson's test: It implies no linear relationship correlation because it is between -1 and +1 with 0, therefore we accept the null hypothesis.

> Spearman's test: Since it is between -1 and +1 with 0, implies that there's no monotonic correlation relationship.

> K-S test: Using a = .05, we reject the null hypothesis that these samples are drawn from the same distribution

### Day vs Night riders
> Pearson's test: It implies no linear relationship correlation because it is between -1 and +1 with 0, therefore we accept the null hypothesis.

> Spearman's test: Since it is between -1 and +1 with 0, implies that there's no monotonic correlation relationship.

> K-S test: Using a = .05, we reject the null hypothesis that these samples are drawn from the same distribution