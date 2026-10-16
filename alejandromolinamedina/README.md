
# Custom Split Keyboard Layout (Lily58 / Corne Type)

Este repositorio contiene la configuración personalizada de mi teclado mecánico split, optimizada para flujos de trabajo de desarrollo, administración de servidores y automatización, manteniendo un acceso rápido a macros específicas y caracteres complejos en distribuciones de teclado en español.

## 🚀 Características Principales
* **Navegación Integrada:** Flechas de dirección accesibles en la sección central (`WASD` e `IJKL`) mediante capas, evitando mover las manos de la fila de inicio.
* **Macros para Símbolos:** Soluciones integradas para caracteres conflictivos en sistemas en español como la arroba (`@`), menor/mayor que (`<`, `>`) y la barra invertida (`\`).
* **Capa de Automatización (Secretos):** Acceso rápido a strings de texto automatizados mediante la inclusión de credenciales locales (`secrets.h`).
* **Control Multimedia:** Configuración nativa de encoders rotativos para la gestión de volumen general.
* **Capa de macOS:** Capa 4 conmutable con `TG(4)`, que cambia los pulgares a Cmd y Option sin tocar el resto del layout. El mismo teclado sirve en Windows/Linux y en Mac.

---

## 🗺️ Mapa de Capas y Distribución

### Capa 0: Base (Principal)
Capa alfanumérica estándar por defecto. Combina modificadores esenciales y la gestión de capas en los pulgares para máxima ergonomía.

* **MO(1):** Mantiene activa la **Capa 1** (Símbolos/Navegación).
* **MO(2):** Mantiene activa la **Capa 2** (Secretos), en el pulgar derecho.
* **TG(3):** Alterna (Toggle) la **Capa 3**, en el pulgar izquierdo. Ojo: la capa 3
  esta casi vacia, asi que si la activas sin querer el teclado parece muerto.
  Se sale presionando esa misma tecla otra vez, o desconectando el teclado.
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
                                         │ TG(3) │ SPACE │ │ ENTER │  ]    │
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


* **Atajos de captura:** `KC_S_S_A` envía `Win + Shift + S` (herramienta de recortes de Windows) y `KC_S_S_AMAC` envía `Cmd + Ctrl + Shift + 4` (captura de región al portapapeles en macOS), en el pulgar derecho.
* **TG(4):** Alterna la **Capa 4** (macOS), en el pulgar derecho. Es la única tecla que entra y sale de esa capa.

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
                                         │       │       │ │SS_MAC │ TG(4) │
                                         │       ├───────┤ ├───────┤       │
                                         │       │       │ │ LGUI  │   \   │
                                         └───────┴───────┘ └───────┴───────┘

```

---

### Capa 2: Secretos y Credenciales

Se activa manteniendo presionado `MO(2)` en el pulgar derecho. Modifica la fila numérica superior para la inserción automatizada de cadenas de texto persistentes.

* **Fila Superior:** `KC_SCRT` a `KC_SCRT3` inyectan los strings `SECRET` a `SECRET3`, definidos de forma privada. `KC_SCRT4` y `KC_SCRT5` escriben un correo completo (usuario, la arroba y el dominio). `KC_SCRT6` inyecta `SECRET6` y es la primera tecla de la mano derecha.
* **Navegación Extra:** Mantiene el bloque de flechas izquierdo activo junto con un acceso directo a `Delete` (`KC_DEL`) en la sección central del pulgar derecho.
* **Pulgares:** sin asignar en esta capa. Los nueve `#define` que necesita `secrets.h` están listados en `secrets.h.example`.

```text
┌────────────────────────────────────────────────────────┐ ┌────────────────────────────────────────────────────────┐
│ SCRT │ SCRT1 │ SCRT2 │ SCRT3 │ SCRT4 │ SCRT5 │          │ │          │ SCRT6 │_______│_______│_______│_______│_______│
├──────┴───┬───┴───┬───┴───┬───┴───┬───┴───┬───┐      │ │      ┌───┴───┬───┴───┬───┴───┬───┴───┬───┴───┬──────┤
│          │   @   │   ↑   │       │       │       │      │ │      │       │       │       │       │       │      │
├──────────┴─┬─┬───┴───┬───┴───┬───┴───┬───┴───┼───┐  │ │  ┌───┼───┬───┴───┬───┴───┬───┴───┬───┴───┬─┴──────────┤
│   RSHIFT   │ ← │   ↓   │   →   │       │       │   │  │ │  │   │   │       │       │       │       │       │      │
├────────────┴─┬─┴───┬───┴───┬───┴───┬───┴───┬───┴───┼──┤ ├──┼───┴───┬───┴───┬───┴───┬───┴───┬───┴─┬──────────┤
│   LCTRL      │     │       │       │       │       │   │ │ │DEL│       │       │       │       │     │          │
└──────────────┴─────┴───────┴───────┴───┬───┴───┬───┴───┤ ├───┴───┬───┴───┬───┴───┬───────┴─────┴──────────┘
                                         │       │       │ │       │       │
                                         │       ├───────┤ ├───────┤       │
                                         │       │       │ │       │       │
                                         └───────┴───────┘ └───────┴───────┘

```

---

### Capa 3: Reserva / Bloqueo

Se alterna con `TG(3)` desde la capa 0. Casi todo son exclusiones (`XXXXXXX`), con solo el bloque de flechas izquierdo, `RSHIFT`, `LCTRL`, `` ` `` y `DEL` definidos, así que al activarla el teclado parece muerto. Se sale con la misma tecla, que sigue siendo `TG(3)` dentro de la capa. Espacio reservado para futuras expansiones.

---

### Capa 4: macOS (Toggle)

Se alterna con `TG(4)`, en el pulgar derecho de la capa 1: se mantiene `MO(1)` y se toca esa tecla, tanto para entrar como para salir.

Cambia **solo dos teclas** de pulgar izquierdo y deja el resto del layout intacto:

* **Cmd** (`KC_LGUI`) donde la capa 0 tiene `LALT`.
* **Option** (`KC_LALT`) a su derecha, donde la capa 0 tiene `TG(3)`.

```text
                                         │ MO(1) │  CMD  │ │ SPACE │ MO(2) │
                                         │       ├───────┤ ├───────┤       │
                                         │OPTION │ SPACE │ │ ENTER │  ]    │
                                         └───────┴───────┘ └───────┴───────┘
