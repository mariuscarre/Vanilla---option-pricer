import numpy as np
from black_scholes import BlackScholes


class MonteCarlo(BlackScholes):

    def __init__(self, S, K, T, r, sigma, n_simulations=100_000, seed=42):
        super().__init__(S, K, T, r, sigma)
        self.n_simulations = n_simulations
        self.seed = seed

    def simulate(self):
        np.random.seed(self.seed)
