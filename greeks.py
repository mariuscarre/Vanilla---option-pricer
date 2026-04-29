import numpy as np
from scipy.stats import norm
from black_scholes import BlackScholes


class Greeks(BlackScholes):
      """
          Computes the Greeks for a European vanilla option using Black-Scholes.

              Inherits from BlackScholes and adds:
                  - Delta  : sensitivity to underlying price
                      - Gamma  : rate of change of delta
                          - Vega   : sensitivity to volatility
                              - Theta  : time decay (per calendar day)
                                  - Rho    : sensitivity to interest rate
                                      """

    def delta(self, option_type: str = "call") -> float:
              """
                      Delta measures the change in option price per $1 change in S.

                              Call Delta = N(d1)
                                      Put  Delta = N(d1) - 1
                                              """
              if option_type.lower() == "call":
                            return norm.cdf(self.d1())
elif option_type.lower() == "put":
            return norm.cdf(self.d1()) - 1
else:
            raise ValueError("option_type must be 'call' or 'put'")

    def gamma(self) -> float:
              """
                      Gamma measures the rate of change of Delta with respect to S.
                              Same for call and put.

                                      Gamma = N'(d1) / (S * sigma * sqrt(T))
                                              """
              return norm.pdf(self.d1()) / (self.S * self.sigma * np.sqrt(self.T))

    def vega(self) -> float:
              """
                      Vega measures sensitivity to a 1% change in volatility.
                              Same for call and put.

                                      Vega = S * N'(d1) * sqrt(T) / 100
                                              """
              return self.S * norm.pdf(self.d1()) * np.sqrt(self.T) / 100

    def theta(self, option_type: str = "call") -> float:
              """
                      Theta measures the daily time decay of the option.

                              Call Theta = [-S*N'(d1)*sigma / (2*sqrt(T)) - r*K*e^(-rT)*N(d2)] / 365
                                      Put  Theta = [-S*N'(d1)*sigma / (2*sqrt(T)) + r*K*e^(-rT)*N(-d2)] / 365
                                              """
              common = -(self.S * norm.pdf(self.d1()) * self.sigma) / (2 * np.sqrt(self.T))
              discount = self.K * np.exp(-self.r * self.T)

        if option_type.lower() == "call":
                      return (common - self.r * discount * norm.cdf(self.d2())) / 365
elif option_type.lower() == "put":
              return (common + self.r * discount * norm.cdf(-self.d2())) / 365
else:
              raise ValueError("option_type must be 'call' or 'put'")

    def rho(self, option_type: str = "call") -> float:
              """
                      Rho measures sensitivity to a 1% change in the risk-free rate.

                              Call Rho = K * T * e^(-rT) * N(d2) / 100
                                      Put  Rho = -K * T * e^(-rT) * N(-d2) / 100
                                              """
              discount = self.K * self.T * np.exp(-self.r * self.T)

        if option_type.lower() == "call":
                      return discount * norm.cdf(self.d2()) / 100
elif option_type.lower() == "put":
              return -discount * norm.cdf(-self.d2()) / 100
else:
              raise ValueError("option_type must be 'call' or 'put'")

    def all_greeks(self, option_type: str = "call") -> dict:
              """Return all Greeks for a given option type."""
              return {
                  "option_type": option_type,
                  "delta": round(self.delta(option_type), 6),
                  "gamma": round(self.gamma(), 6),
                  "vega": round(self.vega(), 6),
                  "theta": round(self.theta(option_type), 6),
                  "rho": round(self.rho(option_type), 6),
              }
