import random
import higher_lower_game_assets

print(higher_lower_game_assets.logo)

celebrity = higher_lower_game_assets.data

player1_score = 0
player2_score = 0
player1_text = ''
player2_text = ''
score = 0
game_over = False
winner = ""


def game():

    def first_a():
        player1 = random.choice(higher_lower_game_assets.data)
        player1_name = player1['name']
        player1_count = player1['follower_count']
        player1_descr = player1['description']
        player1_country = player1['country']
        print(f"Compare A: {player1_name}, a {player1_descr}, from {player1_country}.")
        global player1_text
        player1_text = str(f"Compare A: {player1_name}, a {player1_descr}, from {player1_country}.")
        global player1_score
        player1_score += player1_count

    def second_b():
        player2 = random.choice(higher_lower_game_assets.data)
        player2_name = player2['name']
        player2_count = player2['follower_count']
        player2_descr = player2['description']
        player2_country = player2['country']
        print(f"Compare B: {player2_name}, a {player2_descr}, from {player2_country}.")
        global player2_text
        player2_text = str(f"Compare B: {player2_name}, a {player2_descr}, from {player2_country}.")
        global player2_score
        player2_score += player2_count

    def compare():
        global winner
        if player1_score > player2_score:
            winner = "A"
        elif player1_score < player2_score:
            winner = "B"

        player_input = input("Who has more followers A or B : ")

        if winner == player_input:
            global score
            score += 1
            print(f"You're right. Current score: {score}")
        else:
            print(f"\nSorry, that's wrong. Final score: {score}")
            global game_over
            game_over = True
            return game_over and winner and score

    while not game_over:
        if score == 0:
            first_a()
            print(higher_lower_game_assets.vs)
            second_b()
        compare()
        if game_over == False and winner == "A":
            global player2_score
            player2_score = 0
            print(higher_lower_game_assets.logo)
            print(player1_text)
            print(higher_lower_game_assets.vs)
            second_b()
        elif game_over == False and winner == "B":
            global player1_score
            player1_score = 0
            print(higher_lower_game_assets.logo)
            print(player2_text)
            print(higher_lower_game_assets.vs)
            first_a()


game()
