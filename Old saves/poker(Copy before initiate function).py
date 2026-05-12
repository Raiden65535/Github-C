import random
import sys
import tkinter as tk
import os
import threading
from PIL import Image, ImageTk

root = tk.Tk()

Suit_option = ["Hearts","Diamonds","Clubs","Spades"]
Flush = []
Cards = []
Suits = []
Nums = []
Balance = []
Folds = []
Bluffs =  []
Current_Bets = []
Labels = []
Chips = []
Computer_label = []
Ace_label = []
Backs = [0,0,0,0,0]
Ratings = [0]

Rating = Cycles = Pot = Highscore = Winner = Computers = Increment = 0
Record_minirank = Record_minirank2 = Number_option = Num = 0
Record_kicker = Record_kicker2 = Record_kicker3 = Record_kicker4 = 0
Quantity = Extra = Difference = Max = Min = Pot_label = 0
Suit = Choice = Tie = Raise_Check = Condition = Returning = Third_printer = ""
Placeholder2 = 0

player_action_event = threading.Event()

def Amount_of_players():
    global Computers
    while True:
        tb_val = Textbox.get("1.0", "end")
        try:
            int(tb_val) > 0
            while int(tb_val) < 0 or int(tb_val) > 22:
                tb_val = Textbox.get("1.0", "end")
                break
            if int(tb_val) < 20:
                Computers = int(tb_val)
                Playing()
                break
                
            break
        except ValueError:
            tb_val = Textbox.get("1.0", "end")
            break


def Playing():
    global Textbox, Button3, Ace_label
    Button1.destroy()
    Button2.destroy()
    if Computers == 0:
        Textbox = tk.Text(root, height = 12, font = ("Arial", 16))
        Textbox.pack(padx=10, pady=10)
        Button3 = tk.Button(root, text="Confirm", font=("Arial", 18), command = Amount_of_players)
        Button3.pack(padx=10, pady=10)
    else:
        Textbox.destroy()
        Button3.destroy()
        Object = open("Balance.txt", "r").readlines()
        for i in range(0,Computers):
            if Object[i] == "0\n" or Object[i] != "0\n":#Change this later
                Object[i] = "10000\n"
            Balance.append(int(Object[i]))
            Current_Bets.append(0)
            Labels.append(0)
            Ace_label.append(0)
            Computer_label.append(0)
            Computer_label.append(0)
            Chips.append(0)
        for i in range(2,(2 * Computers) + 5):
            Cards_Test()
        Drawing()
        Drawing()
        Bet_Graphic()


def Drawing():
    global Ace, Increment, Ace_label
    if Increment == 0:
        Ace_label.append(0)
        Ace_label.append(0)
        for i in range(0,5):
            img = Image.open("Back.png")
            img = img.resize((150,200), Image.Resampling.LANCZOS)
            Ace = ImageTk.PhotoImage(img)
            Backs[i] = tk.Label(root, image=Ace)
            Backs[i].image = Ace
            Backs[i].place(x=250 + i * 250, y=450)
            pass

    if Increment < 2:
        files = os.listdir(Suits[Increment])
        path = os.path.join(Suits[Increment], files[Nums[Increment]-1])
        img = Image.open(path)
        img = img.resize((150, 200), Image.Resampling.LANCZOS)
        Ace = ImageTk.PhotoImage(img)
        Ace_label[Increment] = tk.Label(root, image=Ace)
        Ace_label[Increment].image = Ace
        Ace_label[Increment].place(x=520 + (Increment) * 460, y=240)
    else:
        Backs[Increment - 2].destroy()
        files = os.listdir(Suits[Increment - 7])
        path = os.path.join(Suits[Increment - 7], files[Nums[Increment - 7]-1])
        img = Image.open(path)
        img = img.resize((150, 200), Image.Resampling.LANCZOS)
        Ace = ImageTk.PhotoImage(img)
        Ace_label[Increment] = tk.Label(root, image=Ace)
        Ace_label[Increment].image = Ace
        Ace_label[Increment].place(x=250 + (Increment - 2) * 250, y=450)

    Increment = Increment + 1


def Bet_Graphic():
    global Button4, Button5
    Button4 = tk.Button(root, text="Check", font=("Arial", 30), command = Checking)
    Button4.place(x=600, y=100)
    Button5 = tk.Button(root, text="  Bet  ", font=("Arial", 30), command = Betting)
    Button5.place(x=800, y=100)


def Checking():
    global Choice, Button4, Button5
    Choice = "Check"
    Button4.destroy()
    Button5.destroy()
    player_action_event.set() 
    Bet()


def Betting():
    global Choice, Textbox2, Button4, Button5, Button6
    Choice = "Bet"
    if Quantity == 0:
        Textbox2 = tk.Text(root, height = 12, width = 20, font = ("Arial", 16))
        Textbox2.place(x=600, y=200)
        Button6 = tk.Button(root, text="Confirm", font=("Arial", 18), command = Trust_me_Bro)
        Button6.place(x=600, y=400)
    else:
        Textbox2.destroy()
        Button4.destroy()
        Button5.destroy()
        Button6.destroy()
        Bet()


