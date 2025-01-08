import svgwrite
import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui, QtSvgWidgets
import tester.NEAConceptsTestt as NEAT

def createSVG(length, molecule):
    
    # Define SVG dimensions
    resolutionX = 1920
    resolutionY = 1080

    # Create SVG
    svg_document = svgwrite.Drawing(filename = "./tester/test-svgwrite.svg",
                                    size = (str(resolutionX) + "px", str(resolutionY) + "px"))

    # Record the number of carbons in the molecule
    numberofCs = length
    
    # Define container for the bond lines
    hlines = svg_document.add(svg_document.g(id='hlines', stroke='black'))

    for i in range(numberofCs):
        
        # Debug print
        print(i)
        symbols = molecule.getSymbols(i)
        print(symbols)
        
        # Increase i by 1 for both atoms
        i += 1
        
        # Define the length of a horizontal line
        X = ((i + 1) * (resolutionX/(numberofCs+5)))
        
        # Define a variable to count the number of symbols, allowing different actions based on 1, 2 or 3 attached atoms
        symNum = 0
        
        # Check if first atom in molecule
        if i == 1:
            
            # Add first symbol to carbon
            svg_document.add(svg_document.text(symbols[symNum],
                                               
            # Define x and y values of its position
            x = (X - resolutionX/(numberofCs+5), X + resolutionX/(numberofCs+5)), y = (resolutionY/2 + 8, resolutionY/2 + 8), style = "font-size:20px; font-family:Arial"))
            
            # Add first bond line
            hlines.add(svg_document.line(
                
            # Define x and y values of its start and end
                start=(((i) * (resolutionX/(numberofCs+5))) + 20, resolutionY/2), end=(((i+1) * (resolutionX/(numberofCs+5))) - 8, resolutionY/2)))
            
            # Increase the symbol count
            symNum += 1
            
            # Add the carbon symbol
            svg_document.add(svg_document.text("C",

            # Define its x and y position
            x = (X, X), y = (resolutionY/2 + 8, resolutionY/2 + 8), style = "font-size:20px; font-family:Arial"))
            
            # Add the second symbol
            svg_document.add(svg_document.text(symbols[symNum],
                                               
            # Define its x and y position
            x = (X, X), y = (resolutionY/3 + 8, resolutionY/3 + 8), style = "font-size:20px; font-family:Arial"))
            
            # Increment the symbol count
            symNum += 1
            
            # Add the third symbol (as this is the first molecule)
            svg_document.add(svg_document.text(symbols[symNum],
                                               
            # Define its x and y position
            x = (X, X), y = (2 * resolutionY/3 + 8, 2*resolutionY/3 + 8), style = "font-size:20px; font-family:Arial"))
            
            # Add the two remaining bond lines 
            hlines.add(svg_document.line(start=(X + 8, resolutionY/3 + 15), end=(X + 8, resolutionY/2 - 15)))
            hlines.add(svg_document.line(start=(X + 8, 2*resolutionY/3 - 15), end=(X + 8, resolutionY/2 + 15)))
            
            
        elif i == numberofCs:
            
            # Add first symbol
            svg_document.add(svg_document.text(symbols[symNum],
                                               
            # Define its X and Y position
            x = (X + resolutionX/(numberofCs+5), X + resolutionX/(numberofCs+5)), y = (resolutionY/2 + 8, resolutionY/2 + 8), style = "font-size:20px; font-family:Arial"))
            
            # Increment the symbol count to access the next symbol
            symNum += 1
            
            # Add the main carbon atom
            svg_document.add(svg_document.text("C",
            x = (X, X), y = (resolutionY/2 + 8, resolutionY/2 + 8), style = "font-size:20px; font-family:Arial"))
            
            # Add the next symbol
            svg_document.add(svg_document.text(symbols[symNum],
            x = (X, X), y = (resolutionY/3 + 8, resolutionY/3 + 8), style = "font-size:20px; font-family:Arial"))
            
            # Increment the symbol count to access the next symbol
            symNum += 1
            
            # Add the final symbol
            svg_document.add(svg_document.text(symbols[symNum],
            x = (X, X), y = (2 * resolutionY/3 + 8, 2*resolutionY/3 + 8), style = "font-size:20px; font-family:Arial"))
            
            # Add the bond lines 
            hlines.add(svg_document.line(start=(X + 8, resolutionY/3 + 15), end=(X + 8, resolutionY/2 - 15)))
            hlines.add(svg_document.line(start=(X + 8, 2*resolutionY/3 - 15), end=(X + 8, resolutionY/2 + 15)))
            
        else:
            
            # Add the main carbon atom
            svg_document.add(svg_document.text("C",
            x = (X, X), y = (resolutionY/2 + 8, resolutionY/2 + 8), style = "font-size:20px; font-family:Arial"))
            
            # Add the first symbol
            svg_document.add(svg_document.text(symbols[symNum],
            x = (X, X), y = (resolutionY/3 + 8, resolutionY/3 + 8), style = "font-size:20px; font-family:Arial"))
            
            # Increment the symbol count by 1
            symNum += 1
            
            # Add the next symbol
            svg_document.add(svg_document.text(symbols[symNum],
            x = (X, X), y = (2 * resolutionY/3 + 8, 2*resolutionY/3 + 8), style = "font-size:20px; font-family:Arial"))
            
            # Add the bond lines
            hlines.add(svg_document.line(start=(X + 8, resolutionY/3 + 15), end=(X + 8, resolutionY/2 - 15)))
            hlines.add(svg_document.line(start=(X + 8, 2*resolutionY/3 - 15), end=(X + 8, resolutionY/2 + 15)))
            
        if i != numberofCs + 2:
            
            # Add a bond line to the next carbon on the right unless its the last carbon
            hlines.add(svg_document.line(start=(X + 20, resolutionY/2), end=(((i+2) * (resolutionX/(numberofCs+5))) - 8, resolutionY/2)))

    # Save the svg
    # svg_document.save()
    return svg_document.tostring()


# DEBUG: Generate molecule and render it  
molecule = NEAT.Molecule(10)
molecule.generate()
createSVG(molecule.length, molecule)



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
