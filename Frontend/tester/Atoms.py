class Atom():
    def __init__(self):
        self.element = None

class Hydrogen(Atom):
    def __init__(self):
        super().__init__()
        self.element = "Hydrogen"
        self.symbol = "H"

class Chlorine(Atom):
    def __init__(self):
        super().__init__()
        self.element = "Chlorine"
        self.symbol = "Cl"

class Bromine(Atom):
    def __init__(self):
        super().__init__()
        self.element = "Bromine"
        self.symbol = "Br"
        
class HydroxyGroup(Atom):
    def __init__(self):
        super().__init__()
        self.element = "Hydroxy"
        self.symbol = "OH"

class AmideGroup(Atom):
    def __init__(self):
        super().__init__()
        self.element = "Amide"
        self.symbol = "NH2"
        
class Oxygen(Atom):
    def __init__(self):
        super().__init__()
        self.element = "Oxygen"
        self.symbol = "O"

class BondableAtom(Atom):
    
    # Define variables
    def __init__(self):
        super().__init__()
        self.bonds = []
        self.bondCount = None
        self.maxBondCount = None
    
    # Add an atom object to the bonds list
    def addBondedAtom(self, atom):
        if self.bondCount < self.maxBondCount:
            self.bonds.append(atom)
            self.bondCount += 1
    
    # Output the carbon and its bonds for debugging
    def returnAtomState(self):
        output = ""
        output += self.element
        for i in self.bonds:
            output += "(" + i.element + ")"
        return output
    
    # Return the atoms in the bonds list
    def getAtoms(self):
        return self.bonds

    
class Carbon(BondableAtom):
    def __init__(self):
        super().__init__()
        self.element = "Carbon"
        self.bondCount = 0
        self.maxBondCount = 4
