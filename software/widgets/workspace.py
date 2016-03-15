from PyQt4 import QtGui
from widgets.fedit import TextEditor


class Workspace(QtGui.QWidget):
    """ The main container widget which allows editing and viewing of files,
        status monitoring, and data visualisation. This widget can contain
        text and visual based file editing, visual and text based data
        review, and is displayed in a tab format.

        Widget is initialized with a single blank file
    """

    def add_file(self, file_path):

        """ Adds a file in the workspace, and allows editing via the drag
            and drop or text based editing windows

            file_path: The path to the file, with the extension
        """

        # Extract the extension and title from the file_path
        extension = file_path.split('.', 1)[-1]
        name = file_path.split('/')[-1]

        # Open the appropriate editor based on file extension
        if extension in ('txt', 'py', 'upl'):
            added_file = TextEditor(name, extension, file_path)
        else:
            added_file = TextEditor(name)

        # Don't replicate the default name for a new, blank file
        if "untitled" in name:
            added_file.fileName += ' ' + str(self.num_of_untitled)
            self.num_of_untitled += 1

        # Add as a tab
        self.main_tabs.addTab(added_file, added_file.fileName)
        self.main_tabs.setCurrentIndex(self.main_tabs.count() - 1)

    def __init__(self):
        super(Workspace, self).__init__()

        # One of the only core components of the workspace itself
        # are the tabs along the top, defined below
        self.main_tabs = QtGui.QTabWidget()
        self.main_tabs.setTabsClosable(True)
        self.main_tabs.tabCloseRequested.connect(self.main_tabs.removeTab)
        self.main_tabs.setMovable(True)

        # Set up initial tab as "untitled" and unsaved
        initial_file = TextEditor('untitled')
        self.main_tabs.addTab(initial_file, initial_file.fileName)

        # Keep track of the "untitled" files
        self.num_of_untitled = 1

        # The layout in this widget is incredibly simple: a single window
        layout = QtGui.QGridLayout()
        layout.addWidget(self.main_tabs)
        self.setLayout(layout)

        self.show()
