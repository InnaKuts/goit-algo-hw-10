import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad


def monte_carlo(f: callable(float), x_range: tuple[float, float], y_range: tuple[float, float], n=10000):
    x0, x1 = x_range
    y0, y1 = y_range
    x_random = np.random.uniform(x0, x1, n)
    y_random = np.random.uniform(y0, y1, n)

    under_curve = y_random < f(x_random)
    count = np.sum(under_curve)
    area = (x1 - x0) * (y1 - y0)
    result = area * (count / n)
    return result, (x_random, y_random, under_curve)


def func(arg):
    return 1 + np.sin(arg)


def main():
    x_range = (0, 2 * np.pi)
    y_range = (0, 2)

    mc_result, (x_random, y_random, under_curve) = monte_carlo(func, x_range, y_range)
    quad_result, _ = quad(func, x_range[0], x_range[1])

    print(f"Monte-Carlo: {mc_result}")
    print(f"Scipy-Quad: {quad_result}")

    rng = x_range[1] - x_range[0]
    x = np.linspace(x_range[0]-rng*0.5, x_range[0] + rng*1.5, 500)
    y = func(x)
    plt.plot(x, y, label='1 + sin(x)', color='blue')
    plt.scatter(x_random[~under_curve], y_random[~under_curve], color='gray', s=1, label='Random Points')
    plt.scatter(x_random[under_curve], y_random[under_curve], color='green', s=1, label='Points under curve')

    plt.axvline(x_range[0], y_range[0], y_range[1])
    plt.axvline(x_range[1], y_range[0], y_range[1])
    plt.title(
        'Integration of `1 + sin(x)`\n'
        f'Monte-Carlo: {mc_result}\n'
        f'Scipy-Quad: {quad_result}'
    )
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    main()
