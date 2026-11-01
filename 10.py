import random

chromosome_length = 8
mutation_rate = 0.1

parent1 = []
parent2 = []

for i in range(chromosome_length):
    parent1.append(random.randint(0, 1))
    parent2.append(random.randint(0, 1))

split_point = random.randint(1, chromosome_length - 1)

child = parent1[:split_point] + parent2[split_point:]

mutated = []

for bit in child:
    if random.random() <= mutation_rate:
        mutated.append(1 - bit)
    else:
        mutated.append(bit)

print("Parent 1:       ", parent1)
print("Parent 2:       ", parent2)
print(f"Crossover Child (Split at index {split_point}):", child)
print("Mutated Child:  ", mutated)