```

Todo lo demás va transparente (`_______`) a propósito, y conviene no "completar" esta capa: QMK resuelve cada tecla de la capa activa más alta hacia abajo y se detiene en la primera que no sea transparente, así que una capa 4 con el layout completo taparía a las capas 1, 2 y 3 — y dejaría `TG(4)`, que vive en la capa 1, inalcanzable: no habría forma de salir salvo desconectar el teclado.

Dos consecuencias de ese diseño:

* Dentro de macOS **no se alterna la capa 3**, porque Option ocupa ese pulgar. Los pulgares izquierdos son solo cuatro: `MO(1)`, Cmd, Option y espacio.
* Las capas 1 y 2 siguen disponibles con sus teclas de siempre, incluida la captura `KC_S_S_AMAC`.

Pendiente: las macros `KC_ARROBA`, `KC_INVERT`, `KC_SCRT4` y `KC_SCRT5` usan `AltGr`, que en macOS es Option y no produce los mismos caracteres.

---

## 🛠️ Estructura de Archivos

* `keymap.c`: Contiene la lógica de inicialización, definición de matrices de teclas, mapa de encoders y las funciones de comportamiento en `process_record_user`.
* `secrets.h`: *(No incluido en el repositorio por seguridad)* Contiene las directivas `#define SECRET...` con las cadenas de texto privadas del usuario.

