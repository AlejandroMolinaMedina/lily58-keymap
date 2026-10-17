import argparse
import pathlib
import re

CELL_W = 6
CELL_H = 2
LABEL_W = CELL_W - 1
TOTAL_KEYS = 58

KEY_GEOMETRY = [
    (0, 0, 0),
    (1, 0, 1),
    (2, 0, 2),
    (3, 0, 3),
    (4, 0, 4),
    (5, 0, 5),
    (10.5, 5, 5),
    (11.5, 5, 4),
    (12.5, 5, 3),
    (13.5, 5, 2),
    (14.5, 5, 1),
    (15.5, 5, 0),
    (0, 1, 0),
    (1, 1, 1),
    (2, 1, 2),
    (3, 1, 3),
    (4, 1, 4),
    (5, 1, 5),
    (10.5, 6, 5),
    (11.5, 6, 4),
    (12.5, 6, 3),
    (13.5, 6, 2),
    (14.5, 6, 1),
    (15.5, 6, 0),
    (0, 2, 0),
    (1, 2, 1),
    (2, 2, 2),
    (3, 2, 3),
    (4, 2, 4),
    (5, 2, 5),
    (10.5, 7, 5),
    (11.5, 7, 4),
    (12.5, 7, 3),
    (13.5, 7, 2),
    (14.5, 7, 1),
    (15.5, 7, 0),
    (0, 3, 0),
    (1, 3, 1),
    (2, 3, 2),
    (3, 3, 3),
    (4, 3, 4),
    (5, 3, 5),
    (6, 4, 5),
    (9.5, 9, 5),
    (10.5, 8, 5),
    (11.5, 8, 4),
    (12.5, 8, 3),
    (13.5, 8, 2),
    (14.5, 8, 1),
    (15.5, 8, 0),
    (2.5, 4, 1),
    (3.5, 4, 2),
    (4.5, 4, 3),
    (6, 4, 4),
    (9.5, 9, 4),
    (11, 9, 3),
    (12, 9, 2),
    (13, 9, 1),
]

LABELS = {
    "KC_ESC": "ESC", "KC_TAB": "TAB", "KC_LSFT": "LSFT", "KC_RSFT": "RSFT",
    "KC_LCTL": "LCTL", "KC_RALT": "RALT", "KC_LALT": "LALT", "KC_LGUI": "LGUI",
    "KC_SPC": "SPC", "KC_ENT": "ENT", "KC_BSPC": "BSPC", "KC_DEL": "DEL",
    "KC_MINS": "-", "KC_LBRC": "[", "KC_RBRC": "]", "KC_QUOT": "'",
    "KC_BSLS": "\\", "KC_COMM": ",", "KC_DOT": ".", "KC_SLSH": "/",
    "KC_GRV": "`", "KC_SCLN": ";", "KC_UP": "\u2191", "KC_DOWN": "\u2193",
    "KC_LEFT": "\u2190", "KC_RIGHT": "\u2192", "KC_ARROBA": "@",
    "KC_PICOL": "<", "KC_PICOR": ">", "KC_INVERT": "ALT\\",
    "KC_S_S_A": "WIN+S", "KC_S_S_AMAC": "MAC+4",
    "XXXXXXX": "", "_______": "\u00b7",
}

MAC_LAYER = 4
MAC_LABELS = {"KC_LGUI": "CMD", "KC_LALT": "OPT"}

BORDERS = {
    (1, 1, 1, 1): "\u253c", (1, 1, 1, 0): "\u2524", (1, 1, 0, 1): "\u251c",
    (1, 0, 1, 1): "\u2534", (0, 1, 1, 1): "\u252c", (1, 1, 0, 0): "\u2502",
    (0, 0, 1, 1): "\u2500", (1, 0, 1, 0): "\u2518", (1, 0, 0, 1): "\u2514",
    (0, 1, 1, 0): "\u2510", (0, 1, 0, 1): "\u250c", (1, 0, 0, 0): "\u2502",
    (0, 1, 0, 0): "\u2502", (0, 0, 1, 0): "\u2500", (0, 0, 0, 1): "\u2500",
}


def repo_root():
    return pathlib.Path(__file__).resolve().parent.parent


def keymap_path():
    return repo_root() / "alejandromolinamedina" / "keymap.c"


def readme_path():
    return repo_root() / "alejandromolinamedina" / "README.md"


def label_for(keycode, layer):
    if layer == MAC_LAYER and keycode in MAC_LABELS:
        return MAC_LABELS[keycode]
    if keycode in LABELS:
        return LABELS[keycode]
    toggle = re.fullmatch(r"(MO|TG|TO|DF|OSL)\((\d+)\)", keycode)
    if toggle:
        return toggle.group(1) + toggle.group(2)
    if keycode.startswith("KC_SCRT"):
        return "SCRT" + keycode[len("KC_SCRT"):]
    if keycode.startswith("KC_"):
        return keycode[len("KC_"):]
    return keycode


