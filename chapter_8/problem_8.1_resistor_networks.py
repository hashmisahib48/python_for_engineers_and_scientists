# Problem 8.1  Series and parallel resistors with + and |
class Resistor:
    """A resistor (or a network that acts like one), ohms."""

    def __init__(self, r, label='R'):
        self.r = r
        self.label = label

    def __add__(self, other):                 # series
        return Resistor(self.r + other.r,
                        f'({self.label} + {other.label})')

    def __or__(self, other):                  # parallel
        return Resistor(self.r * other.r / (self.r + other.r),
                        f'({self.label} | {other.label})')

    def __str__(self):
        return f'{self.label} = {self.r:.2f} ohm'


r1 = Resistor(100.0, 'R1')
r2 = Resistor(220.0, 'R2')
r3 = Resistor(330.0, 'R3')
r4 = Resistor(470.0, 'R4')
net = (r1 + (r2 | r3)) | r4
print(r2 | r3)
print(net)

V = 12.0                                      # supply, V
i_total = V / net.r                           # A
i_branch = V / (r1 + (r2 | r3)).r             # A, left branch
v_par = i_branch * (r2 | r3).r                # V across R2 | R3
print(f'Supply current {i_total * 1e3:.2f} mA, '
      f'power {V * i_total:.3f} W')
print(f'Current in R3 {v_par / r3.r * 1e3:.2f} mA')
