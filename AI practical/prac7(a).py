import random
from colorama import init, Fore

# program to suffle deck of cards

# Initialize colorama with autoreset
init(autoreset=True)

# Function to create a deck of cards
def create_deck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    return [f'{rank} of {suit}' for suit in suits for rank in ranks]

# Function to shuffle the deck
def shuffle_deck(deck):
    random.shuffle(deck)

# Function to print the deck of cards
def print_deck(deck):
    for card in deck:
        print(card)

if __name__ == "__main__":
    deck = create_deck()
    print(Fore.RED + "Original Deck:")
    print_deck(deck)
    
    shuffle_deck(deck)
    print(Fore.GREEN + "\nShuffled Deck:")
    print_deck(deck)
