# Taller 11 - Bots
---
## Fecha de entrega: 05 Noviembre 2025
---
## ¿Qué son los Bots en oTree?

Los Bots son **simulaciones de jugadores** que recorren tu aplicación de oTree paso a paso, respondiendo automáticamente a las preguntas o decisiones que se presentan en las páginas.
Sirven para verificar que la lógica del juego, los pagos, las condiciones y la navegación funcionen correctamente.

---

## ¿Dónde se definen?

Se definen dentro del archivo principal `__init__.py` (en versiones nuevas de oTree).
El bloque típico es así:

```python
    from otree.api import Bot, Submission

    class PlayerBot(Bot):

        def play_round(self):
            # Ejemplo: responder una pregunta llamada "choice"
            yield self.page_class('DecisionPage', {'choice': 1})

            # Continuar a la siguiente página
            yield self.page_class('ResultsPage')
```

---

## ¿Cómo ejecutar los Bots?

En la terminal, dentro del proyecto oTree, ejecutas:
 
```bash
    otree test nombre_app
```


o para probar todo el proyecto:

```bash
    otree test
```

Esto simula varios jugadores y grupos según lo definido en `Constants`.

---

## ¿Qué puedes probar con ellos?

- Que las páginas se muestran en el orden correcto.

- Que las variables y pagos se calculan bien.

- Que las condiciones (`is_displayed`, tiempos, etc.) funcionan.

- Que las decisiones y respuestas del jugador son válidas.

---

## 📚 Actividad practica


❗**Nota:** `Recordar usar el método de entrega de actividades y parciales indicado en la sección de "Entrega de actividades y parciales" del curso.` *[Click para visitar "Entrega de actividades y parciales" en la introducción del curso.](../../README.md)*

1. [QUIZ Markets and Auctions](https://forms.gle/9S1QaHSUsTvyQCqRA)

2. Decision Bots:

    - Versión A - B:

        a. Realizar un Fetch del repositorio de GitHub.

        b. En el condicional de la pagina `Decision`, definir el `player.choice` dependiendo de la versión asignada.

        c. En `tests.py` definir el Bot para que escoja la opción correspondiente a la versión asignada.

        d. En el `NAME_IN_URL` del init, definir el nombre correspondiente a la versión asignada (Después del nombre por defecto con un **"_"**).

        e. Corregir el `settings.py` para que el proyecto reconozca la app con el nombre correcto.

        f. Ejecutar el Bot y tomar una ScreenShot del resultado en la terminal. Usar el comando `otree test nombre_app`.



❗**Nota:** `Este taller es igual para ambas versiones, con la diferencia de asignación en la letra correspondiente.`


En la siguiente lista se realiza la asignación de la versión a entregar. La asignación se realizó **al azar** y a **cada ID** de le asignó **una versión**: 

<img src="../../imgs/9/Lista_Taller_9.png" style="margin: 20px;">

Dependiendo de la versión asignada, deberás cumplir con las tareas correspondientes a cada una y para una mejor verificación de lo realizado **tomar una ScreenShot al finalizar cada inciso**, **adjuntar las imágenes con el proyecto creado en un zip al correo designado**. Evitar archivos adicionales en el zip, **solo** debe contener la carpeta del proyecto y las imágenes solicitadas. Verificar que el proyecto enviado tenga los **cambios guardados**.

Enlaces de interés:

- [Apoyo Taller 11]()

- [Rúbrica de calificación]()