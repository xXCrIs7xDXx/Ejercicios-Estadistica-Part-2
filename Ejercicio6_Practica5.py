import scipy.stats as stats
import math

p, E, confianza = 1/6, 0.002, 0.95
Z = stats.norm.ppf((1 + confianza) / 2)
n = math.ceil((Z/E)**2 * p * (1-p))

print(f'Lanzamientos necesarios: {n}')
