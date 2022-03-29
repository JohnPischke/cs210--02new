<<<<<<< Updated upstream
'''
Authors:
Logan Crossley
John Pischke
Seth Whetten

Description:
This is a director class that has card objects, Score,
and functions that run the game Hi/lo.
'''
=======
>>>>>>> Stashed changes

from game.card import Card
import random

class Director:

    def __init__(self):
        # Initialize attributes
        self.card_list = []
        self.is_playing = True
        self.total_score = 300
        self.last_card = 0
        self.guess = ''

    def start_game(self):
        # Set starting values
        for card_num in range(1, 14):
            new_card = Card()
            new_card.value = card_num
            self.card_list.append(new_card)

        self.last_card = self.draw_card()
        print(f'Your score is: {self.total_score}')

        # Start game loop
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
    # Asks for inputs
    def get_inputs (self):
        print(f'The card is: {self.last_card}')
        self.guess = input('Higher or lower? [h/l] ').lower()
        while self.guess not in ['h', 'l']:
            print('Invalid input: Please enter \'h\' or \'l\'')
            self.guess = input('Higher or lower? [h/l] ')
    # Updates different values 
    def do_updates (self):
        if not self.is_playing:
            return
        
        high = True if self.guess == 'h' else False
        
        new_card = self.draw_card()
        while new_card == self.last_card:
            new_card = self.draw_card()
        result = self.compare_cards(new_card)

        self.total_score += 100 if result == high else -75
        if self.total_score < 1:
            self.total_score = 0
        self.last_card = new_card
    # Displays the results of the inputs
    def do_outputs (self):
        if not self.is_playing:
            return
        print("\n")
        print(f'Next card was: {self.last_card}')
        print(f'Your score is: {self.total_score}')

        if self.total_score > 0:
            self.is_playing = True if input('Play again? [y/n] ').lower() == 'y' else False
            print("\n")
        else:
            self.is_playing = False
            print("\nYou Lose!\nThanks for playing!")

    # Compares the new card and last card
    def compare_cards (self, new_card):
        return self.last_card < new_card
    # Draws a card
    def draw_card (self):
        return self.card_list[random.randint(0, 12)].value
