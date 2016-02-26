import sys
from PyQt4 import QtGui


class TextEditor(QtGui.QWidget):
    """ A file editor widget. Files are edited as text files. """

    def __init__(self, name = None, ext = None, path = None, saved = False):
        """ Parameters
            fname: The name of the file
            ext: The file extension
            path: The relative path to the file
        """
        super(TextEditor, self).__init__()

        self.fileName = name
        self.fileExt = ext
        self.filePath = path
        self.isSaved = saved

        self.init_view(name, ext)
        self.show()

    def init_view(self, name = None, ext = None):
        """ Initializes the view of the file editor widget

            Parameters
            fname: Name of the file being edited
            ext: Extension of the file being edited
        """

        text_editor = QtGui.QTextEdit(self)

        layout = QtGui.QGridLayout()
        layout.addWidget(text_editor)
        self.setLayout(layout)

        self.show()
