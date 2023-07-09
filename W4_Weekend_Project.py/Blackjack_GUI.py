"""
GUI For BlackJack game.
--RUN HERE--
Gives player scale 1-1000 for how much to bet.
User can HIT, STAND, PLAY AGAIN, QUIT, or SHUFFLE.
Displays Images of cards, player points, dealer points, round
Displays if Win/Lost or Blackjack.
Closes if amount to bet is below 0.
Enjoy!
"""
from tkinter import *
from tkinter import messagebox
from Deck import Deck
from PIL import Image, ImageTk


window = Tk()
window.title('blackJack')
window.geometry('1000x600')
window.configure(background='green')
window.iconbitmap("info")

#Global Variables - Keeps track of player score, round, dealer score, and bet
initial_amount = 1000
game_round = 0
user_points = 0
computer_points = 0
bet_amount = 0

#Player Takes Their Turn
def hit(): #O(n)
    global initial_amount, user_points, bet_amount, computer_points
    if deck.get_deck_count() < 4:
        deck.new_deck()
    if user_points == 0:
        dealer_img_lbl.grid_forget()
        player_img_lbl.grid_forget()
        hit_btn.configure(text="HIT")
        stand_btn.configure(text="STAND")
        deck.start_round()
        if deck.check_blackjack(deck.player_cards):
            user_points = 21
            initial_amount += bet_scale.get() * 2
            result_lbl.configure(text='--BLACKJACK--\nYou won!')
            update_info()
            return end_of_round()
        user_points = deck.player_points
        computer_points = deck.dealer_cards[1].value
        bet_amount = bet_scale.get()
    else: 
        deck.player_add_card_to_hand(deck.player_cards)
        if deck.player_points > 21:
            user_points = deck.player_points
            initial_amount -= bet_amount
            result_lbl.configure(text='You lost!')
            return end_of_round()
        elif deck.player_points == 21:
            user_points = deck.player_points
            return stand()
        else:
            user_points = deck.player_points
    update_info()

#Stand: Starts Dealer's Turn
def stand(): #O(n)
    global computer_points, bet_amount, initial_amount
    if stand_btn['text'] == 'QUIT':
        messagebox.showwarning('blackJack!',f"Thanks for playing blackJack!\nYour earnings were ${initial_amount - 1000}")
        window.destroy()
    if user_points == 0:
        return
    if deck.get_deck_count() < 2:
        deck.new_deck()
    dealer_img_lbl.grid_forget()
    show_dealer_img('f')
    computer_points = deck.dealer_points
    dealer_lbl.configure(text=f"Dealer Points: {computer_points}\nRound: {game_round}")
    if deck.check_blackjack(deck.dealer_cards):
        computer_points = 21
        initial_amount -= bet_amount
        result_lbl.configure(text='You lost!\n--BLACKJACK--')
    elif deck.dealer_points > 21:
        initial_amount += bet_amount
        result_lbl.configure(text='You won!')
    elif deck.dealer_points >= 17:
        if deck.player_points == deck.dealer_points:
            result_lbl.configure(text='Tie!')
        elif deck.player_points > deck.dealer_points:
            result_lbl.configure(text='You won!')
            initial_amount += bet_amount
        else:
            result_lbl.configure(text='You lost!')
            initial_amount -= bet_amount
    else:
        deck.dealer_add_card_to_hand(deck.dealer_cards)
        return stand()
    end_of_round()
    
#During Round updates points and Displays
def update_info(): #O(n)
    deck_count.configure(text=f'Deck count: {deck.get_deck_count()}')
    player_lbl.configure(text=f"Your Points: {user_points}\nYour Amount: ${initial_amount}")
    scale_lbl.configure(text=f"Bet Amount: ${bet_amount} (Fixed)")
    dealer_lbl.configure(text=f"Dealer Points: {computer_points}\nRound: {game_round}")
    show_dealer_img()
    show_player_img()

#Resets points and Displays/ checks if no money
def end_of_round(): #O(n)
    show_dealer_img('f')
    show_player_img()
    global game_round, computer_points, user_points, initial_amount
    dealer_lbl.configure(text=f"Dealer Points: {computer_points}\nRound: {game_round}")
    player_lbl.configure(text=f"Your Points: {user_points}\nYour Amount: ${initial_amount}")
    hit_btn.config(state='disabled')
    hit_btn.after(1000, lambda: hit_btn.config(state='active'))
    result_lbl.after(3000, lambda: result_lbl.configure(text=''))
    game_round += 1
    computer_points = 0
    user_points = 0
    hit_btn.configure(text="PLAY AGAIN?")
    stand_btn.configure(text="QUIT")
    bet_scale['to'] = initial_amount
    scale_lbl.configure(text=f"Bet Amount: ${bet_scale.get()}")
    if initial_amount <= 0:
        messagebox.showwarning('blackJack!',"You've run out of money!\nCome again some other time.")
        window.destroy()

