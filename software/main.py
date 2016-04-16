import sys
from PyQt4 import QtGui, QtCore
from widgets.resources import BrowseWidget
from widgets.manager import WorkspaceManager
from widgets.workspace import Workspace
from utils import fileop, ser_con, fedit


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
        new_blank_file = QtGui.QAction(
                QtGui.QIcon('img/file_new.png'), 'New Empty File', self)
        new_blank_file.setIconVisibleInMenu(False)
        new_blank_file.setShortcut('Ctrl+Shift+N')
        new_blank_file.setStatusTip('Create a new blank file')
        new_blank_file.triggered.connect(
                lambda: fileop.create_blank_file(self.workspace))

        # New Project Menu Option
        new_proj = QtGui.QAction('Create New Project', self)
        new_proj.setIconVisibleInMenu(False)
        new_proj.setStatusTip('Create a new project')
        new_proj.triggered.connect(fileop.create_proj)

        # New Project File Menu Option
        new_proj_file = QtGui.QAction(
                QtGui.QIcon('img/file_proj_new.png'), 'New Project File', self)
        new_proj_file.setIconVisibleInMenu(False)
        new_proj_file.setStatusTip('Create a new application file')
        new_proj_file.triggered.connect(fileop.create_proj_file)

        # New Library Menu Option
        new_lib = QtGui.QAction('New Library', self)
        new_lib.setIconVisibleInMenu(False)
        new_lib.setStatusTip('Create a new library')
        new_lib.triggered.connect(fileop.create_lib)

        # Open File Menu Option
        open_file = QtGui.QAction(QtGui.QIcon('img/file_open.png'),
                                  'Open File', self)
        open_file.setIconVisibleInMenu(False)
        open_file.setShortcut('Ctrl+O')
        open_file.setStatusTip('Open a file')
        open_file.triggered.connect(
                lambda: fileop.open_file(self, self.work_path, self.workspace))

        # Import Project Menu Option
        import_proj = QtGui.QAction(QtGui.QIcon('import_proj.png'),
                                    'Import Project', self)
        import_proj.setIconVisibleInMenu(False)
        import_proj.setStatusTip('Import an existing project')
        import_proj.triggered.connect(fileop.import_proj)

        # Save File Menu Option
        save_file = QtGui.QAction(QtGui.QIcon('img/file_save.png'),
                                  'Save', self)
        save_file.setIconVisibleInMenu(False)
        save_file.setShortcut('Ctrl+S')
        save_file.setStatusTip('Save current file')
        save_file.triggered.connect(
                lambda: fileop.save_file(self, self.work_path, self.workspace))

        # Save As File Menu Option
        save_as = QtGui.QAction('Save As', self)
        save_as.setStatusTip('Save current file')
        save_as.triggered.connect(
                lambda: fileop.save_as(self, self.work_path, self.workspace))

        # Exit Main app Menu Option
        exit_app = QtGui.QAction(QtGui.QIcon('exit.png'), 'Exit', self)
        exit_app.setIconVisibleInMenu(False)
        exit_app.setShortcut('Ctrl+Q')
        exit_app.setStatusTip('Exit Pico Commander')
        exit_app.triggered.connect(QtGui.qApp.quit)

        # Basic Connect option
        board_connect = QtGui.QAction(
                QtGui.QIcon('img/connect.png'), 'Detect and Connect', self)
        board_connect.setIconVisibleInMenu(False)
        board_connect.setShortcut('Ctrl+Shift+C')
        board_connect.setStatusTip('Establish a connection to a board')
        board_connect.triggered.connect(
                lambda: ser_con.detect_and_connect())

        # Add a tile to the drag and drop editor
        add_tile = QtGui.QAction(
                QtGui.QIcon('img/add_tile.png'), 'Add Tile', self)
        add_tile.setIconVisibleInMenu(False)
        add_tile.setShortcut('Ctrl+Shift+A')
        add_tile.setStatusTip('Add a tile to the current editor')
        add_tile.triggered.connect(
                lambda: fedit.add_tile(self.workspace))

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
        file_menu.addAction(save_as)
        file_menu.addAction(exit_app)

        connect_menu = menubar.addMenu('&Connect')
        connect_menu.addAction(board_connect)

        editor_menu = menubar.addMenu('&Editor')
        editor_menu.addAction(add_tile)

        # Create toolbars
        icon_size = QtCore.QSize(20, 20)
        file_tool_bar = self.addToolBar('File')
        file_tool_bar.setIconSize(icon_size)
        file_tool_bar.addAction(new_blank_file)
        file_tool_bar.addAction(new_proj_file)
        file_tool_bar.addAction(open_file)
        file_tool_bar.addAction(save_file)

        connect_tool_bar = self.addToolBar('Connect')
        connect_tool_bar.setIconSize(icon_size)
        connect_tool_bar.addAction(board_connect)

        editor_tool_bar = self.addToolBar('Editor')
        editor_tool_bar.setIconSize(icon_size)
        editor_tool_bar.addAction(add_tile)

    def update_workspace(self, new_path):
        """ Changes the current workspace path variable and file structure
            in the file_browser dock widget
        """

        self.resource_browser.file_browser.change_path(new_path)
        self.work_path = new_path

    def init_view(self):
        """ Initializes, wraps, and adds widgets to the main window """

        # Initialize the workspace main widget (Central Widget)
        # Workspace() defined in widgets/fedit.py
        self.workspace = Workspace()
        workspace_wrap = QtGui.QDockWidget('Workspace', self)
        workspace_wrap.setWidget(self.workspace)

        # Initialize the resource browser dock widget (left side)
        # BrowseWidget() defined in widgets/resources.py
        self.work_path = 'C:/Users/ajans/Documents/workspace'
        self.resource_browser = BrowseWidget(self.work_path)
        self.resource_browser.file_browser.openWork.connect(
                    self.workspace.add_file)
        resource_browser_wrap = QtGui.QDockWidget('Resource Browse', self)
        resource_browser_wrap.setWidget(self.resource_browser)

        # Initialize the workspace management widget
        # WorkspaceManager() is defined in widgets/manager.py
        self.work_manager = WorkspaceManager()
        self.work_manager.newPath.connect(self.update_workspace)
        workspace_change = QtGui.QDockWidget('Manage Workspace', self)
        workspace_change.setWidget(self.work_manager)

        # Set central widget and add dock widgets
        self.setCentralWidget(workspace_wrap)
        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, workspace_change)
        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, resource_browser_wrap)


if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    user_program = main_app()
    sys.exit(app.exec_())
