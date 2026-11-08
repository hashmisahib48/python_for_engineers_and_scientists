# try, except, else and finally on four pressure readings (kPa)
def check_pressure(p):
    """Return the absolute pressure p (kPa), or raise ValueError."""
    if p < 0:
        raise ValueError(f'negative absolute pressure {p} kPa')
    return p


readings = ['101.3', 'OVERRANGE', '-4.0', '100.4']
good = []
for text in readings:
    try:
        p = check_pressure(float(text))
    except ValueError as err:
        print(f'  rejected: {err}')
    else:
        good.append(p)                  # runs only without an error
    finally:
        print(f'checked {text}')        # runs in every case
print(f'Accepted {len(good)} of {len(readings)}: {good}')
