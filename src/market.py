import numpy as np

def generate_price(n = 100, market_drift = 0.05):
    prices = [100]

    for _ in range(n):
        noise = np.random.normal(0, 1)
        change = market_drift + noise
        prices.append(prices[-1] + change)
        
    return prices