def Trust_me_Bro():
    global Quantity, Textbox2
    while True:
        tb_val = Textbox2.get("1.0", "end")
        try:
            int(tb_val) > 0
            while int(tb_val) < 0 or int(tb_val) % 10 != 0: #And greater than a blind
                tb_val = Textbox2.get("1.0", "end")
                break
            if int(tb_val) > 0 and int(tb_val) % 10 == 0:
                Quantity = int(tb_val)
                Betting()
                break       
            break
        except ValueError:
            tb_val = Textbox2.get("1.0", "end")
            break


def Reraise_Graphic():
    global Button7, Button8, Button9, Label10, Extra, Textbox3, Button10
    Label10 = tk.Label(root, text = str(Extra) + " to call", font = ("Arial", 20))
    Label10.place(x=750, y=300)
    Button7 = tk.Button(root, text=" Call ", font=("Arial", 30), command = Calling)
    Button7.place(x=600, y=100)
    Button8 = tk.Button(root, text="  Raise  ", font=("Arial", 30), command = Raising)
    Button8.place(x=800, y=100)
    Button9 = tk.Button(root, text="  Fold  ", font=("Arial", 30), command = Folding)
    Button9.place(x=1000, y=100)   


def Calling():
    global Choice2, Button7, Button8, Button9, Label10
    Choice2 = "Call"
    Label10.destroy()
    Button7.destroy()
    Button8.destroy()
    Button9.destroy()
    player_action_event.set()
    root.update()
    Player_raise()


def Raising():
    global Choice2, Button7, Button8, Button9, Label10, Textbox3, Button10, Extra
    Choice2 = "Raise"
    if Placeholder2 == 0:
        Textbox3 = tk.Text(root, height = 12, width = 20, font = ("Arial", 16))
        Textbox3.place(x=600, y=200)
        Button10 = tk.Button(root, text="Confirm", font=("Arial", 18), command = This_aint_lasting)
        Button10.place(x=600, y=400)
    else:
        Extra = Placeholder2
        Label10.destroy()
        Button7.destroy()
        Button8.destroy()
        Button9.destroy()
        Button10.destroy()
        Textbox3.destroy()
        player_action_event.set()
        root.update()
        Player_raise()
    print()


def Folding():
    global Choice2, Button7, Button8, Button9
    Choice2 = "Fold"
    Button7.destroy()
    Button8.destroy()
    Button9.destroy()
    player_action_event.set()
    root.update()
    Player_raise()


def This_aint_lasting():
    global Placeholder2, Textbox3
    while True:
        tb_val = Textbox3.get("1.0", "end")
        try:
            int(tb_val) > 0
            while int(tb_val) < 0 or int(tb_val) % 10 != 0: #And greater than a blind
                tb_val = Textbox3.get("1.0", "end")
                break
            if int(tb_val) > 0 and int(tb_val) % 10 == 0:
                Placeholder2 = int(tb_val)
                Raising()
                break         
            break
        except ValueError:
            tb_val = Textbox3.get("1.0", "end")
            break




def Chips_Graphic(i):
    global Pot_label
    if Chips[i] != 0:
        Chips[i].destroy()
    Chips[i] = tk.Label(root, text = "Computer " + str(i) + " has " + str(Balance[i]) + " Chips.")
    Chips[i].place(x=1200, y=i*75)
    if Pot_label != 0:
        Pot_label.destroy()
    Pot_label = tk.Label(root, text = "Total Pot is " + str(Pot))
    Pot_label.place(x=750, y=400)


def Confirm():
    global Button35, Condition
    Button35 = tk.Button(root, text = "Confirm", font=("Arial", 18), command = Confirmation)
    Button35.place(x=500, y=250)


def Confirmation():
    global Condition
    Condition = "True"
    pass


def Pause():
    print("Entered Pause")
    pass


