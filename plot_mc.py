import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from monte_carlo import MonteCarlo

mc = MonteCarlo(S=100, K=100, T=1.0, r=0.05, sigma=0.20, n_simulations=100_000)
bs_call = mc.call_price()
bs_put  = mc.put_price()

fig = plt.figure(figsize=(16, 12))
fig.suptitle('Monte Carlo - Visualisation complete', fontsize=16, fontweight='bold')
gs = gridspec.GridSpec(2, 2, hspace=0.4, wspace=0.35)

ax1 = fig.add_subplot(gs[0, 0])
np.random.seed(42)
n_paths = 300
steps = 252
dt = mc.T / steps
t = np.linspace(0, mc.T, steps + 1)
paths = np.zeros((steps + 1, n_paths))
paths[0] = mc.S
for i in range(1, steps + 1):
    Z = np.random.standard_normal(n_paths)
    paths[i] = paths[i-1] * np.exp((mc.r - 0.5 * mc.sigma**2) * dt + mc.sigma * np.sqrt(dt) * Z)
ax1.plot(t, paths, alpha=0.07, color='steelblue', linewidth=0.8)
ax1.axhline(mc.K, color='red', linestyle='--', linewidth=1.5, label=f'Strike K={mc.K}')
ax1.axhline(mc.S, color='orange', linestyle=':', linewidth=1.5, label=f'Spot S={mc.S}')
ax1.set_title('Trajectoires simulees du sous-jacent', fontweight='bold')
ax1.set_xlabel('Temps (annees)')
ax1.set_ylabel('Prix S(t)')
ax1.legend(fontsize=9)

ax2 = fig.add_subplot(gs[0, 1])
ST = mc.simulate()
ax2.hist(ST, bins=120, color='steelblue', edgecolor='none', alpha=0.75, density=True)
ax2.axvline(mc.K, color='red', linestyle='--', linewidth=1.5, label=f'Strike K={mc.K}')
ax2.axvline(ST.mean(), color='green', linestyle='-', linewidth=1.5, label=f'Moyenne ST={ST.mean():.1f}')
itm_call = ST[ST > mc.K]
ax2.hist(itm_call, bins=120, color='green', edgecolor='none', alpha=0.35, density=True, label='ITM (call)')
ax2.set_title('Distribution des prix finaux ST', fontweight='bold')
ax2.set_xlabel('Prix final ST')
ax2.set_ylabel('Densite')
ax2.legend(fontsize=9)

ax3 = fig.add_subplot(gs[1, 0])
payoff_call = np.maximum(ST - mc.K, 0)
payoff_put  = np.maximum(mc.K - ST, 0)
discount    = np.exp(-mc.r * mc.T)
ax3.hist(payoff_call[payoff_call > 0], bins=80, color='green', alpha=0.6,
         label=f'Call payoffs (prix MC={discount*payoff_call.mean():.4f})', density=True)
ax3.hist(payoff_put[payoff_put > 0], bins=80, color='tomato', alpha=0.6,
         label=f'Put payoffs (prix MC={discount*payoff_put.mean():.4f})', density=True)
ax3.axvline(bs_call / discount, color='green', linestyle='--', linewidth=1.5,
            label=f'BS Call E[payoff]={bs_call/discount:.4f}')
ax3.axvline(bs_put  / discount, color='red',   linestyle='--', linewidth=1.5,
            label=f'BS Put E[payoff]={bs_put/discount:.4f}')
ax3.set_title('Distribution des payoffs (ITM uniquement)', fontweight='bold')
ax3.set_xlabel('Payoff')
ax3.set_ylabel('Densite')
ax3.legend(fontsize=8)

ax4 = fig.add_subplot(gs[1, 1])
np.random.seed(42)
ns = np.logspace(2, 5, 60).astype(int)
Z_all = np.random.standard_normal(100_000)
ST_all = mc.S * np.exp((mc.r - 0.5*mc.sigma**2)*mc.T + mc.sigma*np.sqrt(mc.T)*Z_all)
mc_calls = []
mc_puts  = []
for n in ns:
    st = ST_all[:n]
    mc_calls.append(np.exp(-mc.r*mc.T) * np.maximum(st - mc.K, 0).mean())
    mc_puts.append( np.exp(-mc.r*mc.T) * np.maximum(mc.K - st, 0).mean())
ax4.semilogx(ns, mc_calls, color='green',  linewidth=1.5, alpha=0.8, label='MC Call')
ax4.semilogx(ns, mc_puts,  color='tomato', linewidth=1.5, alpha=0.8, label='MC Put')
ax4.axhline(bs_call, color='green',  linestyle='--', linewidth=1.2, label=f'BS Call={bs_call:.4f}')
ax4.axhline(bs_put,  color='red',    linestyle='--', linewidth=1.2, label=f'BS Put={bs_put:.4f}')
ax4.set_title('Convergence MC -> Black-Scholes', fontweight='bold')
ax4.set_xlabel('Nombre de simulations (log)')
ax4.set_ylabel('Prix estime')
ax4.legend(fontsize=9)
ax4.grid(True, alpha=0.3)

plt.savefig('monte_carlo_visualisation.png', dpi=150, bbox_inches='tight')
print("Graphique sauvegarde : monte_carlo_visualisation.png")
plt.show()
