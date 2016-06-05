class State(object):

    def __init__(self, name):
        self.name = name

    def apply(self):
        return self.name


class Context(object):

    def __init__(self, state):
        self.state = state

    def set_state(self, state):
        self.state = state

    def get_state(self):
        return self.state.name

start = State("start")
stop = State("stop")

context = Context(start)
print context.get_state()
context.set_state(stop)
print context.get_state()