def Ranking_Graphic(Computer_tracker):
    global Printer, Second_printer, Third_printer, Labels, Flush_suit, Score
    if Computer_tracker == 0:
        Third_printer = "You have "
    else:
        Third_printer = "Computer " + str(Computer_tracker) + " has "
    if Score != 0 and Score != 5 and Score != 4:
        Third_printer = Third_printer + "a "
    if Score == 10:
        Labels[Computer_tracker] = tk.Label(root, text = Third_printer + "Royal flush.", font = ("Arial", 10))
    elif Score == 9:
        Labels[Computer_tracker] = tk.Label(root, text = Third_printer + "Straight flush.", font = ("Arial", 10))
    elif Score == 8:
        Labels[Computer_tracker] = tk.Label(root, text = Third_printer + " Four of a kind with " + Printer + ".", font = ("Arial", 10))
    elif Score == 7:
        Labels[Computer_tracker] = tk.Label(root, text = Third_printer + " Full house with " + Printer + " and " + Second_printer + ".", font = ("Arial", 10))
    elif Score == 6:
        Labels[Computer_tracker] = tk.Label(root, text = Third_printer + "Flush of " + Flush_suit + ".", font = ("Arial", 10))
    elif Score == 5:
        Labels[Computer_tracker] = tk.Label(root, text = Third_printer + "Straight that`s " + Printer + " high.", font = ("Arial", 10))
    elif Score == 4:
        Labels[Computer_tracker] = tk.Label(root, text = Third_printer + "Triple " + Printer + ".", font = ("Arial", 10))
    elif Score == 3:
        Labels[Computer_tracker] = tk.Label(root, text = Third_printer + "Two pair with " + Printer + " and " + Second_printer + ".", font = ("Arial", 10))
    elif Score == 2:
        Labels[Computer_tracker] = tk.Label(root, text = Third_printer + "Pair of " + Printer + ".", font = ("Arial", 10))
    else:
        Labels[Computer_tracker] = tk.Label(root, text = Third_printer + Printer + " high.", font = ("Arial", 10))
    Labels[Computer_tracker].place(x=100, y=Computer_tracker*75)





def Computer_Drawing(i,j):
    files = os.listdir(Suits[(2*i) + j])
    path = os.path.join(Suits[(2*i) + j], files[Nums[(2*i) + j]-1])
    img = Image.open(path)
    img = img.resize((45, 60), Image.Resampling.LANCZOS)
    Ace = ImageTk.PhotoImage(img)
    Computer_label[(2*i) + j] = tk.Label(root, image=Ace)
    Computer_label[(2*i) + j].image = Ace
    Computer_label[(2*i) + j].place(x=1150 + (j * 215), y=i*75)

def Finish():
    global Button60, Victor_label
    for i in range(1,Computers):
        if i in Folds:
            pass
        else:
            for j in range(0,2):
                Computer_Drawing(i,j)
    if Tie == "Yes":
        Victor_label = tk.Label(root, text = "There is a tie.", font = ("Arial", 18))

    elif Winner == 0:
        Balance[Winner] = Balance[Winner] + Pot
        Victor_label = tk.Label(root, text = "You win!", font = ("Arial", 18))
    else:
        Balance[Winner] = Balance[Winner] + Pot
        Victor_label = tk.Label(root, text = "Computer " + str(Winner) + " Wins.")

    Victor_label.pack()

    with open("Balance.txt", "w") as f:
        for i in range(0,len(Balance)):
            f.write(str(Balance[i]) + "\n")

    Button60 = tk.Button(root, text = "Next round", font=("Arial",18), command = Reset)
    Button60.pack()

def Reset():
    global Ace_label, Labels, Button60, Pot_label
    Button60.destroy()
    for i in range(0,Computers):
        Labels[i].destroy()
    for i in range(0,7):
        Ace_label[i].destroy()
    for i in range(2,(2 * Computers)):
        Computer_label[i].destroy()
    Victor_label.destroy()
    Pot_label.destroy()
    pass


def Tutorial():
    print("%")
    Tutorial = open("Tutorial.txt", "r")
    print(Tutorial.read())
    sys.exit()


def King_Maker():   #Converts numbers into their poker value equivalent. Only used for displays
    global Placeholder
    if Placeholder == "1" or Placeholder == "14":
        Placeholder = "Ace"
    elif Placeholder == "11":
        Placeholder = "Jack"
    elif Placeholder == "12":
        Placeholder = "Queen"
    elif Placeholder == "13":
        Placeholder = "King"     


def Cards_Test():   #Creates a list of all previous cards and checks the current card to ensure it is unique
    global Placeholder, Card_placeholder
    global Num, Suit, Number_option
    Card_check = ""
    Suit = random.choice(Suit_option)
    Number_option = random.randint(1,13)
    Placeholder = str(Number_option)
    King_Maker()

    Num = Placeholder 
    Card_placeholder = Num + " " + "of" + " " + Suit
    for i in range(0,len(Cards)):
        if Card_placeholder == Cards[i]:
            Card_check = "No"
            Cards_Test()

    if Card_check == "":
        Cards.append(Card_placeholder)
        Nums.append(Number_option)
        Suits.append(Suit)   


