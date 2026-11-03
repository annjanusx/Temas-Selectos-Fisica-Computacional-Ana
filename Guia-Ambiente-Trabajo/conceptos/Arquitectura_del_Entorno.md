[← Índice de conceptos](../INDICE_CONCEPTOS.md) · [Guía principal](../Guia_Ambiente_Conda_VSCode_Python310_Internet.md)

---

# ¿Por qué esta combinación completa?


La selección puede entenderse por capas.

## Capa 1 — Reproducibilidad

```text
Miniconda + Conda + ambiente virtual
```

## Capa 2 — Lenguaje

```text
Python 3.10
```

## Capa 3 — Computación científica

```text
NumPy
SciPy
Matplotlib
Pandas
SymPy
```

## Capa 4 — Análisis y aprendizaje automático

```text
Scikit-learn
iminuit
uncertainties
```

## Capa 5 — Física de altas energías

```text
Scikit-HEP
├── uproot
├── awkward
├── vector
├── hist
├── mplhep
└── particle
```

## Capa 6 — Desarrollo

```text
VS Code
Jupyter
pytest
ruff
black
```

La intención es que cada capa aparezca cuando el problema físico la necesite.

No se pretende enseñar bibliotecas de manera aislada.

La filosofía es:

```text
problema físico
      ↓
necesidad computacional
      ↓
herramienta adecuada
```

y no:

```text
biblioteca
      ↓
buscar después un problema para usarla
```

---

---

[← Índice de conceptos](../INDICE_CONCEPTOS.md) · [Guía principal](../Guia_Ambiente_Conda_VSCode_Python310_Internet.md)
