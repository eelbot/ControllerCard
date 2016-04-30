from PyQt4 import QtGui
import serial
import serial.tools.list_ports

BAUD_RATE = 9600
TIMEOUT = 0.5
CONNECTION_INFO = []


def detect_and_connect(master_app):
    available_ports = list(serial.tools.list_ports.comports())
    for port in available_ports:
        if "USB Serial Device" in port[1]:
            CONNECTION_INFO = port
    if CONNECTION_INFO == []:
        QtGui.QMessageBox.warning(master_app, "Connection", "Could not connect! Please connect a board and try again")

    ser = serial.Serial()
    ser.baudrate = BAUD_RATE
    ser.port = CONNECTION_INFO[0]
    ser.timeout = TIMEOUT
    ser.open()
    QtGui.QMessageBox.information(master_app, "Connection", "Connection successful!")
    ser.close()

def upload(master_app):
    available_ports = list(serial.tools.list_ports.comports())
    for port in available_ports:
        if "USB Serial Device" in port[1]:
            CONNECTION_INFO = port
    if CONNECTION_INFO == []:
        QtGui.QMessageBox.warning(master_app, "Connection", "Could not connect! Please connect a board and try again")

    upl_file_path = QtGui.QFileDialog.getOpenFileName(master_app.workspace, "File to Upload", master_app.work_path, "Upload (*.upl)")
    upl_file = open(upl_file_path, 'rb')

    ser = serial.Serial()
    ser.baudrate = BAUD_RATE
    ser.port = CONNECTION_INFO[0]
    ser.timeout = TIMEOUT
    ser.open()
    ser.write(upl_file.readline())

    response = ser.read(10).decode()
    if response == "conf":
        QtGui.QMessageBox.information(master_app, "Connection", "Upload Successful! Program will begin execution")

    ser.close()
