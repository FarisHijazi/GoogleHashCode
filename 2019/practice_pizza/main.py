import numpy as np
import matplotlib.pyplot as plt
from matplotlib import interactive


def readFile(fname):
    with open(fname) as f:
        lines = f.readlines()
        pizza = lines[1:]    # removing the first row (containing the numbers)
        r, c, l, h = [int(x) for x in lines[0].split(' ')]
        pizza = np.array([np.array(list(map(lambda char: 1 if char == 'T' else 0, row.strip()))) for row in pizza])
        return r, c, l, h, pizza

# trying to solve
def solve(pizza, constraints):
    
    pass


import sys

if __name__ =='__main__':
    pizza_file = sys.argv[1]

    # pizzas = {
    #     "a": "a_example.in",
    #     "b": "b_small.in",
    #     "c": "c_medium.in",
    #     "d": "d_big.in"
    # }
    r, c, l, h, pizza = readFile(pizza_file)

    print(str((r, c, l, h)) + "\n" + str(pizza))

    # plot
    # plt.plot(pizza)
    fig, ax = plt.subplots()
    ax.imshow(pizza)
    ax.set_title(f'medium.in shape is {pizza.shape}, max. score {pizza.size}\nmin. ingredients is {l}, max. pizza slice is {h}')
    plt.show()

    # input("enter anything...")

