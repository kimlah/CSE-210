from game.casting.actor import Actor

# TODO: Implement the Artifact class here. Don't forget to inherit from Actor!
class Artifact(Actor):
    """A collection of Artifacts

    The responsibility of Artifact is to display a message when touched
    
    Attributes:
    _message
    """

    def __init__(self):
        super().__init__()
        self._message=""

    def get_message(self):
        """Get message for artifact
           Returns: 
           message string
        """
        return self._message

    def set_message(self, message):
        """updates message to chosen one
           Args:
           message: selected message string
        """
        self._message = message