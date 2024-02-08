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
    #      krok
    #      kontrola mezi
    #      ulozeni nejelpsiho
    
    return best_x, best_fx


def main():
    # rndwalk(lb=2, ub=4.5, dim=2, objfunc=f)
    x, fx = rndwalk(2, 4.5, 10, f)
    print('x:', x)
    print('f(x):', fx)


if __name__ == '__main__':
    main()