def read_layers():
    source = keymap_path().read_text()
    body = source[source.index("keymaps[][MATRIX_ROWS][MATRIX_COLS]"):]
    layers = {}
    for match in re.finditer(r"\[(\d+)\]\s*=\s*LAYOUT\((.*?)\n\)", body, re.S):
        stripped = re.sub(r"//[^\n]*", "", match.group(2))
        keycodes = [k.strip() for k in stripped.split(",") if k.strip()]
        number = int(match.group(1))
        if len(keycodes) != TOTAL_KEYS:
            raise SystemExit(
                f"la capa {number} tiene {len(keycodes)} teclas y el LAYOUT pide {TOTAL_KEYS}"
            )
        layers[number] = keycodes
    if not layers:
        raise SystemExit("no se encontro ninguna capa en keymap.c")
    return layers


def visual_row(matrix_row, matrix_col):
    half_row = matrix_row if matrix_row < 5 else matrix_row - 5
    if half_row == 4 and matrix_col == 5:
        return 3
    return half_row


def draw_layer(keycodes, layer):
    placements = []
    for (x, matrix_row, matrix_col), keycode in zip(KEY_GEOMETRY, keycodes):
        left = int(x * CELL_W + 0.5)
        top = visual_row(matrix_row, matrix_col) * CELL_H
        placements.append((left, top, keycode))

    width = max(left for left, _, _ in placements) + CELL_W + 1
    height = max(top for _, top, _ in placements) + CELL_H + 1
    horizontal = [[False] * width for _ in range(height)]
    vertical = [[False] * width for _ in range(height)]
    glyphs = [[" "] * width for _ in range(height)]

    for left, top, keycode in placements:
        for x in range(left, left + CELL_W + 1):
            horizontal[top][x] = horizontal[top + CELL_H][x] = True
        for y in range(top, top + CELL_H + 1):
            vertical[y][left] = vertical[y][left + CELL_W] = True
        text = label_for(keycode, layer).center(LABEL_W)[:LABEL_W]
        for offset, char in enumerate(text):
            glyphs[top + 1][left + 1 + offset] = char

    lines = []
    for y in range(height):
        line = []
        for x in range(width):
            if horizontal[y][x] or vertical[y][x]:
                up = y > 0 and vertical[y - 1][x]
                down = y < height - 1 and vertical[y + 1][x]
                left_side = x > 0 and horizontal[y][x - 1]
                right_side = x < width - 1 and horizontal[y][x + 1]
                line.append(BORDERS.get((up, down, left_side, right_side), "\u2500"))
            else:
                line.append(glyphs[y][x])
        lines.append("".join(line).rstrip())
    return "\n".join(line for line in lines if line.strip())


def fenced(diagram):
    return "```text\n" + diagram + "\n```"


def update_readme(layers):
    path = readme_path()
    text = path.read_text()
    missing = []
    for number in sorted(layers):
        heading = re.search(rf"^### Capa {number}\b.*$", text, re.M)
        if not heading:
            missing.append(number)
            continue
        section_end = text.find("\n### ", heading.end())
        if section_end == -1:
            section_end = len(text)
        section = text[heading.end():section_end]
        block = re.search(r"```text\n.*?\n```", section, re.S)
        diagram = fenced(draw_layer(layers[number], number))
        if block:
            section = section[:block.start()] + diagram + section[block.end():]
        else:
            section = section.rstrip("\n-\n ") + "\n\n" + diagram + "\n\n---\n"
        text = text[:heading.end()] + section + text[section_end:]
    if missing:
        print("sin seccion en el README: capas " + ", ".join(str(n) for n in missing))
    path.write_text(text)
    return path


def main():
    parser = argparse.ArgumentParser(
        description="Dibuja las capas del keymap con la forma real del Lily58."
    )
    parser.add_argument("layers", nargs="*", type=int, help="capas a dibujar (por omision, todas)")
    parser.add_argument("--write", action="store_true", help="sustituye los diagramas del README")
    args = parser.parse_args()

    layers = read_layers()
    if args.write:
        print("actualizado " + str(update_readme(layers)))
        return
    chosen = args.layers or sorted(layers)
    for number in chosen:
        if number not in layers:
            raise SystemExit(f"la capa {number} no existe en keymap.c")
        print(f"### Capa {number}")
        print(draw_layer(layers[number], number))
        print()


if __name__ == "__main__":
    main()
