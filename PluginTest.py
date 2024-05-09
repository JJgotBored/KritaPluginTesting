from krita import *

def triggerMyPlugin():
    Krita.instance().action("python_scripter").trigger()
