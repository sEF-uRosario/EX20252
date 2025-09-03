# Taller 5 - Pages
---
## Fecha de entrega: 10 Septiembre 2025
---

## Definición básica

- Cada *Page* es una clase en el archivo `__init__.py`.

- Controla qué se muestra y cómo interactúa el jugador.

- Se asocia normalmente con una plantilla *HTML* en la carpeta `templates`.

```python
    class MyPage(Page):
        form_model = 'player'
        form_fields = ['age', 'gender']
```

Esto muestra un formulario con las variables `age` y `gender` del jugador.

---

## Atributos importantes

`form_model` → indica de qué modelo provienen los campos (`player`, `group`, `subsession`).

`form_fields` → lista de variables que aparecerán como formulario.

`timeout_seconds` → tiempo límite en segundos para esa página.

`timer_text` → texto que se muestra junto al contador.

---

## Métodos comunes

`is_displayed(self)`

Decide si la página se muestra o no:

```python
    def is_displayed(self):
        return self.player.round_number == 1
```

`before_next_page(self, timeout_happened)`

Se ejecuta justo antes de avanzar a la siguiente página:

```python
    def before_next_page(self, timeout_happened):
        if timeout_happened:
            self.player.response = -1
```

`vars_for_template(self)`

Pasa variables extra al HTML:

```python
    def vars_for_template(self):
        return dict(payoff=self.player.payoff)
```

---

## Orden de las páginas

Al final del archivo `__init__.py` se define la lista `page_sequence`, que indica en qué orden se muestran:

```python
    page_sequence = [Consent, Instructions, MyPage, Results]
```

---

## Plantillas HTML

- Cada Page busca un archivo con el mismo nombre en templates/nombre_app/.

- Ejemplo: para class MyPage(Page) → templates/nombre_app/MyPage.html.

Ejemplo de HTML:

```html
    {% extends "global/Page.html" %}
    {% block content %}
        <h1>Por favor ingresa tus datos</h1>
        {{ formfields }}
        <button type="submit">Continuar</button>
    {% endblock %}
```

---

## Resumen

- Las Pages son las pantallas del experimento.

- Cada clase Page controla qué ve el participante, qué datos ingresa, cuánto tiempo tiene y en qué orden aparece.

- Se conectan con plantillas HTML para mostrar la interfaz.

---

### Recursos útiles

- [Documentación oficial de oTree - Models](https://otree.readthedocs.io/en/latest/pages.html)

- [Ejemplos oficiales de oTree](https://www.otreehub.com/)

- [Guía rápida de oTree en español (GitHub)](https://github.com/otree-org/otree)

---
## 📚 Actividad practica 


❗**Nota:** `Recordar usar el método de entrega de actividades y parciales indicado en la sección de "Entrega de actividades y parciales" del curso.` *[Click para visitar "Entrega de actividades y parciales" en la introducción del curso.](../../README.md)*

1. [QUIZ Coordination](https://forms.gle/fkPgumXodH44Xj5i9)

2. :

    - Versión A:

        a. Realizar un Fetch del repositorio de GitHub.

        b. 

    ---

    - Versión B:

        a. Realizar un Fetch del repositorio de GitHub.

        b. 

En la siguiente lista se realiza la asignación de la versión a entregar. La asignación se realizó **al azar** y a **cada ID** de le asignó **una versión**: 

<img src="../../imgs/5/Lista_Taller_5.png" style="margin: 20px;">

Dependiendo de la versión asignada, deberás cumplir con las tareas correspondientes a cada una y para una mejor verificación de lo realizado **tomar una ScreenShot al finalizar cada inciso**, **adjuntar las imágenes con el proyecto creado en un zip al correo designado**. Evitar archivos adicionales en el zip, **solo** debe contener la carpeta del proyecto y las imágenes solicitadas. Verificar que el proyecto enviado tenga los **cambios guardados**.

Enlaces de interés:

- [Apoyo Taller 4]()

- [Rúbrica de calificación]()