import random
Suits = ["Hearts","Diamonds","Clubs","Spades"]
Flush = []
Cards = []
Object = open("Balance.txt", "r").readlines()
Balance = int(Object[0])
if Balance == 0:
    print("You`re poor. here`s some benfits")
    Balance = 1000
Pot = 0
Player_tracker = 0
Highscore = 0
Temp = 0
Winner = 0 
Record_minirank = 0
Record_minirank2 = 0
Record_kicker = 0
Record_kicker2 = 0
Record_kicker3 = 0
Record_kicker4 = 0
Num = 0
Number_option = 0
Suit = ""
Choice = ""


Computers = int(input("(0 For tutorial)How many computers will be playing? "))
if Computers == 0:
    Tutorial = open("Tutorial.txt", "r")
    print(Tutorial.read())
    
while Computers < 1 or Computers > 22:
    print("Error message, put a usable amount of computers in")
    Computers = int(input("How many computers will be playing? "))
if Computers == 22:
    Choice = "All in"

#Does a small check to see how many CPUs the player wants to play against
def King_maker():
    global Placeholder
    if Placeholder == "1" or Placeholder == "14":
        Placeholder = "Ace"
    elif Placeholder == "11":
        Placeholder = "Jack"
    elif Placeholder == "12":
        Placeholder = "Queen"
    elif Placeholder == "13":
        Placeholder = "King"

#Converts numbers into their poker value equivalent. Only used for displays
        
def Cards_test():    
    global Placeholder, Card_placeholder
    global Num, Suit, Number_option
    Card_check = ""
    for i in range(0,len(Cards)):
        if Card_placeholder == Cards[i]:
            Card_check = "No"
            Suit = random.choice(Suits)
            Number_option = random.randint(1,13)
            Placeholder = str(Number_option)
            King_maker()
            Num = Placeholder
            Card_placeholder = Num + Suit
            break             
    if Card_check == "":
        Cards.append(Card_placeholder)
    else:
         Cards_test()

#Creates a list of all previous cards and checks the current card to ensure it is unique
        


def Player_Cards():
    global Balance
    global Placeholder, Card_placeholder
    global Number_option1, Number_option2
    global Suit1, Suit2
    global Num, Suit, Number_option
    while Balance % 10 > 0:
        Balance = random.randint(1000,10000)
        
    print("you have", Balance,"chips")
    Suit1 = random.choice(Suits)
    Number_option1 = random.randint(1,13)
    Placeholder = str(Number_option1)
    King_maker()
    Num1 = Placeholder
    Card_placeholder = Num1 + Suit1
    Suit = Suit1
    Num = Num1
    Number_option = Number_option1 
    Cards_test()
    Suit1 = Suit
    Num1 = Num
    Number_option1 = Number_option

    print("your first card is the", Num1,"of", Suit1)


    Suit2 = random.choice(Suits)
    Number_option2 = random.randint(1,13)
    Placeholder = str(Number_option2)
    King_maker()
    Num2 = Placeholder
    Card_placeholder = Num2 + Suit2
    Suit = Suit2
    Num = Num2
    Number_option = Number_option2
    Cards_test()
    Suit2 = Suit
    Num2 = Num
    Number_option2 = Number_option
        
    print("your second card is the", Num2,"of", Suit2)
    Bet()
    Universal()
    Ranking_System()

#generates a hand for the real players    
#Generates a random suit and random number
#Sends the generated number off to become an ace, jack queen or king.
#repeats code to generate another player card
#Calls multiple functions in sequencial order
#Number_option is used for printing whereas Num is the inherant value
    
def Bet():
    global Balance, Choice, Pot
    if Choice == "All in" or Choice == "all in" or Choice == "e":
        print()
    else:
        Choice = input("Check, Raise or Fold: ")
        if Choice == "Check" or Choice == "check" or Choice == "C" or Choice == "c" :
            print("both players check")
            for i in range(0,Computers):
                Computer_check()
        elif Choice == "Raise" or Choice == "raise" or Choice == "R" or Choice == "r":
            Quantity = int(input("how much do you want to raise by? "))
            while Quantity > Balance:
                Quantity = int(input("you dont have that many chips, raise again. "))
            Balance = Balance - Quantity
            Pot = Pot + Quantity
        elif Choice == "Fold" or Choice == "fold" or Choice == "F" or Choice == "f":
            print("you have folded")
            quit()
        elif Choice == "All in" or Choice == "all in" or Choice == "e":
            print("opponent calls, skipping all future betting rounds")
            Pot = Pot + Balance
            Balance = 0
        else:
            print("Try again")
            Bet()
        print()
        
