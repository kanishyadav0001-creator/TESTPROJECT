import scipy.stats as stats

prob1 = 1 - stats.poisson.cdf(12, 10)
print("Probability of 12 or more days of rain:", prob1)

prob2 = stats.poisson.cdf(18, 10) - stats.poisson.cdf(12, 10)
print("Probability of between 12 and 18 days of rain:", prob2)
