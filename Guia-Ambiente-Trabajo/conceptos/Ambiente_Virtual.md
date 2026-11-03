[← Índice de conceptos](../INDICE_CONCEPTOS.md) · [Guía principal](../Guia_Ambiente_Conda_VSCode_Python310_Internet.md)

---

# Ambiente virtual


## ¿Qué es?

Un **ambiente virtual** es un espacio aislado que contiene una versión específica de Python y un conjunto definido de bibliotecas.

Conceptualmente podemos representarlo como

```text
Sistema operativo
│
├── Python del sistema
│
└── ambiente fisica-computacional
    ├── Python 3.10
    ├── NumPy
    ├── SciPy
    ├── Matplotlib
    └── ...
```

## ¿Por qué lo utilizamos?

Porque evita que el curso dependa de la configuración particular de cada computadora.

Dos estudiantes pueden utilizar sistemas operativos diferentes y, aun así, trabajar con versiones compatibles de Python y de las bibliotecas.

También evita modificar innecesariamente el Python que utiliza el propio sistema operativo.

## ¿Qué problema resuelve?

Sin un ambiente aislado pueden aparecer situaciones como:

```text
Estudiante A → NumPy versión X
Estudiante B → NumPy versión Y
Estudiante C → Python distinto
```

y un mismo programa podría comportarse de forma diferente.

Con un ambiente común buscamos aproximarnos a:

```text
misma versión de Python
        +
mismo conjunto de dependencias
        ↓
resultados reproducibles
```

## ¿Por qué es importante en física?

La **reproducibilidad computacional** forma parte del método científico. No basta con que un cálculo funcione una vez en una computadora particular; debemos poder reconstruir el entorno en el que se obtuvo.

---

---

[← Índice de conceptos](../INDICE_CONCEPTOS.md) · [Guía principal](../Guia_Ambiente_Conda_VSCode_Python310_Internet.md)
