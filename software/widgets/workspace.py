from PyQt4 import QtGui
from widgets.fedit import TextEditor


class Workspace(QtGui.QWidget):
    """ The main container widget which allows editing and viewing of files,
        status monitoring, and data visualisation. This widget can contain
        text and visual based file editing, visual and text based data
        review, and is displayed in a tab format.

        Widget is initialized with a single blank file
    """

    def add_file(self, file_path, index=0):

        """ Adds a file in the workspace, and allows editing via the drag
            and drop or text based editing windows

            file_path: The path to the file, with the extension
            index: The location of the tab to be inserted. If index
                   is equal to 0, the tab is added onto the end.
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

        # Add as a tab, at a certain index if indicated
        if index:
            self.main_tabs.insertTab(index, added_file, added_file.fileName)
            self.main_tabs.setCurrentIndex(index)
        else:
            self.main_tabs.addTab(added_file, added_file.fileName)
            self.main_tabs.setCurrentIndex(self.main_tabs.count() - 1)

        # Add a checker and updater to check for changes (saved vs. unsaved)
        added_file.text_editor.textChanged.connect(lambda: self.save_state_change(False))

    def save_state_change(self, isSaved):
        """ Adds or removes an asterisk from the current tab when text changes
            or the file is saved to denote to the user if their changes are
            currently saved.

            isSaved: Whether the file has become saved (True) or unsaved (False)
        """
        i = self.main_tabs.currentIndex()
        current_name = self.main_tabs.tabText(i)
        if isSaved and '*' in current_name:
            self.main_tabs.setTabText(i, current_name[:-1])
            self.main_tabs.currentWidget().isSaved = True
        else:
            if '*' not in current_name:
                self.main_tabs.setTabText(i, current_name + '*')
                self.main_tabs.currentWidget().isSaved = False

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
