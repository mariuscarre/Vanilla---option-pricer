# Vanilla Option Pricer

A Python implementation of the **Black-Scholes model** for pricing European vanilla options (Call & Put) with full Greeks computation.

## Features

- European Call and Put pricing using Black-Scholes formula
- - Greeks: Delta, Gamma, Vega, Theta, Rho
  - - Put-Call Parity validation
    - - Monte Carlo simulation for price verification
     
      - ## Project Structure
     
      - ```
        vanilla-option-pricer/
        ├── black_scholes.py    # Black-Scholes pricing model
        ├── greeks.py           # Greeks computation (Delta, Gamma, Vega, Theta, Rho)
        ├── main.py             # Usage example
        └── requirements.txt    # Dependencies
        ```

        ## Parameters

        | Parameter | Symbol | Description |
        |-----------|--------|-------------|
        | S | Spot price | Current price of the underlying asset |
        | K | Strike price | Option exercise price |
        | T | Time to maturity | In years |
        | r | Risk-free rate | Annual risk-free interest rate |
        | sigma | Volatility | Annual volatility of the underlying |

        ## Quick Start

        ```python
        from black_scholes import BlackScholes

        bs = BlackScholes(S=100, K=100, T=1, r=0.05, sigma=0.2)

        print(f"Call price : {bs.call_price():.4f}")
        print(f"Put price  : {bs.put_price():.4f}")
        ```

        ## Greeks

        ```python
        from greeks import Greeks

        g = Greeks(S=100, K=100, T=1, r=0.05, sigma=0.2)

        print(f"Delta : {g.delta('call'):.4f}")
        print(f"Gamma : {g.gamma():.4f}")
        print(f"Vega  : {g.vega():.4f}")
        print(f"Theta : {g.theta('call'):.4f}")
        print(f"Rho   : {g.rho('call'):.4f}")
        ```

        ## Installation

        ```bash
        git clone https://github.com/mariuscarre/Vanilla---option-pricer.git
        cd Vanilla---option-pricer
        pip install -r requirements.txt
        ```

        ## Dependencies

        - numpy
        - - scipy
         
          - ## License
         
          - MIT
