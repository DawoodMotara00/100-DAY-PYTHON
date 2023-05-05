import requests
import art


def get_follower_count(username):
    """
    This function takes a username and returns the number of followers for that user.
    """
    response = requests.get(f"https://www.instagram.com/{username}/?__a=1")
    if response.status_code == 200:
        data = response.json()
        return data["graphql"]["user"]["edge_followed_by"]["count"]
    else:
        return -1


a_username = input("Enter the first Instagram username: ")
b_username = input("Enter the second Instagram username: ")

a_followers = get_follower_count(a_username)
b_followers = get_follower_count(b_username)

print(a_followers)
print(b_followers)

# from random import randint
# from data import data
# from time import sleep
# import art
# import os
#
#
# def clear_console():
#     """
#     This function clears the console screen.
#     """
#     os.system('cls' if os.name == 'nt' else 'clear')
#
#
# def winner(a, b):
#     """
#     This function get the 2 parameteres and decicides who has the most followers
#     """
#     followers_a = data[a].get('follower_count')
#     followers_b = data[b].get('follower_count')
#
#     if followers_b > followers_a:
#         return ["b", b]
#     elif followers_a > followers_b:
#         return ["a", a]
#     else:
#         return "this is for some reason not working"
#
#
#
# def game():
#     a = randint(0, 30)
#     got_right = 0
#     game_is_on = True
#     while game_is_on:
#         b = randint(0, 30)
#
#         if a == b:
#             while a == b:
#                 b = randint(0, 30)
#
#         print(art.LOGO)
#         print(f"A:  {a} B:  {b}")
#         print(f"a: {data[a].get('name')}, {data[a].get('description')}, {data[a].get('country')}")
#         print(art.VS)
#         print(f"B: {data[b].get('name')}, {data[b].get('description')}, {data[b].get('country')}")
#
#         user_answer = input("Does 'a' or 'B' have more followers on \"instagram\"").lower()
#         if user_answer == winner(a, b)[0]:
#             got_right += 1
#             print("you got it right")
#             sleep(2)
#             clear_console()
#             a = winner(a,b)[1]
#         else:
#             print(f"sorry, you got {got_right} right, before you got it wrong")
#
#             exit()
#
#
# game()
