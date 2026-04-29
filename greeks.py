import numpy as np
from scipy.stats import norm
from black_scholes import BlackScholes


class Greeks(BlackScholes):
    def delta(self, option_type="call"):
        if option_type.lower() == "call":
            return norm.cdf(self.d1())
        elif option_type.lower() == "put":
            return norm.cdf(self.d1()) - 1
        else:
            raise ValueError("option_type must be 'call' or 'put'")

    def gamma(self):
        return norm.pdf(self.d1()) / (self.S * self.sigma * np.sqrt(self.T))

    def vega(self):
        return self.S * norm.pdf(self.d1()) * np.sqrt(self.T) / 100

    def theta(self, option_type="call"):
        common = -(self.S * norm.pdf(self.d1()) * self.sigma) / (2 * np.sqrt(self.T))
        discount = self.K * np.exp(-self.r * self.T)
        if option_type.lower() == "call":
            return (common - self.r * discount * norm.cdf(self.d2())) / 365
        elif option_type.lower() == "put":
            return (common + self.r * discount * norm.cdf(-self.d2())) / 365
        else:
            raise ValueError("option_type must be 'call' or 'put'")

    def rho(self, option_type="call"):
        discount = self.K * self.T * np.exp(-self.r * self.T)
        if option_type.lower() == "call":
            return discount * norm.cdf(self.d2()) / 100
        elif option_type.lower() == "put":
            return -discount * norm.cdf(-self.d2()) / 100
        else:
            raise ValueError("option_type must be 'call' or 'put'")

    def all_greeks(self, option_type="call"):
        return {
            "option_type": option_type,
            "delta": round(self.delta(option_type), 6),
            "gamma": round(self.gamma(), 6),
            "vega": round(self.vega(), 6),
            "theta": round(self.theta(option_type), 6),
            "rho": round(self.rho(option_type), 6),
        }
