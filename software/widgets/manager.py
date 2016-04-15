from PyQt4 import QtGui, QtCore


class WorkspaceManager(QtGui.QWidget):

    # The signal that is emitted when the path is changed.
    # This signal carries a str that is the path of the desired workspace
    newPath = QtCore.pyqtSignal(str)

    def change_workspace(self):
        """ Lets the user select a folder and emits a "newPath" signal"""

        # Obtain the parent folder of the new workspace path
        new_path = str(QtGui.QFileDialog.getExistingDirectory(
                        self, "Select Directory"))

        # Ensure that a path was selected, and emit a newPath signal
        if new_path != "":
            self.newPath.emit(new_path)

    def __init__(self):

        super(WorkspaceManager, self).__init__()

        # Button that emits a signal to change the workspace path
        self.change_path = QtGui.QPushButton("Change Workspace Path", self)
        self.change_path.clicked.connect(self.change_workspace)

        # Set a simple grid layout
        layout = QtGui.QGridLayout()
        layout.addWidget(self.change_path, 0, 0)
        self.setLayout(layout)

        self.show()
