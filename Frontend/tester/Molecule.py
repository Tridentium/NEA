import random
import tester.Atoms as atom
import tester.FunctionalGroups as fg
import math


# List of IUPAC prefixes for both length and repetition of groups
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
        
        # Define the allowed groups at the end and at the centre of a molecule for later validation
        self.centralGroups = ["alkane", "amine", "alcohol", "alkene", "ketone"]
        self.endGroups = ["endalcohol", "aldehyde", "carboxylicacid", "amide", "acylchloride"]
    
    # Generate an instance of a molecule
    def generate(self):
        
        # Initial determination of whether the functional group will be at the end of the molecule
        funcEndChance = random.randint(1, 3)
        self.funcEndBool = False
        
        if funcEndChance >= 3:
            self.funcEndBool = True

        # Ensure that funcEndBool is true if only end functional groups have been selected and vica versa
        if self.funcEndBool:
            
            funcEndBoolNotValid = True
            
            # Check whether there is an end functional group in the selection
            for i in self.validGroups:
                if i in self.endGroups:
                    funcEndBoolNotValid = False
            
            # Set funcEndBool to false if there are no end groups in the molecule
            if funcEndBoolNotValid:
                self.funcEndBool = False
        else:
            
            funcEndBoolNotValid = True
            
            # Check whether there is an central functional group in the selection
            for i in self.validGroups:
                if i in self.centralGroups:
                    funcEndBoolNotValid = False
            
            # Set funcEndBool to true if there are no central groups in the molecule
            if funcEndBoolNotValid:
                self.funcEndBool = True
        
        # Validation to catch an invalid combination of max length and select groups (string presented as an error message)
        
        if self.maxLength == 2 and self.funcEndBool == False:
            return "That combination of lengths and functional groups is invalid"
        
        # Validation to catch if the user forgets to select a functional group (string presented as an error message)
        
        if not self.validGroups:
            return "You must select at least one functional group"
        
        # Define a valid length and position of functional group for the molecule
        if self.funcEndBool:
            self.length = random.randint(1, self.maxLength - 1)
            self.functionGroupPos = random.randint(0, 1)
            
            # Sets the functional group position to the other end of the moleulce if the random value is 1
            
            if self.functionGroupPos == 1:
                self.functionGroupPos = self.length - 1
        
        # Define a valid length and position of functional group for the molecule      
        else:
            
            # The molecule must have at least one atom between its end atoms, and therefore must have a minimum length of 3
            self.length = random.randint(3, self.maxLength)
            
            # If block to catch errors when the length of the molecule is exactly 3 (self.length - 2 == 1 causing randint to break)
            if self.length == 3:
                self.functionGroupPos = 1
            else:
                self.functionGroupPos = random.randint(1, self.length - 2)

        # Debug prints:
        # print("-------------------")
        # print(self.length)
        # print(self.validGroups)
        # print(self.funcEndBool)
        # print(self.functionGroupPos)
        # print("-------------------")
        
        # Iteration to create each carbon object in the molecule
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
        
        # Also activates if length == 1 as that carbon would need 4 bonding groups to be 'full'
        if self.functionGroupPos != self.length - 1 or self.length == 1:
            
            # Adds an extra hydrogen to the last carbon if it does not contain the functional group
            self.atoms[self.length-1].addBondedAtom(atom.Hydrogen())
    
    # Function to decide whether to add a hydrogen or halogen atom to a chain carbon            
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
    
    # Function to decide which functional group should be added to the molecule
    def addFunctionalGroup(self, carbon, funcEndBool):
        
        # Check whether the functional group will be at the end of the atom
        if funcEndBool:
            
            # Generates random number to decide which functional group will be added to the molecule
            diceRoll = random.randint(0, 100)
            
            # 20% chance that an Alcohol will be the main functional group of the molecule if selected
            if diceRoll <= 20 and "alcohol" in self.validGroups:
                
                # Instantiates functional group and updates molecule variables
                functionalGroup = fg.EndAlcohol()
                functionalGroup.addFunctionalGroup(carbon)
                self.stem = functionalGroup.stem
                return functionalGroup.name
            
            # 20% chance that an Aldehyde will be the main functional group of the molecule if selected
            elif diceRoll <= 40 and "aldehyde" in self.validGroups:
                
                # Instantiates functional group and updates molecule variables
                functionalGroup = fg.Aldehyde()
                functionalGroup.addFunctionalGroup(carbon)
                self.stem = functionalGroup.stem
                return functionalGroup.name
            
            # 20% chance that an Carboxylic acid will be the main functional group of the molecule if selected
            elif diceRoll <= 60 and "carboxylicacid" in self.validGroups:
                
                # Instantiates functional group and updates molecule variables
                functionalGroup = fg.CarboxylicAcid()
                functionalGroup.addFunctionalGroup(carbon)
                self.stem = functionalGroup.stem
                return functionalGroup.name
            
            # 20% chance that an Amide will be the main functional group of the molecule if selected
            elif diceRoll <= 80 and "amide" in self.validGroups:
                
                # Instantiates functional group and updates molecule variables
                functionalGroup = fg.Amide()
                functionalGroup.addFunctionalGroup(carbon)
                self.stem = functionalGroup.stem
                return functionalGroup.name
            
            # 20% chance that an Acyl Chloride will be the main functional group of the molecule if selected
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
            
            # 20% chance that the molecule will be an Alkane if selected
            if diceRoll <= 20 and "alkane" in self.validGroups:
                
                # Instantiates functional group and updates molecule variables
                functionalGroup = fg.Alkane()
                functionalGroup.addFunctionalGroup(carbon)
                self.stem = functionalGroup.stem
                return functionalGroup.name
            
            # 20% chance that the molecule will be an Amine if selected
            elif diceRoll <= 40 and "amine" in self.validGroups:
                
                # Instantiates functional group and updates molecule variables
                functionalGroup = fg.Amine()
                functionalGroup.addFunctionalGroup(carbon)
                self.stem = functionalGroup.stem
                return functionalGroup.name
            
            # 20% chance that the molecule will be an Alcohol if selected
            elif diceRoll <= 60 and "alcohol" in self.validGroups:
                
                # Instantiates functional group and updates molecule variables
                functionalGroup = fg.Alcohol()
                functionalGroup.addFunctionalGroup(carbon)
                self.stem = functionalGroup.stem
                return functionalGroup.name
            
            # 20% chance that the molecule will be an Alkene if selected
            elif diceRoll <= 80 and "alkene" in self.validGroups:
                
                # Instantiates functional group and updates molecule variables
                functionalGroup = fg.Alkene()
                functionalGroup.addFunctionalGroup(carbon)
                self.stem = functionalGroup.stem
                return functionalGroup.name
            # 20% chance that the molecule will be an Ketone if selected
            elif diceRoll <= 100 and "ketone" in self.validGroups:
                
                # Instantiates functional group and updates molecule variables
                functionalGroup = fg.Ketone()
                functionalGroup.addFunctionalGroup(carbon)
                self.stem = functionalGroup.stem
                return functionalGroup.name
            else:
                return self.addFunctionalGroup(carbon, funcEndBool)
            
    # Function to calculate and return the name of the molecule
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
        
        # Define a boolean to indicate whether the molecule should be flipped when minimising the numbers in its name
        FlipValues = False
        
        # Minimise the value of the functional group position via rotation if it is past the midpoint of the molecule
        if self.functionGroupPos + 1 > math.ceil(self.length / 2) and self.functionalGroupName != "Alkane":
            FlipValues = True
        
        # If the functional group is at the centre of the molecule (which has to therefore have an odd length) check whether it is possible to minimise the number value of the extra groups
        elif (self.length % 2 == 1 and self.length//2 == self.functionGroupPos) or self.functionalGroupName == "Alkane":
            addedGroupsKeys = addedGroupsDict.keys()
            
            for i in addedGroupsKeys:
                if addedGroupsDict[i]:
                    
                    # Check whether the closest group to the other side of the molecule is closer than the closest group on the original side
                    addedGroupsDict[i].sort(reverse=True)
                    tempAddedGroupsDict = addedGroupsDict[i]
                    addedGroupsDict[i].sort()
                    if self.length - int(tempAddedGroupsDict[0]) < int(addedGroupsDict[i][0]):
                        FlipValues = True
                    else:
                        break
        
        # Logic check
        if self.length == 1:
            FlipValues = False
        
        
        # Flip the number values if necessary
        if FlipValues:
            
            # Calculate the value of the flipped functional group position
            self.functionGroupPos = self.length - self.functionGroupPos - 1
            
            # For each extra group, calculate its flipped position and assign to the main dictionary
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
        
        # Define a validation bool
        otherGroupsPresent = False
        
        # Loop through the items in addedGroupsDict
        for x, y in addedGroupsDict.items():
            
            # Check there are values in the dictionary
            if len(y) >= 1:
                
                # Change the value of the bool to reflect the presence of extra groups
                otherGroupsPresent = True
                
                # Reset instancecount variable
                instancecount = 0
                
                # If only one value present, just add it to the name
                if len(y) == 1:
                    name += y[0]
                
                # If more than one value is present, loop through each value and concatenate them to the name seperated by , and - as appropriate
                else:
                    for i in y:
                        
                        # Add each individual number to the start of the stem, seperated by a comma (e.g. 1,2-dibromo...)
                        name += i
                        instancecount += 1
                        name += ","
                    name = name[:-1]    
                # Add the stems to the name
                name += "-" + IUPACRepetitionPrefixes[instancecount] + x + "-"
                
        # Remove the last , or - to allow it to combine with the main stem
        if len(name) > 0:
            name = name[:-1]
        
        # Selection tree for each naming case:
        
        # A short alcohol without extra groups shouldn't have a position number
        if self.functionalGroupName == "endalcohol" and self.length <= 2 and not otherGroupsPresent:
            name += IUPACLengthStems[self.length - 1] + "an" + self.stem
        
        # Alkane and end groups do not need a position indicator (unless it is a long alcohol, as alcohols can be both end and central groups)
        elif self.functionalGroupName == "alkane" or (self.functionalGroupName in self.endGroups and self.functionalGroupName != "endalcohol"):
            name += IUPACLengthStems[self.length - 1] + self.stem
        
        # Alkenes have a more complicated naming process
        elif self.functionalGroupName == "alkene":
            
            # Short alkenes do not need a position number
            if self.length <= 3:
                name += IUPACLengthStems[self.length - 1] + self.stem
                
            else:
                # If an alkene is flipped, its position should be counted from the closest carbon to the other side
                if FlipValues:
                    name += IUPACLengthStems[self.length - 1] + "-" + str(self.functionGroupPos) + "-" + str(self.stem)
                else:
                    name += IUPACLengthStems[self.length - 1] + "-" + str(self.functionGroupPos + 1) + "-" + str(self.stem)
        
        # Central groups in a 3-length molecule only have one possible position and therefore do not need a number (apart from alcohols as aforementioned)
        elif self.length == 3 and self.functionalGroupName in self.centralGroups and self.functionalGroupName != "alcohol":
            name += IUPACLengthStems[self.length - 1] + "an" + self.stem
        
        # If all other checks failed, add the general name structure
        else:
            name += IUPACLengthStems[self.length - 1] + "an-" + str(self.functionGroupPos + 1) + "-" + str(self.stem)
        return name
    
    # Get symbols on atoms for rendering
    def getSymbols(self, index):
        
        # Define and add symbols from each atom object
        symbols = []
        for j in self.atoms[index].getAtoms():
            symbols.append(j.symbol)
        return symbols

# Debugging functions
# newMolecule = Molecule(3)
# newMolecule.generate()
# print(newMolecule.outputMolecule())

