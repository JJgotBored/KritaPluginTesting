# figure out how to configure vs code to recognise krita import
from krita import *
from PyQt5.QtWidgets import QWidget, QMessageBox

def showwin():
    QMessageBox.information(QWidget(), "WindowTest", "It works")

class PluginTest(Extension):
    def __init__(self, parent):
        #This is initialising the parent, always important wnen subclassing
        super(PluginTest, self).__init__(parent)

    def setup(self):
        pass

    def createActions(self, window):
        action = window.createAction("window_test_id", "Window Test", "tools/scripts")
        action.triggered.connect(showwin)

Krita.instance().addExtension(PluginTest(Krita.instance()))

# test function that opens scripter terminal within krita via the scrtipter using:
#   import PluginTest
#   PluginTest.triggerMyPlugin()
def triggerMyPlugin():
    Krita.instance().action("python_scripter").trigger()
