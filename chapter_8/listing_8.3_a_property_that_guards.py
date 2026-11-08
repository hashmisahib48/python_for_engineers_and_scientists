# Listing 8.3  A property that guards absolute zero
class Temperature:
    """A temperature stored in kelvins, readable in degC."""

    def __init__(self, kelvin):
        self.kelvin = kelvin              # K

    @property
    def celsius(self):
        """The same temperature in degC (read like an attribute)."""
        return self.kelvin - 273.15

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError(f'{value} degC is below absolute zero')
        self.kelvin = value + 273.15


lox = Temperature(90.19)          # liquid oxygen at 1 atm, K
print(f'LOX: {lox.kelvin:.2f} K = {lox.celsius:.2f} degC')
lox.celsius = -150.0              # set through the property
print(f'Warmed: {lox.kelvin:.2f} K')
try:
    lox.celsius = -300.0
except ValueError as err:
    print('Rejected:', err)
