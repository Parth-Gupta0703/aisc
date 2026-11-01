def trap(x, a, b, c, d):
    if x <= a or x >= d:
        return 0.0
    elif a < x < b:
        return (x - a) / (b - a)
    elif b <= x <= c:
        return 1.0
    elif c < x < d:
        return (d - x) / (d - c)


inputs = [1, 3, 4, 6, 8]
a, b, c, d = 2, 4, 7, 9

print("Trapezoidal Membership Function")
print(f"a = {a}, b = {b}, c = {c}, d = {d}\n")

for x in inputs:
    degree = trap(x, a, b, c, d)
    print(f"Input: {x} -> Membership Degree: {degree:.2f}")
