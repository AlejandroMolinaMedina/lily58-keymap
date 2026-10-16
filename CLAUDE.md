# lily58-keymap

## Antes de commitear un cambio de layout

Un cambio en `alejandromolinamedina/keymap.c` — capas, teclas, macros de
`process_record_user`, `encoder_map` — o en `config.h` / `rules.mk` que altere el
mapa obliga a revisar `alejandromolinamedina/README.md` **antes** del commit:

1. Compara capa por capa el keymap real contra el README: la descripcion de cada
   capa, su diagrama ASCII y las secciones que la mencionen (lista de macros,
   caracteristicas, teclas de pulgar).
2. Si hay desfase, actualiza el README. Si no lo hay, no lo toques.
3. El README actualizado se commitea: en el **mismo commit** que el keymap cuando
   ese cambio todavia no esta commiteado, o en un **commit propio de docs** cuando
   el cambio del layout ya quedo en un commit anterior.

No se sube un cambio de layout con el README desactualizado.

El README de la raiz (`README.md`) es otra cosa: instalacion, flasheo y notas de
hardware. Solo se toca si el cambio afecta como se compila o se flashea, no por
mover teclas.
