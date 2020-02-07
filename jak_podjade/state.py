class State:
    def __init__(self, should_exit):
        self.should_exit = should_exit

    def change_state(self):
        self.should_exit = not self.should_exit
