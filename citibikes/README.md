Citibikes HW 3

citibikes_group.ipynb
data: Sept. 2015

IDEA
Riders are likely to ride faster during rush hours.

NULL HYPOTHESIS
The average speed for riders during rush hours are higher or the same compared to rides taken during off-peak hours.

$H_0: \mu_r ≥ \mu_p$
$H_1: \mu_r < \mu_r$

Significance level: $\alpha = 0.05$

where μp = mean speed for off-peak hours, μr = mean speed for rush hours

I specifically used starttime column to come up with rush hours. Assume morning rush hour: 7am - 10am, afternoon rush hours: 4pm - 7pm, off-peak hours: 7pm - 7am and 10am - 4pm. The goal is to see if there's any relationships between the speed during rush hours (both morning and afternoon) and the speed during off-peak hours, then integrate the mean speed into hours. I then ran a test statistics too see whether I should reject the null hypothesis. 