def Ranking_System(i):
    global Highscore, Placeholder, Computer_tracker, Tie, Winner, Score
    global Record_minirank, Record_minirank2, Printer, Second_printer, Flush_suit
    global Record_kicker, Record_kicker2, Record_kicker3, Record_kicker4
    for j in range(0,len(Folds)):
        if i == Folds[j]:
            return    
        
    Pair_num = Second_pair = Triple_num = Quad_num = 0
    Kicker = Kicker2 = Kicker3 = Kicker4 = 0
    Minirank = Minirank2 = Counter = Score = 0    
    Computer_tracker = i 
    Straight_check = Flush_check = ""
    Printer = Second_printer = ""
    Unsorted_suits = []
    Unsorted_nums = []

    Suit_list = [Suits[2*i],Suits[(2*i)+1],Suits[-5],Suits[-4],Suits[-3],Suits[-2],Suits[-1]]
    Num_list = [Nums[2*i],Nums[(2*i)+1],Nums[-5],Nums[-4],Nums[-3],Nums[-2],Nums[-1]]
    for j in range(len(Suit_list)):
        Unsorted_suits.append(Suit_list[j])
        Unsorted_nums.append(Num_list[j])
    Num_list.sort()
    Suit_list.sort()

    if i == 0:
        print("Your first card is the ", Cards[0], sep = "")
        print("Your second card is the ", Cards[1], sep = "")
        print(Num_list)   
    if i > 0 and Cycles != 3:
        print("Computer ", i , "`s",  " first card is the ", Cards[2*i], sep = "") 
        print("Computer ", i , "`s", " second card is the ", Cards[(2*i)+1], sep = "")
        print(Num_list)

#Compiles all the numbers and suits together in their own respective lists
#Creates 2 different versions of each list, one sorted, one unsorted. This becomes relevant with Straight flushes


    for i in range(0,len(Num_list)-1):
        if Num_list[i] == Num_list[i+1] and Pair_num < Num_list[i] and Counter < 1:
            Counter = Counter + 1
            Pair_num = Num_list[i]          
            Score = 2
        if Num_list[i] == Num_list[i+1] and Num_list[i] != Pair_num and Counter > 0 and Pair_num == 1:
            Second_pair = Num_list[i]
            Counter = Counter + 1
            Score = 3
        if Num_list[i] == Num_list[i+1] and Num_list[i] != Pair_num and Counter > 0 and Pair_num != 1:
            Second_pair = Pair_num
            Pair_num = Num_list[i]
            Counter = Counter + 1
            Score = 3

        Minirank = Pair_num
        Minirank2 = Second_pair
        Placeholder = Pair_num
        Second_placeholder = Second_pair  

#Num_list[i] == Num_list[i+1] checks the sorted list to see if they are the same value.
#Pair_num < Num_list[i] is so Triples, Full houses and double pairs are Evaluated correctly
#Counter < 1 is to ensure double pairs are evaluated correctly
#Miniranks and Placeholders are assigned at the end, relevant later for scoring / printing respectively


    for i in range(0,len(Num_list)-2):
        if Num_list[i] == Num_list[i+2] and Score < 4:
            Triple_num = Num_list[i]
            Minirank = Triple_num
            Placeholder = Triple_num
            Score = 4   

#The same as the check for pairs but now MUCH simpler with no second pair

    Temp_list = Num_list
    Temp_list = list(dict.fromkeys(Temp_list))
    if Temp_list[0] == 1:
        Temp_list.append(14)
    for i in range(0,(len(Temp_list)-4) + (len(Num_list)) - 7):
        Num = Temp_list[i]
        if Num + 4 == Temp_list[i+4]:
            Straight_check = "Yes"
            Score = 5
            Minirank = Temp_list[i+4]
            Placeholder = Temp_list[i+4]  

#Removes duplicates from the list
#Has the list act as if a 1 is the same as a 1 and a 14, like an ace would function
#To avoid an index error, we make it run a specfic amount. it doesnt run if there are only 4 values, as a straight needs 5 numbers.
#"Num" is needed because python didnt like Temp_list[i] + 4


    for i in range(0,len(Num_list)-4):
        Flush = []
        for j in range(i,i+5):
            Flush.append(Suit_list[j])
        if Flush[0] == Flush[4]:
            Flush_suit = Suit_list[4]
            Flush_check = "Yes"
            Score = 6

#Creats a new list and puts suits 1-5 in the list, then checks if its a flush.
#Then the list resets and checks for suits 2-6, then again with 3-7.
#Works because the suits are sorted together


    if Triple_num > 0 and Counter > 1:
        Score = 7
        Minirank = Triple_num
        if Pair_num != Triple_num:
            Minirank2 = Pair_num
            Second_placeholder = Pair_num
        else:
            Minirank2 = Second_pair
            Second_placeholder = Second_pair

#Mostly empty, besides for careful assignment of Minirank and placeholder


    for i in range(0,len(Num_list)-3):
        if Num_list[i] == Num_list[i+3] and Score < 8:
            Quad_num = Num_list[i]
            Placeholder = Quad_num
            Score = 8
            Minirank = Quad_num

#Identical to Triple check besides [i+2] being [i+3]


    if Score == 6:
        Temp_list = []
        Blank = []
        for i in range(0,len(Num_list)):
            if Flush_suit == Unsorted_suits[i]:
                Blank.append(i)
        for i in range(0,len(Blank)):
            Temp_list.append(Unsorted_nums[Blank[i]])
        Temp_list.sort(reverse=True)
        if Temp_list[-1] == 1:
            Temp_list.insert(0,14)
        Minirank = Temp_list[0]
        Kicker = Temp_list[1]
        Kicker2 = Temp_list[2]
        Kicker3 = Temp_list[3]
        Kicker4 = Temp_list[4]

