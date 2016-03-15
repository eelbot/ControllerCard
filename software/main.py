import sys
from PyQt4 import QtGui, QtCore
from widgets.resources import BrowseWidget
from widgets.workspace import Workspace
from utils import fileop


class main_app(QtGui.QMainWindow):

    def __init__(self):
        super(main_app, self).__init__()

        # Initialize the application main window (toolbars, menus, workspace)
        # See bottom of main_app class definition for initUI() code. initUI()
        # calls all of the very large functions defined below
        statusbar = self.statusBar()
        menubar = self.menuBar()

        self.init_view()
        self.create_file_menu(menubar)

        self.setWindowTitle('PicoCommander')
        self.showMaximized()
        self.show()

    def create_file_menu(self, menubar):
        """ Creates the file menu """

        # New Blank File Menu Option
        new_blank_file = QtGui.QAction('New Empty File', self)
        new_blank_file.setShortcut('Ctrl+Shift+N')
        new_blank_file.setStatusTip('Create a new blank file')
        new_blank_file.triggered.connect(
                lambda: fileop.create_blank_file(self.workspace))

        # New Project Menu Option
        new_proj = QtGui.QAction('Create New Project', self)
        new_proj.setStatusTip('Create a new project')
        new_proj.triggered.connect(fileop.create_proj)

        # New Project File Menu Option
        new_proj_file = QtGui.QAction('New Project File', self)
        new_proj_file.setStatusTip('Create a new application file')
        new_proj_file.triggered.connect(fileop.create_proj_file)

        # New Library Menu Option
        new_lib = QtGui.QAction('New Library', self)
        new_lib.setStatusTip('Create a new library')
        new_lib.triggered.connect(fileop.create_lib)

        # Open File Menu Option
        open_file = QtGui.QAction(QtGui.QIcon('open_file.png'),
                                  'Open File', self)
        open_file.setShortcut('Ctrl+O')
        open_file.setStatusTip('Open a file')
        open_file.triggered.connect(
                lambda: fileop.open_file(self, self.work_path, self.workspace))

        # Import Project Menu Option
        import_proj = QtGui.QAction(QtGui.QIcon('import_proj.png'),
                                    'Import Project', self)
        import_proj.setStatusTip('Import an existing project')
        import_proj.triggered.connect(fileop.import_proj)

        # Save File Menu Option
        save_file = QtGui.QAction(QtGui.QIcon('save_file.png'),
                                  'Save File', self)
        save_file.setShortcut('Ctrl+S')
        save_file.setStatusTip('Save current file')
        save_file.triggered.connect(fileop.save_file)
        save_file.setEnabled(False)

        # Save As File Menu Option
        save_file = QtGui.QAction('Save As', self)
        save_file.setStatusTip('Save current file')
        save_file.triggered.connect(fileop.save_as_file)
        save_file.setEnabled(False)

        # Exit Main app Menu Option
        exit_app = QtGui.QAction(QtGui.QIcon('exit.png'), 'Exit', self)
        exit_app.setShortcut('Ctrl+Q')
        exit_app.setStatusTip('Exit Pico Commander')
        exit_app.triggered.connect(QtGui.qApp.quit)

        # Create file menu
        file_menu = menubar.addMenu('&File')
        new_menu = file_menu.addMenu('&New')
        new_menu.addAction(new_blank_file)
        new_menu.addAction(new_proj)
        new_menu.addAction(new_proj_file)
        new_menu.addAction(new_lib)
        file_menu.addAction(open_file)
        file_menu.addAction(import_proj)
        file_menu.addAction(save_file)
        file_menu.addAction(exit_app)

    def init_view(self):
        """ Initializes, wraps, and adds widgets to the main window """

        # Initialize the resource browser dock widget (left side)
        # BrowseWidget() defined in widgets/fbrowse.py
        self.work_path = 'C:/Users/ajans/Documents/workspace'
        self.resource_browser = BrowseWidget(
                    'C:/Users/ajans/Documents/workspace')
        resource_browser_wrap = QtGui.QDockWidget('Resource Browse', self)
        resource_browser_wrap.setWidget(self.resource_browser)

        # Initialize the workspace main widget (Central Widget)
        # Workspace() defined in widgets/fedit.py
        self.workspace = Workspace()
        workspace_wrap = QtGui.QDockWidget('Workspace', self)
        workspace_wrap.setWidget(self.workspace)

        # Set central widget and add dock widgets
        self.setCentralWidget(workspace_wrap)
        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, resource_browser_wrap)


if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    user_program = main_app()
    sys.exit(app.exec_())
