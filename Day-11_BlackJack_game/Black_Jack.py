import random
import Black_Jack_Logo

print(Black_Jack_Logo.logo)
print("Welcome to a game of Black Jack!")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_hand = []
cpu_hand = []


def deal():
    user_hand.append(random.choice(cards))
    cpu_hand.append(random.choice(cards))
    user_score = sum(user_hand)
    cpu_score = sum(cpu_hand)
    print(f"The user has {len(user_hand)} card/s and {user_score} points!")
    print(f"The dealer has {len(cpu_hand)} card/s and {cpu_score} points!")
    if user_score == 21:
        print("You win the round with a Black Jack!")
    elif cpu_score == 21:
        print("You loose the dealer got a Black Jack!")
    elif user_score == 21 and cpu_score == 21:
        print("It's a draw, you both get Black Jack!")
    elif user_score > 21:
        if 11 in user_hand:
            user_score -= 10
            if user_score > 21:
                print(f"You have {user_score} and went over 21 and loose!")
        else:
            print(f"You have {user_score} and went over 21 and loose!")
    elif cpu_score > 21:
        if 11 in cpu_hand:
            cpu_score -= 10
            if user_score > 21:
                print(f"Dealer has {cpu_score} went over 21 and you win!")
        else:
            print(f"Dealer has {cpu_score} went over 21 and you win!")
    else:
        next_round = input("Would you like another card?y/n: ")
        if next_round == "y":
            deal()
        else:
            if cpu_score <= 17:
                cpu_hand.append(random.choice(cards))
                cpu_score = sum(cpu_hand)
                if cpu_score == 21:
                    print("You loose the dealer got a Black Jack!")
                elif cpu_score > 21:
                    if 11 in cpu_hand:
                        cpu_score -= 10
                        if user_score > 21:
                            print(f"Dealer has {cpu_score} went over 21 and you win!")
                        else:
                            print(f"Dealer has {cpu_score} went over 21 and you win!")
        if user_score == 21:
            print("You win the round with a Black Jack!")
        elif cpu_score == 21:
            print("You loose the dealer got a Black Jack!")
        elif user_score == 21 and cpu_score == 21:
            print("It's a draw, you both get Black Jack!")
        elif user_score > 21:
            if 11 in user_hand:
                user_score -= 10
                if user_score > 21:
                    print(f"You have {user_score} and went over 21 and loose!")
            else:
                print(f"You have {user_score} and went over 21 and loose!")
        elif cpu_score > 21:
            if 11 in cpu_hand:
                cpu_score -= 10
                if user_score > 21:
                    print(f"Dealer has {cpu_score} went over 21 and you win!")
            else:
                print(f"Dealer has {cpu_score} went over 21 and you win!")


deal()