#Fills the list "blank" with numbers. These numbers represent which numbers in the unsorted list are part of the flush
#Temp_list has all the numbers from Num_list that are part of a flush
#Put the list in descending order, and have 1 act as both a 1 and 14
#Record_temp is the version of the list with the highest minirank
#Miniranks and Kickers are then assigned going down the list, useful for tiebreaking


    if Flush_check == "Yes" and Straight_check == "Yes":
        Temp_list = []
        Blank = []
        for i in range(0,len(Num_list)):
            if Flush_suit == Unsorted_suits[i]:
                Blank.append(i)
        for i in range(0,len(Blank)):
            Temp_list.append(Unsorted_nums[Blank[i]])   
        Temp_list.sort()
        Temp_list = list(dict.fromkeys(Temp_list))
        if Temp_list[0] == 1:
            Temp_list.append(14)
        for i in range(0,len(Temp_list) - 4): #VERIFY IT HAS BEEN STUPID
            Num = Temp_list[i]
            if Num + 4 == Temp_list[i+4]:
                Score = 9
                Minirank = Temp_list[i+4]
            if Temp_list[-1] == 14 and Temp_list[-2] == 13 and Temp_list[-3] == 12:
                Score = 10     

#Repeats first part of code to only get flushed numbers
#Then uses similar code to the straight testing, only now only with flushed numbers
#Last 2 lines of code are to check for a royal flush


    if Score == 0:
        Temp_list = Num_list
        Temp_list.sort(reverse=True)
        if Temp_list[-1] == 1:
            Temp_list.insert(0,14)
        Minirank = Temp_list[0]
        Kicker = Temp_list[1]
        Kicker2 = Temp_list[2]
        Kicker3 = Temp_list[3]
        Kicker4 = Temp_list[4]
        Placeholder = Minirank

#This part only runs if the Computer hasnt got a set
#Same as assigning values for Flushes, but now with the entire hand
        
    if Score < 5 or Score == 8 and Score > 1:
        if Num_list[0] == 1:
            Num_list.append(14)
        Num_list.sort(reverse=True)
        for i in range(0,7):
            if Num_list[i] != Minirank and Num_list[i] != Minirank2:
                Kicker = Num_list[i]
                break

    if Score == 2 or Score == 4:
        for i in range(0,7):
            if Num_list[i] != Minirank and Num_list[i] != Kicker:
                Kicker2 = Num_list[i]
                break     

    if Score == 2:
        for i in range(0,7):
            if Num_list[i] != Minirank and Num_list[i] != Kicker and Num_list[i] != Kicker2:
                Kicker3 = Num_list[i]
                break

#Kickers help break ties
#Kickers are only assigned to certain hands because poker cares about the best 5 card hand

    Placeholder = str(Placeholder)
    King_Maker()
    Printer = Placeholder 
    Placeholder = str(Second_placeholder)
    King_Maker()
    Second_printer = Placeholder
    if Score != 0 and Score != 5:
        Printer = Printer + "`s"
        Second_printer = Second_printer + "`s"

    if Cycles == 3:
        return
    if Minirank == 1:
        Minirank = 14
    if Score > 3 and Score != 7:
        Minirank2 = 0 

    print("Printer is", Printer)
    print("Kicker1 is", Kicker)
    print("Kicker2 is", Kicker2)
    print("Kicker3 is", Kicker3)
    print("Kicker4 is", Kicker4)

    Ranking_Graphic(Computer_tracker)
#Light adjustments so everything is valued correctly

    if Score > Highscore:                                                      
        Highscore = Score
        Record_minirank = Minirank
        Record_minirank2 = Minirank2
        Record_kicker = Kicker
        Record_kicker2 = Kicker2
        Record_kicker3 = Kicker3
        Record_kicker4 = Kicker4
        Winner = Computer_tracker
        Tie = ""
    elif Score == Highscore and Minirank > Record_minirank:
        Record_minirank = Minirank
        Record_minirank2 = Minirank2
        Record_kicker = Kicker
        Record_kicker2 = Kicker2
        Record_kicker3 = Kicker3
        Record_kicker4 = Kicker4
        Winner = Computer_tracker
        Tie = ""
    elif Score == Highscore and Minirank == Record_minirank and Minirank2 > Record_minirank2:
        Record_minirank2 = Minirank2
        Record_kicker = Kicker
        Record_kicker2 = Kicker2
        Record_kicker3 = Kicker3
        Record_kicker4 = Kicker4
        Winner = Computer_tracker
        Tie = ""
    elif Score == Highscore and Minirank == Record_minirank and Minirank2 == Record_minirank2 and Kicker > Record_kicker:
        Record_kicker = Kicker
        Record_kicker2 = Kicker2
        Record_kicker3 = Kicker3
        Record_kicker4 = Kicker4
        Winner = Computer_tracker
        Tie = ""
    elif Score == Highscore and Minirank == Record_minirank and Minirank2 == Record_minirank2 and Kicker == Record_kicker and Kicker2 > Record_kicker2:
        Record_kicker2 = Kicker2
        Record_kicker3 = Kicker3
        Record_kicker4 = Kicker4
        Winner = Computer_tracker
        Tie = ""
    elif Score == Highscore and Minirank == Record_minirank and Minirank2 == Record_minirank2 and Kicker == Record_kicker and Kicker2 == Record_kicker2 and Kicker3 > Record_kicker3:
        Record_kicker3 = Kicker3
        Record_kicker4 = Kicker4
        Winner = Computer_tracker
        Tie = ""
    elif Score == Highscore and Minirank == Record_minirank and Minirank2 == Record_minirank2 and Kicker == Record_kicker and Kicker2 == Record_kicker2 and Kicker3 == Record_kicker3 and Kicker4 > Record_kicker4:
        Record_kicker4 = Kicker4
        Winner = Computer_tracker
        Tie = ""
    elif Score == Highscore and Minirank == Record_minirank and Minirank2 == Record_minirank2 and Kicker == Record_kicker and Kicker2 == Record_kicker2 and Kicker3 == Record_kicker3 and Kicker4 == Record_kicker4:
        Tie = "Yes"


