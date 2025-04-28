import statistics
import numpy as np
from scipy import stats

# ─── Sample data ──────────────────────────────────────────────────────────────
data = [1.5, 2.3, 3.7, 2.3, 1.5, 4.8, 3.7, 3.7]
print("Data:", data)

# ─── Built-in statistics ──────────────────────────────────────────────────────
print("Mean (built-in):", statistics.mean(data))
print("Median (built-in):", statistics.median(data))
print("Mode (built-in):", statistics.mode(data))
print("Sample Std Dev (built-in):", statistics.stdev(data))

# ─── NumPy (for consistency) ──────────────────────────────────────────────────
arr = np.array(data)
print("Mean (NumPy):", arr.mean())
print("Std Dev (NumPy):", arr.std(ddof=1))  # ddof=1 for sample std

# ─── SciPy descriptive stats ─────────────────────────────────────────────────
print("Skewness (SciPy):", stats.skew(data))
print("Kurtosis (SciPy):", stats.kurtosis(data))

# ─── Hypothesis test: one-sample t-test ─────────────────────────────────────────
# Test H₀: popmean = 3.0
t_stat, p_value = stats.ttest_1samp(data, popmean=3.0)
print(f"One-sample t-test vs μ=3.0 → t = {t_stat:.3f}, p = {p_value:.3f}")

# ─── Fitting & evaluating a distribution ──────────────────────────────────────
# Fit a normal distribution to the data
(mu, sigma) = stats.norm.fit(data)
print(f"Fitted normal → μ = {mu:.3f}, σ = {sigma:.3f}")

rv = stats.norm(loc=mu, scale=sigma)
print("PDF at x=μ:", rv.pdf(mu))
print("CDF at x=μ:", rv.cdf(mu))

# ─── Generating random variates ────────────────────────────────────────────────
sample = rv.rvs(size=5)
print("5 random draws from fitted normal:", sample)
