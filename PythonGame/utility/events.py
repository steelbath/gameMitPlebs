
from types import FunctionType as Function


class EVENT_TYPE:
    """Contains list of events that affect wide array objects across the program.
    Add more if needed."""
    PLAYER_SPAWN = 1
    PLAYER_DIE = 2


class Event():
    """Static event manager that uses bit more memory to avoid polling events every
    single frame"""

    # Dictionary of sets, use sets because they are faster when removing data
    events = dict()

    @classmethod
    def listen(event: EVENT_TYPE, callable: Function):
        """Add function to events dict, which will be called when the event is
        triggered"""
        pass

    @classmethod
    def trigger(event: EVENT_TYPE, *args, **kwargs):
        """Triggers event and calls all the stored functions with args and kwargs"""
        pass

    @classmethod
    def remove(event: EVENT_TYPE, callable: Function):
        """Removes given function from listened events"""
        pass

    @classmethod
    def remove_all(event: EVENT_TYPE):
        """Clears all listened events of specific type"""
        pass
