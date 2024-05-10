from krita import *

# test function
def triggerMyPlugin():
    Krita.instance().action("python_scripter").trigger()
