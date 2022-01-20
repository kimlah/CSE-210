from game.die import Die


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        dice (List[Die]): A list of Die instances.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        # create dice instance where die are added after being rolled & points
        self.dice = []
        # boolean for if the game is still being played
        self.is_playing = True
        # score at the beginning of each round
        self.score = 0
        # score as each round is played until no 1 or 5 is rolled
        self.total_score = 0

        # create 5 die from/in die.py (so iterate through die.py 5 times)
        for i in range(5):
            die = Die()
            self.dice.append(die)

    # game loop invokes 3 other classes in director class
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Ask the user if they want to roll.

        Args:
            self (Director): An instance of Director.
        """
        roll_dice = input("Roll dice? [y/n] ")
        self.is_playing = (roll_dice == "y")
       
    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        # if play is not continuing then return
        if not self.is_playing:
            return 

        # if play is continuing then loop through list of die in Dice, rolling each die
        for i in range(len(self.dice)):
            die = self.dice[i]
            die.roll()
            self.score += die.points 
            self.total_score += self.score

    def do_outputs(self):
        """Displays the dice and the score. Also asks the player if they want to roll again. 

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return
        
        values = ""
        self.score = 0
        for i in range(len(self.dice)):
            die = self.dice[i]
            values += f"{die.value} "

        print(f"You rolled: {values}")
        print(f"Your score for this round is: {self.score}\n")
        print(f"Your total score is: {self.total_score}\n")
        self.is_playing = (self.score > 0)