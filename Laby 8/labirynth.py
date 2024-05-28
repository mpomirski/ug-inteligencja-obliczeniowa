from typing import Callable
import pygad
import matplotlib.pyplot as plt
import time

labirynth: list[list[int]] = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1],
    [1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 2, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]
    
moves = ['U', 'D', 'L', 'R']
gene_space = [0, 1, 2, 3]

#definiujemy funkcję fitness
def fitness_func(model, solution, solution_idx):
    x = 1
    y = 1
    for i in range(len(solution)):
        if solution[i] == 0:
            x -= 1
        elif solution[i] == 1:
            x += 1
        elif solution[i] == 2:
            y -= 1
        elif solution[i] == 3:
            y += 1
        if labirynth[x][y] == 2:
            return 9
        if labirynth[x][y] == 1:
            return -99 - (abs(10-x) + abs(10-y))
    return -(abs(10-x) + abs(10-y))

def fitness_func_given_position(x, y):
    if labirynth[x][y] == 2:
        return 9
    if labirynth[x][y] == 1:
        return -99 - (abs(10-x) + abs(10-y))
    return -(abs(10-x) + abs(10-y))

def calculate_position(solution):
    x = 1
    y = 1
    for i in range(len(solution)):
        if solution[i] == 0:
            x -= 1
        elif solution[i] == 1:
            x += 1
        elif solution[i] == 2:
            y -= 1
        elif solution[i] == 3:
            y += 1
        if labirynth[x][y] == 2:
            return [x, y]
        if labirynth[x][y] == 1:
            return [x, y]
    return [x, y]

fitness_function: Callable = fitness_func

#ile chromsomów w populacji
#ile genow ma chromosom
sol_per_pop: int = 100
num_genes: int = 30 # max 30 ruchów

#ile wylaniamy rodzicow do "rozmanazania" (okolo 50% populacji)
#ile pokolen
#ilu rodzicow zachowac (kilka procent)
num_parents_mating = 5
num_generations = 100
keep_parents = 5

#jaki typ selekcji rodzicow?
#sss = steady, rws=roulette, rank = rankingowa, tournament = turniejowa
parent_selection_type = "sss"

#w il =u punktach robic krzyzowanie?
crossover_type = "single_point"

#mutacja ma dzialac na ilu procent genow?
#trzeba pamietac ile genow ma chromosom
mutation_type = "random"
mutation_percent_genes = 8

#inicjacja algorytmu z powyzszymi parametrami wpisanymi w atrybuty
ga_instance = pygad.GA(gene_space=gene_space,
                       gene_type=int,
                       num_generations=num_generations,
                       num_parents_mating=num_parents_mating,
                       fitness_func=fitness_function,
                       sol_per_pop=sol_per_pop,
                       num_genes=num_genes,
                       parent_selection_type=parent_selection_type,
                       keep_parents=keep_parents,
                       crossover_type=crossover_type,
                       mutation_type=mutation_type,
                       mutation_percent_genes=mutation_percent_genes)

#uruchomienie algorytmu
ga_instance.run()

#podsumowanie: najlepsze znalezione rozwiazanie (chromosom+ocena)
solution, solution_fitness, solution_idx = ga_instance.best_solution()
print(solution)
print(f"Parameters of the best solution : {[moves[i] for i in solution]}")
print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))

#tutaj dodatkowo wyswietlamy sume wskazana przez jedynki
prediction = fitness_func(None, solution, solution_idx)
print("Predicted output based on the best solution : {prediction}".format(prediction=prediction))

#wyswietlenie wykresu: jak zmieniala sie ocena na przestrzeni pokolen
ga_instance.plot_fitness()

# wyświetl najlepsze rozwiązanie
best_position = calculate_position(solution)

# generate heatmap for values of each field in labirynth
heatmap = [[0 for _ in range(12)] for _ in range(12)]
for i in range(12):
    for j in range(12):
        heatmap[i][j] = fitness_func_given_position(i, j)
plt.imshow(heatmap)
plt.scatter(best_position[1], best_position[0], c='red')
plt.show()

# If stops, calculate average time
test_rounds: int = 10
times: list[float] = []
while test_rounds > 0:
    start = time.time()
    ga_instance = pygad.GA(gene_space=gene_space,
                           gene_type=int,
                           num_generations=num_generations,
                           num_parents_mating=num_parents_mating,
                           fitness_func=fitness_function,
                           sol_per_pop=sol_per_pop,
                           num_genes=num_genes,
                           parent_selection_type=parent_selection_type,
                           keep_parents=keep_parents,
                           crossover_type=crossover_type,
                           mutation_type=mutation_type,
                           mutation_percent_genes=mutation_percent_genes)
    ga_instance.run()
    solution, solution_fitness, solution_idx = ga_instance.best_solution()
    if solution_fitness == 9:   
        times.append(time.time() - start)
        test_rounds -= 1

print(f'Średni czas wykonania algorytmu jeżeli znaleziono rozwiązanie: {sum(times)/len(times)}s')