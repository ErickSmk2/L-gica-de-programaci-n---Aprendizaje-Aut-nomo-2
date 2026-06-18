# Adivina el Número (MVC + Tkinter)

## Descripción
Este proyecto consiste en un juego interactivo en el que la computadora intenta adivinar un número pensado por el usuario dentro de un rango del 1 al 100.

El sistema realiza la predicción utilizando un enfoque basado en búsqueda binaria, lo que permite reducir el número de intentos de manera eficiente.

---

## Objetivo
Aplicar los conceptos fundamentales de lógica de programación mediante:
- Uso de estructuras condicionales
- Implementación de estructuras repetitivas
- Organización del código con el patrón MVC
- Desarrollo de una interfaz gráfica

---

## Funcionamiento del sistema

1. El usuario piensa un número entre 1 y 100.
2. El sistema propone un número.
3. El usuario responde mediante botones:
   - "Es mayor"
   - "Es menor"
   - "Correcto"
4. El sistema ajusta el rango de búsqueda.
5. El proceso se repite hasta adivinar correctamente.

---

## Arquitectura (MVC)

El proyecto está organizado bajo el patrón Modelo-Vista-Controlador:

### Modelo (Model)
Gestiona los datos del sistema:
- Rango mínimo y máximo
- Número de intentos
- Cálculo del número candidato

### Vista (View)
Interfaz gráfica desarrollada con Tkinter:
- Muestra la información al usuario
- Incluye botones de interacción

### Controlador (Controller)
Contiene la lógica del juego:
- Interpreta las acciones del usuario
- Actualiza el modelo
- Controla el flujo del sistema

---

## Tecnologías utilizadas

- Python 3
- Tkinter (interfaz gráfica)
- Git y GitHub

---

## Estructuras de control utilizadas

- Condicionales (`if`, `elif`, `else`) para decisiones del sistema
- Ciclo implícito mediante `mainloop()` de Tkinter para interacción continua

---

## Análisis del desarrollo

Durante la implementación del proyecto se pudo aplicar el patrón MVC para organizar correctamente la lógica del sistema. Además, se evidenció que el uso de un algoritmo de búsqueda binaria permite optimizar la solución, reduciendo significativamente el número de intentos.

También se observó que el uso de interfaces gráficas mejora la experiencia del usuario en comparación con programas en consola.

---

## Limitaciones

El sistema depende de que el usuario proporcione respuestas correctas. Si el usuario responde de manera incorrecta o inconsistente, el algoritmo puede fallar o no encontrar el número.

---

## Posibles mejoras

- Implementar un botón de reinicio del juego
- Mostrar el número de intentos en pantalla
- Mejorar el diseño de la interfaz gráfica
- Validar errores del usuario

---

## Autor

Erick Obando  
Carrera: Ingeniería de Software  
Materia: Lógica de Programación