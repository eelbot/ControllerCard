from PyQt4 import QtGui, QtCore
from widgets.tile import tile


class TextEditor(QtGui.QTextEdit):
    """ A file editor widget. Files are edited as text. """

    def __init__(self, name=None, ext=None, path='', saved=False):
        """ Parameters
            name: The name of the file
            ext: The file extension
            path: The relative path to the file
        """
        super(TextEditor, self).__init__()

        self.fileName = name
        self.fileExt = ext
        self.filePath = path
        self.isSaved = saved

        self.init_view(name, ext, path)
        self.show()

    def init_view(self, name=None, ext=None, path=''):
        """ Initializes the view of the file editor widget

            Parameters
            name: Name of the file being edited
            ext: Extension of the file being edited
        """

        # Try to open a file and display it's contents.
        # If the file cannot be opened, let the user know it does not exist.
        # If it can be opened, display the contents of the file as text
        try:
            with open(path, "rt") as file:
                self.setText(file.read())
            self.isSaved = True
        except FileNotFoundError:
            if name in ("untitled.upl", "untitled.pro", "untitled"):
                pass
            else:
                QtGui.QMessageBox.question(self, 'Message',
                                           "File does not exist")

        # Create final layout and display widget
        layout = QtGui.QGridLayout()
        self.setLayout(layout)

        self.show()


class DragDropEditor(QtGui.QWidget):
    """ A drag and drop based file editor """

    def __init__(self, name=None, ext=None, path='', saved=False):
        """ Parameters
            name: The name of the file
            ext: The file extension
            path: The relative path to the file
        """
        super(DragDropEditor, self).__init__()

        self.fileName = name
        self.fileExt = ext
        self.filePath = path
        self.isSaved = saved

        self.currentlyDrawing = False
        self.inix = 0
        self.iniy = 0
        self.finx = 0
        self.finy = 0

        self.numOfChildren = 1

        self.setMouseTracking(True)

        self.init_view(name, ext, path)

    def init_view(self, name=None, ext=None, path=''):
        """ Initializes the view of the file editor widget

            Parameters
            name: Name of the file being edited
            ext: Extension of the file being edited
        """

        self.show()

    def drawArrow(self, currentlyDrawing, eventx, eventy):
        self.currentlyDrawing = currentlyDrawing
        if self.currentlyDrawing:
            self.inix = eventx
            self.iniy = eventy
        else:
            self.finx = eventx
            self.finy = eventy


    def mouseMoveEvent(self, e):
        super(DragDropEditor, self).mouseMoveEvent(e)
        self.finx = e.x()
        self.finy = e.y()

    def paintEvent(self, e):
        super(DragDropEditor, self).paintEvent(e)
        if self.currentlyDrawing:
            self.paintArrow()
        self.update()

    def paintArrow(self):
        #INSERT CODE HERE TO DRAW ARROW, WHATEVER THAT MAY BE
        pass
