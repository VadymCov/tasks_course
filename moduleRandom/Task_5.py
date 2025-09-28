# 🎯 Monte Carlo Area Calculation for Complex Shape
# 
# 📌 Problem Definition:
# Calculate the area of a figure bounded by the system of inequalities:
#     -2 ≤ x ≤ 2
#     -2 ≤ y ≤ 2
#     x³ + y⁴ + 2 ≥ 0
#     3x + y² ≤ 2
#
# 🎲 Monte Carlo Method Approach:
# 1. Define bounding box: rectangle from (-2,-2) to (2,2) with area = 4×4 = 16
# 2. Generate random points uniformly distributed within this bounding box
# 3. For each point (x,y), check if it satisfies ALL inequalities:
#    - x³ + y⁴ + 2 ≥ 0  (cubic and quartic boundary)
#    - 3x + y² ≤ 2      (parabolic boundary)
# 4. Count successful points that meet all conditions
# 5. Area ≈ (successful points / total points) × area of bounding box
#
# ⚙️ Technical Implementation:
# - Use random.uniform(-2, 2) for both x and y coordinates
# - Typical sample size: 1,000,000 points for good accuracy
# - Boolean checks for inequality conditions
# - Area calculation: 16 × (points_inside / total_points)
#
# 📊 Expected Characteristics:
# - The shape is bounded by interesting curves:
#   • x³ + y⁴ = -2 (complex curve)
#   • 3x + y² = 2 (sideways parabola)
# - The area should be less than 16 (full bounding box)
# - Method provides statistical estimate with error ~1/√N
#
# 🔍 Validation:
# - Compare multiple runs to check consistency
# - Increase point count to improve accuracy
# - Analytical solution possible but complex due to curve shapes

# Test ____________________________________________________

import random

n = 10**6       
k = 0
s0 = 16
for _ in range(n):
    x = random.uniform(-2, 2)
    y = random.uniform(-2, 2)
    if (x ** 3 + y ** 4 + 2 >= 0) & (3 * x + y ** 2 <= 2):
        k += 1
print((k/n) * s0)