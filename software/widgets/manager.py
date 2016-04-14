from PyQt4 import QtGui, QtCore
import os


class WorkspaceManager(QtGui.QWidget):

    # The signal that carries the folder of a new workspace path
    newPath = QtCore.pyqtSignal(str)

    def change_workspace(self):
        """ Lets the user select a folder and emits a "newPath" signal"""

        new_path = str(QtGui.QFileDialog.getExistingDirectory(
                        self, "Select Directory"))
        if new_path != "":
            self.newPath.emit(new_path)

    def __init__(self):

        super(WorkspaceManager, self).__init__()

        # The first button: Changes the workspace path
        self.change_path = QtGui.QPushButton("Change Workspace Path", self)
        self.change_path.clicked.connect(self.change_workspace)

        # The layout in this widget is incredibly simple: a single window
        layout = QtGui.QGridLayout()
        layout.addWidget(self.change_path, 0, 0)
        self.setLayout(layout)

        self.show()
