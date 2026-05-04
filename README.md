# Vanilla Option Pricer

Pricer d'options vanilles européennes développé from scratch — projet pédagogique et portfolio pour un stage en finance quantitative.

**Marius Carré** · Étudiant en Finance Quantitative

---

## Fonctionnalités

| Produit | Modèles / Méthodes |
|---|---|
| Options vanilles | Black-Scholes-Merton, Monte Carlo |
| Grecques | Delta, Gamma, Vega, Theta, Rho |
| Validation | Parité Put-Call, comparaison BS vs Monte Carlo |

- **Formules analytiques** : prix Call & Put via Black-Scholes, d1 et d2
- - **Grecques complètes** : Delta, Gamma, Vega (par 1% de vol), Theta (par jour), Rho (par 1% de taux)
  - - **Monte Carlo** : simulation du mouvement brownien géométrique sur 100 000 trajectoires avec graine fixe pour la reproductibilité
    - - **Visualisation** : 4 graphiques matplotlib (trajectoires simulées, distribution terminale, convergence MC, comparaison BS/MC)
      - - **Parité Put-Call** : vérification numérique intégrée (`np.isclose`, tolérance 1e-6)
       
        - ---

        ## Installation

        ```bash
        git clone https://github.com/mariuscarre/Vanilla---option-pricer.git
        cd Vanilla---option-pricer
        pip install -r requirements.txt
        ```

        ## Lancement

        ```bash
        python main.py
        ```

        Pour générer les visualisations Monte Carlo :

        ```bash
        python plot_mc.py
        ```

        ---

        ## Paramètres

        | Paramètre | Symbole | Description |
        |---|---|---|
        | Spot price | S | Prix actuel du sous-jacent |
        | Strike price | K | Prix d'exercice de l'option |
        | Time to maturity | T | Durée jusqu'à l'échéance (en années) |
        | Risk-free rate | r | Taux sans risque annuel |
        | Volatilité | σ | Volatilité annuelle du sous-jacent |

        ---

        ## Exemple d'utilisation

        ```python
        from black_scholes import BlackScholes
        from greeks import Greeks

        bs = BlackScholes(S=100, K=100, T=1, r=0.05, sigma=0.2)
        print(f"Call : {bs.call_price():.4f}")  # 10.4506
        print(f"Put  : {bs.put_price():.4f}")   # 5.5735

        g = Greeks(S=100, K=100, T=1, r=0.05, sigma=0.2)
        print(f"Delta : {g.delta('call'):.4f}")  # 0.6368
        print(f"Gamma : {g.gamma():.4f}")        # 0.0188
        print(f"Vega  : {g.vega():.4f}")         # 0.3752
        print(f"Theta : {g.theta('call'):.4f}")  # -0.0177
        print(f"Rho   : {g.rho('call'):.4f}")    # 0.5323
        ```

        ---

        ## Structure du projet

        ```
        Vanilla---option-pricer/
        ├── black_scholes.py   # Modèle BSM : prix Call/Put, d1/d2, parité Put-Call
        ├── greeks.py          # Grecques : Delta, Gamma, Vega, Theta, Rho
        ├── monte_carlo.py     # Simulation Monte Carlo (mouvement brownien géométrique)
        ├── plot_mc.py         # Visualisations matplotlib
        ├── main.py            # Script de démonstration terminal
        └── requirements.txt   # Dépendances (numpy, scipy, matplotlib)
        ```

        ---

        ## Architecture

        Le projet repose sur une hiérarchie de classes simple et cohérente :

        ```
        BlackScholes              ← classe de base (pricing, d1/d2, parité Put-Call)
            ├── Greeks            ← héritage : calcul des grecques
            └── MonteCarlo        ← héritage : simulation GBM + comparaison BS
        ```

        ---

        ## Stack technique

        - **Python**, NumPy, SciPy
        - - **Matplotlib** (visualisations)
          - - Licence : MIT
