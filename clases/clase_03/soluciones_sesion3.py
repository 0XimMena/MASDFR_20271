# ============================================================================
#  Soluciones — Sesión 3 (Severidad en la práctica: transformaciones)
#  Matemáticas Actuariales para Seguro de Daños, Fianzas y Reaseguro · UNAM
#
#  Cada bloque es EXACTAMENTE el código que va en la celda del ejercicio.
#  Usa las variables que ya existen en el notebook (ramos, x, real, stats, np).
# ============================================================================


# --- Ejercicio 1 — el rango de un ramo -------------------------------------
ramo_sel = ramos["Autos"]                 # cámbialo por el ramo que quieras
p95 = ramo_sel.ppf(0.95)

print(f"p95 = {p95:,.0f}")
print(f"P(X > 2·p95) = {ramo_sel.sf(2 * p95):.2%}")
print(f"Rango razonable para simular (p1–p99): "
      f"{ramo_sel.ppf(0.01):,.0f} a {ramo_sel.ppf(0.99):,.0f}")
# Muy pocos siniestros superan el doble del p95: eso es la cola.
# Simular fuera del intervalo p1–p99 genera montos que casi nunca ocurren
# en ese ramo — un error clásico al montar la cartera simulada.


# --- Ejercicio 2 — censura y truncamiento ----------------------------------
d2 = 100
print(f"Deducible d = {d2}")
print(f"Pagan 0 (censura)            : {(x <= d2).mean():.1%}")
print(f"Desaparecen si hay truncamiento: {(x <= d2).sum():,} de {len(x):,}")
print(f"Siniestros que quedan visibles : {(x > d2).sum():,}")
# Con un deducible más chico, menos siniestros caen por debajo: se pierde/censura
# menos información que con d = 200. El deducible decide cuánto de la parte baja
# de la severidad llegas siquiera a observar.


# --- Ejercicio 3 — mide el sesgo -------------------------------------------
d3 = 300
obs3 = x[x > d3]                            # datos truncados con un deducible mayor
pr3 = stats.lognorm.fit(obs3, floc=0)       # ajuste INGENUO (ignora el truncamiento)
media_ingenua = stats.lognorm(*pr3).mean()
err = (media_ingenua - real.mean()) / real.mean()

print(f"d = {d3}")
print(f"Media ingenua = {media_ingenua:,.1f}   vs   real = {real.mean():,.1f}")
print(f"Error relativo = {err:+.1%}")
# El sesgo CRECE al subir el deducible: entre más grande d, más se recorta la
# parte baja de la distribución, y el ajuste ingenuo cree que la severidad
# 'arranca' más arriba → sobrestima cada vez más la media.


# --- Ejercicio 4 — la esperanza limitada -----------------------------------
for L4 in [400, 1000]:
    lev = np.minimum(x, L4).mean()
    print(f"L = {L4:>5}:  E[min(X,L)] = {lev:>8,.1f}   "
          f"({lev / x.mean():.1%} de la prima cruda E[X])")
# Al subir L, la prima limitada se acerca a la prima cruda: cubres más de la cola.
# Con L chico, gran parte del riesgo caro queda fuera y la cobertura es más barata.


# --- Ejercicio 5 — arma tu combinación -------------------------------------
d5, L5, alpha5 = 150, 800, 0.9
pago5 = alpha5 * np.minimum(np.maximum(x - d5, 0), L5 - d5)   # coaseguro·(deducible ∧ límite)
prima5 = pago5.mean()

print(f"Deducible={d5}, Límite={L5}, Coaseguro={alpha5}")
print(f"Prima combinada : {prima5:,.1f}")
print(f"Prima cruda E[X]: {x.mean():,.1f}")
print(f"→ la combinación deja la prima en {prima5 / x.mean():.1%} de la cruda.")
# Cada cláusula recorta una parte del riesgo: el deducible quita la base, el
# límite quita la cola cara y el coaseguro escala todo. Juntas explican por qué
# la prima del producto es muy inferior a la severidad ground-up.
