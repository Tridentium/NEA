# Define the general atom class
class Atom():
    def __init__(self, element, symbol):
        self.__element = element
        self.__symbol = symbol
    
    def getElement(self):
        return self.__element
    
    def getSymbol(self):
        return self.__symbol

# Define a ghost class for a double bond
class DoubleBond(Atom):
    def __init__(self):
        super().__init__("N/A", "N/A")

# Define the Hydrogen class
class Hydrogen(Atom):
    def __init__(self):
        super().__init__("Hydrogen", "H")

# Define the Chlorine class
class Chlorine(Atom):
    def __init__(self):
        super().__init__("Chlorine", "Cl")

# Define the Bromine class
class Bromine(Atom):
    def __init__(self):
        super().__init__("Bromine", "Br")

# Define the hydroxy (-OH group) class  
class HydroxyGroup(Atom):
    def __init__(self):
        super().__init__("Hydroxy", "OH")

# Define the amine class (NH2 group) class
class AmideGroup(Atom):
    def __init__(self):
        super().__init__("Amide", "NH2")
        
# Define the single oxygen class
class Oxygen(Atom):
    def __init__(self):
        super().__init__("Oxygen", "O")

# Define the ghost class for handling an oxygen double bond
class OxygenDouble(Atom):
    def __init__(self):
        super().__init__("N/A", "ODB")

# Define and implement the functions to handle bonding and access to bonded atoms on core atoms
class BondableAtom(Atom):
    
    # Define variables
    def __init__(self, element, symbol, bondCount, maxBondCount):
        super().__init__(element, symbol)
        self.__bonds = []
        self.__bondCount = bondCount
        self.__maxBondCount = maxBondCount
    
    # Add an atom object to the bonds list
    def addBondedAtom(self, atom):
        if self.__bondCount < self.__maxBondCount:
            self.__bonds.append(atom)
            self.__bondCount += 1
    
    # Output the carbon and its bonds for debugging
    def returnAtomState(self):
        output = ""
        output += self.__element
        for i in self.__bonds:
            output += "(" + i.getElement() + ")"
        return output
    
    # Return the atoms in the bonds list
    def getAtoms(self):
        return self.__bonds

# Define carbon atoms as bondable
class Carbon(BondableAtom):
    def __init__(self):
        super().__init__("Carbon", "C", 0, 4)
