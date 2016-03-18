from PyQt4 import QtGui


class TextEditor(QtGui.QWidget):
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

        self.text_editor = QtGui.QTextEdit(self)

        # Try to open a file and display it's contents.
        # If the file cannot be opened, let the user know it does not exist.
        # If it can be opened, display the contents of the file as text
        try:
            with open(path, "rt") as file:
                self.text_editor.setText(file.read())
            self.isSaved = True
        except FileNotFoundError:
            if name == "untitled":
                pass
            else:
                QtGui.QMessageBox.question(self, 'Message',
                                           "File does not exist")

        # Create final layout and display widget
        layout = QtGui.QGridLayout()
        layout.addWidget(self.text_editor)
        self.setLayout(layout)

        self.show()
