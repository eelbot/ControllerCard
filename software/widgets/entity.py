from PyQt4 import QtGui, QtCore

class tile(QtGui.QPushButton):
    """ This is the class that implements objects that can be drag
        and dropped in the drag and drop editor
    """

    # The signal the is emitted when drawing starts or stops for an arrow
    drawConnection = QtCore.pyqtSignal(int, int, int, str)

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
        self.func_dict = {}
        self.set_value = "None"
        self.arrows = []

        super(tile, self).__init__(parent)

        self.clicked.connect(self.delete_tile)

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

    def contextMenuEvent(self, e):
        # Somehow the opening of the dialog box during a right click
        # activates the context menu
        return

    def mouseReleaseEvent(self, e):
        """ A re-implementation of the mouseMoveEvent.
            Parameters
                e: The event of mouseMoveEvent
        """

        super(tile, self).mouseReleaseEvent(e)
        # Return the tile to it's original color once right click is done
        if e.button() == QtCore.Qt.RightButton:
            self.setStyleSheet(
                        "QPushButton{background-color:#AAAAAA; border:none;}")

            if self.func_dict == {}:
                assign_please = QtGui.QMessageBox.information(self.parent, "Warning", "You must assign a function to a block before making a connection")
                return

            sel = None
            # Ask the user which input they would like to connect to
            if self.parent.start_wid != None:
                items = []
                i = 1
                while(1):
                    try:
                        items.append(self.func_dict['Input' + str(i)][2:])
                        i += 1
                    except KeyError:
                        break
                sel = QtGui.QInputDialog.getItem(self.parent, "Select Input", "Input", items, 0, False)

            # Emit a signal to draw an arrow
            if(sel != None):
                self.drawConnection.emit(self.ref, self.x() + (self.width() / 2), self.y() + (self.height() / 2), sel[0])
            else:
                self.drawConnection.emit(self.ref, self.x() + (self.width() / 2), self.y() + (self.height() / 2), "None")
            self.fileChange.emit()

    # Display current function info, and allow user to select a new function
    def mouseDoubleClickEvent(self, e):
        super(tile, self).mouseDoubleClickEvent(e)
        items = []
        for option in self.parent.libs:
            items.append(option['FunctionName'])
        function_name = QtGui.QInputDialog.getItem(self.parent, "Select Block Function", "Function", items, 0, False)

        for option in self.parent.libs:
            if option['FunctionName'] == function_name[0] and function_name[1] == True:
                self.func_dict = option
                self.setToolTip(self.func_dict['ToolTip'])
                self.setText(self.func_dict['FunctionName'])
                try:
                    if self.func_dict['Input1'][-3:] == "set":
                        set_value = QtGui.QInputDialog.getText(self.parent, "Set Value", "Input set value")
                        self.set_value = set_value[0]
                except KeyError:
                    break

    def delete_tile(self):
        modifier = QtGui.QApplication.keyboardModifiers()
        if modifier == QtCore.Qt.ControlModifier:
            for arrow in self.arrows:
                arrow.deleteLater()
            self.fileChange.emit()
            self.deleteLater()



class arrow(QtGui.QWidget):

    fileChange = QtCore.pyqtSignal()

    def __init__(self, inix, iniy, finx, finy, in_ref, out_ref, sel_in):
        super(arrow, self).__init__()

        self.inix = inix
        self.iniy = iniy
        self.finx = finx
        self.finy = finy
        self.input = in_ref # The input relative to the arrow (connected to a tile output)
        self.output = out_ref # The output relative to the arrow (connected to an input of a tile)
        self.sel_in = sel_in

        self.setGeometry(0, 0, 2000, 2000)

        #self.clicked.connect(self.delete_tile)

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

    def mouseReleaseEvent(self, e):
        modifier = QtGui.QApplication.keyboardModifiers()
        if modifier == QtCore.Qt.ControlModifier:
            tiles = self.parentWidget().findChildren(tile)
            for v in tiles:
                if self in v.arrows:
                    v.arrows.remove(self)
            self.fileChange.emit()
            self.deleteLater()
