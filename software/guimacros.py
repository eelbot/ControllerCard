from PyQt4 import QtGui


def create_menu_item(name, masterapp, action, status_tip=None,
                     shortcut=None, icon_path=None, enabled=True):

    """Create an QAction to be added to a menu

    Parameters
    name:       String containing name of the menu item
    masterapp:  Parent application. New menu item will be attached to masterapp
    action:     Function that is called upon menu item selection
    shortcut:   String containing keyboard shortcut for action
    icon_path:  String containg path for icon
    status_tip: String containing status tip (for "on hover")
    enabled:    Whether the menu option is available by default

    Returns
    menu_action: A QAction ready to be added to a menu
    """

    if isinstance(icon_path, str):
        menu_action = QtGui.QAction(QtGui.QIcon(icon_path), name, masterapp)
    else:
        menu_action = QtGui.QAction(name, masterapp)

    if isinstance(shortcut, str):
        menu_action.setShortcut(shortcut)
    if isinstance(status_tip, str):
        menu_action.setStatusTip(status_tip)

    menu_action.triggered.connect(action)

    return menu_action
