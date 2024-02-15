import numpy as np


def f(x: np.ndarray):
    return np.sum(x**2+4*x-6)


def rndwalk(lb, ub, dim, objfunc):
    """
        lb, ub - spodni a horni meze
        dim - pocet dimenzi
        objfunc - ucelova funkce, musi byt Callable
    """
    # TODO: inicializace; nejlepsi reseni je nutno si pamatovat
    best_x = np.random.uniform(lb, ub, dim)
    best_fx = objfunc(best_x)
    # TODO: aktualni reseni
    x: np.ndarray = best_x.copy()

    # TODO: max velikost kroku z rozsahu intervalu

    max_step = (ub-lb)* 0.01

    # TODO: iterace algoritmu
    #      1) krok
    #      2) kontrola mezi
    #      3) ulozeni nejelpsiho

    for i in range(100000):
        step = np.random.uniform(-max_step, max_step, dim) # pozri si co robi metoda uniform()
        x += step

    if any(x < lb) or any(x > ub): # 2) kontrola medzí
        x = np.random.uniform(lb, ub, dim)

    fx = objfunc(x) # pozri si funkciu objfunc
    if fx < best_fx:
        best_fx = fx
        best_x = x.copy()

    
    return best_x, best_fx


def main():
    # rndwalk(lb=2, ub=4.5, dim=2, objfunc=f)
    x, fx = rndwalk(2, 4.5, 2, f)
    print('x:', x)
    print('f(x):', fx)


if __name__ == '__main__':
    main()