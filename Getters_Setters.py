from operator import iconcat
from os import nice


class Switchgear:
    def __init__(self, nv, ni, icc) -> None:
        self.nominal_voltage = nv
        self.__nominal_current = ni
        self.shortcircuit_current = icc 
        self.factor = pow(3, 0.5)

    def S_power(self):
        return 's = {:.2f} kVA'.format((self.factor * self.nominal_voltage * self.__nominal_current) / 1000)

tab_1 = Switchgear(440, 1600, 65)

print(tab_1.S_power())

tab_1.__nominal_current = 2200

print(tab_1.S_power())
