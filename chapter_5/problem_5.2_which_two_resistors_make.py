# Problem 5.2  Decode a drawer of resistors, build a divider
digit = {'black': 0, 'brown': 1, 'red': 2, 'orange': 3,
         'yellow': 4, 'green': 5, 'blue': 6, 'violet': 7,
         'gray': 8, 'white': 9}
drawer = [('brown', 'black', 'red'), ('red', 'red', 'red'),
          ('yellow', 'violet', 'red'), ('orange', 'orange', 'red'),
          ('blue', 'gray', 'red'), ('brown', 'gray', 'red'),
          ('orange', 'white', 'red'), ('brown', 'black', 'orange'),
          ('red', 'red', 'orange'), ('brown', 'black', 'red')]
v_in, v_target = 5.0, 3.3          # supply and logic level, V
i_max = 1.0e-3                     # allowed divider current, A

ohms = [(10 * digit[a] + digit[b]) * 10 ** digit[c]
        for a, b, c in drawer]
values = sorted(set(ohms))         # distinct values, ohm
print('Decoded:', [f'{r / 1e3:g}k' for r in ohms])
print(f'{len(values)} distinct values')

options = []
for r1 in values:                  # r1 on top, r2 to ground
    for r2 in values:
        i = v_in / (r1 + r2)
        if r1 != r2 and i <= i_max:
            v_out = v_in * r2 / (r1 + r2)
            err = abs(v_out - v_target)
            options.append((err, r1, r2, v_out, i))
options.sort()
print('  R1      R2     V_out   error    I (mA)')
for err, r1, r2, v_out, i in options[:3]:
    print(f'{r1:6d}{r2:8d}{v_out:9.3f}{err:8.3f}{i * 1e3:9.3f}')
print(f'Pairs checked: {len(options)}')
