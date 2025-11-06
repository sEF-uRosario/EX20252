# Taller 12 - Admin, Rooms y Currency
---
## Fecha de entrega: 12 Noviembre 2025
---

## Admin

El Admin (administrador) es la interfaz de control de los experimentos.

- Se accede usualmente desde: `http://localhost:8000/admin` (modo local) o `https://tu-servidor/admin`.

- Permite:

    - Crear sesiones de los experimentos.

    - Ver y eliminar sesiones existentes.

    - Ver los participantes y su progreso.

    - Exportar los datos en formato CSV.

    - Supervisar si los jugadores están activos o no.

🔹 En resumen: el admin es la “sala de control” del investigador.

---

## Rooms

Las rooms (salas) permiten organizar o controlar cómo los participantes entran a los experimentos.

- Se configuran en el archivo `settings.py` o `__init__.py` (según la versión).

- Ejemplo:

```python
    ROOMS = [
        dict(
            name='laboratorio',
            display_name='Sala del Laboratorio',
            participant_label_file='_rooms/laboratorio.txt',
        ),
    ]
```

- En el archivo laboratorio.txt pones los nombres o códigos de los participantes (uno por línea).

- Luego acceden por una URL tipo:

```bash
    http://localhost:8000/room/laboratorio
```

🔹 En resumen: las rooms sirven para controlar el acceso de los jugadores y asignarlos fácilmente a sesiones.

---

## Currency

La currency (moneda) en oTree representa el dinero o puntos que los participantes ganan en el experimento.

- Se maneja con el tipo Currency (abreviado c).

- Ejemplo:

```python
    from otree.api import *

    class Player(BasePlayer):
        pago = models.CurrencyField()

    # Asignar valor
    p1.pago = c(100)   # 100 unidades de la moneda experimental
```

- Puedes mostrarlo en plantillas:

```html
    Tu pago es {{ player.pago }}
```


- En `settings.py` puedes definir:

```python
    REAL_WORLD_CURRENCY_CODE = 'USD'
    USE_POINTS = True
```


Esto indica si trabajas con dinero real o puntos experimentales.

🔹 En resumen: la currency es el sistema de dinero/puntos que acumulan los participantes y que luego puede convertirse en pago real.

---
### Recursos útiles

- [Documentación oficial de oTree - Admin](https://otree.readthedocs.io/en/latest/admin.html)

- [Documentación oficial de oTree - Rooms](https://otree.readthedocs.io/en/latest/rooms.html)

- [Documentación oficial de oTree - Currency](https://otree.readthedocs.io/en/latest/currency.html)

- [Ejemplos oficiales de oTree](https://www.otreehub.com/)

- [Guía rápida de oTree en español (GitHub)](https://github.com/otree-org/otree)

---

## 📚 Actividad practica

1. [Cuestionario Admin, Rooms y Currency](https://forms.gle/iWSAPFk2Uka6yeqT6)

❗**Nota:** `En esta ocasión debido a que la temática tratada no da pie para muchas variaciones, no es necesario subir código, solo responder el cuestionario.`

