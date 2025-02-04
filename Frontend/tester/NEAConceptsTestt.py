import random
import tester.Atoms as atom
import tester.FunctionalGroups as fg


# List of IUPAC main prefixes
IUPACLengthStems = ["meth", "eth", "prop", "but", "pent", "hex", "hept", "oct", "non", "dec"]
IUPACRepetitionPrefixes = ["", "", "di", "tri", "tetra", "penta", "hexa", "hepta", "octa", "nona", "deca"]

class Molecule():
    
    # Define Variables for molecule
    def __init__(self, maxLength, valid_groups):
        self.atoms = []
        self.maxLength = maxLength
        self.functionalGroupName = ""
        self.length = 0
        self.stem = None
        self.funcEndBool = False
        self.functionGroupPos = 0
        self.addedGroups = {}
        self.validGroups = valid_groups
        self.centralGroups = ["alkane", "amine", "alcohol", "alkene", "ketone"]
        self.endGroups = ["alcohol", "aldehyde", "carboxylicacid", "amide", "alcohol", "acylchloride"]
    
    # Generate an instance of a molecule
    def generate(self):
        
        # Define the number of carbons in the molecule
        self.length = random.randint(1, self.maxLength)
        
        # Determine whether the functional group will be at the end of the molecule
        funcEndChance = random.randint(1, 3)
        self.funcEndBool = False
        
        if funcEndChance >= 3:
            self.funcEndBool = True
        
        # Check whether only end or central groups selected
        if self.funcEndBool:
            
            funcEndBoolNotValid = True
            for i in self.validGroups:
                print(i)
                if i in self.endGroups:
                    funcEndBoolNotValid = False
            
            if funcEndBoolNotValid:
                self.funcEndBool = False
        else:
            
            funcEndBoolNotValid = True
            for i in self.validGroups:
                print(i)
                if i in self.centralGroups:
                    funcEndBoolNotValid = False
            
            if funcEndBoolNotValid:
                self.funcEndBool = True
        
        if self.funcEndBool:
            self.functionGroupPos = random.randint(0, 1)
            if self.functionGroupPos == 1:
                self.functionGroupPos = self.length - 1
        else:
            if self.length > 2:
                self.functionGroupPos = random.randint(1, self.length-2)
            else:
                self.functionGroupPos = random.randint(0, 1)
            
        for i in range(self.length):
            
            if i != self.functionGroupPos:
                
                # Adds either a hydrogen or halogen to the current carbon
                carbon = atom.Carbon()
                carbon.addBondedAtom(self.decideAtom(i))
                carbon.addBondedAtom(self.decideAtom(i))
            else:
                
                # Adds the functional group combination to the current carbon
                carbon = atom.Carbon()
                self.functionalGroupName = self.addFunctionalGroup(carbon, self.funcEndBool)
            self.atoms.append(carbon)
        
        if self.functionGroupPos != 0:
            # Adds an extra hydrogen to the first carbon if it does not contain the functional group
            self.atoms[0].addBondedAtom(atom.Hydrogen())
        if self.functionGroupPos != self.length - 1 or self.length == 1:
            # Adds an extra hydrogen to the last carbon if it does not contain the functional group
            self.atoms[self.length-1].addBondedAtom(atom.Hydrogen())
            
    def decideAtom(self, index):
        
        # Generates random number to decide which atom/group is to be added to the carbon
        diceRoll = random.randint(0, 100)

        # 90% of the time it'll be a Hydrogen
        if diceRoll <= 30:
            hydrogen = atom.Hydrogen()  
            return hydrogen
        
        # 5% of the time it'll be a Chlorine
        elif diceRoll <= 90:
            
            # Adding value to naming algorithm
            if not str(index) in self.addedGroups:
                self.addedGroups[str(index)] = ["chloro"]
            else:
                self.addedGroups[str(index)].append("chloro")
            
            # Creating Chlorine atom
            chlorine = atom.Chlorine()
            return chlorine
        
        # 5% of the time it'll be a Bromine
        elif diceRoll <= 100:
            
            # Adding value to naming algorithm
            if not str(index) in self.addedGroups:
                self.addedGroups[str(index)] = ["bromo"]
            else:
                self.addedGroups[str(index)].append("bromo")
            
            # Creating Bromine atom
            bromine = atom.Bromine()
            return bromine
    
    
    def addFunctionalGroup(self, carbon, funcEndBool):
        
        # Check whether the functional group will be at the end of the atom
        if funcEndBool:
            
            # Generates random number to decide which functional group will be added to the molecule
            diceRoll = random.randint(0, 100)
            
            # 20% chance that an Alcohol will be the main functional group of the molecule
            if diceRoll <= 20 and "alcohol" in self.validGroups:
                
                # Instantiates functional group and updates molecule variables
                functionalGroup = fg.EndAlcohol()
                functionalGroup.addFunctionalGroup(carbon)
                self.stem = functionalGroup.stem
                return functionalGroup.name
            
            # 20% chance that an Alcohol will be the main functional group of the molecule
            elif diceRoll <= 40 and "aldehyde" in self.validGroups:
                
                # Instantiates functional group and updates molecule variables
                functionalGroup = fg.Aldehyde()
                functionalGroup.addFunctionalGroup(carbon)
                self.stem = functionalGroup.stem
                return functionalGroup.name
            
            # 20% chance that an Alcohol will be the main functional group of the molecule
            elif diceRoll <= 60 and "carboxylicacid" in self.validGroups:
                
                # Instantiates functional group and updates molecule variables
                functionalGroup = fg.CarboxylicAcid()
                functionalGroup.addFunctionalGroup(carbon)
                self.stem = functionalGroup.stem
                return functionalGroup.name
            
            # 20% chance that an Alcohol will be the main functional group of the molecule
            elif diceRoll <= 80 and "amide" in self.validGroups:
                
                # Instantiates functional group and updates molecule variables
                functionalGroup = fg.Amide()
                functionalGroup.addFunctionalGroup(carbon)
                self.stem = functionalGroup.stem
                return functionalGroup.name
            
            # 20% chance that an Alcohol will be the main functional group of the molecule
            elif diceRoll <= 100 and "acylchloride" in self.validGroups:
                
                # Instantiates functional group and updates molecule variables
                functionalGroup = fg.AcylChloride()
                functionalGroup.addFunctionalGroup(carbon)
                self.stem = functionalGroup.stem
                return functionalGroup.name

            else:
                return self.addFunctionalGroup(carbon, funcEndBool)
        else:
            
            # Generates random number to decide which functional group will be added to the molecule
            diceRoll = random.randint(0, 100)
            
            # 25% chance that the molecule will be an Alkane
            if diceRoll <= 20 and "alkane" in self.validGroups:
                
                # Instantiates functional group and updates molecule variables
                functionalGroup = fg.Alkane()
                functionalGroup.addFunctionalGroup(carbon)
                self.stem = functionalGroup.stem
                return functionalGroup.name
            
            # 25% chance that the molecule will be an Amine
            elif diceRoll <= 40 and "amine" in self.validGroups:
                
                # Instantiates functional group and updates molecule variables
                functionalGroup = fg.Amine()
                functionalGroup.addFunctionalGroup(carbon)
                self.stem = functionalGroup.stem
                return functionalGroup.name
            
            # 25% chance that the molecule will be an Alcohol
            elif diceRoll <= 60 and "alcohol" in self.validGroups:
                
                # Instantiates functional group and updates molecule variables
                functionalGroup = fg.Alcohol()
                functionalGroup.addFunctionalGroup(carbon)
                self.stem = functionalGroup.stem
                return functionalGroup.name
            
            # 25% chance that the molecule will be an Alcohol
            elif diceRoll <= 80 and "alkene" in self.validGroups:
                
                # Instantiates functional group and updates molecule variables
                functionalGroup = fg.Alkene()
                functionalGroup.addFunctionalGroup(carbon)
                self.stem = functionalGroup.stem
                return functionalGroup.name
                        # 25% chance that the molecule will be an Alcohol
            elif diceRoll <= 100 and "ketone" in self.validGroups:
                
                # Instantiates functional group and updates molecule variables
                functionalGroup = fg.Ketone()
                functionalGroup.addFunctionalGroup(carbon)
                self.stem = functionalGroup.stem
                return functionalGroup.name
            else:
                return self.addFunctionalGroup(carbon, funcEndBool)
            

    def outputMolecule(self):
         
        # Create name variable    
        name = ""
        
        # Define dictionary for adding prefix groups
        addedGroupsDict = {
                            "bromo": [],
                            "chloro": []
                            }
        
        # Loop through added prefix groups on each carbon add them and their positions to the dictionary 
        for x, y in self.addedGroups.items():
            for i in y:
                addedGroupsDict[i].append(str(int(x) + 1))
        
        FlipValues = False
        
        # Minimise the value of the functional group position via rotation
        if self.functionGroupPos + 1 > self.length // 2 and self.functionalGroupName != "Alkane":
            FlipValues = True
        elif (self.functionGroupPos % 2 == 1 and self.functionGroupPos//2 == self.length) or self.functionalGroupName == "Alkane":
            addedGroupsKeys = addedGroupsDict.keys()
            for i in addedGroupsKeys:
                if addedGroupsDict[i]:
                    addedGroupsDict[i].sort(reverse=True)
                    tempAddedGroupsDict = addedGroupsDict[i]
                    addedGroupsDict[i].sort()
                if self.length - int(tempAddedGroupsDict[0]) < int(addedGroupsDict["bromo"][0]):
                    FlipValues = True
                else:
                    break
        
        
        # Flip the number values if necessary
        if FlipValues:
            self.functionGroupPos = self.length - self.functionGroupPos - 1
            
            tempBromo = []
            tempChloro = []
            for i in addedGroupsDict["chloro"]:
                tempChloro.append(str(self.length - int(i) + 1))
            for i in addedGroupsDict["bromo"]:
                tempBromo.append(str(self.length - int(i) + 1))
            tempBromo.sort()
            tempChloro.sort()
            addedGroupsDict["bromo"] = tempBromo
            addedGroupsDict["chloro"] = tempChloro
        
        
        # Loop through the items in addedGroupsDict
        for x, y in addedGroupsDict.items():
            
            # Check there are values in the dictionary
            if len(y) >= 1:
                instancecount = 0
                # If only one value present, just add it to the name
                if len(y) == 1:
                    name += y[0]
                
                # If more than one value is present, loop through each value and concatenate them to the name seperated by , and - as appropriate
                else:
                    for i in y:
                        name += i
                        instancecount += 1
                        name += ","
                    name = name[:-1]    
                name += "-" + IUPACRepetitionPrefixes[instancecount] + x + "-"
                
        # Remove the last , or - to allow it to combine with the main stem
        if len(name) > 0:
            name = name[:-1]
        
        # No functional group name needed for an alkane
        if self.funcEndBool or self.functionalGroupName == "Alkane":
            name += IUPACLengthStems[self.length - 1] + self.stem
        elif self.functionalGroupName == "Alkene":
            if self.length <= 3:
                name += IUPACLengthStems[self.length - 1] + self.stem
            else:
                if FlipValues:
                    name += IUPACLengthStems[self.length - 1] + "-" + str(self.functionGroupPos) + "-" + str(self.stem)
                else:
                    name += IUPACLengthStems[self.length - 1] + "-" + str(self.functionGroupPos) + "-" + str(self.stem)
        # Add functional group name, position and main length stem to name
        else:
            name += IUPACLengthStems[self.length - 1] + "an-" + str(self.functionGroupPos + 1) + "-" + str(self.stem)
        return name
    
    # Get symbols on atoms for rendering
    def getSymbols(self, index):
        
        # Define and add symbols
        symbols = []
        for j in self.atoms[index].getAtoms():
            symbols.append(j.symbol)
        return symbols

# Debugging functions
# newMolecule = Molecule(3)
# newMolecule.generate()
# print(newMolecule.outputMolecule())

