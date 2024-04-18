from random import sample, shuffle
from flet import (Page, MainAxisAlignment, TextField, Slider, app, Text, Checkbox, Row, ElevatedButton,
                  RoundedRectangleBorder, MaterialState, ButtonStyle, FontWeight, ExpansionTile, TileAffinity)


def main(page: Page):
    page.title = 'Password generator'
    page.window_width = 900
    page.window_height = 500
    page.theme_mode = 'dark'
    page.window_resizable = False
    page.horizontal_alignment = MainAxisAlignment.CENTER
    symbols = []
    list_letters_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                          'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    list_letters_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                          't', 'u', 'v', 'w', 'x', 'y', 'z']
    list_symbols = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '-', '_', '=', '/']
    list_numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    pass_field = TextField(value='', disabled=False, height=50)
    pass_len = Slider(min=0, max=24, divisions=24, label="{value}", width=880, disabled=True)

    def generation_password(e):
        shuffle(symbols)
        pass_field.value = ''.join(sample(symbols, int(pass_len.value)))
        print(symbols)
        page.update()

    def add_letters_upper(e):
        if add_let_upper.value:
            symbols.extend(list_letters_upper)
        elif not add_let_upper.value:
            for item in list_letters_upper:
                if item in symbols:
                    symbols.remove(item)
                else:
                    continue
        if symbols is not None:
            pass_len.disabled = False
        page.update()

    def add_letters_lower(e):
        if add_let_lower.value:
            symbols.extend(list_letters_lower)
        elif not add_let_lower.value:
            for item in list_letters_lower:
                if item in symbols:
                    symbols.remove(item)
                else:
                    continue
        if symbols is not None:
            pass_len.disabled = False
        page.update()

    def add_symbols(e):
        if add_symb.value:
            symbols.extend(list_symbols)
        elif not add_symb.value:
            for item in list_symbols:
                if item in symbols:
                    symbols.remove(item)
                else:
                    continue
        if symbols is not None:
            pass_len.disabled = False
        page.update()

    def add_numbers(e):
        if add_nums.value:
            symbols.extend(list_numbers)
        elif not add_nums.value:
            for item in list_numbers:
                if item in symbols:
                    symbols.remove(item)
                else:
                    continue
        if symbols is not None:
            pass_len.disabled = False
        page.update()

    page.add(
        Row(
            [
                Text(value='Password Generator', size=20, weight=FontWeight.W_700),
            ], alignment=MainAxisAlignment.CENTER
        ),
        Row(
            [
                pass_field,
                ElevatedButton(text='Generate', height=50, style=ButtonStyle(
                    shape={

                        MaterialState.DEFAULT: RoundedRectangleBorder(radius=5),
                    }
                ), on_click=generation_password
                ),

            ]
        )
    )

    add_let_upper = Checkbox(
        label='Use capital letters '
              '(A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z)',
        on_change=add_letters_upper)
    add_let_lower = Checkbox(
        label='Use lowercase letters '
              '(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z)',
        on_change=add_letters_lower)
    add_symb = Checkbox(label='Use symbols (!, @, #, $, %, &, *, (, ), -, _, =, /)', on_change=add_symbols)
    add_nums = Checkbox(label='Use numbers (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)', on_change=add_numbers)

    page.add(
        ExpansionTile(
            title=Text('Settings'),
            affinity=TileAffinity.LEADING,
            initially_expanded=True,
            shape=None,
            controls=[
                add_let_upper,
                add_let_lower,
                add_symb,
                add_nums,
                Text(value='Password length'),
                pass_len
            ],

        ),
    )


app(target=main)
