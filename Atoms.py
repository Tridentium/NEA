class Atom():
    def __init__(self):
        self.element = None

class Hydrogen(Atom):
    def __init__(self):
        super().__init__()
        self.element = "Hydrogen"

class Chlorine(Atom):
    def __init__(self):
        super().__init__()
        self.element = "Chlorine"

class Bromine(Atom):
    def __init__(self):
        super().__init__()
        self.element = "Bromine"
        
class HydroxyGroup(Atom):
    def __init__(self):
        super().__init__()
        self.element = "Hydroxy"

class AmideGroup(Atom):
    def __init__(self):
        super().__init__()
        self.element = "Amide"
        
class Oxygen(Atom):
    def __init__(self):
        super().__init__()
        self.element = "Oxygen"

class BondableAtom(Atom):
    def __init__(self):
        super().__init__()
        self.bonds = []
        self.bondCount = None
        self.maxBondCount = None
    
    def addBondedAtom(self, atom):
        if self.bondCount < self.maxBondCount:
            self.bonds.append(atom)
            self.bondCount += 1
    
    def returnAtomState(self):
        output = ""
        output += self.element
        for i in self.bonds:
            output += "(" + i.element + ")"
        return output

    
class Carbon(BondableAtom):
    def __init__(self):
        super().__init__()
        self.element = "Carbon"
        self.bondCount = 0
        self.maxBondCount = 4
