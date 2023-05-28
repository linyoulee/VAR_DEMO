# VAR_DEMO

This is a simple VAR DEMO specifically for Boris K to demonstrate python code abilities + simple risk evaluation steps

This is not a ready product, the aim of the code is to demonstrate some simple concept + language handling capabilities


Here
Portfolio is a class representing a portfolio of assets. It has methods to calculate the CVaR of the portfolio (calculate_cvar), to rebalance the portfolio based on CVaR (rebalance_portfolio), and to rebalance the portfolio over time (rebalance_over_time).

In this code, we create a Portfolio object for the given symbols and dates, and then call rebalance_over_time to simulate the rebalancing of the portfolio over time. This will print the portfolio's CVaR at each rebalancing period.

Remember, this is a simplified simulation and there are many improvements that can be made. For example, it does not consider transaction costs, it assumes constant asset prices within the rebalancing period, and it uses a simple rebalancing strategy that only depends on the CVaR. In a real-world application, you would likely want to consider these factors.
