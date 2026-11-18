"""Genetic Algorithm for Delivery Route Optimisation.

Finds a short route that starts at depot A, visits B to G exactly once,
and returns to A. Uses the fictional delivery distance table from the
assignment.

Run from the repository root:
    python Submissions/Lab09_Assignment/ga_delivery_route.py
"""
import random

# Distance between locations in kilometres (symmetric).
LOCATIONS = ["A", "B", "C", "D", "E", "F", "G"]
DISTANCE = [
    [0, 4, 8, 6, 7, 9, 5],  # A
    [4, 0, 5, 7, 3, 8, 6],  # B
    [8, 5, 0, 4, 6, 3, 7],  # C
    [6, 7, 4, 0, 5, 6, 8],  # D
    [7, 3, 6, 5, 0, 4, 6],  # E
    [9, 8, 3, 6, 4, 0, 5],  # F
    [5, 6, 7, 8, 6, 5, 0],  # G
]
DEPOT = "A"
DELIVERIES = ["B", "C", "D", "E", "F", "G"]

# GA settings
SEED = 42
POPULATION_SIZE = 50
GENERATIONS = 100
TOURNAMENT_SIZE = 3
MUTATION_RATE = 0.2
N_ELITE = 2

# Fixed seed so the experiment can be reproduced.
random.seed(SEED)


def distance(a, b):
    return DISTANCE[LOCATIONS.index(a)][LOCATIONS.index(b)]


def route_distance(chromosome):
    """Total km of the full trip A, chromosome, A. Lower is better."""
    full_route = [DEPOT] + chromosome + [DEPOT]
    return sum(distance(a, b) for a, b in zip(full_route, full_route[1:]))


def random_route():
    """A chromosome is one ordering of the six delivery locations."""
    route = DELIVERIES[:]
    random.shuffle(route)
    return route


def tournament_selection(population):
    """Pick a few random routes and return the shortest one."""
    contestants = random.sample(population, TOURNAMENT_SIZE)
    return min(contestants, key=route_distance)


def order_crossover(parent1, parent2):
    """Copy a slice from parent1, then fill the gaps in parent2's order.
    Every location ends up in the child exactly once."""
    start, end = sorted(random.sample(range(len(parent1)), 2))
    child = [None] * len(parent1)
    child[start:end + 1] = parent1[start:end + 1]
    remaining = [loc for loc in parent2 if loc not in child]
    for i in range(len(child)):
        if child[i] is None:
            child[i] = remaining.pop(0)
    return child


def swap_mutation(route):
    """Swap two delivery locations. The route stays valid."""
    route = route[:]
    if random.random() < MUTATION_RATE:
        i, j = random.sample(range(len(route)), 2)
        route[i], route[j] = route[j], route[i]
    return route


def format_route(chromosome):
    return " -> ".join([DEPOT] + chromosome + [DEPOT])


def genetic_algorithm():
    # Start with a population of random valid routes.
    population = [random_route() for _ in range(POPULATION_SIZE)]

    for generation in range(1, GENERATIONS + 1):
        population.sort(key=route_distance)
        best = population[0]
        if generation == 1 or generation % 10 == 0:
            print(f"Generation {generation:3d}: best distance = {route_distance(best)} km  "
                  f"({format_route(best)})")

        # Elitism: the best routes go to the next generation unchanged.
        next_population = [route[:] for route in population[:N_ELITE]]

        # Fill the rest with children made by selection, crossover and mutation.
        while len(next_population) < POPULATION_SIZE:
            parent1 = tournament_selection(population)
            parent2 = tournament_selection(population)
            child = order_crossover(parent1, parent2)
            child = swap_mutation(child)
            next_population.append(child)

        population = next_population

    best = min(population, key=route_distance)
    return best, route_distance(best)


if __name__ == "__main__":
    print("Genetic Algorithm - Delivery Route Optimisation")
    print(f"Seed {SEED} | population {POPULATION_SIZE} | generations {GENERATIONS}\n")
    best_route, best_km = genetic_algorithm()
    print("\nBest route found:", format_route(best_route))
    print("Total distance:", best_km, "km")
