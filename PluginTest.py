# figure out how to configure vs code to recognise krita import
from krita import *

# test function
def triggerMyPlugin():
    Krita.instance().action("python_scripter").trigger()
