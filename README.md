# Keymap personalizado para Lily58 Pro (QMK)

Este repositorio contiene el keymap personalizado llamado `alejandromolinamedina` para el teclado **Lily58 Pro** usando el firmware **QMK**.

El repositorio es autocontenido: trae su `keymap.c`, su `config.h` y su `rules.mk`, así que al enlazarlo en QMK compila el firmware correcto sin configuración extra.

---

## 📦 Requisitos

- Tener instalado QMK CLI — [documentación oficial](https://docs.qmk.fm/newbs_getting_started).
- Haber clonado el firmware oficial de QMK en tu sistema (por ejemplo en `~/qmk_firmware`).

---

## 🛠 Instrucciones

### 1. Clona este repositorio

```bash
git clone https://github.com/AlejandroMolinaMedina/lily58-keymap.git
```

### 2. Crea tu `secrets.h`

**Este paso es obligatorio.** `secrets.h` está en `.gitignore` a propósito, así que el clon no lo trae y sin él la compilación falla con `error: 'SECRET' undeclared`.

```bash
cd lily58-keymap
cp alejandromolinamedina/secrets.h.example alejandromolinamedina/secrets.h
```

Luego edita `secrets.h` y pon tus valores. Los ocho `#define` son obligatorios; el archivo de ejemplo explica qué es cada uno.

### 3. Elimina el keymap original en QMK (si existe)

```bash
rm -rf ~/qmk_firmware/keyboards/mechboards/lily58/pro/keymaps/alejandromolinamedina
```

### 4. Crea un enlace simbólico hacia este repositorio

```bash
ln -s ~/lily58-keymap/alejandromolinamedina ~/qmk_firmware/keyboards/mechboards/lily58/pro/keymaps/alejandromolinamedina
```

> Ajusta las rutas si QMK o este repositorio están en otras ubicaciones.

### 5. (Opcional) Fija el teclado y el keymap por omisión

```bash
qmk config user.keyboard=mechboards/lily58/pro
qmk config user.keymap=alejandromolinamedina
```

Con eso basta escribir `qmk flash` sin argumentos. Los comandos de `qmk` funcionan desde cualquier carpeta.

---

## 🚀 Compilar y flashear

```bash
qmk flash -kb mechboards/lily58/pro -km alejandromolinamedina
```

Cuando aparezca `Waiting for USB serial port - reset your controller now`, toca el botón de reset del controlador y **no muevas el cable por unos 10 segundos**. El bootloader Caterina solo se queda disponible ~8 segundos y la escritura necesita ~5.

### Qué mitad hay que flashear

El cable USB va en la **mitad derecha**, que es la maestra (`MASTER_RIGHT` en `config.h`).

- **Cambios de keymap** (teclas, capas, macros): basta flashear la **derecha**. En un split de QMK la mitad esclava solo manda el estado crudo de su matriz; toda la interpretación la hace la maestra.
- **Cambios de `config.h` o `rules.mk`**: hay que flashear **las dos mitades**, una a la vez, moviendo el cable USB.

---

## 🧠 Notas de hardware

- Controladores: dos **ATmega32U4** en formato Pro Micro (clones que se anuncian como `Arduino Micro`: `2341:8037` corriendo y `2341:0037` en el bootloader).
- Bootloader **Caterina**, se flashea con `avrdude` por el puerto serie. **No genera `.uf2`** ni usa modo BOOTSEL.
- **No se usa `CONVERT_TO`**: el ATmega32U4 es el procesador nativo de la placa.
- Esta placa **no tiene OLED ni LEDs RGB**. Por eso `rules.mk` los apaga; es obligatorio, no una preferencia. Con el OLED activado el firmware intenta hablar por i2c con una pantalla ausente y acaba bloqueando el escaneo de la matriz.
- El firmware ocupa **18420 de 28672 bytes (64%)**. Con OLED y RGB activados se va al 97%, sin margen para agregar nada.

### Si el teclado deja de responder

1. ¿Activaste la capa 3 sin querer con `TG(3)`? Está casi vacía, así que el teclado parece muerto. Presiona esa misma tecla otra vez, o desconecta y vuelve a conectar.
2. ¿Compilaste con `OLED_ENABLE` activado? Revisa que `rules.mk` sea el de este repositorio.
3. Si `avrdude` se queda girando al 100% de CPU, el puerto desapareció a media escritura. Mátalo con `pkill -x avrdude` (con `-x`, nunca con `-f`) y repite.

---

## 🗺️ Mapa de capas

El detalle de cada capa, con diagramas, está en [`alejandromolinamedina/README.md`](alejandromolinamedina/README.md).

## 🌿 Ramas

- `master` — Windows y Linux (distribución en español).
- `feature/mac-layout` — variante para macOS: Cmd donde está Ctrl, captura con `Cmd+Shift+4`, arroba con `Option+2`.
