import tester.Atoms as atom

# Define the general functional group class
class FunctionalGroup():
    def __init__(self, name, stem):
        self.__name = name
        self.__stem = stem
    
    def addFunctionalGroup(carbon):
        return
    
    def getStem(self):
        return self.__stem
    
    def getName(self):
        return self.__name
    
    def addFunctionalGroup(self, carbon):
        return

# Central functional groups:


# Define the Alkane class
class Alkane(FunctionalGroup):
    def __init__(self):
        super().__init__("alkane", "ane")
    
    # An alkane has 2 Hydrogens on its functional group (effectively does not have a functional group)
    def addFunctionalGroup(self, carbon):
        carbon.addBondedAtom(atom.Hydrogen())
        carbon.addBondedAtom(atom.Hydrogen())

# Define the Alkene class
class Alkene(FunctionalGroup):
    def __init__(self):
        super().__init__("alkene", "ene")
    
    # An alkene has a double bond and a single Hydrogen
    def addFunctionalGroup(self, carbon):
        carbon.addBondedAtom(atom.DoubleBond())
        carbon.addBondedAtom(atom.Hydrogen())
        
# Define the Alcohol class
class Alcohol(FunctionalGroup):
    def __init__(self):
        super().__init__("alcohol", "ol")

    # An alcohol has a hydroxy group and a single hydrogen
    def addFunctionalGroup(self, carbon):
        carbon.addBondedAtom(atom.HydroxyGroup())
        carbon.addBondedAtom(atom.Hydrogen())

# Define the Amine class
class Amine(FunctionalGroup):
    def __init__(self):
        super().__init__("amine", "amine")

    # An amine has a NH2 group and a single hydrogen
    def addFunctionalGroup(self, carbon):
        carbon.addBondedAtom(atom.AmideGroup())
        carbon.addBondedAtom(atom.Hydrogen())

# Define the Ketone class
class Ketone(FunctionalGroup):
    def __init__(self):
        super().__init__("ketone", "one")
    
    # A ketone has a double bonded oxygen
    def addFunctionalGroup(self, carbon):
        carbon.addBondedAtom(atom.Oxygen())
        carbon.addBondedAtom(atom.OxygenDouble())


#End functional groups:

# Define the Carboxylic Acid class
class CarboxylicAcid(FunctionalGroup):
    def __init__(self):
        super().__init__("carboxylicacid", "anoic acid")
    
    # A carboxylic acid has a hydroxy group and a double-bonded oxygen
    def addFunctionalGroup(self, carbon):
        carbon.addBondedAtom(atom.HydroxyGroup())
        carbon.addBondedAtom(atom.OxygenDouble())
        carbon.addBondedAtom(atom.Oxygen())

# Define the Aldehyde class
class Aldehyde(FunctionalGroup):
    def __init__(self):
        super().__init__("aldehyde", "anal")
    
    # An aldehyde has a hydrogen and a double-bonded oxygen
    def addFunctionalGroup(self, carbon):
        carbon.addBondedAtom(atom.Hydrogen())
        carbon.addBondedAtom(atom.OxygenDouble())
        carbon.addBondedAtom(atom.Oxygen())

# Define the Acyl Chloride class
class AcylChloride(FunctionalGroup):
    def __init__(self):
        super().__init__("acylchloride", "anoyl chloride")
    
    # An acyl chloride has a double bonded oxygen and a chlorine atom
    def addFunctionalGroup(self, carbon):
        carbon.addBondedAtom(atom.Chlorine())
        carbon.addBondedAtom(atom.OxygenDouble())
        carbon.addBondedAtom(atom.Oxygen())

# Define the Amide class
class Amide(FunctionalGroup):
    def __init__(self):
        super().__init__("amide", "anamide")
    
    # An amide has a double bonded oxygen and a NH2 group
    def addFunctionalGroup(self, carbon):
        carbon.addBondedAtom(atom.AmideGroup())
        carbon.addBondedAtom(atom.OxygenDouble())
        carbon.addBondedAtom(atom.Oxygen())

# Define the Alcohol class
class EndAlcohol(FunctionalGroup):
    def __init__(self):
        super().__init__("endalcohol", "ol")
    
    # An alcohol at the end of a molecule has a hydroxy group and two hydrogens
    def addFunctionalGroup(self, carbon):
        carbon.addBondedAtom(atom.HydroxyGroup())
        carbon.addBondedAtom(atom.Hydrogen())
        carbon.addBondedAtom(atom.Hydrogen())