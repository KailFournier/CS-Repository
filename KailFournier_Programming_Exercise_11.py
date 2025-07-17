import random

class Deck:
    def __init__(self, size):
        self.card_list = [i for i in range(size)]
        random.shuffle(self.card_list)
        self.current_card = 0
        self.size = size
        self.cards_in_play_list = []
        self.discards_list = []

    def deal(self):
        if self.size - self.current_card < 1:
            random.shuffle(self.card_list)
            self.current_card = 0
            print('Reshuffling...!!!')
        self.current_card += 1
        card = self.card_list[self.current_card - 1]
        self.cards_in_play_list.append(card)
        return card

    def new_hand(self):
        self.discards_list += self.cards_in_play_list
        self.cards_in_play_list.clear()


# Define suits and ranks for a standard poker deck
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']


def card_to_string(card):
    """Convert card number to rank and suit (e.g., card 0 -> '2 of Hearts')."""
    rank = ranks[card % 13]
    suit = suits[card // 13]
    return f"{rank} of {suit}"


def play_poker():
    # Create a deck with 52 cards (standard poker deck)
    deck = Deck(52)

    # Deal initial 5-card hand
    hand = [deck.deal() for _ in range(5)]
    print("\nYour initial hand:")
    for i, card in enumerate(hand, 1):
        print(f"Card {i}: {card_to_string(card)}")

    # Prompt user for cards to replace (1-5, comma-separated)
    while True:
        try:
            input_str = input("\nEnter the numbers (1-5) of cards to replace (e.g., '1,3,5' or 'none' to keep all): ")
            if input_str.lower() == 'none':
                replace_indices = []
                break
            # Parse input into list of indices (0-based)
            replace_indices = [int(x.strip()) - 1 for x in input_str.split(',')]
            # Validate indices
            if all(0 <= i < 5 for i in replace_indices) and len(replace_indices) == len(set(replace_indices)):
                break
            else:
                print("Invalid input! Please enter numbers between 1 and 5, separated by commas, with no duplicates.")
        except ValueError:
            print("Invalid input! Please enter numbers separated by commas or 'none'.")

    # Replace selected cards
    for i in replace_indices:
        hand[i] = deck.deal()

    # Print final hand
    print("\nYour final hand after draw:")
    for i, card in enumerate(hand, 1):
        print(f"Card {i}: {card_to_string(card)}")


# Run the game
if __name__ == "__main__":
    print("Welcome to 5-Card Draw Poker!")
    play_poker()