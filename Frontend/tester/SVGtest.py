import svgwrite
import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui, QtSvgWidgets
import tester.Molecule as NEAT

def createSVG(length, molecule):
    
    # Define the number of carbons in the molecule
    numberofCs = length
    
    # Define the SVG's dimensions
    resolutionX = calculateDistance(numberofCs + 1, (numberofCs + 1) * 2, numberofCs + 3, 0)
    resolutionY = calculateDistance(2, 4, 4, 0)

    # Create the SVG
    svg_document = svgwrite.Drawing(filename = "./tester/test-svgwrite.svg",
                                    size = (str(resolutionX) + "px", str(resolutionY) + "px"))

    # Define the bool variable that will be used to shift the molecule if there's a two letter group at the start of the molecule
    doubleletter = False
    
    # Define container for the bond lines
    hlines = svg_document.add(svg_document.g(id='hlines', stroke='black'))

    for i in range(numberofCs):
        
        # Reset the double bond flags
        alkenepresent = False
        oxygendoublebond = False
        
        # Debug print
        # print(i)
        
        # Access the symbol list of the current carbon's bonded atoms
        symbols = molecule.getSymbols(i)
        # print("symbols" + str(symbols))
        
        # Increase i by 1 for both atoms
        i += 1
        
        # Define a variable to count the number of symbols, allowing different actions based on 1, 2 or 3 attached atoms
        symNum = 0
        
        # Check if first atom in molecule
        if i == 1:
            
            # Add first symbol to carbon, reversing it if it contains more than two symbols to ensure the bond connects to the correct atom
            if symbols[symNum] == symbols[symNum].upper() and symbols[symNum][::-1] != symbols[symNum]:
                
                # Ensure that the 2 in NH2 is positioned correctly and reverse letters
                if "₂" not in symbols[symNum]:
                    initialtext = symbols[symNum][::-1]
                else:
                    initialtext = symbols[symNum][1] + symbols[symNum][2] + symbols[symNum][0]
                doubleletter = True
            else:
                initialtext = symbols[symNum]
                doubleletter = False
            
            # Add the first symbol to the SVG
            svg_document.add(svg_document.text(initialtext,
                                            
            # Define x and y values of its position
            x = (calculateDistance(0, 0, 0, 0), ), 
            y = (calculateDistance(1, 2, 2, 0), ), style = "font-size:20px; font-family:Arial",))
            
            # Add first bond line
            hlines.add(svg_document.line(
                
            # Define x and y values of its start and end
            start=(calculateDistance(0, 1, 1, 0, doubleletter), calculateDistance(1, 2, 2, 1)), 
            end=(calculateDistance(1, 1, 1, 0, doubleletter), calculateDistance(1, 2, 2, 1))))

            # Increase the symbol count
            symNum += 1
            
            # If an oxygen double bond is present, add a second line to the bond and don't add the temporary symbol
            if symbols[symNum] == "ODB":
                oxygendoublebond = True
                hlines.add(svg_document.line(
                            start=(
                                calculateDistance(i, (i) * 2, i, -0.5, doubleletter), 
                                calculateDistance(0, 1, 1, 0)), 
                            end=(
                                calculateDistance(i, (i) * 2, i, -0.5, doubleletter), 
                                calculateDistance(1, 1, 1, 0))))
                
            # If an oxygen double bond is not present, add the symbol as usual
            else: 
                svg_document.add(svg_document.text(symbols[symNum],
                x = (calculateDistance(i, (i) * 2, i, 0, doubleletter), ), 
                y = (calculateDistance(2, 4, 3, 0), ), style = "font-size:20px; font-family:Arial"))
            
            # Add the carbon symbol
            svg_document.add(svg_document.text("C",

            # Define its x and y position
            x = (calculateDistance(1, 2, 1, 0, doubleletter), ), 
            y = (calculateDistance(1, 2, 2, 0), ), style = "font-size:20px; font-family:Arial"))
            
            # Increment the symbol count
            symNum += 1
            
            # Add the third symbol (as this is the first atom)
            svg_document.add(svg_document.text(symbols[symNum],
                                               
            # Define its x and y position
            x = (calculateDistance(1, 2, 1, 0, doubleletter), ), 
            y = (calculateDistance(0, 0, 1, 0), ), style = "font-size:20px; font-family:Arial"))
            
            # Add the next bond line, slightly shifted if an oxygen double bond is present
            if not oxygendoublebond:
                hlines.add(svg_document.line(
                    start=(
                        calculateDistance(1, 2, 1, -1, doubleletter), 
                        calculateDistance(0, 1, 1, 0)), 
                    end=(
                        calculateDistance(1, 2, 1, -1, doubleletter), 
                        calculateDistance(1, 1, 1, 0))))
            else:
                hlines.add(svg_document.line(
                    start=(
                        calculateDistance(1, 2, 1, -1.5, doubleletter), 
                        calculateDistance(0, 1, 1, 0)), 
                    end=(
                        calculateDistance(1, 2, 1, -1.5, doubleletter), 
                        calculateDistance(1, 1, 1, 0))))
                
            # Add the final line if there is a symbol present
            if not oxygendoublebond:
                hlines.add(svg_document.line(
                                            start=(
                                                calculateDistance(i, (i) * 2, i, -1, doubleletter), 
                                                calculateDistance(1, 3, 2, 0)), 
                                            end=(
                                                calculateDistance(i, (i) * 2, i, -1, doubleletter), 
                                                calculateDistance(2, 3, 2, 0))))
            
 
        elif i == numberofCs:
            
            # If the last atom has an oxygen double bond, the accessed symbols need to be switched
            if symbols[symNum + 1] != "ODB":
                # Add first symbol
                svg_document.add(svg_document.text(symbols[symNum],
                                                
                # Define its X and Y position
                x = (calculateDistance(numberofCs, (numberofCs) * 2, numberofCs, 0, doubleletter), ), 
                y = (calculateDistance(0, 0, 1, 0), ), style = "font-size:20px; font-family:Arial"))
            else:
                # Add first symbol
                svg_document.add(svg_document.text(symbols[symNum + 2],
                                                
                # Define its X and Y position
                x = (calculateDistance(numberofCs, (numberofCs) * 2, numberofCs, 0, doubleletter), ), 
                y = (calculateDistance(0, 0, 1, 0), ), style = "font-size:20px; font-family:Arial"))
            
            # Increment the symbol count to access the next symbol
            symNum += 1
            
            # Add the main carbon atom
            svg_document.add(svg_document.text("C",
            x = (calculateDistance(numberofCs, (numberofCs) * 2, numberofCs, 0, doubleletter), ),
            y = (calculateDistance(1, 2, 2, 0), ), style = "font-size:20px; font-family:Arial"))
            
            # If an oxygen double bond is present, add a second line to the bond and don't add the temporary symbol
            if symbols[symNum] == "ODB":
                oxygendoublebond = True
                hlines.add(svg_document.line(
                            start=(
                                calculateDistance(i, (i) * 2, i, -0.5, doubleletter), 
                                calculateDistance(0, 1, 1, 0)), 
                            end=(
                                calculateDistance(i, (i) * 2, i, -0.5, doubleletter), 
                                calculateDistance(1, 1, 1, 0))))
                
            # If an oxygen double bond is not present, add the symbol as usual
            else: 
                svg_document.add(svg_document.text(symbols[symNum],
                x = (calculateDistance(i, (i) * 2, i, 0, doubleletter), ), 
                y = (calculateDistance(2, 4, 3, 0), ), style = "font-size:20px; font-family:Arial"))
            
            # Add the next bond line, slightly shifted if an oxygen double bond is present
            if not oxygendoublebond:
                hlines.add(svg_document.line(
                    start=(
                            calculateDistance(numberofCs, (numberofCs) * 2, numberofCs, -1, doubleletter), 
                            calculateDistance(0, 1, 1, 0)), 
                    end=(
                            calculateDistance(numberofCs, (numberofCs) * 2, numberofCs, -1, doubleletter), 
                            calculateDistance(1, 1, 1, 0))))
            else:
                hlines.add(svg_document.line(
                    start=(
                            calculateDistance(numberofCs, (numberofCs) * 2, numberofCs, -1.5, doubleletter), 
                            calculateDistance(0, 1, 1, 0)), 
                    end=(
                            calculateDistance(numberofCs, (numberofCs) * 2, numberofCs, -1.5, doubleletter), 
                            calculateDistance(1, 1, 1, 0))))
            # Add the final line if there is a symbol present
            if not oxygendoublebond:
                hlines.add(svg_document.line(
                    start=(
                            calculateDistance(numberofCs, (numberofCs) * 2, numberofCs, -1, doubleletter), 
                            calculateDistance(1, 3, 2, 0)), 
                    end=(
                            calculateDistance(numberofCs, (numberofCs) * 2, numberofCs, -1, doubleletter), 
                            calculateDistance(2, 3, 2, 0))))
            # Increment the symbol count to access the next symbol
            symNum += 1

            # Add the final symbol to the atom
            if oxygendoublebond:
                svg_document.add(svg_document.text(symbols[symNum - 2],
                x = (calculateDistance(numberofCs + 1, (numberofCs + 1) * 2, numberofCs + 1, 0, doubleletter), ), 
                y = (calculateDistance(1, 2, 2, 0), ), style = "font-size:20px; font-family:Arial"))
            else:
                svg_document.add(svg_document.text(symbols[symNum],
                x = (calculateDistance(numberofCs + 1, (numberofCs + 1) * 2, numberofCs + 1, 0, doubleletter), ), 
                y = (calculateDistance(1, 2, 2, 0), ), style = "font-size:20px; font-family:Arial"))
        
        else:
            # Add the main carbon atom
            svg_document.add(svg_document.text("C",
            x = (calculateDistance(i, (i) * 2, i, 0, doubleletter), ), 
            y = (calculateDistance(1, 2, 2, 0), ), style = "font-size:20px; font-family:Arial"))
            
            # If a double bond is present, add the necessary bond line to the next atom along
            if symbols[symNum] == "N/A":
                alkenepresent = True
                hlines.add(svg_document.line(start=(
                                            calculateDistance(i, (i) * 2 + 1, i + 1, 0, doubleletter), 
                                            calculateDistance(1, 2, 2, 1.5)), 
                                        end=(
                                            calculateDistance(i + 1, (i) * 2 + 1, i + 1, 0, doubleletter), 
                                            calculateDistance(1, 2, 2, 1.5))))
            # Add the next symbol as usual
            else:
                # Add the first symbol
                svg_document.add(svg_document.text(symbols[symNum],
                x = (calculateDistance(i, (i) * 2, i, 0, doubleletter), ), 
                y = (calculateDistance(0, 0, 1, 0), ), style = "font-size:20px; font-family:Arial"))
   
            # Increment the symbol count by 1
            symNum += 1
            
            # If an oxygen double bond is present, add a second line to the bond and don't add the temporary symbol       
            if symbols[symNum] == "ODB":
                oxygendoublebond = True
                hlines.add(svg_document.line(
                            start=(
                                calculateDistance(i, (i) * 2, i, -0.5, doubleletter), 
                                calculateDistance(0, 1, 1, 0)), 
                            end=(
                                calculateDistance(i, (i) * 2, i, -0.5, doubleletter), 
                                calculateDistance(1, 1, 1, 0))))
            
            # If an oxygen double bond is not present, add the symbol as usual
            else: 
                svg_document.add(svg_document.text(symbols[symNum],
                x = (calculateDistance(i, (i) * 2, i, 0, doubleletter), ), 
                y = (calculateDistance(2, 4, 3, 0), ), style = "font-size:20px; font-family:Arial"))
            
            # If a standard double bond isn't present, add the next line
            if not alkenepresent:
                # Slightly shifted if an oxygen double bond is present
                if not oxygendoublebond:
                    hlines.add(svg_document.line(
                                                start=(
                                                    calculateDistance(i, (i) * 2, i, -1, doubleletter), 
                                                    calculateDistance(0, 1, 1, 0)), 
                                                end=(
                                                    calculateDistance(i, (i) * 2, i, -1, doubleletter), 
                                                    calculateDistance(1, 1, 1, 0))))
                else: 
                    hlines.add(svg_document.line(
                                                start=(
                                                    calculateDistance(i, (i) * 2, i, -1.5, doubleletter), 
                                                    calculateDistance(0, 1, 1, 0)), 
                                                end=(
                                                    calculateDistance(i, (i) * 2, i, -1.5, doubleletter), 
                                                    calculateDistance(1, 1, 1, 0))))
            
            if not oxygendoublebond:
                hlines.add(svg_document.line(
                                            start=(
                                                calculateDistance(i, (i) * 2, i, -1, doubleletter), 
                                                calculateDistance(1, 3, 2, 0)), 
                                            end=(
                                                calculateDistance(i, (i) * 2, i, -1, doubleletter), 
                                                calculateDistance(2, 3, 2, 0))))
        
        # Shift the rightmost bond down if a double bond there is present
        if alkenepresent:
            # Add a bond line to the next carbon on the right unless its the last carbon
            hlines.add(svg_document.line(start=(
                                                calculateDistance(i, (i) * 2 + 1, i + 1, 0, doubleletter), 
                                                calculateDistance(1, 2, 2, 0.5)), 
                                            end=(
                                                calculateDistance(i + 1, (i) * 2 + 1, i + 1, 0, doubleletter), 
                                                calculateDistance(1, 2, 2, 0.5))))
        else:
            # Add a bond line to the next carbon on the right unless its the last carbon
            hlines.add(svg_document.line(start=(
                                                calculateDistance(i, (i) * 2 + 1, i + 1, 0, doubleletter), 
                                                calculateDistance(1, 2, 2, 1)), 
                                            end=(
                                                calculateDistance(i + 1, (i) * 2 + 1, i + 1, 0, doubleletter), 
                                                calculateDistance(1, 2, 2, 1))))
    
    # Add the fourth symbol if it is a one carbon molecule
    if numberofCs == 1:
            # Increment the symbol count to access the next symbol
            symNum += 1
            
            # Add the final symbol
            svg_document.add(svg_document.text(symbols[symNum],
            x = (calculateDistance(numberofCs + 1, (numberofCs + 1) * 2, numberofCs + 1, 0, doubleletter), ), 
            y = (calculateDistance(1, 2, 2, 0), ), style = "font-size:20px; font-family:Arial"))

    # Return the svg
    return svg_document.tostring()