#Allows players to spend their balance
#First checks that the player hasnt already requested to skip
#If player checks, nothing happens
#If player raises, currently all that happens is a line of code is written
#If player goes all in, betting is skipped


def Universal():
    global Placeholder, Card_placeholder
    global Number_option3, Number_option4, Number_option5, Number_option6,Number_option7
    global Suit3, Suit4, Suit5, Suit6, Suit7
    global Num, Suit, Number_option
    Suit3 = random.choice(Suits)
    Number_option3 = random.randint(1,13)
    Placeholder = str(Number_option3)
    King_maker()
    Num3 = Placeholder
    Card_placeholder = Num3 + Suit3
    Suit = Suit3
    Num = Num3
    Number_option = Number_option3
    Cards_test()
    Suit3 = Suit
    Num3 = Num
    Number_option3 = Number_option
        

    print("the first card in the flop is the", Num3,"of", Suit3)


    Suit4 = random.choice(Suits)
    Number_option4 = random.randint(1,13)
    Placeholder = str(Number_option4)
    King_maker()
    Num4 = Placeholder
    Card_placeholder = Num4 + Suit4
    Suit = Suit4
    Num = Num4
    Number_option = Number_option4
    Cards_test()
    Suit4 = Suit
    Num4 = Num
    Number_option4 = Number_option
    
    print("the second card in the flop is the", Num4,"of", Suit4)

    Suit5 = random.choice(Suits)
    Number_option5 = random.randint(1,13)
    Placeholder = str(Number_option5)
    King_maker()
    Num5 = Placeholder
    Card_placeholder = Num5 + Suit5
    Suit = Suit5
    Num = Num5
    Number_option = Number_option5
    Cards_test()
    Suit5 = Suit
    Num5 = Num
    Number_option5 = Number_option
        
    print("the third card in the flop is the", Num5,"of", Suit5)
    Bet()

    Suit6 = random.choice(Suits)
    Number_option6 = random.randint(1,13)
    Placeholder = str(Number_option6)
    King_maker()
    Num6 = Placeholder
    Card_placeholder = Num6 + Suit6
    Suit = Suit6
    Num = Num6
    Number_option = Number_option6
    Cards_test()
    Suit6 = Suit
    Num6 = Num
    Number_option6 = Number_option
        
    print("the turn is the", Num6,"of", Suit6)
    Bet()

    Suit7 = random.choice(Suits)
    Number_option7 = random.randint(1,13)
    Placeholder = str(Number_option7)
    King_maker()
    Num7 = Placeholder
    Card_placeholder = Num7 + Suit7
    Suit = Suit7
    Num = Num7
    Number_option = Number_option7
    Cards_test()
    Suit7 = Suit
    Num7 = Num
    Number_option7 = Number_option
    
    print("the river is the", Num7,"of", Suit7)
    Bet()

#Cards every player can use

def Ranking_System():
    global Highscore, Placeholder, Player_tracker, Tie, Winner
    global Record_minirank, Record_minirank2
    global Record_kicker, Record_kicker2, Record_kicker3, Record_kicker4
    Pair_num = Second_pair = Triple_num = Quad_num = 0
    Kicker = Kicker2 = Kicker3 = Kicker4 = 0
    Minirank = Minirank2 = Counter = Score = 0    
    Straight_check = ""
    Flush_check = ""
    Unsorted_suits = []
    Unsorted_nums = []

#Resets a lot of variables to allow this function to work as a loop
    
    Suit_list = [Suit1,Suit2,Suit3,Suit4,Suit5,Suit6,Suit7]
    Num_list = [Number_option1,Number_option2,Number_option3,Number_option4,Number_option5,Number_option6,Number_option7]
    for i in range(len(Suit_list)):
        Unsorted_suits.append(Suit_list[i])
        Unsorted_nums.append(Num_list[i])
    Num_list.sort()
    Suit_list.sort()
    print(Num_list)

