import random
cards = ["Diamonds", "Clubs", "Spades", "Hearts"]
ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jacks", "Queen", "Kings", "Ace",]

def pick_a_card():
    card = random.choices(cards)
    rank = random.choices(ranks)
    return(f"The {rank} of {card} ")

print(pick_a_card())
