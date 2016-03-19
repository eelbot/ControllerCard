from PyQt4 import QtGui
import os


def create_blank_file(workspace):
    # Add a blank, untitled file
    workspace.add_file("untitled")
    workspace.save_state_change(False)


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
    for i in range(workspace.count()):
        if (workspace.widget(i).filePath == file_path and
                                        workspace.widget(i).filePath):
            QtGui.QMessageBox.question(parent, 'Message',
                                        "The file is already in the editor")
            workspace.setCurrentIndex(i)
            break

    # IF a file is selected and the editor is not empty:
    #   IF the file is not already in the editor
    #       ADD the file
    # ELSE IF - The file is selected
    #   Add the file
    if file_path and workspace.count():
        if workspace.currentWidget().filePath != file_path:
            workspace.add_file(file_path)
    elif file_path:
        workspace.add_file(file_path)


def import_proj():
    pass


def save_file(parent, work_path, workspace):
    # Get the current widget and extract the text from it
    current_tab = workspace.currentWidget()
    text = current_tab.toPlainText()

    # Check if the file exists. If not, create one and write the text to it
    if os.path.isfile(current_tab.filePath):
        with open(current_tab.filePath, 'w') as f:
            f.write(text)
        f.close()
        workspace.save_state_change(True)
    else:
        new_save_path = QtGui.QFileDialog.getSaveFileName(
                parent, 'Open File', work_path)
        # Line below generates file not found error if dialog is closed
        try:
            with open(new_save_path, 'w') as f:
                f.write(text)
            f.close()
            i = workspace.currentIndex()
            workspace.removeTab(i)
            workspace.add_file(new_save_path, i)
            workspace.save_state_change(True)
        except FileNotFoundError:
            pass


def save_as(parent, work_path, workspace):
    current_tab = workspace.currentWidget()
    text = current_tab.toPlainText()

    new_save_path = QtGui.QFileDialog.getSaveFileName(
            parent, 'Open File', work_path)
    # Line below generates file not found error if dialog is closed
    try:
        with open(new_save_path, 'w') as f:
            f.write(text)
        f.close()
        i = workspace.currentIndex()
        workspace.removeTab(i)
        workspace.add_file(new_save_path, i)
        workspace.save_state_change(True)
    except FileNotFoundError:
        pass
