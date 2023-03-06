import scipy.optimize as opt
import matplotlib.pyplot as plt
import numpy as np


def objective_function(ABpair, alpha=0.3):
    A = ABpair[0]
    B = ABpair[1]
    U = (B**alpha)*(A**(1-alpha))
    return -U


def simulate(pA, objFunction, wageRange):
    wageGrid = np.linspace(wageRange[0], wageRange[1], 1000)
    optimalRatios = np.zeros(len(wageGrid))
    initialGuess = [0.1, 0.1]
    boundOfAB = ([0, 10], [0, 10])
    for i in range(len(wageGrid)):
        constraintOfUtility = (
            {'type': 'lt', 'fun': lambda ABpair: (pA*ABpair[0])+ABpair[1]-wageGrid[i]})
        minima = opt.minimize(objFunction, initialGuess, method='trust-constr',
                              bounds=boundOfAB, constraints=constraintOfUtility)
        optimalRatios[i] = minima[1]/minima[0]

    # Plot
    fig, ax = plt.subplots()
    ax.plot(wageGrid, optimalRatios)
    ax.set_xlabel("W")
    ax.set_ylabel("B/A")
    ax.legend(["optimal ratio of B to A"])

    return optimalRatios


simulate(2, objective_function, [1, 3], 10)