#Compiles all the numbers and suits together in their own respective lists
#Creates 2 different versions of each list, one sorted, one unsorted. This becomes relevant with Straight flushes
    

    for i in range(0,6):
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

        
             
    for i in range(0,5):
        if Num_list[i] == Num_list[i+2]:
            Triple_num = Num_list[i]
            Minirank = Triple_num
            Placeholder = Triple_num
            Score = 4
            
#The same as the check for pairs but now MUCH simpler with no second pair
            
    Temp_list = Num_list
    Temp_list = list(dict.fromkeys(Temp_list))
    if Temp_list[0] == 1:
        Temp_list.append(14)
    for i in range(0,len(Temp_list)-4):
        Num = Temp_list[i]
        if Num + 4 == Temp_list[i+4]:
            Straight_check = "Yes"
            Score = 5
            Minirank = Temp_list[i+4]

#Removes duplicates from the list
#Has the list act as if a 1 is the same as a 1 and a 14, like an ace would function
#To avoid an index error, we make it run a specfic amount. it doesnt run if there are only 4 values, as a straight needs 5 numbers.
#"Num" is needed because python didnt like Temp_list[i] + 4

            
    for i in range(0,3):
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
            

    for i in range(0,4):
        if Num_list[i] == Num_list[i+3] and Score < 8:
            Quad_num = Num_list[i]
            Placeholder = Quad_num
            Score = 8
            Minirank = Quad_num

#Identical to Triple check besides [i+2] being [i+3]



    if Score == 6:
        Temp_list = []
        Blank = []
        for i in range(0,7):
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
        for i in range(0,7):
            if Flush_suit == Unsorted_suits[i]:
                Blank.append(i)
        for i in range(0,len(Blank)):
            Temp_list.append(Unsorted_nums[Blank[i]])
            
        Temp_list.sort()
        Temp_list = list(dict.fromkeys(Temp_list))
        if Temp_list[0] == 1:
            Temp_list.append(14)
        for i in range(0,len(Temp_list) - 4):
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
            Score = 1
        Minirank = Temp_list[0]
        Kicker = Temp_list[1]
        Kicker2 = Temp_list[2]
        Kicker3 = Temp_list[3]
        Kicker4 = Temp_list[4]
        Placeholder = Minirank
        
#This part only runs if the player hasnt got a set
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
    King_maker()
    Printer = Placeholder
    Placeholder = str(Second_placeholder)
    King_maker()
    Second_printer = Placeholder
    
    

    if Score == 10:
        print("A royal flush")
    elif Score == 9:
        print("A straight flush")
    elif Score == 8:
        print("Quad ",Printer,"s", sep = "")
    elif Score == 7:
        print("A full house with ",Printer,"s", " And", " " ,Second_printer,"s", sep = "")
    elif Score == 6:
        print("A flush")
    elif Score == 5:
        print("A straight")
    elif Score == 4:
        print("Triple ",Printer,"s", sep = "")
    elif Score == 3:
        print("Pair of pairs with ",Printer,"s", " And", " " ,Second_printer,"s", sep = "")
    elif Score == 2:
        print("Pair of ",Printer,"s", sep = "")
    else:
        print(Printer, "high")

