import matplotlib.pyplot as plt
import random

from aco import AntColony


plt.style.use("dark_background")

def a():
    COORDS = (
        (20, 52),
        (43, 50),
        (20, 84),
        (70, 65),
        (29, 90),
        (87, 83),
        (73, 23),
    )


    def random_coord():
        r = random.randint(0, len(COORDS))
        return r


    def plot_nodes(w=12, h=8):
        for x, y in COORDS:
            plt.plot(x, y, "g.", markersize=15)
        plt.axis("off")
        fig = plt.gcf()
        fig.set_size_inches([w, h])


    def plot_all_edges():
        paths = ((a, b) for a in COORDS for b in COORDS)

        for a, b in paths:
            plt.plot((a[0], b[0]), (a[1], b[1]))


    plot_nodes()

    colony = AntColony(COORDS, ant_count=300, alpha=0.5, beta=1.2, 
                        pheromone_evaporation_rate=0.40, pheromone_constant=1000.0,
                        iterations=300)

    optimal_nodes = colony.get_path()

    for i in range(len(optimal_nodes) - 1):
        plt.plot(
            (optimal_nodes[i][0], optimal_nodes[i + 1][0]),
            (optimal_nodes[i][1], optimal_nodes[i + 1][1]),
        )


    plt.show()

def b():
    COORDS = (
        (20, 52),
        (43, 50),
        (20, 84),
        (70, 65),
        (29, 90),
        (87, 83),
        (73, 23),
        (50, 10),
        (10, 10),
        (10, 50),
        (50, 50),
        (30, 30),
        (70, 30),
        (70, 70),
    )


    def random_coord():
        r = random.randint(0, len(COORDS))
        return r


    def plot_nodes(w=12, h=8):
        for x, y in COORDS:
            plt.plot(x, y, "g.", markersize=15)
        plt.axis("off")
        fig = plt.gcf()
        fig.set_size_inches([w, h])


    def plot_all_edges():
        paths = ((a, b) for a in COORDS for b in COORDS)

        for a, b in paths:
            plt.plot((a[0], b[0]), (a[1], b[1]))


    plot_nodes()

    colony = AntColony(COORDS, ant_count=300, alpha=0.5, beta=1.2, 
                        pheromone_evaporation_rate=0.40, pheromone_constant=1000.0,
                        iterations=300)

    optimal_nodes = colony.get_path()

    for i in range(len(optimal_nodes) - 1):
        plt.plot(
            (optimal_nodes[i][0], optimal_nodes[i + 1][0]),
            (optimal_nodes[i][1], optimal_nodes[i + 1][1]),
        )


    plt.show()

#b()
# base
def c1():
    COORDS = (
    (20, 52),
    (43, 50),
    (20, 84),
    (70, 65),
    (29, 90),
    (87, 83),
    (73, 23),
    (50, 10),
    (10, 10),
    (10, 50),
    (50, 50),
    (30, 30),
    (70, 30),
    (70, 70),
    )


    def random_coord():
        r = random.randint(0, len(COORDS))
        return r


    def plot_nodes(w=12, h=8):
        for x, y in COORDS:
            plt.plot(x, y, "g.", markersize=15)
        plt.axis("off")
        fig = plt.gcf()
        fig.set_size_inches([w, h])


    def plot_all_edges():
        paths = ((a, b) for a in COORDS for b in COORDS)

        for a, b in paths:
            plt.plot((a[0], b[0]), (a[1], b[1]))


    plot_nodes()

    colony = AntColony(COORDS, ant_count=300, alpha=0.5, beta=1.2, 
                        pheromone_evaporation_rate=0.40, pheromone_constant=1000.0,
                        iterations=300)

    optimal_nodes = colony.get_path()

    for i in range(len(optimal_nodes) - 1):
        plt.plot(
            (optimal_nodes[i][0], optimal_nodes[i + 1][0]),
            (optimal_nodes[i][1], optimal_nodes[i + 1][1]),
        )


    plt.show()

