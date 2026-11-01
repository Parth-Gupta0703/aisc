A = {"x1": 0.2, "x2": 0.7, "x3": 0.4, "x4": 1.0}
B = {"x1": 0.5, "x2": 0.3, "x3": 0.9, "x4": 0.0}

union = {}
intersection = {}
complement = {}

for k in A:
    union[k] = max(A[k], B[k])
    intersection[k] = min(A[k], B[k])
    complement[k] = round(1.0 - A[k], 1)

print("Fuzzy Set A:      ", A)
print("Fuzzy Set B:      ", B)
print("Union (A U B):    ", union)
print("Intersect (A n B):", intersection)
print("Complement (~A):  ", complement)