#, sep = "" is to remove the space between the number and the s, so 5s instead of 5 s

    

    if Minirank == 1:
        Minirank = 14
    if Score > 3 and Score != 7:
        Minirank2 = 0
    Player_tracker = Player_tracker + 1
    print(Player_tracker)
    #Light adjustments so everything is valued correctly
    
    if Score > Highscore:                                                      
        Highscore = Score
        Record_minirank = Minirank
        Record_minirank2 = Minirank2
        Record_kicker = Kicker
        Record_kicker2 = Kicker2
        Record_kicker3 = Kicker3
        Record_kicker4 = Kicker4
        Winner = Player_tracker
        Tie = ""
        print("A")

    elif Score == Highscore and Minirank > Record_minirank:
        Record_minirank = Minirank
        Record_minirank2 = Minirank2
        Record_kicker = Kicker
        Record_kicker2 = Kicker2
        Record_kicker3 = Kicker3
        Record_kicker4 = Kicker4
        Winner = Player_tracker
        Tie = ""
        print("B")
        
    elif Score == Highscore and Minirank == Record_minirank and Minirank2 > Record_minirank2:
        Record_minirank2 = Minirank2
        Record_kicker = Kicker
        Record_kicker2 = Kicker2
        Record_kicker3 = Kicker3
        Record_kicker4 = Kicker4
        Winner = Player_tracker
        Tie = ""
        print("C")
        
    elif Score == Highscore and Minirank == Record_minirank and Minirank2 == Record_minirank2 and Kicker > Record_kicker:
        Record_kicker = Kicker
        Record_kicker2 = Kicker2
        Record_kicker3 = Kicker3
        Record_kicker4 = Kicker4
        Winner = Player_tracker
        Tie = ""
        print("D")
        
    elif Score == Highscore and Minirank == Record_minirank and Minirank2 == Record_minirank2 and Kicker == Record_kicker and Kicker2 > Record_kicker2:
        Record_kicker2 = Kicker2
        Record_kicker3 = Kicker3
        Record_kicker4 = Kicker4
        Winner = Player_tracker
        Tie = ""
        print("E")
        
    elif Score == Highscore and Minirank == Record_minirank and Minirank2 == Record_minirank2 and Kicker == Record_kicker and Kicker2 == Record_kicker2 and Kicker3 > Record_kicker3:
        Record_kicker3 = Kicker3
        Record_kicker4 = Kicker4
        Winner = Player_tracker
        Tie = ""
        print("F")
    elif Score == Highscore and Minirank == Record_minirank and Minirank2 == Record_minirank2 and Kicker == Record_kicker and Kicker2 == Record_kicker2 and Kicker3 == Record_kicker3 and Kicker4 > Record_kicker4:
        Record_kicker4 = Kicker4
        Winner = Player_tracker
        Tie = ""
        print("G")
    elif Score == Highscore and Minirank == Record_minirank and Minirank2 == Record_minirank2 and Kicker == Record_kicker and Kicker2 == Record_kicker2 and Kicker3 == Record_kicker3 and Kicker4 == Record_kicker4:
        Tie = "Yes"
        print("H")
#Checks each of the 7 Ranking values, Highscore, Miniranks and the 4 kickers, and compares it to the record versions
#To my understanding, every one of these must be checked simulataneously like shown
#The last line is to ensure only a tying hand would tie, not a losing hand

    print()
    
    

Player_Cards()
print()


def Computer_cards():
    global Placeholder, Card_placeholder
    global Number_option1, Number_option2
    global Suit1, Suit2
    global Num, Suit, Number_option
    Suit1 = random.choice(Suits)
    Number_option1 = random.randint(1,13)
    Placeholder = str(Number_option1)
    King_maker()
    Num1 = Placeholder
    Card_placeholder = Num1 + Suit1
    Suit = Suit1
    Num = Num1
    Number_option = Number_option1
    Cards_test()
    Suit1 = Suit
    Num1 = Num
    Number_option1 = Number_option


    print("Computers first card is the", Num1,"of", Suit1)

    Suit2 = random.choice(Suits)
    Number_option2 = random.randint(1,13)
    Placeholder = str(Number_option2)
    King_maker()
    Num2 = Placeholder
    Card_placeholder = Num2 + Suit2
    Suit = Suit2
    Num = Num2
    Number_option = Number_option2
    Cards_test()
    Suit2 = Suit
    Num2 = Num
    Number_option2 = Number_option


    print("Computers second card is the", Num2,"of", Suit2)
#Basically the same as the Player_cards function without betting

for i in range(0,Computers):
    Computer_cards()
    Ranking_System()

    



if Tie == "Yes":
    print("There is a tie")
else:
    print("Player number", Winner,"Wins")

if Winner == 1:
    Balance = Balance + Pot
    
Object = open("Balance.txt", "w")
Object.write(str(Balance))
Object.close()


#For now im concerned about the players balance, the balance of the computers comes later
#I`ve had Record_Minirank_2 = 0 exist for a while with no errors. Why didnt it break?
#I`ve also had Kicker_1 exist for a decently long time with no errors? what??