# pheromone_evaporation_rate=0.10
def c2():
    COORDS = (
    (20, 52),
    (43, 50),
    (20, 84),
    (70, 65),
    (29, 90),
    (87, 83),
    (73, 23),
    (50, 10),
    (10, 10),
    (10, 50),
    (50, 50),
    (30, 30),
    (70, 30),
    (70, 70),
    )


    def random_coord():
        r = random.randint(0, len(COORDS))
        return r


    def plot_nodes(w=12, h=8):
        for x, y in COORDS:
            plt.plot(x, y, "g.", markersize=15)
        plt.axis("off")
        fig = plt.gcf()
        fig.set_size_inches([w, h])


    def plot_all_edges():
        paths = ((a, b) for a in COORDS for b in COORDS)

        for a, b in paths:
            plt.plot((a[0], b[0]), (a[1], b[1]))


    plot_nodes()

    colony = AntColony(COORDS, ant_count=300, alpha=0.5, beta=1.2, 
                        pheromone_evaporation_rate=0.10, pheromone_constant=1000.0,
                        iterations=300)

    optimal_nodes = colony.get_path()

    for i in range(len(optimal_nodes) - 1):
        plt.plot(
            (optimal_nodes[i][0], optimal_nodes[i + 1][0]),
            (optimal_nodes[i][1], optimal_nodes[i + 1][1]),
        )


    plt.show()

# Pheromone constant = 500.0
def c3():
    COORDS = (
    (20, 52),
    (43, 50),
    (20, 84),
    (70, 65),
    (29, 90),
    (87, 83),
    (73, 23),
    (50, 10),
    (10, 10),
    (10, 50),
    (50, 50),
    (30, 30),
    (70, 30),
    (70, 70),
    )


    def random_coord():
        r = random.randint(0, len(COORDS))
        return r


    def plot_nodes(w=12, h=8):
        for x, y in COORDS:
            plt.plot(x, y, "g.", markersize=15)
        plt.axis("off")
        fig = plt.gcf()
        fig.set_size_inches([w, h])


    def plot_all_edges():
        paths = ((a, b) for a in COORDS for b in COORDS)

        for a, b in paths:
            plt.plot((a[0], b[0]), (a[1], b[1]))


    plot_nodes()

    colony = AntColony(COORDS, ant_count=300, alpha=0.5, beta=1.2, 
                        pheromone_evaporation_rate=0.40, pheromone_constant=500.0,
                        iterations=300)

    optimal_nodes = colony.get_path()

    for i in range(len(optimal_nodes) - 1):
        plt.plot(
            (optimal_nodes[i][0], optimal_nodes[i + 1][0]),
            (optimal_nodes[i][1], optimal_nodes[i + 1][1]),
        )


    plt.show()

# Bigger ant count = 600, pheromone_evaporation_rate=0.10, pheromone_constant=100.0
def c4():
    COORDS = (
    (20, 52),
    (43, 50),
    (20, 84),
    (70, 65),
    (29, 90),
    (87, 83),
    (73, 23),
    (50, 10),
    (10, 10),
    (10, 50),
    (50, 50),
    (30, 30),
    (70, 30),
    (70, 70),
    )


    def random_coord():
        r = random.randint(0, len(COORDS))
        return r


    def plot_nodes(w=12, h=8):
        for x, y in COORDS:
            plt.plot(x, y, "g.", markersize=15)
        plt.axis("off")
        fig = plt.gcf()
        fig.set_size_inches([w, h])


    def plot_all_edges():
        paths = ((a, b) for a in COORDS for b in COORDS)

        for a, b in paths:
            plt.plot((a[0], b[0]), (a[1], b[1]))


    plot_nodes()

    colony = AntColony(COORDS, ant_count=1000, alpha=0.5, beta=1.2, 
                        pheromone_evaporation_rate=0.10, pheromone_constant=100.0,
                        iterations=300)

    optimal_nodes = colony.get_path()

    for i in range(len(optimal_nodes) - 1):
        plt.plot(
            (optimal_nodes[i][0], optimal_nodes[i + 1][0]),
            (optimal_nodes[i][1], optimal_nodes[i + 1][1]),
        )


    plt.show()    

# c1()
# c2()
# c3()
c4()

# base result = 362.20183871736674
# smaller evaporation rate = 362.20183871736674
# smaller pheromone constant = 362.20183871736674
# Bigger ant count, small pheromone_evaporation_rate, small pheromone_constant = 362.20183871736674