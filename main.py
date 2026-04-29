from black_scholes import BlackScholes
from greeks import Greeks


def main():
      # --- Parameters ---
      S = 100       # Spot price
    K = 100       # Strike price (at-the-money)
    T = 1.0       # Time to maturity: 1 year
    r = 0.05      # Risk-free rate: 5%
    sigma = 0.20  # Volatility: 20%

    print("=" * 50)
    print("       VANILLA OPTION PRICER - BLACK SCHOLES")
    print("=" * 50)
    print(f"  Spot (S)      : {S}")
    print(f"  Strike (K)    : {K}")
    print(f"  Maturity (T)  : {T} year(s)")
    print(f"  Risk-free (r) : {r * 100:.1f}%")
    print(f"  Volatility    : {sigma * 100:.1f}%")
    print("=" * 50)

    # --- Pricing ---
    bs = BlackScholes(S=S, K=K, T=T, r=r, sigma=sigma)

    print("\n  PRICES")
    print(f"  Call price    : {bs.call_price():.4f}")
    print(f"  Put price     : {bs.put_price():.4f}")
    print(f"  d1            : {bs.d1():.4f}")
    print(f"  d2            : {bs.d2():.4f}")
    print(f"  Put-Call Parity OK: {bs.put_call_parity_check()}")

    # --- Greeks ---
    g = Greeks(S=S, K=K, T=T, r=r, sigma=sigma)

    print("\n  GREEKS - CALL")
    print(f"  Delta  : {g.delta('call'):.4f}")
    print(f"  Gamma  : {g.gamma():.4f}")
    print(f"  Vega   : {g.vega():.4f}  (per 1% vol move)")
    print(f"  Theta  : {g.theta('call'):.4f}  (per day)")
    print(f"  Rho    : {g.rho('call'):.4f}   (per 1% rate move)")

    print("\n  GREEKS - PUT")
    print(f"  Delta  : {g.delta('put'):.4f}")
    print(f"  Gamma  : {g.gamma():.4f}")
    print(f"  Vega   : {g.vega():.4f}  (per 1% vol move)")
    print(f"  Theta  : {g.theta('put'):.4f}  (per day)")
    print(f"  Rho    : {g.rho('put'):.4f}   (per 1% rate move)")

    print("\n" + "=" * 50)


if __name__ == "__main__":
      main()
