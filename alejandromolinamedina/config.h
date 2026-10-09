#pragma once

// ===========================================================================
// Configuracion del hardware de este Lily58
// ---------------------------------------------------------------------------
// Controladores: dos ATmega32U4 en formato Pro Micro (clones que se anuncian
// como "Arduino Micro", 2341:8037 corriendo y 2341:0037 en el bootloader
// Caterina). El procesador nativo de la placa, asi que NO se usa CONVERT_TO.
//
// El cable USB va en la mitad IZQUIERDA. Ese es el comportamiento por omision
// de QMK: la mitad con USB es la maestra y ocupa las filas 0-4. Por eso aqui
// no se define MASTER_RIGHT. Si algun dia pasas el cable a la derecha,
// descomenta la linea de abajo y vuelve a flashear LAS DOS mitades.
//
// #define MASTER_RIGHT
//
// Sin MATRIX_MASKED: las dos mitades dan sus 29 posiciones completas, con las
// 6 columnas buenas. (Hubo una epoca con columnas muertas, pero era dano del
// controlador RP2040 que se uso antes, no de la PCB.)
// ===========================================================================
