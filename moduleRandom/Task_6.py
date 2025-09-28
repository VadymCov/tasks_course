# 🎯 Monte Carlo Simulation for π Estimation
# 
# 📌 Concept: Estimate π using the ratio of areas between a unit circle and its bounding square
# 
# 🎲 Mathematical Basis:
# - Unit circle: x² + y² = 1 (radius = 1)
# - Area of circle: πr² = π (since r=1)
# - Bounding square: from (-1,-1) to (1,1) with area = 2×2 = 4
# - Ratio: (circle area)/(square area) = π/4
# - Therefore: π ≈ 4 × (points inside circle)/(total points)
#
# ⚙️ Method:
# 1. Generate random points in the square [-1,1]×[-1,1]
# 2. Check if each point satisfies x² + y² ≤ 1 (inside unit circle)
# 3. Count points inside the circle
# 4. π ≈ 4 × (inside points)/(total points)
#
# 📊 Parameters:
# - Using 1,000,000 points for good accuracy
# - Error decreases as 1/√N (N = number of points)
# - Expected result: π ≈ 3.14159...

# Test __________________________________________

import random

n = 10**6 
k = 0
s0 = 4
for _ in range(n):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x ** 2 + y ** 2 <= 1:
        k += 1
    
print(k / n * s0)



