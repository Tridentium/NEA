import random
import Atoms as atom
import FunctionalGroups as fg


# List of IUPAC main prefixes
IUPACLengthStems = ["meth", "eth", "prop", "but", "pent", "hex", "hept", "oct", "non", "dec"]


class Molecule():
    
    # Define Variables for molecule
    def __init__(self, maxLength):
        self.atoms = []
        self.maxLength = maxLength
        self.functionalGroupName = ""
        self.length = 0
        self.stem = None
        self.funcEndBool = False
        self.functionGroupPos = 0
        self.addedGroups = {}
    
    # Generate an instance of a molecule
    def generate(self):
        
        # Define the number of carbons in the molecule
        self.length = random.randint(3, self.maxLength)
        
        # Determine whether the functional group will be at the end of the molecule
        funcEndChance = random.randint(1, 1)
        self.funcEndBool = False
        
        
        if funcEndChance >= 3:
            
            # Choose the location of the end functional group
            self.functionGroupPos = random.randint(0, 1)
            if self.functionGroupPos == 1:
                self.functionGroupPos = self.length - 1
            self.funcEndBool = True
        else:
            
            # Choose the location of the central functional group
            if self.length > 2:
                self.functionGroupPos = random.randint(1, self.length-2)
            else:
                self.functionGroupPos = random.randint(0, 1)
                if self.functionGroupPos == 1:
                    self.functionGroupPos = self.length - 1
                self.funcEndBool = True
        
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
        if diceRoll <= 90:
            hydrogen = atom.Hydrogen()  
            return hydrogen
        
        # 5% of the time it'll be a Chlorine
        elif diceRoll <= 95:
            
            # Adding value to naming algorithm
            if not str(index) in self.addedGroups:
                self.addedGroups[str(index)] = ["Chloro"]
            else:
                self.addedGroups[str(index)].append("Chloro")
            
            # Creating Chlorine atom
            chlorine = atom.Chlorine()
            return chlorine
        
        # 5% of the time it'll be a Bromine
        elif diceRoll <= 100:
            
            # Adding value to naming algorithm
            if not str(index) in self.addedGroups:
                self.addedGroups[str(index)] = ["Bromo"]
            else:
                self.addedGroups[str(index)].append("Bromo")
            
            # Creating Bromine atom
            bromine = atom.Bromine()
            return bromine
    
    
    def addFunctionalGroup(self, carbon, funcEndBool):
        
        # Check whether the functional group will be at the end of the atom
        if funcEndBool:
            
            # Generates random number to decide which functional group will be added to the molecule
            diceRoll = random.randint(0, 100)
            
            # 20% chance that an Alcohol will be the main functional group of the molecule
            if diceRoll <= 20:
                
                # Instantiates functional group and updates molecule variables
                functionalGroup = fg.EndAlcohol()
                functionalGroup.addFunctionalGroup(carbon)
                self.stem = functionalGroup.stem
                return functionalGroup.name
            
            # 20% chance that an Alcohol will be the main functional group of the molecule
            elif diceRoll <= 40:
                
                # Instantiates functional group and updates molecule variables
                functionalGroup = fg.EndAlcohol()
                functionalGroup.addFunctionalGroup(carbon)
                self.stem = functionalGroup.stem
                return functionalGroup.name
            
            # 20% chance that an Alcohol will be the main functional group of the molecule
            elif diceRoll <= 60:
                
                # Instantiates functional group and updates molecule variables
                functionalGroup = fg.EndAlcohol()
                functionalGroup.addFunctionalGroup(carbon)
                self.stem = functionalGroup.stem
                return functionalGroup.name
            
            # 20% chance that an Alcohol will be the main functional group of the molecule
            elif diceRoll <= 80:
                
                # Instantiates functional group and updates molecule variables
                functionalGroup = fg.Amide()
                functionalGroup.addFunctionalGroup(carbon)
                self.stem = functionalGroup.stem
                return functionalGroup.name
            
            # 20% chance that an Alcohol will be the main functional group of the molecule
            elif diceRoll <= 100:
                
                # Instantiates functional group and updates molecule variables
                functionalGroup = fg.EndAlcohol()
                functionalGroup.addFunctionalGroup(carbon)
                self.stem = functionalGroup.stem
                return functionalGroup.name
        else:
            
            # Generates random number to decide which functional group will be added to the molecule
            diceRoll = random.randint(0, 100)
            
            # 25% chance that the molecule will be an Alkane
            if diceRoll <= 25:
                
                # Instantiates functional group and updates molecule variables
                functionalGroup = fg.Alkane()
                functionalGroup.addFunctionalGroup(carbon)
                self.stem = functionalGroup.stem
                return functionalGroup.name
            
            # 25% chance that the molecule will be an Amine
            elif diceRoll <= 50:
                
                # Instantiates functional group and updates molecule variables
                functionalGroup = fg.Amine()
                functionalGroup.addFunctionalGroup(carbon)
                self.stem = functionalGroup.stem
                return functionalGroup.name
            
            # 25% chance that the molecule will be an Alcohol
            elif diceRoll <= 75:
                
                # Instantiates functional group and updates molecule variables
                functionalGroup = fg.Alcohol()
                functionalGroup.addFunctionalGroup(carbon)
                self.stem = functionalGroup.stem
                return functionalGroup.name
            
            # 25% chance that the molecule will be an Alcohol
            elif diceRoll <= 100:
                
                # Instantiates functional group and updates molecule variables
                functionalGroup = fg.Alcohol()
                functionalGroup.addFunctionalGroup(carbon)
                self.stem = functionalGroup.stem
                return functionalGroup.name


    def outputMolecule(self):
        
        # Remove in final product
        print(self.functionalGroupName)
        
        # Remove in final product
        for i in self.atoms:
            print(i.returnAtomState())
         
         
        # Create name variable    
        name = ""
        
        # Define dictionary for adding prefix groups
        addedGroupsDict = {
                            "Chloro": [],
                            "Bromo": []
                            }
        
        # Loop through added prefix groups on each carbon add them and their positions to the dictionary 
        for x, y in self.addedGroups.items():
            for i in y:
                addedGroupsDict[i].append(str(int(x) + 1))
        
        # Loop through the items in addedGroupsDict
        for x, y in addedGroupsDict.items():
            
            # Check there are values in the dictionary
            if len(y) >= 1:
                
                # If only one value present, just add it to the name
                if len(y) == 1:
                    name += y[0]
                
                # If more than one value is present, loop through each value and concatenate them to the name seperated by , and - as appropriate
                else:
                    for i in y:
                        name += i
                        name += ","
                    name = name[:-1]    
                name += "-" + x + "-"
        # Remove the last , or - to allow it to combine with the main stem
        if len(name) > 0:
            name = name[:-1]
        
        # No functional group name needde for an alkane
        if self.funcEndBool or self.functionalGroupName == "Alkane":
            name += IUPACLengthStems[self.length - 1] + self.stem
            
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
newMolecule = Molecule(3)
newMolecule.generate()
print(newMolecule.outputMolecule())

