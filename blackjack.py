import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def first_deal(x):
    for i in range(0, 2):
        x.append(random.choice(cards))


def sum_of_list(numbered_list):
    total = 0
    for i in numbered_list:
        total += i
    return total


def total_score(cards):
    return sum_of_list(cards)


def calculate_score(p_cards, d_cards):
    p_total = total_score(p_cards)
    d_total = total_score(d_cards)

    if d_total == 21:
        print("Blackjack! You lose.")
        return True
    elif p_total == 21:
        print("Blackjack! You win!")
        return True
    elif p_total > 21:
        print("Bust! You lose.")
        return True
    elif d_total > 21:
        print("Dealer bust! You win.")
        return True

    return False


def play_blackjack():
    print(logo)
    player = []
    dealer = []

    first_deal(player)
    first_deal(dealer)

    while True:
        print(f"Your cards: {player}, current score: {total_score(player)}")
        print(f"Dealer's first card: {dealer[0]}")

        if calculate_score(player, dealer):
            break

        if input("Type 'y' to get another card, 'n' to pass: ").lower() == "y":
            player.append(random.choice(cards))
            if total_score(player) > 21 and 11 in player:
                player.remove(11)
                player.append(1)
        else:
            while total_score(dealer) < 17:
                dealer.append(random.choice(cards))
                print(f"Dealer's cards: {dealer}, current score: {total_score(dealer)}")

            if calculate_score(player, dealer):
                break

            if total_score(player) > total_score(dealer):
                print("You win!")
            elif total_score(player) < total_score(dealer):
                print("You lose.")
            else:
                print("Draw.")

            if input("Type 'y' to play again, 'n' to quit: ").lower() == "y":
                player.clear()
                dealer.clear()
                first_deal(player)
                first_deal(dealer)
            else:
                break

play_blackjack()


#below is the first try

#import random
#
# logo = """
# .------.            _     _            _    _            _
# |A_  _ |.          | |   | |          | |  (_)          | |
# |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
# | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
# |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   <
# `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
#       |  \/ K|                            _/ |
#       `------'                           |__/
# """
#
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#
#
# def first_deal(x):
#     for i in range(0, 2):
#         x.append(random.choice(cards))
#
#
# def sum_of_list(numbered_list):
#     sum = 0
#     for i in numbered_list:
#         sum += i
#     return sum
#
#
# def total_score(cards):
#     return sum_of_list(cards)
#
#
# def calculate_score(p_cards, d_cards):
#     if total_score(d_cards) == 21:
#         print("BlackJack YOU LOSE")
#         exit()
#     elif total_score(p_cards) == 21:
#         print("BlackJack YOU WIN")
#         exit()
#     elif total_score(p_cards) > 21:
#         print("this is too much, you lose")
#         exit()
#     elif total_score(d_cards) > 21:
#         print("you win")
#         exit()
#     elif abs(21 - total_score(p_cards)) == abs(21 - total_score(d_cards)):
#         print("you draw")
#         exit()
#     elif abs(21 - total_score(p_cards)) < abs(21 - total_score(d_cards)):
#         print("you win")
#         exit()
#     elif abs(21 - total_score(p_cards)) > abs(21 - total_score(d_cards)):
#         print("you lose")
#         exit()
#
#
# def play_blackjack():
#     player = []
#     dealer = []
#
#     def player_score_statement():
#         print(f"your cards:  {player},  current score is {sum_of_list(player)}")
#         print(f"dealers cards:  {dealer},  current score is {sum_of_list(dealer)}")
#         # print(f"dealers cards:  {dealer[0]}")
#
#     play = input("input 'y' to play and 'n' to not play: ").lower()
#
#     if play == "y":
#         first_deal(player)
#         first_deal(dealer)
#
#         player_score_statement()
#
#         if total_score(dealer) == 21:
#             print("BlackJack YOU LOSE")
#             exit()
#         elif total_score(player) == 21:
#             print("BlackJack YOU WIN")
#             exit()
#
#         continue_play = True
#         while continue_play:
#             if input("type 'y' to get another card, type 'n' to pass: ").lower() == "n":
#                 while total_score(dealer) < 17:
#                     dealer.append(random.choice(cards))
#                     calculate_score(player, dealer)
#             else:
#                 player.append(random.choice(cards))
#                 if total_score(player) > 21 and 11 in player:
#                     player.remove(11)
#                     player.append(1)
#                 player_score_statement()
#                 if total_score(player) > 21 or total_score(dealer) > 21:
#                     calculate_score(player, dealer)
#
#
# play_blackjack()

