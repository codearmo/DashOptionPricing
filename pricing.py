import numpy as np
from scipy.stats import norm

# Alias for the cumulative distribution function (CDF) of the standard normal distribution
N = norm.cdf

# Black-Scholes formula for European call options with dividends
def BS_CALLDIV(S, K, T, r, q, sigma):
    """
    Calculate the Black-Scholes price for a European call option with dividends.

    Parameters:
    S : float
        Current stock price
    K : float
        Strike price
    T : float
        Time to maturity (in years)
    r : float
        Risk-free interest rate (annualized)
    q : float
        Dividend yield (annualized)
    sigma : float
        Volatility of the underlying stock (annualized)

    Returns:
    float
        Price of the European call option
    """
    # Calculate d1 and d2 using the Black-Scholes formula
    d1 = (np.log(S/K) + (r - q + sigma**2/2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    # Calculate the call option price
    call_price = S * np.exp(-q * T) * N(d1) - K * np.exp(-r * T) * N(d2)
    return call_price

# Black-Scholes formula for European put options with dividends
def BS_PUTDIV(S, K, T, r, q, sigma):
    """
    Calculate the Black-Scholes price for a European put option with dividends.

    Parameters:
    S : float
        Current stock price
    K : float
        Strike price
    T : float
        Time to maturity (in years)
    r : float
        Risk-free interest rate (annualized)
    q : float
        Dividend yield (annualized)
    sigma : float
        Volatility of the underlying stock (annualized)

    Returns:
    float
        Price of the European put option
    """
    # Calculate d1 and d2 using the Black-Scholes formula
    d1 = (np.log(S/K) + (r - q + sigma**2/2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    # Calculate the put option price
    put_price = K * np.exp(-r * T) * N(-d2) - S * np.exp(-q * T) * N(-d1)
    return put_price
