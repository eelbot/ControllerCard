from PyQt4 import QtGui, QtCore
import os


class BrowseWidget(QtGui.QTabWidget):
    """ A wrapper widget that appears in a dock, allowing the user to
        browse libraries and files.
    """

    def __init__(self, workspace='C:/', libraries=[]):
        """ Parameters
            workspace: The initial file path displayed in the file tree
        """
        super(BrowseWidget, self).__init__()

        self.init_view(workspace)
        self.show()

    def init_view(self, current_path):

        # 200px is the minimum width for usability of this widget
        self.setMinimumWidth(200)

        # Initialize the Resource widgets
        self.file_browser = FileBrowser(current_path)
        self.lib_browser = LibraryBrowser()

        # Create tabs at the top of the widget for different information
        self.addTab(self.file_browser, "Files")
        self.addTab(self.lib_browser, "Library")

        # Set layout and add the "tabs" structure
        layout = QtGui.QGridLayout()
        self.setLayout(layout)


class FileBrowser(QtGui.QTreeView):
    """Initializes the contents and look of the File Browser widget"""

    openWork = QtCore.pyqtSignal(str)

    def open_file(self):
        index = self.selectedIndexes()[0]
        self.openWork.emit(self.model().filePath(index))

    def change_path(self, new_path):
        """ Parameters

            new_path: The path to the new workspace
        """
        self.setRootIndex(self.file_model.index(new_path))
        self.file_model.setRootPath(QtCore.QDir.currentPath())

    def __init__(self, current_path):
        """ Parameters

            current_path: Initial file path for tree view
        """
        super(FileBrowser, self).__init__()

        self.doubleClicked.connect(self.open_file)

        # If the workspace path does not exist, create it
        if not os.path.isdir(current_path):
            os.makedirs(current_path, exist_ok=True)

        # Create a generic file model and display it in tree view
        self.file_model = QtGui.QFileSystemModel()
        self.setModel(self.file_model)
        self.setRootIndex(self.file_model.index(current_path))
        self.file_model.setRootPath(QtCore.QDir.currentPath())


class LibraryBrowser(QtGui.QWidget):

    def __init__(self):

        super(LibraryBrowser, self).__init__()
        test_lbl = QtGui.QLabel('Insert Library Here', self)
