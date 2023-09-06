
import random

card_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

u_card = []
c_card = []

def user_card (card_list):
    for _ in range(2):
        u_card.append(random.choice(card_list))

def computer_card(card_list):
    for _ in range(2):
        c_card.append(random.choice(card_list))

def another_user_card(card_list):
    u_card.append(random.choice(card_list))

def another_computer_card(card_list):
    c_card.append(random.choice(card_list))

def user_total(u_card):
    u_total = 0
    for number in u_card:
        u_total = u_total + number
    
    return u_total

def computer_total(c_card):
    c_total = 0
    for number in c_card:
        c_total = c_total + number
    
    return c_total  

user_hand = user_card(card_list)
computer_hand = computer_card(card_list)
u_total = user_total(u_card)
c_total = computer_total(c_card)

diff1 = abs(21 - u_total)
diff2 = abs(21 - c_total)


if c_total > 21 and u_total > 21:
    print("Both went over. Tie")

elif u_total > 21 :
    print("You went over 21. You loose.")

elif c_total > 21:
    print("Computer went over 21. You win.")

elif diff1 < diff2:
    print("You won")

elif diff2 < diff1:
    print("You loose")




print(f"{u_total} {u_card}")
print(f"{c_total} {c_card}")
# user_card(card_list)
# computer_card(card_list)
# print(u_card, c_card)
# user_start = input("\nDo you want to play game of BlackJack? Type 'yes' or 'no': ").lower()