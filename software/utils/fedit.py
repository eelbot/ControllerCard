from PyQt4 import QtGui, QtCore
from widgets.editor import TextEditor, DragDropEditor
from widgets.tile import tile


def add_tile(workspace):
    """ Adds a tile to the current file being edited
        Parameters
            workspace: The current workspace widget

    """
    new_tile = tile(workspace.currentWidget(), workspace.currentWidget().numOfChildren, 30, 30)
    new_tile.drawConnection.connect(workspace.currentWidget().drawArrow)
    workspace.currentWidget().numOfChildren += 1
    workspace.update()
