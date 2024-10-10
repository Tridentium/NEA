import random
import Atoms as atom
import FunctionalGroups as fg

IUPACLengthStems = ["meth", "eth", "prop", "but", "pent", "hex", "hept", "oct", "non", "dec"]


class Molecule():
    def __init__(self, maxLength):
        self.atoms = []
        self.maxLength = maxLength
        self.functionalGroupName = ""
        self.length = 0
        self.stem = None
        self.funcEndBool = False
        self.functionGroupPos = 0
        self.addedGroups = {}
    
    def generate(self):
        self.length = random.randint(3, self.maxLength)
        
        funcEndChance = random.randint(1, 1)
        self.funcEndBool = False
        
        
        if funcEndChance >= 3:
            self.functionGroupPos = random.randint(0, 1)
            if self.functionGroupPos == 1:
                self.functionGroupPos = self.length - 1
            self.funcEndBool = True
        else:
            if self.length > 2:
                self.functionGroupPos = random.randint(1, self.length-2)
            else:
                self.functionGroupPos = random.randint(0, 1)
                if self.functionGroupPos == 1:
                    self.functionGroupPos = self.length - 1
                self.funcEndBool = True
        
        for i in range(self.length):
            if i != self.functionGroupPos:
                carbon = atom.Carbon()
                carbon.addBondedAtom(self.decideAtom(i))
                carbon.addBondedAtom(self.decideAtom(i))
            else:
                carbon = atom.Carbon()
                self.functionalGroupName = self.addFunctionalGroup(carbon, self.funcEndBool)
            self.atoms.append(carbon)
        
        if self.functionGroupPos != 0:
            self.atoms[0].addBondedAtom(atom.Hydrogen())
        if self.functionGroupPos != self.length - 1 or self.length == 1:
            self.atoms[self.length-1].addBondedAtom(atom.Hydrogen())
            
    def decideAtom(self, index):
        diceRoll = random.randint(0, 100)
        if diceRoll <= 100:
            hydrogen = atom.Hydrogen()  
            return hydrogen
        
        elif diceRoll <= 95:
            if not str(index) in self.addedGroups:
                self.addedGroups[str(index)] = ["Chloro"]
            else:
                self.addedGroups[str(index)].append("Chloro")
            chlorine = atom.Chlorine()
            return chlorine
        
        elif diceRoll <= 100:
            if not str(index) in self.addedGroups:
                self.addedGroups[str(index)] = ["Bromo"]
            else:
                self.addedGroups[str(index)].append("Bromo")
            bromine = atom.Bromine()
            return bromine
    
    
    def addFunctionalGroup(self, carbon, funcEndBool):
        if funcEndBool:
            diceRoll = random.randint(0, 100)
            if diceRoll <= 20:
                functionalGroup = fg.EndAlcohol()
                functionalGroup.addFunctionalGroup(carbon)
                self.stem = functionalGroup.stem
                return functionalGroup.name
            elif diceRoll <= 40:
                functionalGroup = fg.Aldehyde()
                functionalGroup.addFunctionalGroup(carbon)
                self.stem = functionalGroup.stem
                return functionalGroup.name
            elif diceRoll <= 60:
                functionalGroup = fg.AcylChloride()
                functionalGroup.addFunctionalGroup(carbon)
                self.stem = functionalGroup.stem
                return functionalGroup.name
            elif diceRoll <= 80:
                functionalGroup = fg.Amide()
                functionalGroup.addFunctionalGroup(carbon)
                self.stem = functionalGroup.stem
                return functionalGroup.name
            elif diceRoll <= 100:
                functionalGroup = fg.CarboxylicAcid()
                functionalGroup.addFunctionalGroup(carbon)
                self.stem = functionalGroup.stem
                return functionalGroup.name
        else:
            diceRoll = random.randint(0, 100)
            if diceRoll <= 100:
                functionalGroup = fg.Alkane()
                functionalGroup.addFunctionalGroup(carbon)
                self.stem = functionalGroup.stem
                return functionalGroup.name
            elif diceRoll <= 50:
                functionalGroup = fg.Amine()
                functionalGroup.addFunctionalGroup(carbon)
                self.stem = functionalGroup.stem
                return functionalGroup.name
            elif diceRoll <= 75:
                functionalGroup = fg.Ketone()
                functionalGroup.addFunctionalGroup(carbon)
                self.stem = functionalGroup.stem
                return functionalGroup.name
            elif diceRoll <= 100:
                functionalGroup = fg.Alcohol()
                functionalGroup.addFunctionalGroup(carbon)
                self.stem = functionalGroup.stem
                return functionalGroup.name


    def outputMolecule(self):
        print(self.functionalGroupName)
        for i in self.atoms:
            print(i.returnAtomState())
            
        name = ""
        addedGroupsDict = {
                            "Chloro": [],
                            "Bromo": []
                            }
        for x, y in self.addedGroups.items():
            for i in y:
                addedGroupsDict[i].append(str(int(x)+1))
        
        for x, y in addedGroupsDict.items():
            if len(y) >= 1:
                if len(y) == 1:
                    name += y[0]   
                else:
                    for i in y:
                        name += i
                        name += ","
                    name = name[:-1]    
                name += "-" + x + "-"
        if len(name) > 0:
            name = name[:-1]
        if self.funcEndBool or self.functionalGroupName == "Alkane":
            name += IUPACLengthStems[self.length - 1] + self.stem
        else:
            name += IUPACLengthStems[self.length - 1] + "an-" + str(self.functionGroupPos + 1) + "-" + self.stem
        return name
    
# newMolecule = Molecule(10)
# newMolecule.generate()
# newMolecule.outputMolecule()