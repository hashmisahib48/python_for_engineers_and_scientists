# Listing 2.2  Current in a resistor, values from the keyboard
text = input('Supply voltage in volts: ')
print('You typed', text, 'which is of type', type(text))

voltage = float(text)                        # V
resistance = float(input('Resistance in ohms: '))   # ohm

current = voltage / resistance               # A
print('Current (A):', current)