#Checks each of the 7 Ranking values, Highscore, Miniranks and the 4 kickers, and compares it to the record versions
#To my understanding, every one of these must be checked simulataneously like shown
#The last line is to ensure only a tying hand would tie, not a losing hand


def Bet():
    global Balance, Choice, Pot, Cycles, Quantity, Raise_Check, Ratings, Button36
    Ratings = [0]
    Raise_Check = ""
    if Choice == "Check":
        for i in range(1,Computers):
            Computer_Decision(i)
        for i in range(1,Computers):
            Computer_Check(i)   

    elif Choice == "Bet":
        Balance[0] = Balance[0] - Quantity
        Pot = Pot + Quantity
        for i in range(1,Computers):
            Computer_Decision(i)
        for i in range(1,Computers):
            Computer_Bet(i)
            
    elif Choice == "Fold":
        print("You have folded")
        for i in range(0,Computers):
            Computer_fold(i) #idk what the hell happened here but hey
        quit()  

    if Raise_Check != "Yes":
        print("Cheat way in")
        Button36 = tk.Button(root, text = "Confirm", command = Finale2)
        Button36.pack()
        Finale()



#Allows Computers to spend their balance
#First checks that the Computer hasnt already requested to skip
#If Computer checks, nothing happens
#If Computer raises, currently all that happens is a line of code is written
#If Computer goes all in, betting is skipped



