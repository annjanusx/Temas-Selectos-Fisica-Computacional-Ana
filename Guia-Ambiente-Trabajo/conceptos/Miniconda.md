[← Índice de conceptos](../INDICE_CONCEPTOS.md) · [Guía principal](../Guia_Ambiente_Conda_VSCode_Python310_Internet.md)

---

# Miniconda


## ¿Qué es?

**Miniconda** es una distribución mínima que proporciona:

- Conda;
- un Python base;
- las herramientas necesarias para crear ambientes.

No instala por defecto una colección enorme de paquetes científicos.

## ¿Por qué Miniconda y no una distribución más grande?

Para este curso interesa que el estudiante vea explícitamente qué bibliotecas se incorporan y cuál es su función.

Con Miniconda construimos el ambiente de manera controlada:

```text
Miniconda
    ↓
crear ambiente
    ↓
instalar solamente lo necesario
```

Esto tiene una ventaja pedagógica: el estudiante distingue entre

```text
Python
```

y

```text
bibliotecas añadidas a Python
```

en lugar de recibir un entorno enorme donde todo parece formar parte del lenguaje.

## ¿Por qué no instalar simplemente Python desde python.org?

Esa instalación sería perfectamente válida para muchos proyectos. Sin embargo, Conda simplifica la administración simultánea de:

- versiones de Python;
- ambientes;
- paquetes científicos;
- dependencias compiladas.

Para un curso con estudiantes utilizando Ubuntu, Windows y macOS, disponer de un administrador de ambientes común reduce diferencias entre plataformas.

## ¿Significa que Miniconda es siempre la mejor opción?

No. Es la opción adoptada **para este curso** porque ofrece un buen equilibrio entre simplicidad, control y reproducibilidad.

---

---

[← Índice de conceptos](../INDICE_CONCEPTOS.md) · [Guía principal](../Guia_Ambiente_Conda_VSCode_Python310_Internet.md)
