class State:
    """
    Klasa przechowująca stan aplikacji, który decyduje o zakończeniu działania lub kontynuowaniu.
    """
    def __init__(self, should_exit):
        """
        Konstruktor
        :param should_exit: wartość inicjująca pole should_exit.
        """
        self.should_exit = should_exit

    def change_state(self):
        """
        Metoda zmienia stan aplikacji.
        """
        self.should_exit = not self.should_exit
