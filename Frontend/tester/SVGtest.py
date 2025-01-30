import svgwrite
import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui, QtSvgWidgets
import tester.NEAConceptsTestt as NEAT

def createSVG(length, molecule):
    
    # Record the number of carbons in the molecule
    numberofCs = length
    
    # Define SVG dimensions
    resolutionX = calculateDistance(numberofCs + 1, (numberofCs + 1) * 2, numberofCs + 2, 0)
    resolutionY = calculateDistance(2, 4, 4, 0)

    # Create SVG
    svg_document = svgwrite.Drawing(filename = "./tester/test-svgwrite.svg",
                                    size = (str(resolutionX) + "px", str(resolutionY) + "px"))

    
    # Define container for the bond lines
    hlines = svg_document.add(svg_document.g(id='hlines', stroke='black'))

    for i in range(numberofCs):
        
        alkenepresent = False
        oxygendoublebond = False
        
        # Debug print
        print(i)
        symbols = molecule.getSymbols(i)
        print("symbols" + str(symbols))
        
        # Increase i by 1 for both atoms
        i += 1
        
        
        # Define a variable to count the number of symbols, allowing different actions based on 1, 2 or 3 attached atoms
        symNum = 0
        
        # Check if first atom in molecule
        if i == 1:
            # Add first symbol to carbon
            svg_document.add(svg_document.text(symbols[symNum][::-1],
                                            
            # Define x and y values of its position
            x = (0, ), 
            y = (calculateDistance(1, 2, 2, 0), ), style = "font-size:20px; font-family:Arial",))
            
            # Add first bond line
            hlines.add(svg_document.line(
                
            # Define x and y values of its start and end
            start=(calculateDistance(0, 1, 1, 0), calculateDistance(1, 2, 2, 1)), 
            end=(calculateDistance(1, 1, 1, 0), calculateDistance(1, 2, 2, 1))))

            # Increase the symbol count
            symNum += 1
            
            if symbols[symNum] == "ODB":
                oxygendoublebond = True
                hlines.add(svg_document.line(
                            start=(
                                calculateDistance(i, (i) * 2, i, -0.5), 
                                calculateDistance(0, 1, 1, 0)), 
                            end=(
                                calculateDistance(i, (i) * 2, i, -0.5), 
                                calculateDistance(1, 1, 1, 0))))
            else: 
                # Add the next symbol
                svg_document.add(svg_document.text(symbols[symNum],
                x = (calculateDistance(i, (i) * 2, i, 0), ), 
                y = (calculateDistance(2, 4, 3, 0), ), style = "font-size:20px; font-family:Arial"))
            
            # Add the carbon symbol
            svg_document.add(svg_document.text("C",

            # Define its x and y position
            x = (calculateDistance(1, 2, 1, 0), ), 
            y = (calculateDistance(1, 2, 2, 0), ), style = "font-size:20px; font-family:Arial"))
            
            # Increment the symbol count
            symNum += 1
            
            # Add the third symbol (as this is the first molecule)
            svg_document.add(svg_document.text(symbols[symNum],
                                               
            # Define its x and y position
            x = (calculateDistance(1, 2, 1, 0), ), 
            y = (calculateDistance(0, 0, 1, 0), ), style = "font-size:20px; font-family:Arial"))
            
            # Add the two remaining bond lines 
            if not oxygendoublebond:
                hlines.add(svg_document.line(
                    start=(
                        calculateDistance(1, 2, 1, -1), 
                        calculateDistance(0, 1, 1, 0)), 
                    end=(
                        calculateDistance(1, 2, 1, -1), 
                        calculateDistance(1, 1, 1, 0))))
            else:
                hlines.add(svg_document.line(
                    start=(
                        calculateDistance(1, 2, 1, -1.5), 
                        calculateDistance(0, 1, 1, 0)), 
                    end=(
                        calculateDistance(1, 2, 1, -1.5), 
                        calculateDistance(1, 1, 1, 0))))
            if not oxygendoublebond:
                hlines.add(svg_document.line(
                                            start=(
                                                calculateDistance(i, (i) * 2, i, -1), 
                                                calculateDistance(1, 3, 2, 0)), 
                                            end=(
                                                calculateDistance(i, (i) * 2, i, -1), 
                                                calculateDistance(2, 3, 2, 0))))
            
 
        elif i == numberofCs:
            
            if symbols[symNum + 1] != "ODB":
                # Add first symbol
                svg_document.add(svg_document.text(symbols[symNum],
                                                
                # Define its X and Y position
                x = (calculateDistance(numberofCs, (numberofCs) * 2, numberofCs, 0), ), 
                y = (calculateDistance(0, 0, 1, 0), ), style = "font-size:20px; font-family:Arial"))
            else:
                # Add first symbol
                svg_document.add(svg_document.text(symbols[symNum + 2],
                                                
                # Define its X and Y position
                x = (calculateDistance(numberofCs, (numberofCs) * 2, numberofCs, 0), ), 
                y = (calculateDistance(0, 0, 1, 0), ), style = "font-size:20px; font-family:Arial"))
            
            # Increment the symbol count to access the next symbol
            symNum += 1
            
            # Add the main carbon atom
            svg_document.add(svg_document.text("C",
            x = (calculateDistance(numberofCs, (numberofCs) * 2, numberofCs, 0), ),
            y = (calculateDistance(1, 2, 2, 0), ), style = "font-size:20px; font-family:Arial"))
            
            if symbols[symNum] == "ODB":
                oxygendoublebond = True
                hlines.add(svg_document.line(
                            start=(
                                calculateDistance(i, (i) * 2, i, -0.5), 
                                calculateDistance(0, 1, 1, 0)), 
                            end=(
                                calculateDistance(i, (i) * 2, i, -0.5), 
                                calculateDistance(1, 1, 1, 0))))
            else: 
                # Add the next symbol
                svg_document.add(svg_document.text(symbols[symNum],
                x = (calculateDistance(i, (i) * 2, i, 0), ), 
                y = (calculateDistance(2, 4, 3, 0), ), style = "font-size:20px; font-family:Arial"))
            
            # Add the bond lines 
            if not oxygendoublebond:
                hlines.add(svg_document.line(
                    start=(
                            calculateDistance(numberofCs, (numberofCs) * 2, numberofCs, -1), 
                            calculateDistance(0, 1, 1, 0)), 
                    end=(
                            calculateDistance(numberofCs, (numberofCs) * 2, numberofCs, -1), 
                            calculateDistance(1, 1, 1, 0))))
            else:
                hlines.add(svg_document.line(
                    start=(
                            calculateDistance(numberofCs, (numberofCs) * 2, numberofCs, -1.5), 
                            calculateDistance(0, 1, 1, 0)), 
                    end=(
                            calculateDistance(numberofCs, (numberofCs) * 2, numberofCs, -1.5), 
                            calculateDistance(1, 1, 1, 0))))
            if not oxygendoublebond:
                hlines.add(svg_document.line(
                    start=(
                            calculateDistance(numberofCs, (numberofCs) * 2, numberofCs, -1), 
                            calculateDistance(1, 3, 2, 0)), 
                    end=(
                            calculateDistance(numberofCs, (numberofCs) * 2, numberofCs, -1), 
                            calculateDistance(2, 3, 2, 0))))
            # Increment the symbol count to access the next symbol
            symNum += 1
            
            # Add the final symbol
            svg_document.add(svg_document.text(symbols[symNum - 2],
            x = (calculateDistance(numberofCs + 1, (numberofCs + 1) * 2, numberofCs + 1, 0), ), 
            y = (calculateDistance(1, 2, 2, 0), ), style = "font-size:20px; font-family:Arial"))
        else:
            
            # Add the main carbon atom
            svg_document.add(svg_document.text("C",
            x = (calculateDistance(i, (i) * 2, i, 0), ), 
            y = (calculateDistance(1, 2, 2, 0), ), style = "font-size:20px; font-family:Arial"))
            
            if symbols[symNum] == "N/A":
                alkenepresent = True
                hlines.add(svg_document.line(start=(
                                            calculateDistance(i, (i) * 2 + 1, i + 1, 0), 
                                            calculateDistance(1, 2, 2, 1.5)), 
                                        end=(
                                            calculateDistance(i + 1, (i) * 2 + 1, i + 1, 0), 
                                            calculateDistance(1, 2, 2, 1.5))))
            else:
                # Add the first symbol
                svg_document.add(svg_document.text(symbols[symNum],
                x = (calculateDistance(i, (i) * 2, i, 0), ), 
                y = (calculateDistance(0, 0, 1, 0), ), style = "font-size:20px; font-family:Arial"))
   
            # Increment the symbol count by 1
            symNum += 1
            
                   
            if symbols[symNum] == "ODB":
                oxygendoublebond = True
                hlines.add(svg_document.line(
                            start=(
                                calculateDistance(i, (i) * 2, i, -0.5), 
                                calculateDistance(0, 1, 1, 0)), 
                            end=(
                                calculateDistance(i, (i) * 2, i, -0.5), 
                                calculateDistance(1, 1, 1, 0))))
            else: 
                # Add the next symbol
                svg_document.add(svg_document.text(symbols[symNum],
                x = (calculateDistance(i, (i) * 2, i, 0), ), 
                y = (calculateDistance(2, 4, 3, 0), ), style = "font-size:20px; font-family:Arial"))
            
            # Add the bond lines
            if not alkenepresent:
                if not oxygendoublebond:
                    hlines.add(svg_document.line(
                                                start=(
                                                    calculateDistance(i, (i) * 2, i, -1), 
                                                    calculateDistance(0, 1, 1, 0)), 
                                                end=(
                                                    calculateDistance(i, (i) * 2, i, -1), 
                                                    calculateDistance(1, 1, 1, 0))))
                else: 
                    hlines.add(svg_document.line(
                                                start=(
                                                    calculateDistance(i, (i) * 2, i, -1.5), 
                                                    calculateDistance(0, 1, 1, 0)), 
                                                end=(
                                                    calculateDistance(i, (i) * 2, i, -1.5), 
                                                    calculateDistance(1, 1, 1, 0))))
            if not oxygendoublebond:
                hlines.add(svg_document.line(
                                            start=(
                                                calculateDistance(i, (i) * 2, i, -1), 
                                                calculateDistance(1, 3, 2, 0)), 
                                            end=(
                                                calculateDistance(i, (i) * 2, i, -1), 
                                                calculateDistance(2, 3, 2, 0))))
            
        if alkenepresent:
            # Add a bond line to the next carbon on the right unless its the last carbon
            hlines.add(svg_document.line(start=(
                                                calculateDistance(i, (i) * 2 + 1, i + 1, 0), 
                                                calculateDistance(1, 2, 2, 0.5)), 
                                            end=(
                                                calculateDistance(i + 1, (i) * 2 + 1, i + 1, 0), 
                                                calculateDistance(1, 2, 2, 0.5))))
        else:
            # Add a bond line to the next carbon on the right unless its the last carbon
            hlines.add(svg_document.line(start=(
                                                calculateDistance(i, (i) * 2 + 1, i + 1, 0), 
                                                calculateDistance(1, 2, 2, 1)), 
                                            end=(
                                                calculateDistance(i + 1, (i) * 2 + 1, i + 1, 0), 
                                                calculateDistance(1, 2, 2, 1))))
    if numberofCs == 1:
            # Increment the symbol count to access the next symbol
            symNum += 1
            
            # Add the final symbol
            svg_document.add(svg_document.text(symbols[symNum],
            x = (calculateDistance(numberofCs + 1, (numberofCs + 1) * 2, numberofCs + 1, 0), ), 
            y = (calculateDistance(1, 2, 2, 0), ), style = "font-size:20px; font-family:Arial"))

    # Save the svg
    # svg_document.save()
    return svg_document.tostring()

def calculateDistance(bondLengthCount, bondSpacingCount, characterSpacingCount, lineDifferenceCount = 0):
    bondLength = 20
    bondSpacing = 8
    characterSpacing = 15
    lineDifference = 7
    
    return bondLength * bondLengthCount + bondSpacing * bondSpacingCount + characterSpacing * characterSpacingCount - lineDifference * lineDifferenceCount


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
        
        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = MyWidget()
    widget.resize(1920, 1080)
    widget.show()

    sys.exit(app.exec())
