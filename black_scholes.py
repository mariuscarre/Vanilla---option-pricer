import numpy as np
from scipy.stats import norm


class BlackScholes:
      """
          Black-Scholes model for pricing European vanilla options.

              Parameters
                  ----------
                      S     : float  - Current spot price of the underlying asset
                          K     : float  - Strike price
                              T     : float  - Time to maturity (in years)
                                  r     : float  - Risk-free interest rate (annual, e.g. 0.05 for 5%)
                                      sigma : float  - Volatility of the underlying asset (annual, e.g. 0.2 for 20%)
                                          """

    def __init__(self, S: float, K: float, T: float, r: float, sigma: float):
              self.S = S
              self.K = K
              self.T = T
              self.r = r
              self.sigma = sigma
              self._d1 = None
              self._d2 = None

    def d1(self) -> float:
              """Compute d1 component of the Black-Scholes formula."""
              if self._d1 is None:
                            self._d1 = (
                                              np.log(self.S / self.K) + (self.r + 0.5 * self.sigma ** 2) * self.T
                            ) / (self.sigma * np.sqrt(self.T))
                        return self._d1

    def d2(self) -> float:
              """Compute d2 component of the Black-Scholes formula."""
        if self._d2 is None:
                      self._d2 = self.d1() - self.sigma * np.sqrt(self.T)
                  return self._d2

    def call_price(self) -> float:
              """
                      Compute the price of a European Call option.

                              C = S * N(d1) - K * e^(-rT) * N(d2)
                                      """
        return (
                      self.S * norm.cdf(self.d1())
                      - self.K * np.exp(-self.r * self.T) * norm.cdf(self.d2())
        )

    def put_price(self) -> float:
              """
                      Compute the price of a European Put option.

                              P = K * e^(-rT) * N(-d2) - S * N(-d1)
                                      """
        return (
                      self.K * np.exp(-self.r * self.T) * norm.cdf(-self.d2())
                      - self.S * norm.cdf(-self.d1())
        )

    def put_call_parity_check(self) -> bool:
              """
                      Verify Put-Call Parity: C - P = S - K * e^(-rT)
                              Returns True if parity holds (within floating point tolerance).
                                      """
        lhs = self.call_price() - self.put_price()
        rhs = self.S - self.K * np.exp(-self.r * self.T)
        return np.isclose(lhs, rhs, atol=1e-6)

    def summary(self) -> dict:
              """Return a summary of inputs and prices."""
        return {
                      "S": self.S,
                      "K": self.K,
                      "T": self.T,
                      "r": self.r,
                      "sigma": self.sigma,
                      "d1": round(self.d1(), 6),
                      "d2": round(self.d2(), 6),
                      "call_price": round(self.call_price(), 6),
                      "put_price": round(self.put_price(), 6),
                      "put_call_parity": self.put_call_parity_check(),
        }
