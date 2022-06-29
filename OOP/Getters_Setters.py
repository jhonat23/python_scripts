class Switchgear:
    def __init__(self, nv, ni, icc) -> None:
        self.nominal_voltage = nv
        self.__nominal_current = ni
        self.shortcircuit_current = icc 
        self.factor = pow(3, 0.5)
    
    @property
    def get_current(self):
        return self.__nominal_current
    
    @get_current.setter
    def set_current(self, current):
        self.__nominal_current = current

    def S_power(self):
        return 's = {:.2f} kVA'.format((self.factor * self.nominal_voltage * self.__nominal_current) / 1000)

tab_1 = Switchgear(440, 1600, 65)

print(tab_1.get_current)# () is not necessary if you created de function into a property
print(tab_1.S_power())
tab_1.set_current = 2200
print(tab_1.S_power())
print(tab_1.get_current)
#print(tab_1.__nominal_current)# It's going to show an error

# print(tab_1.nominal_voltage)
# print(tab_1.S_power())
# tab_1.__nominal_current = 2200
# print(tab_1.S_power())
# print(dir(tab_1))
