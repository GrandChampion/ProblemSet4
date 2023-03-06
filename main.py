import scipy.optimize as opt
import matplotlib.pyplot as plt
import numpy as np

p_A = 2
p_B = 1
alpha = 0.3


def objective_function(params, alpha=0.3):
    A, B = params
    U = B**alpha * A**(1-alpha)
    return -U

# simulate and plot the optimal ratio of B to A


def simulate(pA, function, range_W, T):
    grid = np.linspace(range_W[0], range_W[1], T)
    opt_ratio = np.zeros(len(grid))

    for i in range(len(grid)):
        initial_guess = [0.1, 0.1]
        bound = ([0, 1000], [0, 1000])  # consumption larger than 0
        constraint = opt.LinearConstraint([pA, 1], 0, grid[i])
        output = opt.minimize(
            function, initial_guess, method='trust-constr', bounds=bound, constraints=constraint)
        # basket = output.x
        b1 = output.x
        b2 = output.fun
        print(b1)
        opt_ratio[i] = basket[1]/basket[0]
# Plot
    fig, ax = plt.subplots()
    ax.plot(grid, opt_ratio)
    ax.set_xlabel("W")
    ax.legend(["optimal ratio of B to A"])

    return opt_ratio


simulate(2, objective_function, [1, 3], 10)


# def objective_function2(params,alpha=0.5):
#     A,B=params
#     U=B**alpha * A**(1-alpha)
#     return -U

# simulate(2,objective_function2,[1,3],10)