def Computer_Decision(i):
    global Rating
    Rating = Pair_num = Triple_num = 0
    for j in range(0,len(Folds)):
        if i == Folds[j]:
            return
    Num_list = [Nums[2*i],Nums[(2*i)+1],Nums[-5],Nums[-4],Nums[-3],Nums[-2]]
    Suit_list = [Suits[2*i],Suits[(2*i)+1],Suits[-5],Suits[-4],Suits[-3],Suits[-2]]


    if Cycles == 0:
        for i in range(2,6):
            Num_list.pop(2)
            Suit_list.pop(2)
        Num_list.sort()

        for i in range(0,len(Num_list)):
            if Num_list[i] == 1:
                Num_list[i] = 14

            if Num_list[0] == Num_list[1]:
                Rating = (2*Num_list[0]) + 70

            if Num_list[0] == Num_list[1] + 1 or Num_list[0] == Num_list[1] - 1:
                Rating = (5*Num_list[0]) + 30
                
            if Num_list[0] == Num_list[1] + 2 or Num_list[0] == Num_list[1] - 2:
                Rating = (3*Num_list[0]) + 20     

            if Suit_list[0] == Suit_list[1] and Rating == 0:
                Rating = ((Num_list[0] + Num_list[1]) / 2) * 6 

            elif Suit_list[0] == Suit_list[1] and Rating > 0:
                Rating = Rating + ((Num_list[0] + Num_list[1]) / 2) * 6 

            if Rating == 0:
                Rating = (3*Num_list[0]) + (3*Num_list[1])


    if Cycles == 1 or Cycles == 2:
        if Cycles == 1:
            Num_list.pop()
            Suit_list.pop()

        for i in range(0,len(Num_list)):
            if Num_list[i] == 1:
                Num_list[i] = 14         
        Num_list.sort()
        Suit_list.sort()


        for i in range(0,len(Num_list) - 2):
            if Num_list[i] == Num_list[i+2]:
                Triple_num = Num_list[i]
                Rating = (3*Num_list[i] + 50)

        for i in range(0,len(Num_list) - 1):
            if Num_list[i] == Num_list[i+1] and Num_list[i] != Triple_num:
                Pair_num = Num_list[i]
                Rating = (2*Num_list[i] + 40)   

        for i in range(0,len(Num_list) - 3):
            if Num_list[i] == Num_list[i+3]:
                Rating = (4*Num_list[i] + 60)  

        for i in range(0,len(Num_list) - 1):
            if Num_list[i] == Num_list[i+1] and Num_list[i] < Pair_num and Rating < ((3*Pair_num) + (2*Num_list[i]) + 30):
                Rating = (3*Pair_num) + (2*Num_list[i]) + 30

        for i in range (0,len(Num_list) - 2):
            if Num_list[i] == Num_list[i+2] and Pair_num > 0 and Rating < (5*Triple_num) + (2*Pair_num) + 40:
                Rating = (5*Triple_num) + (2*Pair_num) + 40


        Temp_list = list(dict.fromkeys(Num_list))
        for i in range(0,len(Num_list)):
            if Num_list[i] == 14:
                Temp_list.insert(0,1)

                
            for i in range(0,len(Temp_list)-2):
                Num = Temp_list[i]
                if Num + 2 == Temp_list[i+2] and Rating < (2*Temp_list[i+2] + 40):
                    Rating = (2*Temp_list[i+2] + 40)

            for i in range(0,len(Temp_list)-3):
                Num = Temp_list[i]
                if Num + 4 == Temp_list[i+3] and Rating < (2*Temp_list[i+3] + 50):
                    Rating = (2*Temp_list[i+3] + 50)

            for i in range(0,len(Temp_list)-3):
                Num = Temp_list[i]
                if Num + 3 == Temp_list[i+3] and Rating < (2*Temp_list[i+3] + 55):
                    Rating = (2*Temp_list[i+3] + 55)

            for i in range(0,len(Temp_list)-4):
                Num = Temp_list[i]
                if Num + 4 == Temp_list[i+4] and Rating < (2*Temp_list[i+4] + 70):
                    Rating = (2*Temp_list[i+4] + 70)

        for i in range(0,len(Suit_list)-2):
            if Suit_list[i] == Suit_list[i+2] and Rating < 40:
                Rating = 40

        for i in range(0,len(Suit_list)-3):
            if Suit_list[i] == Suit_list[i+3] and Rating < 75:
                Rating = 75

        for i in range(0,len(Suit_list)-4):
            if Suit_list[i] == Suit_list[i+4] and Rating < 90:
                Rating = 90

            
    if Cycles == 3:
        Ranking_System(i)
        Rating = Score * 10


    Bluff = random.randint(1,100)
    if Bluff < (Rating * 0.2) + 10:
        Bluffs.append(i)   

    for j in range(0,len(Bluffs)):
        if i == Bluffs[j]:
            Rating = random.randint(70,100)
    Ratings.append(Rating)



def Computer_Check(i):
    global Raise_Check
    if Raise_Check == "Yes":
        return
    for j in range(0,len(Folds)):
        if i == Folds[j]:
            return
    if Ratings[i] <= 70:
        Computer_Checking(i)
    else:
        Computer_Raise(i)
    Chips_Graphic(i)


def Computer_Bet(i):
    global Raise_Check, Difference, Quantity
    if Raise_Check == "Yes":
        return
    for j in range(0,len(Folds)):
        if i == Folds[j]:
            return

    if Ratings[i] <= 60:
        print("Going into Computer_folding")
        Computer_Fold(i)
    elif Ratings[i] <= 70:
        Difference = Quantity
        Computer_Call(i)
    else:
        Computer_Raise(i)
    Chips_Graphic(i)



def Computer_Checking(i):
    global Labels
    Labels[i] = tk.Label(root, text = "Computer " + str(i) + " Checks.")
    Labels[i].place(x=100, y=i*75)


        

def Computer_Call(i):
    global Current_Bets, Balance, Max, Pot, Difference, Labels
    Current_Bets[i] = Max
    Balance[i] = Balance[i] - Difference
    Pot = Pot + Difference
    Labels[i] = tk.Label(root, text = "Computer " + str(i) + " Calls for " + str(Difference) + ".")
    Labels[i].place(x=100, y=i*75)


def Computer_Fold(i):
    global Labels
    Folds.append(i)
    Labels[i] = tk.Label(root, text = " Computer " + str(i) + " Folds.")
    Labels[i].place(x=100, y=i*75)
    if len(Folds) == Computers - 1:
        Labels[i] = tk.label(root, text ="All players have folded.")
        Labels[i].place(x=100, y=i*75)
        quit()

def Computer_Raise(i):
    global Pot, Max, Difference, Min, Extra, Quantity, Labels, Replacement, Raise_Check
    Raise_Check = "Yes"
    Replacement = i
    Extra = random.randint(1,30)
    while (Extra * 100) <= Quantity:
        Extra = random.randint(1,30)
    Extra = Extra * 100

    Current_Bets[i] = Quantity + Extra
    Balance[i] = Balance[i] - Current_Bets[i]
    Pot = Pot + Current_Bets[i]
    Max = max(Current_Bets)
    if Quantity > 0:
        Current_Bets[0] = Quantity
        Labels[i] = tk.Label(root, text = "Computer " + str(i) + " Calls for " + str(Quantity) + " and raises for " + str(Extra - Quantity) + ", for a total of " + str(Extra) + " Chips.")
        Labels[i].place(x=100, y=i*75)
    else:
        Labels[i] = tk.Label(root, text = "Computer " + str(i) + " Bets " + str(Extra) + ".")
        Labels[i].place(x=100, y=i*75)
    Chips_Graphic(i)
    Step()

