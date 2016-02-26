import sys
from PyQt4 import QtGui
from widgets.fedit import TextEditor


class Workspace(QtGui.QWidget):
    """ The main container widget which allows editing and viewing of files,
        status monitoring, and data visualisation. This widget can contain
        text and visual based file editing, visual and text based data
        review, and is displayed in a tab format.

        Widget is initialized with a single blank file
    """

    def __init__(self):

        super(Workspace, self).__init__()

        # One of the only core components of the workspace itself
        # are the tabs along the top, defined below
        main_tabs = QtGui.QTabWidget()
        initial_file = TextEditor('untitled')
        main_tabs.addTab(initial_file, initial_file.fileName)

        # The layout in this widget is incredibly simple: a single window
        layout = QtGui.QGridLayout()
        layout.addWidget(main_tabs)
        self.setLayout(layout)

        self.show()
