[← Índice de conceptos](../INDICE_CONCEPTOS.md) · [Guía principal](../Guia_Ambiente_Conda_VSCode_Python310_Internet.md)

---

# Conda


## ¿Qué es?

**Conda** cumple dos funciones relacionadas:

1. administra ambientes;
2. instala paquetes y sus dependencias.

Por ejemplo:

```bash
conda create -n fisica-computacional python=3.10
```

significa, conceptualmente:

```text
crear un espacio aislado
        +
instalar Python 3.10 dentro de él
```

## ¿Por qué lo usamos?

Porque necesitamos controlar la versión de Python y mantener un entorno semejante en los tres sistemas operativos considerados.

Conda resulta especialmente conveniente cuando algunas dependencias científicas incluyen componentes compilados.

## Conda no es Python

Conviene separar ambos conceptos:

```text
Conda → administra el entorno

Python → ejecuta nuestros programas
```

---

---

[← Índice de conceptos](../INDICE_CONCEPTOS.md) · [Guía principal](../Guia_Ambiente_Conda_VSCode_Python310_Internet.md)
