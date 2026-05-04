# Vanilla Option Pricer

Pricer d'options vanilles européennes développé from scratch — projet pédagogique et portfolio pour un stage

**Marius Carré** · Étudiant en Finance

---

## Fonctionnalités

| Produit | Modèles / Méthodes |
|---|---|
| Options vanilles | Black-Scholes-Merton, Monte Carlo |
| Grecques | Delta, Gamma, Vega, Theta, Rho |
| Validation | Parité Put-Call, comparaison BS vs Monte Carlo |

- **Formules analytiques** : prix Call & Put via Black-Scholes, d1 et d2
- **Grecques complètes** : Delta, Gamma, Vega (par 1% de vol), Theta (par jour), Rho (par 1% de taux)
- **Monte Carlo** : simulation du mouvement brownien géométrique sur 100 000 trajectoires
- **Visualisation** : 4 graphiques matplotlib (trajectoires simulées, distribution terminale, convergence MC, comparaison BS/MC)
- **Parité Put-Call** : vérification numérique intégrée

---

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
