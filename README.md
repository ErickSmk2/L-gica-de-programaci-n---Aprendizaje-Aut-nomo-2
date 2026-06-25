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

## Funcionalidades

- Generación automática del número candidato  
- Interacción mediante botones (mayor, menor, correcto)  
- Conteo de intentos en tiempo real  
- Registro del historial de intentos mediante una lista  
- Función para reiniciar el juego  
- Interfaz gráfica con Tkinter  

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
- Historial de intentos

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

## Fecha

25 Junio 2026

---

## Autor

Erick Obando  
Carrera: Ingeniería de Software  
Materia: Lógica de Programación