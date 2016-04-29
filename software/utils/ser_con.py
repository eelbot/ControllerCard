from PyQt4 import QtGui
import serial
import serial.tools.list_ports

BAUD_RATE = 9600
TIMEOUT = 5


def detect_and_connect():
    available_ports = list(serial.tools.list_ports.comports())
    print(available_ports)
