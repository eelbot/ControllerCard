from PyQt4 import QtGui, QtCore
from widgets.entity import tile, arrow


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
        self.libs = []

        self.currentlyDrawing = False
        self.start_wid = None
        self.end_wid = None
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

    def drawArrow(self, wid_ref, eventx, eventy):
        #self.currentlyDrawing = currentlyDrawing

        if self.start_wid == None and self.end_wid == None:
            self.start_wid = wid_ref
            self.inix = eventx
            self.iniy = eventy
        elif self.start_wid != None and self.end_wid == None:
            self.end_wid = wid_ref
            if self.end_wid != self.start_wid:
                self.finx = eventx
                self.finy = eventy
                new_arrow = arrow(self.inix, self.iniy, self.finx, self.finy, self.start_wid, self.end_wid)
                new_arrow.setParent(self)
                new_arrow.lower()
                new_arrow.show()
                tiles = self.findChildren(tile)
                for i in tiles:
                    if i.ref == self.start_wid or i.ref == self.end_wid:
                        i.arrows.append(new_arrow)
            self.start_wid = None
            self.end_wid = None
