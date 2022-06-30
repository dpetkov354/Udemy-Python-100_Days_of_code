from replit import clear
import art
print(art.logo)
person_bid = {}
next_person = True
highest_bid_name = ""
highest_bid = 0
while next_person is True:
  name = input(f"Please type in your name:\n")
  bid = int(input(f"Please enter your bid:\n$"))
  person_bid[name] = bid
  next = input(f"Is there another bidder?[y/n]\n")
  if highest_bid < bid:
    highest_bid = bid
    highest_bid_name = name
  if next == "y":
    clear()
  elif next == "n":
    next_person = False

print(f"The highest bidder is {highest_bid_name} with a bid of ${highest_bid}.")