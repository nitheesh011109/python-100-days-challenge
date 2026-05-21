import os
print("Welcome to secret auction program")
def find_highest_bid(bidding_dict):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dict:
        bid_amount = bidding_dict[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} and the bid amount was {highest_bid}")
bids = {}
continue_bids = True
while continue_bids:
    name = input("What is your name?:")
    price = int(input("What is your bid?:"))
    bids[name] = price
    others = input("Are there any other bidders? Type 'yes' or 'no'\n").lower()
    if others == 'no':
        continue_bids = False
        find_highest_bid(bids)
    elif others == 'yes':
        os.system('cls')