#Shuffles Deck
def shuffle_deck(): #O(n)
    if hit_btn['text'] != "HIT":
        deck.new_deck()
        deck.shuffle()
        dealer_img_lbl.grid_forget()
        player_img_lbl.grid_forget()
        deck_count.configure(text=f'Deck count: {deck.get_deck_count()}')
    else:
        shuffle_lbl.configure(text='Cannot Shuffle\nduring round', fg='red') 
        shuffle_lbl.after(2000, lambda: shuffle_lbl.configure(text=''))
        
#Displays Dealer's Cards
def show_dealer_img(img='b'): #O(n)
    if img == 'f':
        cards = [Image.open(card.img).resize((100, 152), Image.ADAPTIVE) for card in deck.dealer_cards]
    elif img == 'b':
        cards = [Image.open(deck.dealer_cards[0].back_img).resize((100, 152), Image.ADAPTIVE), Image.open(deck.dealer_cards[1].img).resize((100, 152), Image.ADAPTIVE)]
    img_dimensions = (100 + (len(cards) - 1)*40, 152)
    dealer_img = Image.new('RGB', (img_dimensions), 'green')
    for i, n in enumerate(cards):
        Image.Image.paste(dealer_img, n, (i*40, 0))
    dealer_rnd = ImageTk.PhotoImage(dealer_img)
    dealer_img_lbl.configure(image=dealer_rnd)
    dealer_img_lbl.image = dealer_rnd
    dealer_img_lbl.grid(row=0,column=0)

#Displays Player's Cards
def show_player_img(): #O(n)
    cards = [Image.open(card.img).resize((100, 152), Image.ADAPTIVE) for card in deck.player_cards]
    img_dimensions = (100 + (len(cards) - 1)*40, 152)
    player_img = Image.new('RGB', (img_dimensions), 'green')
    for i, n in enumerate(cards):
        Image.Image.paste(player_img, n, (i*40, 0))
    player_rnd = ImageTk.PhotoImage(player_img)
    player_img_lbl.configure(image=player_rnd)
    player_img_lbl.image = player_rnd
    player_img_lbl.grid(row=6,column=0, columnspan=12)

deck = Deck() #O(n)
    
#Dealer Widgets:
dealer_img_lbl = Label(bg='green')
dealer_lbl = Label(window, text=f"Dealer Points: {computer_points}\nRound: {game_round}", bg='green', fg='white')

#Shuffle Widgets:
cards = [Image.open('W4_Weekend_Project.py\Flat_Playing_Cards_Set\Back_Covers\Pomegranate.png').resize((100, 152), Image.ADAPTIVE) for card in range(0,3)]
img_dimensions = (100 + (len(cards) - 1)*40, 152 + (len(cards) - 1)*5)
shuffle_img = Image.new('RGB', (img_dimensions), 'green')
for i, n in enumerate(cards):
        Image.Image.paste(shuffle_img, n, (i*5, i*5))
shuffle_rnd = ImageTk.PhotoImage(shuffle_img)
shuffle_img_lbl = Label(image=shuffle_rnd, bg='green')
shuffle_img_lbl.image = shuffle_rnd
shuffle_btn = Button(window, text='SHUFFLE',command=shuffle_deck, padx=30)
shuffle_lbl = Label(window, text='', bg='green', fg='white')
deck_count = Label(window, text=f'Deck count: {deck.get_deck_count()}', bg='green', fg='white')

#Player Widgets:
player_img_lbl = Label(bg='green', height=200)
result_lbl = Label(window, text='', bg='green', fg='white', font=('Arial', 25))
player_lbl = Label(window, text=f"Your Points: {user_points}\nYour Amount: ${initial_amount}", bg='green', fg='white')
hit_btn = Button(window, text="START GAME", command=hit, width=13)
stand_btn = Button(window, text="STAND",command=stand, width=9)
bet_scale = Scale(window, from_=1, to=initial_amount, orient=HORIZONTAL,bg='green', fg='white', highlightthickness=0,borderwidth=0)
scale_lbl = Label(window, text= f"Bet Amount: ${bet_scale.get()}",bg='green', fg='white')

#Grid Configuration:
window.rowconfigure(5, weight=1)
window.columnconfigure(0, weight=1)
window.rowconfigure(4, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(6, weight=2)
window.rowconfigure(95, weight=1)
window.rowconfigure(101, weight=1, minsize=10)

dealer_img_lbl.grid(row=0,column=0, columnspan=6)
dealer_lbl.grid(row=1,column=0)

shuffle_img_lbl.grid(row=0, column= 10)
shuffle_btn.grid(row=2,column=10)
shuffle_lbl.grid(row=3,column=10)
deck_count.grid(row=1,column=10)

player_img_lbl.grid(row=95,column=0, columnspan=12)
result_lbl.grid(row=5,column=0, columnspan=12, sticky=EW)
player_lbl.grid(row=99, column=2, columnspan=3)

hit_btn.grid(row=100, column=2, sticky=S)
stand_btn.grid(row=100, column=3, sticky=S, padx=13)

scale_lbl.grid(row=99,column=5, sticky=S)
bet_scale.grid(row=100,column=5, sticky=S, padx=20)

window.mainloop()