import matplotlib.pyplot as plt
import numpy as np

def sharpe_ratio(equity_curve):
    equity_curve = np.array(equity_curve)

    returns = np.diff(equity_curve) / equity_curve[:-1]

    if len(returns) == 0 or np.std(returns) == 0:
        return 0

    return np.mean(returns) / np.std(returns)


def summarize(name, results, sharpes):
    print(f"\n{name}")
    print("Average Final Value:", np.mean(results))
    print("Std Dev:", np.std(results))
    print("Avg Sharpe:", np.mean(sharpes))


def plot_equity_curves(results_dict):
    plt.figure()

    for name, curve in results_dict.items():
        plt.plot(curve, label=name)

    plt.title("Equity Curves Comparison")
    plt.xlabel("Time")
    plt.ylabel("Portfolio Value")
    plt.legend()

    plt.savefig("results/equity_curves.png")
    plt.show()

def average_curve(curves):
    min_len = min(len(c) for c in curves)
    trimmed = [c[:min_len] for c in curves]
    return np.mean(trimmed, axis = 0)