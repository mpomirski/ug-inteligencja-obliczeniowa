import math
from pickletools import optimize
import pyswarms as ps
from pyswarms.utils.functions import single_obj as fx
import numpy as np

def endurance(vals) -> float:
    return math.exp(-2*(vals[1]-math.sin(vals[0]))**2)+math.sin(1)+math.cos(1)


def a():
    c1: float = 0.5
    c2: float = 0.3
    w: float = 0.9

    options: dict[str, float] = {'c1': c1, 'c2': c2, 'w': w}

    x_max: list[int] = [2, 2]
    x_min: list[int] = [1, 1]
    my_bounds: tuple[list[int], list[int]] = (x_min, x_max)


    optimizer: ps.single.GlobalBestPSO = ps.single.GlobalBestPSO(n_particles=10, dimensions=2, options=options, bounds=my_bounds)

    optimizer.optimize(fx.sphere, iters=1000)

def b():
    c1: float = 0.5
    c2: float = 0.3
    w: float = 0.9

    options: dict[str, float] = {'c1': c1, 'c2': c2, 'w': w}

    x_max: list[int] = [1, 1, 1, 1, 1, 1]
    x_min: list[int] = [0, 0, 0, 0, 0, 0]
    my_bounds: tuple[list[int], list[int]] = (x_min, x_max)

    optimizer: ps.single.GlobalBestPSO = ps.single.GlobalBestPSO(n_particles=10, dimensions=6, options=options, bounds=my_bounds)
    raise NotImplementedError
    optimizer.optimize(endurance, iters=1000)


def cde():
    c1: float = 0.5
    c2: float = 0.3
    w: float = 0.9

    x_max: list[int] = 5 * np.ones(6)
    x_min: list[int] = 5 * np.zeros(6)
    my_bounds: tuple[list[int], list[int]] = (x_min, x_max)

    options: dict[str, float] = {'c1': c1, 'c2': c2, 'w': w}
    
    optimizer = ps.single.GlobalBestPSO(n_particles=10, dimensions=6, options=options, bounds=my_bounds)
    cost, pos = optimizer.optimize(np.vectorize(endurance), iters=1000)
    print(f'{cost=}')
    print(f'{pos=}')

cde()