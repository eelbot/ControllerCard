from PyQt4 import QtGui
import os


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
    # THIS CODE CAN BE SIMPLIFIED AND CLEANED UP
    # Get the file path from the file dialog
    file_path = QtGui.QFileDialog.getOpenFileName(
            parent, 'Open File', work_path)

    # Determine if the file is already in the editor
    for i in range(workspace.main_tabs.count()):
        if (workspace.main_tabs.widget(i).filePath == file_path and
                                        workspace.main_tabs.widget(i).filePath):
            QtGui.QMessageBox.question(parent, 'Message',
                                        "The file is already in the editor")
            workspace.main_tabs.setCurrentIndex(i)
            break

    # IF a file is selected and the editor is not empty:
    #   IF the file is not already in the editor
    #       ADD the file
    # ELSE IF - The file is selected
    #   Add the file
    if file_path and workspace.main_tabs.count():
        if workspace.main_tabs.currentWidget().filePath != file_path:
            workspace.add_file(file_path)
    elif file_path:
        workspace.add_file(file_path)


def import_proj():
    pass


def save_file(parent, work_path, workspace):
    # Get the current widget and extract the text from it
    current_tab = workspace.main_tabs.currentWidget()
    text = current_tab.text_editor.toPlainText()

    # Check if the file exists. If not, create one and write the text to it
    if os.path.isfile(current_tab.filePath):
        with open(current_tab.filePath, 'w') as f:
            f.write(text)
        f.close()
    else:
        new_save_path = QtGui.QFileDialog.getSaveFileName(
                parent, 'Open File', work_path)
        with open(new_save_path, 'w') as f:
            f.write(text)
        f.close()
        i = workspace.main_tabs.currentIndex()
        workspace.main_tabs.removeTab(i)
############################################################OPENS IN WRONG TAB INDEX
        workspace.add_file(new_save_path)


def save_as_file(parent, workspace):
    pass
