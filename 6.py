import random

# Function to maximize
def fitness(x):
    # print(x)
    return x * x     # f(x) = x^2

# Convert binary string → integer
def decode(chromosome):
    return int(chromosome, 2)

# Create random chromosome of length 5
def random_chromosome():
    return ''.join(random.choice(['01','00','10','11']) for _ in range(5))

# Single-point crossover
def crossover(p1, p2):
    point = random.randint(1, len(p1)-1)
    return p1[:point] + p2[point:], p2[:point] + p1[point:]

# Bit-flip mutation
def mutate(chromosome, rate=0.1):
    new = ""
    for bit in chromosome:
        if random.random() < rate:
            new += '1' if bit == '0' else '0'
        else:
            new += bit
    return new

population_size = 8
generations = 20

# Initial population
population = [random_chromosome() for _ in range(population_size)]
# print(population)

for gen in range(generations):
    # Evaluate fitness
    scored = [(chrom, fitness(decode(chrom))) for chrom in population]

    # Sort by fitness (descending)
    scored.sort(key=lambda x: x[1], reverse=True)

    print(f"Generation {gen} | Best: {scored[0][0]} → {scored[0][1]}")

    # Selection (top 50%)
    selected = [c for c, _ in scored[:population_size // 2]]
    '''
    print(scored[:population_size // 2])
    print(selected)
    '''
    # Create next generation
    next_gen = []

    while len(next_gen) < population_size:
        p1, p2 = random.sample(selected, 2)
        c1, c2 = crossover(p1, p2)
        next_gen.append(mutate(c1))
        next_gen.append(mutate(c2))

    population = next_gen

print("\nFinal Best Solution:")
best = max(population, key=lambda c: fitness(decode(c)))
print(f"Chromosome: {best}")
print(f"x = {decode(best)},  f(x) = {fitness(decode(best))}")