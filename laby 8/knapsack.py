import pygad
import numpy
from typing import Callable, TypedDict
import time

class Item(TypedDict):
    item: str
    value: int
    weight: int

items: dict[int, Item] = {
    1: {
        'item': 'zegar',
        'value': 100,
        'weight': 7
    },
    2: {
        'item': 'obraz-pejzaż',
        'value': 300,
        'weight': 7
    },
    3: {
        'item': 'obraz-portret',
        'value': 200,
        'weight': 6
    },
    4: {
        'item': 'radio',
        'value': 40,
        'weight': 2
    },
    5: {
        'item': 'laptop',
        'value': 500,
        'weight': 5
    },
    6: {
        'item': 'lampka nocna',
        'value': 70,
        'weight': 6
    },
    7: {
        'item': 'srebrne sztućce',
        'value': 100,
        'weight': 1
    },
    8: {
        'item': 'porcelana',
        'value': 250,
        'weight': 3
    },
    9: {
        'item': 'figura z brązu',
        'value': 300,
        'weight': 10
    },
    10: {
        'item': 'skórzana torebka',
        'value': 280,
        'weight': 3
    },
    11: {
        'item': 'odkurzacz',
        'value': 300,
        'weight': 15
    }
}

MAX_WEIGHT: int = 25
BEST_POSSIBLE_SUM: int = 1630

#definiujemy parametry chromosomu
#geny to liczby: 0 lub 1
gene_space = [0, 1]

#definiujemy funkcję fitness
def fitness_func(model, solution, solution_idx) -> int:
    total_weight: int = 0
    total_value: int = 0
    for i in range(len(solution)):
        if solution[i] == 1:
            total_weight += items[i+1]['weight']
            total_value += items[i+1]['value']
    if total_weight > MAX_WEIGHT:
        return 0
    return total_value

fitness_function: Callable = fitness_func

#ile chromsomów w populacji
#ile genow ma chromosom
sol_per_pop: int = 100
num_genes: int = len(items)

#ile wylaniamy rodzicow do "rozmanazania" (okolo 50% populacji)
#ile pokolen
#ilu rodzicow zachowac (kilka procent)
num_parents_mating: int = int(0.4 * sol_per_pop)
num_generations: int = 200
keep_parents: int = int(0.2 * sol_per_pop)

#jaki typ selekcji rodzicow?
#sss = steady, rws=roulette, rank = rankingowa, tournament = turniejowa
parent_selection_type: str = "sss"

#w il =u punktach robic krzyzowanie?
crossover_type: str = "single_point"

#mutacja ma dzialac na ilu procent genow?
#trzeba pamietac ile genow ma chromosom
mutation_type: str = "random"
mutation_percent_genes = 10

#inicjacja algorytmu z powyzszymi parametrami wpisanymi w atrybuty
ga_instance = pygad.GA(gene_space=gene_space,
                       num_generations=num_generations,
                       num_parents_mating=num_parents_mating,
                       fitness_func=fitness_function,
                       sol_per_pop=sol_per_pop,
                       num_genes=num_genes,
                       parent_selection_type=parent_selection_type,
                       keep_parents=keep_parents,
                       crossover_type=crossover_type,
                       mutation_type=mutation_type,
                       mutation_percent_genes=mutation_percent_genes,
                       stop_criteria=f"reach_{BEST_POSSIBLE_SUM}"
                    )

# d
ga_instance.run()

#podsumowanie: najlepsze znalezione rozwiazanie (chromosom+ocena)
solution, solution_fitness, solution_idx = ga_instance.best_solution()
print(f"Parameters of the best solution : {[items[i+1]['item'] for i in range(len(solution)) if solution[i] == 1]}")
print(f"Fitness value of the best solution = {solution_fitness}")

prediction = numpy.sum([items[i+1]['value'] for i in range(len(solution)) if solution[i] == 1])
print(f"Predicted output based on the best solution : {prediction}")
ga_instance.plot_fitness()


# e
test_rounds: int = 10
best_counter: int = 0
times: list[float] = []

for _ in range(test_rounds):
    start = time.time()
    ga_instance = pygad.GA(gene_space=gene_space,
                       num_generations=num_generations,
                       num_parents_mating=num_parents_mating,
                       fitness_func=fitness_function,
                       sol_per_pop=sol_per_pop,
                       num_genes=num_genes,
                       parent_selection_type=parent_selection_type,
                       keep_parents=keep_parents,
                       crossover_type=crossover_type,
                       mutation_type=mutation_type,
                       mutation_percent_genes=mutation_percent_genes,
                       stop_criteria=f"reach_{BEST_POSSIBLE_SUM}"
                    )
    ga_instance.run()
    solution, solution_fitness, solution_idx = ga_instance.best_solution()
    prediction = numpy.sum([items[i+1]['value'] for i in range(len(solution)) if solution[i] == 1])

    if prediction == BEST_POSSIBLE_SUM:
        best_counter += 1
    end = time.time()
    times.append(end-start)

print(f'Optymalne rozwiązanie osiągnięto w {best_counter} przypadkach ({best_counter/test_rounds*100}%)')
print(f'Średni czas wykonania algorytmu: {sum(times)/len(times)}s')

# f
cases: int = 20
i: int = 0
times: list[float] = []
while i < cases:
    start = time.time()
    ga_instance = pygad.GA(gene_space=gene_space,
                       num_generations=num_generations,
                       num_parents_mating=num_parents_mating,
                       fitness_func=fitness_function,
                       sol_per_pop=sol_per_pop,
                       num_genes=num_genes,
                       parent_selection_type=parent_selection_type,
                       keep_parents=keep_parents,
                       crossover_type=crossover_type,
                       mutation_type=mutation_type,
                       mutation_percent_genes=mutation_percent_genes,
                       stop_criteria=f"reach_{BEST_POSSIBLE_SUM}"
                    )
    ga_instance.run()

    solution, solution_fitness, solution_idx = ga_instance.best_solution()
    prediction = numpy.sum([items[i+1]['value'] for i in range(len(solution)) if solution[i] == 1])

    end = time.time()
    if prediction == BEST_POSSIBLE_SUM:
        i += 1
        times.append(end-start)

print(f'Średni czas wykonania algorytmu przy znalezieniu najlepszego rozwiazania: {sum(times)/len(times)}s')