# Define a function to calculate the location of a specific value, removing unecessary repetition of variables
def calculateDistance(bondLengthCount, bondSpacingCount, characterSpacingCount, lineDifferenceCount = 0, doubleletter = False):
    bondLength = 20
    bondSpacing = 8
    characterSpacing = 20
    lineDifference = 7
    
    distance = 0
    if doubleletter:
        distance += characterSpacing - lineDifference * 1.5
    
    return distance + bondLength * bondLengthCount + bondSpacing * bondSpacingCount + characterSpacing * characterSpacingCount - lineDifference * lineDifferenceCount


# DEBUG: Generate molecule and render it  
# molecule = NEAT.Molecule(10)
# molecule.generate()
# createSVG(molecule.length, molecule)



# DEBUG: Display SVG
# class MyWidget(QtSvgWidgets.QSvgWidget):
#     def __init__(self):
#         super().__init__()
#         self.text = QtWidgets.QLabel(str(molecule.outputMolecule()),
#                                      alignment=QtCore.Qt.AlignHCenter)
#         font = QtGui.QFont()
#         font.setPointSize(20)
#         self.text.setFont(font)
#         self.layout = QtWidgets.QVBoxLayout(self)
#         self.layout.addWidget(self.text)
#         self.load("test-svgwrite.svg")
                
# if __name__ == "__main__":
#     app = QtWidgets.QApplication([])
#     widget = MyWidget()
#     widget.resize(1920, 1080)
#     widget.show()

#     sys.exit(app.exec())
