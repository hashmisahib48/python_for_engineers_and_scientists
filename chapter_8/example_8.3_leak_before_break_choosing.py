# Example 8.3  Leak before break: choosing a pressure-vessel alloy
import math
from dataclasses import dataclass


@dataclass(frozen=True)
class Alloy:
    """Room-temperature properties (Callister, Table 8.1)."""
    name: str
    sigma_y: float                    # yield strength, MPa
    k_ic: float                       # toughness, MPa m^0.5

    def wall(self, p, r, sf=2.0):
        """Wall thickness (m) for hoop stress = sigma_y / sf."""
        return p * r * sf / self.sigma_y

    def k_through_crack(self, p, r, sf=2.0):
        """K_I (MPa m^0.5) for a crack as long as the wall."""
        sigma = self.sigma_y / sf                 # hoop stress, MPa
        return sigma * math.sqrt(math.pi * self.wall(p, r, sf) / 2)


P, R = 10.0, 0.50                     # pressure MPa, radius m
alloys = [Alloy('Al 2024-T3', 345.0, 44.0),
          Alloy('Al 7075-T651', 495.0, 24.0),
          Alloy('Ti-6Al-4V', 910.0, 55.0),
          Alloy('4340 at 260 C', 1640.0, 50.0),
          Alloy('4340 at 425 C', 1420.0, 87.4)]
print(alloys[2])
print('Alloy           t (mm)  K_I   K_Ic  verdict')
for a in alloys:
    k_i = a.k_through_crack(P, R)
    verdict = 'leaks first' if k_i < a.k_ic else 'BURSTS'
    print(f'{a.name:15}{a.wall(P, R) * 1e3:6.1f}{k_i:6.1f}'
          f'{a.k_ic:6.1f}  {verdict}')
