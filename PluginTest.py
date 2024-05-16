# figure out how to configure vs code to recognise krita import
from krita import *

# test function that opens scripter terminal within krita 
def triggerMyPlugin():
    Krita.instance().action("python_scripter").trigger()
