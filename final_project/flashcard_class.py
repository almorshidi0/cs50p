class Flashcard:
    def __init__(self, front_text="Type the front_text of the card here",
                 back_text="Type the back_text of the card here",
                 card_strength=1, review_interval=1):
        """
        Initialize a new flashcard.

        Parameters:
        - front_text (str): The front_text on the flashcard.
        - back_text (str): The back_text of the flashcard.
        - card_strength (int): The card_strength of the flashcard for spaced repetition.
        - review_interval (int): The review review_interval for spaced repetition.

        Returns:
        None
        """
        self.front_text   = front_text
        self.back_text     = back_text
        self.card_strength   = card_strength  # Card card_strength for spaced repitition
        self.review_interval   = review_interval # Review review_interval for spaced repitition
        
    def __str__(self):
        """
        Return a formatted string representation of the flashcard.

        Returns:
        str: Formatted string representation of the flashcard.
        """
        return f"Front: {self.front_text}\nBack: {self.back_text}"
    
    # Property and setter methods for encapsulation
    
    @property
    def front_text(self):
        return self._front_text
    
    @front_text.setter
    def front_text(self, front_text):
        self._front_text = front_text
    
    @property
    def back_text(self):
        return self._back_text
    
    @back_text.setter
    def back_text(self, back_text):
        self._back_text = back_text
    
    @property
    def card_strength(self):
        return self._card_strength
    
    @card_strength.setter
    def card_strength(self, card_strength):
        self._card_strength = card_strength
        
    @property
    def review_interval(self):
        return self._review_interval
    
    @review_interval.setter
    def review_interval(self, review_interval):
        self._review_interval = review_interval
