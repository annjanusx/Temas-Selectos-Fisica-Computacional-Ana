[← Índice de conceptos](../INDICE_CONCEPTOS.md) · [Guía principal](../Guia_Ambiente_Conda_VSCode_Python310_Internet.md)

---

# Intérprete de Python


## ¿Qué significa “intérprete”?

El intérprete es el ejecutable de Python que realmente ejecuta el programa.

Cuando existen varios ambientes puede haber varios Python instalados:

```text
Python del sistema
Python del ambiente A
Python del ambiente B
```

Seleccionar un intérprete en VS Code significa decir:

> **utiliza este Python concreto para ejecutar mis archivos.**

## ¿Por qué debemos seleccionar `fisica-computacional`?

Porque las bibliotecas del curso fueron instaladas en ese ambiente.

Si VS Code utiliza otro Python, puede aparecer un error como:

```text
ModuleNotFoundError
```

aunque la biblioteca esté correctamente instalada en Conda.

---

---

[← Índice de conceptos](../INDICE_CONCEPTOS.md) · [Guía principal](../Guia_Ambiente_Conda_VSCode_Python310_Internet.md)
