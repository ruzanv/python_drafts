from sweetest import sweetest_icecream
from ice_cream_class import IceCream

ice1 = IceCream('Plain', 13)
ice2 = IceCream('Plain', 20)
ice3 = IceCream('Vanilla', 12)

if __name__ == '__main__':
    print(sweetest_icecream([ice1, ice2, ice3]))
    print(sweetest_icecream([ice1, ice3]))
    print(sweetest_icecream([ice1]))