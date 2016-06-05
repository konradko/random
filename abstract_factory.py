class WinButton(object):

    def paint(self):
        print "Paint Win button"


class WinFactory(object):
    
    def create_button(self):
        return WinButton()


class OSXButton(object):

    def paint(self):
        print "Paint OSX button"


class OSXFactory(object):
    
    def create_button(self):
        return OSXButton()


class Application(object):
    
    def __init__(self, gui_factory):
        button = gui_factory.create_button()
        button.paint()


system = "OSX"

if system == "OSX":
    factory = OSXFactory()
else:
    factory = WinFactory()

Application(factory)
