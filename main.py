from src.market import generate_price
from src.strategy import buy_and_hold, momentum, random_strategy
from src.utils import sharpe_ratio, summarize, plot_equity_curves, average_curve
import numpy as np


def run_strategy(strategy_fn, trials=100):
    results = []
    sharpes = []
    curves = []

    for _ in range(trials):
        prices = generate_price()
        equity = strategy_fn(prices)

        curves.append(equity)
        results.append(equity[-1])
        sharpes.append(sharpe_ratio(equity))

    return results, sharpes, curves


def main():
    bh_results, bh_sharpes, bh_curves = run_strategy(buy_and_hold)
    mom_results, mom_sharpes, mom_curves = run_strategy(momentum)
    rand_results, rand_sharpes, rand_curves = run_strategy(random_strategy)

    summarize("Buy & Hold", bh_results, bh_sharpes)
    summarize("Momentum", mom_results, mom_sharpes)
    summarize("Random", rand_results, rand_sharpes)

    bh_avg = average_curve(bh_curves)
    mom_avg = average_curve(mom_curves)
    rand_avg = average_curve(rand_curves)

    plot_equity_curves({
        "Buy & Hold": bh_avg,
        "Momentum": mom_avg,
        "Random": rand_avg
    })


if __name__ == "__main__":
    main()