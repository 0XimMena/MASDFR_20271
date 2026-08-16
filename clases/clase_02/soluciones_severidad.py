# ============================================================================
#  Soluciones — Severidad (Semana 1, Sesión de Severidad)
#  Matemáticas Actuariales para Seguro de Daños, Fianzas y Reaseguro · UNAM
#
#  Cada bloque es EXACTAMENTE el código que va en la celda del ejercicio.
#  Cópialo y pégalo en la celda correspondiente del notebook: usa las mismas
#  variables que ya existen ahí (sev, x, ajustes, aic, mejor).
# ============================================================================


# --- Ejercicio 1 — ¿qué tan sesgada está? ----------------------------------
razon = sev.mean() / sev.median()
cv    = sev.std() / sev.mean()

print(f"media / mediana = {razon:.2f}")
print(f"CV = σ/μ        = {cv:.2f}")
# Interpretación:
# media > mediana (razón > 1) y un CV alto (> 1) indican una distribución
# sesgada a la derecha, con cola pesada: unos pocos siniestros grandes
# jalan la media por encima de la mediana.


# --- Ejercicio 2 — leer la cola --------------------------------------------
p500  = (x > 500).mean()
p1000 = (x > 1000).mean()

print(f"P(X > 500)  ≈ {p500:.3f}")
print(f"P(X > 1000) ≈ {p1000:.3f}")
print(f"Un siniestro de 1000 es ~{p500 / p1000:.1f} veces más raro que uno de 500.")
# La probabilidad cae rápido al alejarnos: la cola concentra pocos eventos,
# pero son los caros. Por eso importa modelarla bien.


# --- Ejercicio 3 — reta a la mejor -----------------------------------------
# Ajustamos una distribución que no estaba en la tabla y comparamos su AIC.
extra = stats.invgauss                    # también puedes probar stats.fisk
pr_extra = extra.fit(x, floc=0)
aic_extra = aic(extra, pr_extra, x)

print(f"AIC InvGauss = {aic_extra:.1f}")
print(f"AIC {mejor} (mejor de la tabla) = {tabla.iloc[0]['AIC']:.1f}")
if aic_extra < tabla.iloc[0]["AIC"]:
    print("→ La inverse-gaussian GANA: su cola captura mejor los siniestros grandes.")
else:
    print("→ No le gana a la mejor de la tabla.")
# La inverse-gaussian tiene una cola algo más pesada que la lognormal en estos
# datos, por eso suele bajar el AIC. La lección: siempre vale probar candidatas
# fuera de la lista clásica y comparar con un criterio objetivo.


# --- Ejercicio 4 — el efecto en la prima -----------------------------------
# Prima pura con un límite L = esperanza limitada  E[min(X, L)].
def prima_limitada(nombre, L):
    d, pr = ajustes[nombre]
    return d(*pr).expect(lambda t: np.minimum(t, L))

print(f"{'L':>6}{'  E[min(X,L)] ' + mejor:>22}{'   E[min(X,L)] Pareto':>24}")
for L in [500, 1000]:
    print(f"{L:>6}{prima_limitada(mejor, L):>20,.1f}{prima_limitada('Pareto', L):>22,.1f}")

# Al subir L, la cobertura cuesta más porque se paga más de la cola.
# La distribución de cola más pesada (Pareto) hace crecer E[min(X,L)] más
# rápido: por eso, elegir mal la distribución subestima la parte cara del
# riesgo — justo la que se transfiere al reaseguro (Tema 5).


# --- Ejercicio 5 — el peso de los datos ------------------------------------
# Duplicamos la exposición y los siniestros y volvemos a graficar el posterior.
a0, b0 = 2.0, 1.0
N_obs, E_obs = 74, 40.0            # el doble que en el ejemplo
a1, b1 = a0 + N_obs, b0 + E_obs

g = np.linspace(0, 4, 400)
plt.plot(g, stats.gamma(a0, scale=1/b0).pdf(g), color="#8FA0C8", lw=2, label="prior")
plt.plot(g, stats.gamma(a1, scale=1/b1).pdf(g), color="#17A69B", lw=2.5, label="posterior (2x datos)")
plt.axvline(N_obs/E_obs, ls="--", color="gray", label=f"MLE={N_obs/E_obs:.2f}")
plt.title("Más datos → posterior más angosto y pegado al MLE")
plt.xlabel("λ"); plt.legend(); plt.show()

print(f"Media posterior = {a1/b1:.3f}   MLE = {N_obs/E_obs:.3f}")
# Con más exposición, los datos pesan más que el prior: el posterior se angosta
# (menos incertidumbre) y se pega al MLE. Esa es la intuición de la credibilidad:
# entre más experiencia propia, menos te apoyas en la información previa.
