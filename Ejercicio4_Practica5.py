import scipy.stats as stats

media_muestra, desviacion_tipica, n, confianza = 23, 3, 40, 0.99
Z = stats.norm.ppf((1 + confianza) / 2)
error_estandar = desviacion_tipica / (n**0.5)
intervalo_confianza = (media_muestra - Z * error_estandar, media_muestra + Z * error_estandar)

print(f'Intervalo de confianza al 99%: {intervalo_confianza}')
