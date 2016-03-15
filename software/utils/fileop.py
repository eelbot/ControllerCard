from PyQt4 import QtGui


def create_blank_file(workspace):
    # Add a blank, untitled file
    workspace.add_file("untitled")


def create_proj():
    pass


def create_proj_file():
    pass


def create_lib():
    pass


def open_file(parent, work_path, workspace):
    # Get the file path from the file dialog
    file_path = QtGui.QFileDialog.getOpenFileName(
            parent, 'Open File', work_path)

    # Determine if the file is already in the editor
    for i in range(workspace.main_tabs.count()):
        if workspace.main_tabs.widget(i).filePath == file_path:
            QtGui.QMessageBox.question(parent, 'Message',
                                       "The file is already in the editor")
            workspace.main_tabs.setCurrentIndex(i)
            break
    # Make a new editor window if the file is selected and not in the editor
    if file_path and workspace.main_tabs.currentWidget().filePath != file_path:
        workspace.add_file(file_path)


def import_proj():
    pass


def save_file():
    pass


def save_as_file():
    pass
