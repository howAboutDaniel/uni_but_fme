import numpy as np
from rndwalk import rndwalk

class Neuron:
    def __init__(self, w: np.ndarray, b: float):
        self.w = w.copy()
        self.b = b

    def apply(self, x: np.ndarray):
        p = np.sum(self.w * x) + self.b
        return np.tanh(p) >= 0

class ANN_XOR:
    def __init__(self):
        self.n = [
            Neuron(np.random.uniform(-1, 1, 2), np.random.uniform(-1, 1, 1)),
            Neuron(np.random.uniform(-1, 1, 2), np.random.uniform(-1, 1, 1)),
            Neuron(np.random.uniform(-1, 1, 2), np.random.uniform(-1, 1, 1))
        ]
        self.y12 = np.zeros(2)
    def apply(self, x: np.ndarray):
        self.y12[0] = self.n[0].apply(x)
        self.y12[1] = self.n[1].apply(x)
        return self.n[2].apply(self.y12) > 0

    def set_params(self, p: np.ndarray):
        self.n[0].w[0] = p[0]
        self.n[0].w[1] = p[1]
        self.n[0].b = p[2]
        self.n[1].w[0] = p[3]
        self.n[1].w[1] = p[4]
        self.n[1].b = p[5]
        self.n[2].w[0] = p[6]
        self.n[2].w[1] = p[7]
        self.n[2].b = p[8]

def main():
    net = ANN_XOR()

    #net.set_params(np.array([-1.21060316, -1.28795002, 0.17472519, -1.60162048, -1.67721405, 1.75087937, -0.02316282,  1.24575274, -1.24138688]))

    def objective_func(x: np.ndarray):
        net.set_params(x)
        correct = 0
        for xt, yt in (([0,0], False), ([0,1], True), ([1,0], True), ([1,1], False)):
            y = net.apply(np.array(xt))
            correct += y == yt
        #print( correct)
        return 4-correct

    p, errors = rndwalk(-2, 2, 9, objective_func)
    print('errors:', errors)
    net.set_params(p)
    for x in ([0,0], [0,1], [1,0], [1,1]):
        y = net.apply(np.array(x))
        print(x, '-->', y)

if __name__ == '__main__':
    main()
