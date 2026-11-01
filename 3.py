def tri(x, a, b, c):
    if x <= a or x >= c:
        return 0.0
    elif a < x <= b:
        return (x - a) / (b - a)
    elif b < x < c:
        return (c - x) / (c - b)
    elif x == b:
        return 1.0


inputs = [1, 4, 5, 6]
a = 2
b = 5
c = 7

print("Triangular Membership Function")
print(f"a = {a}, b = {b}, c = {c}\n")

for x in inputs:
    degree = tri(x, a, b, c)
    print(f"Input: {x} -> Membership Degree: {degree:.2f}")
