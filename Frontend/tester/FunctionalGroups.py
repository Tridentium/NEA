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
        self.name = "alkane"
        self.stem = "ane"
    
    def addFunctionalGroup(self, carbon):
        carbon.addBondedAtom(atom.Hydrogen())
        carbon.addBondedAtom(atom.Hydrogen())

class Alkene(FunctionalGroup):
    def __init__(self):
        super().__init__()
        self.name = "alkene"
        self.stem = "ene"
    
    def addFunctionalGroup(self, carbon):
        carbon.addBondedAtom(atom.DoubleBond())
        carbon.addBondedAtom(atom.Hydrogen())
        


class Alcohol(FunctionalGroup):
    def __init__(self):
        super().__init__()
        self.name = "alcohol"
        self.stem = "ol"
    
    def addFunctionalGroup(self, carbon):
        carbon.addBondedAtom(atom.HydroxyGroup())
        carbon.addBondedAtom(atom.Hydrogen())

class Amine(FunctionalGroup):
    def __init__(self):
        super().__init__()
        self.name = "amine"
        self.stem = "amine"
    
    def addFunctionalGroup(self, carbon):
        carbon.addBondedAtom(atom.AmideGroup())
        carbon.addBondedAtom(atom.Hydrogen())

class Ketone(FunctionalGroup):
    def __init__(self):
        super().__init__()
        self.name = "ketone"
        self.stem = "one"
    
    def addFunctionalGroup(self, carbon):
        carbon.addBondedAtom(atom.Oxygen())
        carbon.addBondedAtom(atom.OxygenDouble())


#End only functional groups
class CarboxylicAcid(FunctionalGroup):
    def __init__(self):
        super().__init__()
        self.name = "carboxylicacid"
        self.stem = "anoic acid"
        self.element = "Hydroxy"
    
    def addFunctionalGroup(self, carbon):
        carbon.addBondedAtom(atom.HydroxyGroup())
        carbon.addBondedAtom(atom.OxygenDouble())
        carbon.addBondedAtom(atom.Oxygen())

class Aldehyde(FunctionalGroup):
    def __init__(self):
        super().__init__()
        self.name = "aldehyde"
        self.stem = "anal"
    
    def addFunctionalGroup(self, carbon):
        carbon.addBondedAtom(atom.Hydrogen())
        carbon.addBondedAtom(atom.OxygenDouble())
        carbon.addBondedAtom(atom.Oxygen())


class AcylChloride(FunctionalGroup):
    def __init__(self):
        super().__init__()
        self.name = "acylchloride"
        self.stem = "anoyl chloride"
    
    def addFunctionalGroup(self, carbon):
        carbon.addBondedAtom(atom.Chlorine())
        carbon.addBondedAtom(atom.OxygenDouble())
        carbon.addBondedAtom(atom.Oxygen())
        
class Amide(FunctionalGroup):
    def __init__(self):
        super().__init__()
        self.name = "amide"
        self.stem = "anamide"
    
    def addFunctionalGroup(self, carbon):
        carbon.addBondedAtom(atom.AmideGroup())
        carbon.addBondedAtom(atom.OxygenDouble())
        carbon.addBondedAtom(atom.Oxygen())

class EndAlcohol(FunctionalGroup):
    def __init__(self):
        super().__init__()
        self.name = "endalcohol"
        self.stem = "ol"
    
    def addFunctionalGroup(self, carbon):
        carbon.addBondedAtom(atom.HydroxyGroup())
        carbon.addBondedAtom(atom.Hydrogen())
        carbon.addBondedAtom(atom.Hydrogen())