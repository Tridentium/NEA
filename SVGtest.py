import svgwrite
import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui, QtSvgWidgets
import NEAConceptsTestt as NEAT

def createSVG(length):
    resolutionX = 1920
    resolutionY = 1080

    svg_document = svgwrite.Drawing(filename = "test-svgwrite.svg",
                                    size = (str(resolutionX) + "px", str(resolutionY) + "px"))

    numberofCs = length 
    hlines = svg_document.add(svg_document.g(id='hlines', stroke='black'))

    for i in range(numberofCs + 2):
        symbols = molecule.getSymbols(int(i/2))
        print(symbols)
        i += 1
        X = (i * (resolutionX/(numberofCs+3)))
        symNum = 0
        if i == 1 or i == numberofCs + 2:
            svg_document.add(svg_document.text(symbols[symNum],
            x = (X, X), y = (resolutionY/2 + 8, resolutionY/2 + 8), style = "font-size:20px; font-family:Arial"))
            symNum += 1
        else:
            svg_document.add(svg_document.text("C",
            x = (X, X), y = (resolutionY/2 + 8, resolutionY/2 + 8), style = "font-size:20px; font-family:Arial"))
            svg_document.add(svg_document.text(symbols[symNum],
            x = (X, X), y = (resolutionY/3 + 8, resolutionY/3 + 8), style = "font-size:20px; font-family:Arial"))
            symNum += 1
            svg_document.add(svg_document.text(symbols[symNum],
            x = (X, X), y = (2 * resolutionY/3 + 8, 2*resolutionY/3 + 8), style = "font-size:20px; font-family:Arial"))
            hlines.add(svg_document.line(start=(X + 8, resolutionY/3 + 15), end=(X + 8, resolutionY/2 - 15)))
            hlines.add(svg_document.line(start=(X + 8, 2*resolutionY/3 - 15), end=(X + 8, resolutionY/2 + 15)))
        if i != numberofCs + 2:
            hlines.add(svg_document.line(start=(X + 20, resolutionY/2), end=(((i+1) * (resolutionX/(numberofCs+3))) - 8, resolutionY/2)))

    svg_document.save()
    
molecule = NEAT.Molecule(10)
molecule.generate()
createSVG(molecule.length)




class MyWidget(QtSvgWidgets.QSvgWidget):
    def __init__(self):
        super().__init__()
        self.text = QtWidgets.QLabel(str(molecule.outputMolecule()),
                                     alignment=QtCore.Qt.AlignHCenter)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.text.setFont(font)
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.load("test-svgwrite.svg")
        
        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(1920, 1080)
    widget.show()

    sys.exit(app.exec())
