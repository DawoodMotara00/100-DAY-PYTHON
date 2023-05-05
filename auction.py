logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
auction = True
bid_dictionary = {}


def find_highest_bid(bids):
    max_bidder = "null"
    max_bid = 0
    for key in bids:
        if bids[key] > max_bid:
            max_bid = bids[key]
            max_bidder = key
    print(f"the max bid is by {max_bidder} at the price of £{max_bid}")


while auction:
    name = input("what is you name:  ")
    price = float(input("what is your max bid price  £"))
    bid_dictionary[name] = price
    carry_on = input("do you want to make another bid 'yes' to carry on and 'no' to finsh")
    if carry_on == "yes":
        continue
    elif carry_on == "no":
        break

find_highest_bid(bid_dictionary)
# print(max_bidder)
# print(max_bid)
# print(bid_dictionary)
# print(bid_dictionary[name])
