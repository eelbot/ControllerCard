from PyQt4 import QtGui, QtCore

class tile(QtGui.QPushButton):
    """ This is the class that implements objects that can be drag
        and dropped in the drag and drop editor
    """

    def __init__(self, parent, xpos=100, ypos=100, width=100, height=100, ref=0):
        """ Parameters
            xpos: Initial x position
            ypos: Initial y position
            ref: A reference to the the associated library function
                 Default value is 0, the null function
        """

        self.xpos = xpos
        self.ypos = ypos
        self.parent = parent

        super(tile, self).__init__(parent)

        self.setGeometry(self.xpos, self.ypos, width, height)
        self.clicked.connect(self.info_display)
        self.setStyleSheet(
                    "QPushButton{background-color:#AAAAAA; border:none;}\
                     QPushButton:pressed{background-color:#AAAAAA;}")
        self.show()

    def mouseMoveEvent(self, e):
        super(tile, self).mouseMoveEvent(e)
        if e.buttons() == QtCore.Qt.LeftButton:
            # adjust offset from clicked point to origin of widget
            currPos = self.mapToGlobal(self.pos())
            globalPos = e.globalPos()
            diff = globalPos - self.__mouseMovePos
            newPos = self.mapFromGlobal(currPos + diff)
            self.move(newPos)
            self.__mouseMovePos = globalPos

    def mousePressEvent(self, e):
        super(tile, self).mousePressEvent(e)
        self.__mousePressPos = None
        self.__mouseMovePos = None
        if e.button() == QtCore.Qt.LeftButton:
            self.__mousePressPos = e.globalPos()
            self.__mouseMovePos = e.globalPos()


    def mouseReleaseEvent(self, e):
        if self.__mousePressPos is not None:
            moved = e.globalPos() - self.__mousePressPos
            if moved.manhattanLength() > 3:
                e.ignore()
                return
        super(tile, self).mouseReleaseEvent(e)

    def info_display(self, e):
        QtGui.QMessageBox.information(self.parent, "About", "INSERT INFO HERE")
