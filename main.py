import numpy as np
import pandas as pd
import yfinance as yf
from scipy.stats import norm
import matplotlib.pyplot as plt

class Portfolio:
    def __init__(self, symbols, start_date, end_date, initial_weights=None):
        self.symbols = symbols
        self.data = yf.download(symbols, start=start_date, end=end_date)['Adj Close']
        self.returns = self.data.pct_change().dropna()
        self.weights = np.array([1/len(symbols) for _ in symbols]) if initial_weights is None else initial_weights

    def calculate_cvar(self, returns, weights, confidence_level=0.05):
        port_return = np.sum(returns.mean() * weights) * 252
        port_variance = np.dot(weights.T, np.dot(returns.cov() * 252, weights))
        port_volatility = np.sqrt(port_variance)

        portfolio_cvar = port_return - (1 / confidence_level) * norm.pdf(norm.ppf(confidence_level)) * port_volatility
        return portfolio_cvar

    def rebalance_portfolio(self, shift=0.01):
        cvars = [self.calculate_cvar(self.returns[[symbol]], [1]) for symbol in self.returns.columns]
        max_cvar_asset = np.argmax(cvars)
        min_cvar_asset = np.argmin(cvars)

        self.weights[max_cvar_asset] -= shift
        self.weights[min_cvar_asset] += shift

    def rebalance_over_time(self, rebalance_days=90):
        for i in range(rebalance_days, len(self.returns), rebalance_days):
            returns_sub = self.returns.iloc[:i]
            self.rebalance_portfolio()

            portfolio_cvar = self.calculate_cvar(returns_sub, self.weights)
            print(f"Portfolio CVaR at day {i}: {portfolio_cvar * 100:.2f}%")

symbols = ['AAPL', 'MSFT', 'GOOG']  # replace with your portfolio stocks
start_date = '2018-01-01'
end_date = '2023-01-01'

portfolio = Portfolio(symbols, start_date, end_date)
portfolio.rebalance_over_time()
