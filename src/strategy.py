def buy_and_hold(prices, spread=0.2):
    cash = 10000
    position = cash / prices[0]
    cash = 0

    equity_curve = []

    for price in prices:
        equity_curve.append(position * price)

    return equity_curve


def momentum(prices, spread=0.2, window=10):
    cash = 10000
    position = 0
    equity_curve = []

    for i in range(len(prices)):
        if i < window:
            equity_curve.append(cash)
            continue

        short_ma = sum(prices[i-3:i]) / 3
        long_ma = sum(prices[i-window:i]) / window
        price = prices[i]

        if short_ma > long_ma:
            position += 1
            cash -= price + spread
        elif short_ma < long_ma and position > 0:
            position -= 1
            cash += price - spread

        equity_curve.append(cash + position * price)

    return equity_curve


def random_strategy(prices, spread=0.2):
    import numpy as np

    cash = 10000
    position = 0
    equity_curve = []

    for i in range(len(prices)):
        price = prices[i]

        if np.random.rand() < 0.5:
            position += 1
            cash -= price + spread
        elif position > 0:
            position -= 1
            cash += price - spread

        equity_curve.append(cash + position * price)

    return equity_curve