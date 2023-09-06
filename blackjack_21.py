
import random

card_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

u_card = []
c_card = []

user_start = input("\nType 'start' to start the BLACKJACK 23 game: ").lower()
if user_start == 'start':

    print(''' 

    ** BLACK JACK 23 **
     _______    _______
    |       |  |       |
    | A     |  | K     |
    |   ♠   |  |   ♥   |
    |     A |  |     K |
    |_______|  |_______|

    ** BLACK JACK 23 **

''')

    def user_card (card_list):
        for _ in range(2):
            u_card.append(random.choice(card_list))

    def computer_card(card_list):
        for _ in range(2):
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

    print(f"\nYour cards: {u_card}. Your current score: {u_total}")
    print(f"Computer's first card: {c_card[0]}")

    another_card = input("\nType 'y' to get another card, type 'n' to pass: ")

    while another_card == 'y':

        u_card.append(random.choice(card_list))
        c_card.append(random.choice(card_list))

        u_total = user_total(u_card)
        c_total = computer_total(c_card)

        if u_total > 23 or c_total > 23:
            break

        print(f"\nYour cards: {u_card}. Your current score: {u_total}")
        print(f"Computer's first card: {c_card[0]}")

        another_card = input("\nType 'y' to get another card, type 'n' to pass: ")
           

    diff1 = abs(23 - u_total)
    diff2 = abs(23 - c_total)
    
    print(f"\n\nYour final hand: {u_card}. Your final score: {u_total}")
    print(f"Computer's final hand: {c_card}. Computer's final score: {c_total}")

    if c_total > 23 and u_total > 23:
        print("\nBoth went over. Tie")

    elif u_total > 23 :
        print("\nYou went over 23. You loose.")

    elif c_total > 23:
        print("\nComputer went over 23. You win.")

    elif diff1 < diff2:
        print("\nYou won 😁")

    elif diff2 < diff1:
        print("\nYou loose 😞")


