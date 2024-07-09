# DashOptionPricing

A Plotly Dash Application to Price European Call and Put Options code for the following post https://www.codearmo.com/python-tutorial/financial-option-pricing-dashboard-python-dash#

Welcome to DashOptionPricing, a powerful and interactive web application built with Plotly Dash to help you price European call and put options. This application provides a user-friendly interface to input various parameters and calculate option prices using the Black-Scholes model, taking into account dividends and other factors.

## Features

- **Interactive UI**: Easily input parameters such as stock price, strike price, days to expiry, risk-free rate, dividend yield, and volatility.
- **Option Types**: Choose between call and put options.
- **Real-time Calculation**: Instantly calculate the option price upon submitting your input.
- **Professional Design**: A polished, intuitive design to enhance user experience.

## How to Use

1. **Option Type**: Select 'Call' or 'Put' from the dropdown.
2. **Stock Price (S)**: Enter the current stock price.
3. **Strike Price (K)**: Enter the strike price of the option.
4. **Days to Expiry**: Enter the number of days until the option expires.
5. **Risk-free Rate (r)**: Enter the annualized risk-free interest rate (default is 0.05).
6. **Dividend Yield (q)**: Enter the annualized dividend yield (default is 0).
7. **Volatility (σ)**: Enter the annualized volatility (default is 0.3).
8. **Submit**: Click the 'Submit' button to calculate the option price.

## Getting Started

To get started with the application, follow these steps:

1. Clone the repository:
   ```sh
   git clone https://github.com/codearmo/DashOptionPricing.git

2. Navigate to project directory
   ```sh
    cd DashOptionPricing

3. Install the requirements 
   ```sh
   pip install -r requirements.txt

4. Run the app 
   ```sh 
   python app.py 


Now you can find the Dash sample application at http://127.0.0.1:8050/

