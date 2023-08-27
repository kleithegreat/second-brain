from scipy.stats import norm

mu = 18.13 #mm
sd = 2.02 #mm, "sigma" = standard deviation = sd

### FIND PROBABILITY THAT PEANUT IS BETWEEN 16 and 20 mm ###
#For probability (area under curve) assosciated with value x
#python gives area under curve from -inf to value x
#norm.cdf(x,mu,sigma)
p16 = norm.cdf(16,mu,sd) #area (probability) from -inf to 16 mm
p20 = norm.cdf(20,mu,sd) #area (probability) from -inf to 20 mm

#subtract two areas to get area under curve from 16 to 20 mm
p1620 = p20-p16
print(f"There is a {p1620*100:.1f}% chance that a peanut from our field is between 16 and 20 mm diameter.")

### FIND DIAMETER OF SMALLEST 2% OF PEANUTS ###
#For value assosciated with probability q
# probability (area under curve) starts at -inf
#norm.ppf(q,mu,sd)
#q must be a fraction: 2% = 0.02
diam2perc = norm.ppf(0.02,mu,sd)
print(f"Throw out peanuts less than {diam2perc:.2f} mm in diameter (for smallest 2%).")