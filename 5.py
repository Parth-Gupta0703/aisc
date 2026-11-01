def mcculloh(inputs, weights, threshold):
    net = 0

    for i in range(len(inputs)):
        net += inputs[i] * weights[i]

    if net >= threshold:
        return 1
    else:
        return 0


inputs = [[0, 0], [0, 1], [1, 0], [1, 1]]
weights = [1, 1]

print("AND Gate")
for x in inputs:
    output = mcculloh(x, weights, 2)
    print(f"Input: {x} -> Output: {output}")

print("\nOR Gate")
for x in inputs:
    output = mcculloh(x, weights, 1)
    print(f"Input: {x} -> Output: {output}")
