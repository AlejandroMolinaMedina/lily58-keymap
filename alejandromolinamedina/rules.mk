ENCODER_MAP_ENABLE = yes

# --- Hardware que esta placa NO tiene ---
# Sin estas tres lineas, QMK compila el codigo del OLED y de los LEDs. El del
# OLED intenta hablar por i2c con una pantalla ausente y acaba bloqueando el
# escaneo de la matriz: el teclado deja de responder. Ademas el firmware se va
# al 97% de los 28672 bytes del ATmega32U4, contra el 64% que ocupa asi.
OLED_ENABLE = no
RGB_MATRIX_ENABLE = no
RGBLIGHT_ENABLE = no

# Bootmagic lee la matriz al arrancar y, si lee una tecla como presionada,
# manda el chip al bootloader en cada encendido.
BOOTMAGIC_ENABLE = no
