import scipy.stats as stats

exitos, n, confianza = 72, 400, 0.90
p_muestra = exitos / n
Z = stats.norm.ppf((1 + confianza) / 2)
error_estandar = ((p_muestra * (1 - p_muestra)) / n)**0.5
intervalo_confianza = (p_muestra - Z * error_estandar, p_muestra + Z * error_estandar)

print(f'Intervalo de confianza al 90%: {intervalo_confianza}')

