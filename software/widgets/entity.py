from PyQt4 import QtGui, QtCore

class tile(QtGui.QPushButton):
    """ This is the class that implements objects that can be drag
        and dropped in the drag and drop editor
    """

    # The signal the is emitted when drawing starts or stops for an arrow
    drawConnection = QtCore.pyqtSignal(int, int, int)

    # The signal that is emitted when something changes
    fileChange = QtCore.pyqtSignal()

    def __init__(self, parent, ref, xpos=100, ypos=100, width=100, height=100):
        """ Parameters
            xpos: Initial x position
            ypos: Initial y position
            ref: A reference to the the associated library function
                 Default value is 0, the null function
        """

        self.xpos = xpos
        self.ypos = ypos
        self.parent = parent
        self.ref = ref
        self.tile_func = None
        self.arrows = []

        super(tile, self).__init__(parent)

        # Position the tile in the open file
        self.setGeometry(self.xpos, self.ypos, width, height)

        # Set the initial style of the tile
        self.setStyleSheet(
                    "QPushButton{background-color:#AAAAAA; border:none;}\
                     QPushButton:pressed{background-color:#AAAAAA;}")
        self.show()



    def mouseMoveEvent(self, e):
        """ A re-implementation of the mouseMoveEvent.
            Parameters
                e: The event of mouseMoveEvent
        """

        super(tile, self).mouseMoveEvent(e)

        # Only drag if left button is clicked
        if e.buttons() == QtCore.Qt.LeftButton:
            # adjust offset from clicked point to origin of widget
            currPos = self.mapToGlobal(self.pos())
            globalPos = e.globalPos()

            # Calculate the difference from the original event and the
            # current mouse position
            diff = globalPos - self.__mouseMovePos

            # Set the tile location to the current position plus the difference
            newPos = self.mapFromGlobal(currPos + diff)
            self.move(newPos)

            self.fileChange.emit()

            for i in self.arrows:
                if i.input == self.ref:
                    i.inix = self.x() + (self.width() / 2)
                    i.iniy = self.y() + (self.height() / 2)
                elif i.output == self.ref:
                    i.finx = self.x() + (self.width() / 2)
                    i.finy = self.y() + (self.height() / 2)

            self.parent.update()
            # Ensure that the mouse position is now equal to the event position
            self.__mouseMovePos = globalPos

    def mousePressEvent(self, e):
        """ A re-implementation of the mouseMoveEvent.
            Parameters
                e: The event of mouseMoveEvent
        """

        super(tile, self).mousePressEvent(e)

        # Change the color of the tile to denote a right click
        if e.button() == QtCore.Qt.RightButton:
            self.setStyleSheet(
                        "QPushButton{background-color:#FF0000; border:none;}")

        # Reset and initialize the variables once a click starts
        self.__mousePressPos = None
        self.__mouseMovePos = None
        if e.button() == QtCore.Qt.LeftButton:
            self.__mousePressPos = e.globalPos()
            self.__mouseMovePos = e.globalPos()


    def mouseReleaseEvent(self, e):
        """ A re-implementation of the mouseMoveEvent.
            Parameters
                e: The event of mouseMoveEvent
        """

        # Return the tile to it's original color once right click is done
        if e.button() == QtCore.Qt.RightButton:
            self.setStyleSheet(
                        "QPushButton{background-color:#AAAAAA; border:none;}")

            # Emit a signal to draw an arrow
            self.drawConnection.emit(self.ref, self.x() + (self.width() / 2), self.y() + (self.height() / 2))
            self.fileChange.emit()

        # If the left mouse button has already been pressed, and the tile
        # has moved a minimum distance, do not run the original mouseReleaseEvent
        #if self.__mousePressPos is not None:
            #moved = e.globalPos() - self.__mousePressPos
            #if moved.manhattanLength() > 3:
                #e.ignore()
                #return
        super(tile, self).mouseReleaseEvent(e)

    def mouseDoubleClickEvent(self, e):
        super(tile, self).mouseDoubleClickEvent(e)
        QtGui.QMessageBox.information(self.parent, "About", "INSERT INFO HERE")


class arrow(QtGui.QWidget):

    def __init__(self, inix, iniy, finx, finy, in_ref, out_ref):
        super(arrow, self).__init__()

        self.inix = inix
        self.iniy = iniy
        self.finx = finx
        self.finy = finy
        self.input = in_ref
        self.output = out_ref

        self.setGeometry(0, 0, 2000, 2000)

    def paintEvent(self, e):

        qp = QtGui.QPainter()
        qp.begin(self)
        pen = QtGui.QPen(QtGui.QColor(0, 0, 0), 3, QtCore.Qt.SolidLine)

        qp.setPen(pen)
        qp.setBrush(QtCore.Qt.NoBrush)
        qp.drawLine(self.inix, self.iniy, self.finx, self.finy)
        qp.end()

    def update(self, inix, iniy, finx, finy):

        qp = QtGui.QPainter()
        qp.begin(self)
        pen = QtGui.QPen(QtGui.QColor(0, 0, 0), 3, QtCore.Qt.SolidLine)

        qp.setPen(pen)
        qp.setBrush(QtCore.Qt.NoBrush)
        qp.drawLine(self.inix, self.iniy, self.finx, self.finy)
        qp.end()
