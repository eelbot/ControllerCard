from PyQt4 import QtGui, QtCore


class WorkspaceManager(QtGui.QWidget):

    # The signal that is emitted when the path is changed.
    # This signal carries a str that is the path of the desired workspace
    newPath = QtCore.pyqtSignal(str)
    importLib = QtCore.pyqtSignal(str)

    def change_workspace(self):
        """ Lets the user select a folder and emits a "newPath" signal"""

        # Obtain the parent folder of the new workspace path
        new_path = str(QtGui.QFileDialog.getExistingDirectory(
                        self, "Select Directory"))

        # Ensure that a path was selected, and emit a newPath signal
        if new_path != "":
            self.newPath.emit(new_path)

    def import_lib(self):
        """ Lets the user import a library for future use"""

        # Obtain the parent folder of the new workspace path
        get_lib = str(QtGui.QFileDialog.getOpenFileName(
                        self, "Import Library", '',"Text Files (*.lib)"))

        # Ensure that a path was selected, and emit a newPath signal
        if get_lib != "":
            self.importLib.emit(get_lib)

    def __init__(self):

        super(WorkspaceManager, self).__init__()

        # Button that emits a signal to change the workspace path
        self.change_path = QtGui.QPushButton("Change Workspace Path", self)
        self.change_path.clicked.connect(self.change_workspace)

        # Button that lets the user import a new library
        self.import_library = QtGui.QPushButton("Import a Library", self)
        self.import_library.clicked.connect(self.import_lib)

        # Set a simple grid layout
        layout = QtGui.QGridLayout()
        layout.addWidget(self.change_path, 0, 0)
        layout.addWidget(self.import_library, 1, 0)
        self.setLayout(layout)

        self.show()
