# Define the general atom class
class Atom():
    def __init__(self):
        self.element = None

# Define a ghost class for a double bond
class DoubleBond():
    def __init__(self):
        super().__init__()
        self.element = "N/A"
        self.symbol = "N/A"

# Define the Hydrogen class
class Hydrogen(Atom):
    def __init__(self):
        super().__init__()
        self.element = "Hydrogen"
        self.symbol = "H"

# Define the Chlorine class
class Chlorine(Atom):
    def __init__(self):
        super().__init__()
        self.element = "Chlorine"
        self.symbol = "Cl"

# Define the Bromine class
class Bromine(Atom):
    def __init__(self):
        super().__init__()
        self.element = "Bromine"
        self.symbol = "Br"

# Define the hydroxy (-OH group) class  
class HydroxyGroup(Atom):
    def __init__(self):
        super().__init__()
        self.element = "Hydroxy"
        self.symbol = "OH"

# Define the amine class (NH2 group) class
class AmideGroup(Atom):
    def __init__(self):
        super().__init__()
        self.element = "Amide"
        self.symbol = "NH₂"
        
# Define the single oxygen class
class Oxygen(Atom):
    def __init__(self):
        super().__init__()
        self.element = "Oxygen"
        self.symbol = "O"

# Define the ghost class for handling an oxygen double bond
class OxygenDouble(Atom):
    def __init__(self):
        super().__init__()
        self.element = "N/A"
        self.symbol = "ODB"

# Define and implement the functions to handle bonding and access to bonded atoms on core atoms
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

# Define carbon atoms as bondable 
class Carbon(BondableAtom):
    def __init__(self):
        super().__init__()
        self.element = "Carbon"
        self.bondCount = 0
        self.maxBondCount = 4
