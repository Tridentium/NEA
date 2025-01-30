import tester.Atoms as atom

class FunctionalGroup():
    def __init__(self):
        self.name = None
        self.stem = None
    
    def addFunctionalGroup(carbon):
        return

class Alkane(FunctionalGroup):
    def __init__(self):
        super().__init__()
        self.name = "Alkane"
        self.stem = "ane"
    
    def addFunctionalGroup(self, carbon):
        carbon.addBondedAtom(atom.Hydrogen())
        carbon.addBondedAtom(atom.Hydrogen())

class Alkene(FunctionalGroup):
    def __init__(self):
        super().__init__()
        self.name = "Alkene"
        self.stem = "ene"
    
    def addFunctionalGroup(self, carbon):
        carbon.addBondedAtom(atom.DoubleBond())
        carbon.addBondedAtom(atom.Hydrogen())
        


class Alcohol(FunctionalGroup):
    def __init__(self):
        super().__init__()
        self.name = "Alcohol"
        self.stem = "ol"
    
    def addFunctionalGroup(self, carbon):
        carbon.addBondedAtom(atom.HydroxyGroup())
        carbon.addBondedAtom(atom.Hydrogen())

class Amine(FunctionalGroup):
    def __init__(self):
        super().__init__()
        self.name = "Amine"
        self.stem = "amine"
    
    def addFunctionalGroup(self, carbon):
        carbon.addBondedAtom(atom.AmideGroup())
        carbon.addBondedAtom(atom.Hydrogen())

class Ketone(FunctionalGroup):
    def __init__(self):
        super().__init__()
        self.name = "Ketone"
        self.stem = "one"
    
    def addFunctionalGroup(self, carbon):
        carbon.addBondedAtom(atom.Oxygen())
        carbon.addBondedAtom(atom.OxygenDouble())


#End only functional groups
class CarboxylicAcid(FunctionalGroup):
    def __init__(self):
        super().__init__()
        self.name = "Carboxylic Acid"
        self.stem = "anoic acid"
        self.element = "Hydroxy"
    
    def addFunctionalGroup(self, carbon):
        carbon.addBondedAtom(atom.HydroxyGroup())
        carbon.addBondedAtom(atom.OxygenDouble())
        carbon.addBondedAtom(atom.Oxygen())

class Aldehyde(FunctionalGroup):
    def __init__(self):
        super().__init__()
        self.name = "Aldehyde"
        self.stem = "anal"
    
    def addFunctionalGroup(self, carbon):
        carbon.addBondedAtom(atom.Hydrogen())
        carbon.addBondedAtom(atom.OxygenDouble())
        carbon.addBondedAtom(atom.Oxygen())


class AcylChloride(FunctionalGroup):
    def __init__(self):
        super().__init__()
        self.name = "Acyl Chloride"
        self.stem = "anoyl chloride"
    
    def addFunctionalGroup(self, carbon):
        carbon.addBondedAtom(atom.Oxygen())
        carbon.addBondedAtom(atom.Chlorine())
        
class Amide(FunctionalGroup):
    def __init__(self):
        super().__init__()
        self.name = "Amide"
        self.stem = "amide"
    
    def addFunctionalGroup(self, carbon):
        carbon.addBondedAtom(atom.Oxygen())
        carbon.addBondedAtom(atom.AmideGroup())

class EndAlcohol(FunctionalGroup):
    def __init__(self):
        super().__init__()
        self.name = "Alcohol"
        self.stem = "anol"
    
    def addFunctionalGroup(self, carbon):
        carbon.addBondedAtom(atom.HydroxyGroup())
        carbon.addBondedAtom(atom.Hydrogen())
        carbon.addBondedAtom(atom.Hydrogen())