def Step():
    global Pot, Max, Difference, Ratings, Balance, Extra, Min, Raise_Check, Labels, Chips, Condition, Returning, Button36, Replacement
    for i in range(Replacement, Computers):
        if Returning == "True":
            Labels[i].destroy()

        if Chips[i] != 0:           
            Chips[i].destroy()
        Difference = Max - Current_Bets[i]
        if i in Folds or Current_Bets[i] == Max: #Not to be checked
            pass
        elif (random.randint(Difference - 50, Difference + 50) + Ratings[i]) / (Current_Bets[i] + 10) < 0.02: #Folds
            Computer_Fold(i)
        elif (random.randint(Difference - 50, Difference + 50) + Ratings[i]) / (Current_Bets[i] + 10) > 0.8: #Raises
            Computer_Reraise(i)
        else: #Calls
            Computer_Call(i)
        Chips_Graphic(i)
        #root.after(5000,Pause)
        #print("Immediately after pause")


    Max = max(Current_Bets)
    Min = min(Current_Bets)
    print("Current_Bets is", Current_Bets)

    if Current_Bets[0] != Max:
        player_action_event.clear()
        Reraise_Graphic()
        Replacement = 1
        Returning = "True"
        root.after(1, wait_for_player)
        return
    
    else:
        print("Success")
        player_action_event.clear()
        Raise_Check = "Yes"
        Button36 = tk.Button(root, text = "Confirm", font = ("Arial", 18) , command = Finale2)
        Button36.pack()
        Finale()


def Finale():
    global Current_Bets, Button36, Difference, Quantity, Raise_Check, Returning, Cycles
    if not player_action_event.is_set():
        root.after(10,Finale)
        return
    else:
        Button36.destroy()
        Current_Bets[0] = 0
        Difference = Quantity = 0
        Returning = Raise_Check =""
        Cycles = Cycles + 1
        for i in range(1,Computers):
            Current_Bets[i] = 0
            if Labels[i] != 0:
                Labels[i].destroy()
        if Cycles == 1:
            Drawing()
            Drawing()
            Drawing()
            Bet_Graphic()
        elif Cycles == 2:
            Drawing()
            Bet_Graphic()
        elif Cycles == 3:
            Drawing()
            Bet_Graphic()
        elif Cycles == 4:
            for i in range(0,Computers):
                Ranking_System(i)
            Finish()
        
        

def Finale2():
    player_action_event.set()



def wait_for_player():
    if not player_action_event.is_set():
        root.after(10, wait_for_player)
        return
    else:
        root.after(1, Step) 
        return
 


def Computer_Reraise(i):
        global Max, Min, Extra, Difference, Balance, Pot
        Extra = random.randint(1,30)
        while (Extra * 100) < Difference:
            Extra = random.randint(1,30)
        Extra = Extra * 100
        if Extra == Difference:
            Labels[i] = tk.Label(root, text = "Computer " + str(i) + " Calls for " + str(Difference))
        else:    
            Labels[i] = tk.Label(root, text = "Computer " + str(i) + " Calls for " + str(Difference) + " and Raises for " + str(Extra - Difference) + ", for a total of " + str(Extra) + " Chips.")
        Labels[i].place(x=100, y=i*75)
        Balance[i] = Balance[i] - Extra
        Pot = Pot + Extra
        Current_Bets[i] = Current_Bets[i] + Extra
        Max = max(Current_Bets)
        Min = min(Current_Bets)


def Player_raise(): 
    global Max, Choice2, Extra, Pot, Current_Bets, Balance
    if Choice2 == "Call":
        Balance[0] = Balance[0] - (Max - Current_Bets[0])
        Current_Bets[0] = Max
    elif Choice2 == "Raise":
        Balance[0] = Balance[0]  - Extra
        Current_Bets[0] = Current_Bets[0] + Extra
        Pot = Pot + Extra
        Max = Current_Bets[0]
    elif Choice2 == "Fold":
        Computer_Fold(i)
        quit()


Cards_Test()
Cards_Test()

root.geometry("1800x1500")
root.title("Poker")

Label = tk.Label(root, text = "Welcome Travelers.", font = ("Arial", 20))
Label.pack(padx = 20, pady = 20)

Button1 = tk.Button(root, text="Start", font=("Arial", 18), command = Playing)
Button1.pack()

Button2 = tk.Button(root, text="Secondary", font=("Arial", 18), command = Tutorial)
Button2.pack()

root.mainloop()

#Straights still have a slight issue
#Second and third kicker might have a slight issue