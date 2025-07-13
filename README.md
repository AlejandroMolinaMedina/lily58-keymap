# Keymap personalizado para Lily58 Pro (QMK)

Este repositorio contiene el keymap personalizado llamado `alejandromolinamedina` para el teclado **Lily58 Pro** usando el firmware **QMK**.

---

## 📦 Requisitos

- Tener instalado QMK CLI
- Haber clonado el firmware oficial de QMK en tu sistema (por ejemplo en `~/qmk_firmware`)

---

## 🛠 Instrucciones

### 1. Clona este repositorio

```bash
git clone https://github.com/TU_USUARIO/lily58-keymap.git
```

### 2. Elimina el keymap original en QMK (si existe)

```bash
rm -rf ~/qmk_firmware/keyboards/mechboards/lily58/pro/keymaps/alejandromolinamedina
```

### 3. Crea un enlace simbólico hacia este repositorio

```bash
ln -s ~/lily58-keymap/alejandromolinamedina ~/qmk_firmware/keyboards/mechboards/lily58/pro/keymaps/alejandromolinamedina
```

> Asegúrate de ajustar las rutas si QMK o este repositorio están en otras ubicaciones en tu sistema.

---

## 🚀 Compilar y flashear

Una vez hecho el enlace simbólico, puedes compilar y flashear con:

```bash
qmk flash -kb mechboards/lily58/pro -km alejandromolinamedina
```

---

## 🧠 Notas

- Este keymap está diseñado para usarse con el controlador **Liatris (RP2040)**.
- El bootloader usado es `rp2040`, y el archivo `.uf2` se puede copiar directamente al dispositivo en modo BOOTSEL.
