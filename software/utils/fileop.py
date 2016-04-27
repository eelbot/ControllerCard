from PyQt4 import QtGui
from widgets.editor import TextEditor, DragDropEditor
from widgets.entity import tile, arrow
import os, datetime


def create_blank_file(workspace):
    # Ask the user what kind of file they would like to create
    items = ["Hex-Based", "Drag and Drop"]
    item = QtGui.QInputDialog.getItem(
            workspace, 'Select File Type', "Format", items, 0, False)

    # Add a blank, untitled file
    if "Hex-Based" in item:
        workspace.add_file("untitled.upl")
    elif "Drag and Drop" in item:
        workspace.add_file("untitled.pro")
    else:
        pass

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
            QtGui.QMessageBox.question(
                    parent, 'Message', "The file is already in the editor")
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
    # Get the current widget
    current_tab = workspace.currentWidget()

    if type(current_tab) is TextEditor:
        # Get the text of the text editor into a variable
        text = current_tab.toPlainText()

        # Check if the file exists. If not, create one and write the text to it
        if os.path.isfile(current_tab.filePath):
            with open(current_tab.filePath, 'w') as f:
                f.write(text)
            f.close()
            workspace.save_state_change(True)
        else:
            new_save_path = QtGui.QFileDialog.getSaveFileName(
                    parent, 'Save File', work_path +"/"+ current_tab.fileName, "Text Files (*.txt *.py *.upl)")
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

    elif type(current_tab) is DragDropEditor:
        arrows = current_tab.findChildren(arrow)
        tiles = current_tab.findChildren(tile)
        save_text = str(datetime.datetime.now())

        # First, save the imported libraries
        already_saved_libs = []
        for v in current_tab.libs:
            if v['LibraryPath'] not in already_saved_libs:
                save_text += "\nL"
                save_text += " " + v['LibraryPath']
                already_saved_libs.append(v['LibraryPath'])

        # Second, aesthetics
        for v in tiles:
            save_text += "\n#"
            save_text += " " + str(v.ref)
            save_text += " " + str(v.x())
            save_text += " " + str(v.y())
            save_text += " " + v.func_dict['FunctionReference']

        # Next, save the connections
        for v in arrows:
            save_text += "\n>"
            save_text += " " + str(int(v.inix))
            save_text += " " + str(int(v.iniy))
            save_text += " " + str(int(v.finx))
            save_text += " " + str(int(v.finy))
            save_text += " " + str(v.input)
            save_text += " " + str(v.output)
            save_text += " " + v.sel_in

        # Check if the file exists. If not, create one and write the text to it
        if os.path.isfile(current_tab.filePath):
            with open(current_tab.filePath, 'w') as f:
                f.write(save_text)
            f.close()
            workspace.save_state_change(True)
        else:
            new_save_path = QtGui.QFileDialog.getSaveFileName(
                    parent, 'Save File', work_path +"/"+ current_tab.fileName, "Text Files (*.pro)")
            # Line below generates file not found error if dialog is closed
            try:
                with open(new_save_path, 'w') as f:
                    f.write(save_text)
                f.close()
                i = workspace.currentIndex()
                workspace.removeTab(i)
                workspace.add_file(new_save_path, i)
                workspace.save_state_change(True)
            except FileNotFoundError:
                pass



def save_as(parent, work_path, workspace):
    current_tab = workspace.currentWidget()

    if type(current_tab) is TextEditor:
        # Get the text of the text editor into a variable
        text = current_tab.toPlainText()

        new_save_path = QtGui.QFileDialog.getSaveFileName(
                parent, 'Save File', work_path +"/"+ current_tab.fileName, "Text Files (*.txt *.py *.upl)")
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

    elif type(current_tab) is DragDropEditor:
        arrows = current_tab.findChildren(arrow)
        tiles = current_tab.findChildren(tile)
        save_text = str(datetime.datetime.now())

        # First, aesthetics
        for v in tiles:
            save_text += "\n#"
            save_text += " " + str(v.ref)
            save_text += " " + str(v.x())
            save_text += " " + str(v.y())
            save_text += " " + v.func_dict['FunctionReference']

        # Next, save the connections
        for v in arrows:
            save_text += "\n>"
            save_text += " " + str(int(v.inix))
            save_text += " " + str(int(v.iniy))
            save_text += " " + str(int(v.finx))
            save_text += " " + str(int(v.finy))
            save_text += " " + str(v.input)
            save_text += " " + str(v.output)

        new_save_path = QtGui.QFileDialog.getSaveFileName(
                parent, 'Save File', work_path +"/"+ current_tab.fileName, "Text Files (*.pro)")
        # Line below generates file not found error if dialog is closed
        try:
            with open(new_save_path, 'w') as f:
                f.write(save_text)
            f.close()
            i = workspace.currentIndex()
            workspace.removeTab(i)
            workspace.add_file(new_save_path, i)
            workspace.save_state_change(True)
        except FileNotFoundError:
            pass

def compile_program(parent, work_path, workspace):
    f = workspace.currentWidget()
    if f.isSaved == False:
        save_now = QtGui.QMessageBox.question(parent, 'Save Before Compile',
                "You must save before compiling. Save now?", QtGui.QMessageBox.Yes |
                QtGui.QMessageBox.No, QtGui.QMessageBox.No)
        if save_now == QtGui.QMessageBox.Yes:
            save_file(parent, work_path, workspace)
        else:
            return
    # Put logic below for compile button
    input_file = open(f.filePath, 'r')
    arrows = f.findChildren(arrow)
