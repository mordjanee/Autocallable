# Autocallable sur un indice
Sous-jacent initial : 100
Maturité : 3 ans
Observation tous les 6 mois
Coupon : 8% par an
Autocall barrier : 100% du niveau initial
Protection barrier à maturité : 60%

# Règles du payoff
À chaque date d’observation :
si le sous-jacent est au-dessus ou égal à 100% du niveau initial
→ remboursement anticipé du nominal + coupon, puis produit terminé
Si le produit n’est jamais autocallé :
à maturité, si le sous-jacent final est au-dessus de 60%
→ remboursement du nominal
sinon
→ perte en capital proportionnelle à la baisse du sous-jacent