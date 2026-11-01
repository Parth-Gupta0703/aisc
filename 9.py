A = {"x1": 0.6, "x2": 0.4, "x3": 0.9}
B = {"x1": 0.5, "x2": 0.2, "x3": 0.3}

bounded_sum = {}
bounded_diff = {}

for k in A:
    bounded_sum[k] = min(1.0, A[k] + B[k])
    bounded_diff[k] = max(0.0, round(A[k] + B[k] - 1.0, 1))
print("Fuzzy Set A:        ", A)
print("Fuzzy Set B:        ", B)
print("Bounded Sum:        ", bounded_sum)
print("Bounded Difference: ", bounded_diff)