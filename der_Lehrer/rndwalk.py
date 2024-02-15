import numpy as np


def f(x: np.ndarray):
    return np.sum(x**2+4*x-6)


def rndwalk(lb, ub, dim, objfunc):
    """
        lb, ub - spodni a horni meze
        dim - pocet dimenzi
        objfunc - ucelova funkce, musi byt Callable
    """
    best_x = np.random.uniform(lb, ub, dim)
    best_fx = objfunc(best_x)

    x: np.ndarray = best_x.copy()

    max_step = (ub-lb) / 200

    for i in range(1000000):
        step = np.random.uniform(-max_step, max_step)
        x += step

        if any(x < ub) or any(x > lb):
            x = np.random.uniform(lb, ub, dim)

        fx = objfunc(x)

        if fx < best_fx:
            print('better fx=', fx)
            best_fx = fx
            best_x = x.copy()

    return best_x, best_fx


def main():
    # rndwalk(lb=2, ub=4.5, dim=2, objfunc=f)
    rndwalk(lb=2, ub=4.5, dim=2, objfunc=f)
    x, fx = rndwalk(2, 4.5, 2, f)
    print('x:', x)
    print('f(x):', fx)


if __name__ == '__main__':
    main()
