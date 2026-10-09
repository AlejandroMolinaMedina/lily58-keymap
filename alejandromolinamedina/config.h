#pragma once

// ===========================================================================
// Configuracion del hardware de este Lily58
// ---------------------------------------------------------------------------
// Controladores: dos ATmega32U4 en formato Pro Micro (clones que se anuncian
// como "Arduino Micro", 2341:8037 corriendo y 2341:0037 en el bootloader
// Caterina). El procesador nativo de la placa, asi que NO se usa CONVERT_TO.
//
// El cable USB va en la mitad DERECHA. Con MASTER_RIGHT, la mitad del USB es
// la maestra y ocupa las filas 5-9, que es donde el keymap tiene las teclas de
// la mano derecha. Sin esta linea QMK asume que la mitad del USB es la
// izquierda y salen las teclas de la mitad equivocada.
//
// Si algun dia pasas el cable a la izquierda, comenta la linea y vuelve a
// flashear LAS DOS mitades: es un cambio de config.h, no de keymap.
#define MASTER_RIGHT
// Sin MATRIX_MASKED: las dos mitades dan sus 29 posiciones completas, con las
// 6 columnas buenas. (Hubo una epoca con columnas muertas, pero era dano del
// controlador RP2040 que se uso antes, no de la PCB.)
// ===========================================================================
