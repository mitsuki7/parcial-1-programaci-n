# Sistema de Gestión de Patentes (Python)

Sistema por consola desarrollado en Python modularizado para la generación, búsqueda, análisis estadístico y ordenamiento de patentes automotrices con formato argentino (`AB123CD`).

---

## 📌 Consignas y Requerimientos del Proyecto

### Formato de Patente
El sistema trabaja con patentes de 7 caracteres compuestas por: **2 letras mayúsculas + 3 números + 2 letras mayúsculas** (Ejemplos: `AB123CD`, `AA001GT`, `JT582QJ`).

---

## ⚙️ Menú de Opciones y Funcionalidades

```text
===== SISTEMA DE PATENTES =====
1. Generar patentes
2. Buscar patente
3. Informar estadísticas
4. Ordenar y mostrar patentes
5. Salir
==============================

## ⚠️ Reglas y Restricciones del Desarrollo

### ❌ Lo que NO se permite
- **Métodos nativos de cadenas y listas:** Prohibido el uso de métodos como `.append()`, `.pop()`, `.sort()`, `.upper()`, `.lower()`, `.find()`, etc.
- **Listas/Strings predefinidos para abecedario:** No se permite definir variables auxiliares como `letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"` para generar caracteres.
- **Acceso directo a opciones:** No se puede ingresar a las opciones 2, 3 o 4 sin haber ejecutado primero la opción 1.
- **Duplicados:** No se pueden generar o almacenar patentes repetidas.

---

### ✅ Lo que SÍ se permite y requiere
- **Uso de `len()`:** Permitido para obtener la longitud de listas y cadenas.
- **Generación mediante ASCII:** Uso exclusivo de la función `chr()` y tablas ASCII para crear letras mayúsculas y números de las patentes.
- **Normalización manual:** Normalización de cadenas ingresadas por el usuario mediante operaciones de código ASCII (para aceptar variantes como `Asc`, `aSC`, `DeSc`).
- **Validación con banderas (*flags*):** Control de flujo para garantizar la generación previa de datos antes de acceder al resto del menú.
- **Algoritmo propio:** Implementación completa y manual del algoritmo de ordenamiento por burbujeo (*Bubble Sort*).
- **Documentación:** Uso obligatorio de *docstrings* explicativas en cada función dentro de `funciones.py`.
