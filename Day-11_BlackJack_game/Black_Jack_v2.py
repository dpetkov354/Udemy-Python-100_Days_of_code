import random
import Black_Jack_Logo


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, cpu_score):
    if user_score == cpu_score:
        return "Draw!"
    elif cpu_score == 0:
        return "You lose!"
    elif user_score == 0:
        return "You win!"
    elif user_score > 21:
        return "You lose!"
    elif cpu_score > 21:
        return "You win!"
    elif user_score > cpu_score:
        return "You lose!"
    else:
        return "You lose"


def game():
    print(Black_Jack_Logo.logo)
    print("Welcome to a game of Black Jack!")
    user_hand = []
    cpu_hand = []
    is_game_over = False

    for _ in range(2):
        user_hand.append(deal_card())
        cpu_hand.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_hand)
        cpu_score = calculate_score(cpu_hand)
        print(f"User cards: {user_hand} and a total score of {user_score}.")
        print(f"Dealer's first card: {cpu_hand[0]}")

        if user_score == 0 or cpu_score == 0 or user_score > 21:
            is_game_over = True
        else:
            next_round = input("Would you like another card?y/n: ")
            if next_round == "y":
                user_hand.append(deal_card())
            else:
                is_game_over = True

    while cpu_score != 0 and cpu_score < 17:
        cpu_hand.append(deal_card())
        cpu_score = calculate_score(cpu_hand)

    print(f"Your final hand is {user_hand} and your score is {user_score}.")
    print(f"The dealer's hand is {cpu_hand} and his score is {cpu_score}.")
    print(compare(user_score, cpu_score))


while input("Would you like to play a game?y/n: ") == "y":
    game()
