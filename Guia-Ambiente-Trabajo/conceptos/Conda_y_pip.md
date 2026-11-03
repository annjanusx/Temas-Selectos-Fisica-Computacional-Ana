[← Índice de conceptos](../INDICE_CONCEPTOS.md) · [Guía principal](../Guia_Ambiente_Conda_VSCode_Python310_Internet.md)

---

# Conda y pip


## ¿Por qué aparecen dos instaladores?

En la guía utilizamos principalmente Conda para construir el ambiente científico base y `pip` para instalar algunas bibliotecas especializadas.

La estrategia es:

```text
Conda
│
├── Python
├── NumPy
├── SciPy
├── Matplotlib
├── Pandas
└── Jupyter

pip
│
└── paquetes especializados adicionales
```

## ¿Qué es pip?

`pip` es el administrador de paquetes estándar del ecosistema Python.

Cuando escribimos:

```bash
python -m pip install paquete
```

nos aseguramos de que `pip` corresponde al mismo Python que está activo.

## ¿Por qué usamos `python -m pip` y no simplemente `pip`?

Porque hace explícita la relación:

```text
este Python
     ↓
este pip
```

y reduce la posibilidad de instalar una biblioteca accidentalmente en otro ambiente.

## Regla práctica del curso

Primero:

```bash
conda activate fisica-computacional
```

y después instalar cualquier paquete adicional.

---

---

[← Índice de conceptos](../INDICE_CONCEPTOS.md) · [Guía principal](../Guia_Ambiente_Conda_VSCode_Python310_Internet.md)
