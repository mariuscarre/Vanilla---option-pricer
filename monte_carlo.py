import numpy as np
from black_scholes import BlackScholes


class MonteCarlo(BlackScholes):

    def __init__(self, S, K, T, r, sigma, n_simulations=100_000, seed=42):
        super().__init__(S, K, T, r, sigma)
        self.n_simulations = n_simulations
        self.seed = seed

    def simulate(self):
        np.random.seed(self.seed)
        Z = np.random.standard_normal(self.n_simulations)
        ST = self.S * np.exp(
            (self.r - 0.5 * self.sigma ** 2) * self.T
            + self.sigma * np.sqrt(self.T) * Z
        )
        return ST

    def call_price_mc(self):
        ST = self.simulate()
        payoff = np.maximum(ST - self.K, 0)
        return np.exp(-self.r * self.T) * np.mean(payoff)

    def put_price_mc(self):
        ST = self.simulate()
        payoff = np.maximum(self.K - ST, 0)
        return np.exp(-self.r * self.T) * np.mean(payoff)

    def summary(self):
        bs_call = self.call_price()
        bs_put = self.put_price()
        mc_call = self.call_price_mc()
        mc_put = self.put_price_mc()
        return {
            "n_simulations": self.n_simulations,
            "call_BS": round(bs_call, 6),
            "call_MC": round(mc_call, 6),
            "call_error": round(abs(mc_call - bs_call), 6),
            "put_BS": round(bs_put, 6),
            "put_MC": round(mc_put, 6),
            "put_error": round(abs(mc_put - bs_put), 6),
        }
