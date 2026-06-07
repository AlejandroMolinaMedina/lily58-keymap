
# Custom Split Keyboard Layout (Lily58 / Corne Type)

Este repositorio contiene la configuración personalizada de mi teclado mecánico split, optimizada para flujos de trabajo de desarrollo, administración de servidores y automatización, manteniendo un acceso rápido a macros específicas y caracteres complejos en distribuciones de teclado en español.

## 🚀 Características Principales
* **Navegación Integrada:** Flechas de dirección accesibles en la sección central (`WASD` e `IJKL`) mediante capas, evitando mover las manos de la fila de inicio.
* **Macros para Símbolos:** Soluciones integradas para caracteres conflictivos en sistemas en español como la arroba (`@`), menor/mayor que (`<`, `>`) y la barra invertida (`\`).
* **Capa de Automatización (Secretos):** Acceso rápido a strings de texto automatizados mediante la inclusión de credenciales locales (`secrets.h`).
* **Control Multimedia:** Configuración nativa de encoders rotativos para la gestión de volumen general.

---

## 🗺️ Mapa de Capas y Distribución

### Capa 0: Base (Principal)
Capa alfanumérica estándar por defecto. Combina modificadores esenciales y la gestión de capas en los pulgares para máxima ergonomía.

* **MO(1):** Mantiene activa la **Capa 1** (Símbolos/Navegación).
* **TG(2):** Alterna (Toggle) el encendido/apagado de la **Capa 2** (Secretos).
* **Encoders:** Giro antihorario (`KC_VOLD` - Bajar volumen) / Giro horario (`KC_VOLU` - Subir volumen).

```text
┌────────────────────────────────────────────────────────┐ ┌────────────────────────────────────────────────────────┐
│  ESC │   1  │   2  │   3  │   4  │   5  │          │ │          │   6  │   7  │   8  │   9  │   0  │   -  │
├──────┴───┬───┴───┬───┴───┬───┴───┬───┴───┬───┐      │ │      ┌───┴───┬───┴───┬───┴───┬───┴───┬───┴───┬──────┤
│   TAB    │   Q   │   W   │   E   │   R   │   T   │      │ │      │   Y   │   U   │   I   │   O   │   P   │   [  │
├──────────┴─┬─┬───┴───┬───┴───┬───┴───┬───┴───┼───┐  │ │  ┌───┼───┬───┴───┬───┴───┬───┴───┬───┴───┬─┴──────────┤
│   LSHIFT   │ A │   S   │   D   │   F   │   G   │   │  │ │  │   │   H   │   J   │   K   │   L   │   '   │   \  │
├────────────┴─┬─┴───┬───┴───┬───┴───┬───┴───┬───┴───┼──┤ ├──┼───┴───┬───┴───┬───┴───┬───┴───┬───┴─┬──────────┤
│   LCTRL      │   Z │   X   │   C   │   V   │   B   │ ` │ │BSPC│   N   │   M   │   ,   │   .   │   / │   RALT   │
└──────────────┴─────┴───────┴───────┴───┬───┴───┬───┴───┤ ├───┴───┬───┴───┬───┴───┬───────┴─────┴──────────┘
                                         │ MO(1) │ LALT  │ │ SPACE │ MO(2) │
                                         │       ├───────┤ ├───────┤       │
                                         │ TG(2) │ SPACE │ │ ENTER │  ]    │
                                         └───────┴───────┘ └───────┴───────┘

```

---

### Capa 1: Navegación y Símbolos (Hold)

Se accede manteniendo presionado el botón asignado en el pulgar izquierdo. Diseñada para navegación rápida y entrada de código.

* **Navegación:** Flechas mapeadas en la mano izquierda (`WASD`) y replicadas en la mano derecha (`IJKL`).
* **Macros de Símbolos:**
* `@` (Arroba): Envía `AltGr + Q`.
* `<` y `>` (Menor/Mayor que): Mapeados nativamente usando el código ISO `KC_NUBS`.
* `\` (Barra invertida): Ubicada en el pulgar derecho inferior, fuerza `AltGr + -` para asegurar su salida en layouts en español.


* **Atajos:** `KC_S_S_A` envía la combinación `Win + Shift + S` para la herramienta de recortes.

```text
┌────────────────────────────────────────────────────────┐ ┌────────────────────────────────────────────────────────┐
│   F1 │  F2   │  F3   │  F4   │  F5   │  F6   │          │ │          │  F7   │  F8   │  F9   │  F10  │  F11  │  F12  │
├──────┴───┬───┴───┬───┴───┬───┴───┬───┴───┬───┐      │ │      ┌───┴───┬───┴───┬───┴───┬───┴───┬───┴───┬──────┤
│          │   @   │   ↑   │       │       │       │      │ │      │       │       │       │       │Win+S+S│      │
├──────────┴─┬─┬───┴───┬───┴───┬───┴───┬───┴───┼───┐  │ │  ┌───┼───┬───┴───┬───┴───┬───┴───┬───┴───┬─┴──────────┤
│  _______   │ ← │   ↓   │   →   │       │       │   │  │ │  │   │   ←   │   ↓   │   ↑   │   →   │   ;   │      │
├────────────┴─┬─┴───┬───┴───┬───┴───┬───┴───┬───┴───┼──┤ ├──┼───┴───┬───┴───┬───┴───┬───┴───┬───┴─┬──────────┤
│  _______   │     │       │       │_______│       │ < │ │ > │       │       │       │       │     │          │
└──────────────┴─────┴───────┴───────┴───┬───┴───┬───┴───┤ ├───┴───┬───┴───┬───┴───┬───────┴─────┴──────────┘
                                         │       │       │ │       │       │
                                         │       ├───────┤ ├───────┤       │
                                         │       │       │ │ LGUI  │   \   │
                                         └───────┴───────┘ └───────┴───────┘

```

---

### Capa 2: Secretos y Credenciales (Toggle)

Se activa por completo presionando una vez el botón `TG(2)`. Modifica la fila numérica superior para la inserción automatizada de cadenas de texto persistentes.

* **Fila Superior:** Mapea las macros de `KC_SCRT` a `KC_SCRT3`, las cuales inyectan los strings `SECRET`, `SECRET1`, `SECRET2` y `SECRET3` definidos de forma privada.
* **Navegación Extra:** Mantiene el bloque de flechas izquierdo activo junto con un acceso directo a `Delete` (`KC_DEL`) en la sección central del pulgar derecho.

```text
┌────────────────────────────────────────────────────────┐ ┌────────────────────────────────────────────────────────┐
│ SCRT │ SCRT1 │ SCRT2 │ SCRT3 │_______│_______│          │ │          │_______│_______│_______│_______│_______│_______│
├──────┴───┬───┴───┬───┴───┬───┴───┬───┴───┬───┐      │ │      ┌───┴───┬───┴───┬───┴───┬───┴───┬───┴───┬──────┤
│          │   @   │   ↑   │       │       │       │      │ │      │       │       │       │       │       │      │
├──────────┴─┬─┬───┴───┬───┴───┬───┴───┬───┴───┼───┐  │ │  ┌───┼───┬───┴───┬───┴───┬───┴───┬───┴───┬─┴──────────┤
│   RSHIFT   │ ← │   ↓   │   →   │       │       │   │  │ │  │   │   │       │       │       │       │       │      │
├────────────┴─┬─┴───┬───┴───┬───┴───┬───┴───┬───┴───┼──┤ ├──┼───┴───┬───┴───┬───┴───┬───┴───┬───┴─┬──────────┤
│   LCTRL      │     │       │       │       │       │   │ │ │DEL│       │       │       │       │     │          │
└──────────────┴─────┴───────┴───────┴───┬───┴───┬───┴───┤ ├───┴───┬───┴───┬───┴───┬───────┴─────┴──────────┘
                                         │       │       │ │       │       │
                                         │       ├───────┤ ├───────┤       │
                                         │ TG(2) │       │ │       │       │
                                         └───────┴───────┘ └───────┴───────┘

```

---

### Capa 3: Reserva / Bloqueo

Capa actualmente configurada con exclusiones (`XXXXXXX`). Actúa como espacio reservado para futuras expansiones del firmware o funciones de macro avanzadas.

---

## 🛠️ Estructura de Archivos

* `keymap.c`: Contiene la lógica de inicialización, definición de matrices de teclas, mapa de encoders y las funciones de comportamiento en `process_record_user`.
* `secrets.h`: *(No incluido en el repositorio por seguridad)* Contiene las directivas `#define SECRET...` con las cadenas de texto privadas del usuario.

