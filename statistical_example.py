import statistics

# Sample data
data = [1.5, 2.3, 3.7, 2.3, 1.5, 4.8, 3.7, 3.7]

print("Data:", data)
print("Count:", len(data))
print("Min / Max:", min(data), "/", max(data))

# Measures of central tendency
print("Mean:", statistics.mean(data))
print("Median:", statistics.median(data))
print("Median Low:", statistics.median_low(data))
print("Median High:", statistics.median_high(data))
print("Mode:", statistics.mode(data))
print("Multimode:", statistics.multimode(data))

# Measures of dispersion
print("Sample Variance:", statistics.variance(data))
print("Sample Standard Deviation:", statistics.stdev(data))
print("Population Variance:", statistics.pvariance(data))
print("Population Standard Deviation:", statistics.pstdev(data))

# Quantiles
# Split into 4 equal-sized groups (quartiles), inclusive method
print("Quartiles:", statistics.quantiles(data, n=4, method="inclusive"))
