class Neuron:
    def __init__(self):
        pass
    def apply(self, x: np.ndarray):
        return 0
    
def main():
    neuron = Neuron()

    # TODO: inicializácia neurónu

    for x in ([0, 0], [0, 1], [1, 0], [1, 1]):
        y = neuron.apply(np.array(x))
        print(x, '→', y)

if __name__ == '__main__':
    main()