# Marketing Simulation and Trading Strategy Backtesting Framework

An experimental modular Python framework for simulating stochastic markets and evaluating trading strategies using Monte Carlo backtesting and risk-adjusted metrics.

---

## Overview

This project simulates artificial financial markets and tests trading strategies under realistic conditions such as:

- Stochastic price movement (drift, market noise)
- Transaction costs (spread)
- Varying trading strategies
- Monte Carlo simulation
- Risk-adjusted evaluation (Sharpe ratio)
- Equity curve visualization

---

## Trading Strategies

### Buy and Hold
Baseline strategy holding full exposure.

### Momentum-Based
Follows the market trend using moving averages across time windows.

### Random Strategy
Control strategy for baseline comparisons.

---

## Key Metrics

- Final portfolio value
- Standard deviation
- Sharpe ratio
- Equity curves

---

## Tech Stack

- Python
- NumPy
- Matplotlib