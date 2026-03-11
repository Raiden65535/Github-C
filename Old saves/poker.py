import random
Suit_option = ["Hearts","Diamonds","Clubs","Spades"]
Flush = []
Cards = []
Suits = []
Nums = []
Folds = []
Rating = 0
Cycles = 0
Pot = 0
Highscore = 0
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
Value = ""
Tie = ""

Object = open("Balance.txt", "r").readlines()
Balance = int(Object[0])
if Balance == 0:
    print("You`re poor. here`s some benfits")
    Balance = 1000


Computers = int(input("(0 For tutorial)How many Computers will be playing? "))
if Computers == 0:
    Tutorial = open("Tutorial.txt", "r")
    print(Tutorial.read())
    
while Computers < 1 or Computers > 22:
    print("Error message, put a usable amount of Computers in")
    Computers = int(input("How many Computers will be playing? "))
if Computers == 22:
    Choice = "All in"


Computers = Computers + 1
#Does a small check to see how many CPUs the Computer wants to play against
def King_Maker():
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
        
def Cards_Test():    
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


#Creates a list of all previous cards and checks the current card to ensure it is unique


        
def Ranking_System(i):
    global Highscore, Placeholder, Computer_tracker, Tie, Winner, Score
    global Record_minirank, Record_minirank2
    global Record_kicker, Record_kicker2, Record_kicker3, Record_kicker4
    for j in range(0,len(Folds)):
        if i == Folds[j]:
            return
        
    Pair_num = Second_pair = Triple_num = Quad_num = 0
    Kicker = Kicker2 = Kicker3 = Kicker4 = 0
    Minirank = Minirank2 = Counter = Score = 0    
    Straight_check = ""
    Flush_check = ""
    Unsorted_suits = []
    Unsorted_nums = []
    Computer_tracker = i


#Resets a lot of variables to allow this function to work as a loop
    
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
        for i in range(0,len(Temp_list) - 4) + len(Num_list) - 7:
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
    
    if Cycles == 3:
        return
        

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
        print("A")

    elif Score == Highscore and Minirank > Record_minirank:
        Record_minirank = Minirank
        Record_minirank2 = Minirank2
        Record_kicker = Kicker
        Record_kicker2 = Kicker2
        Record_kicker3 = Kicker3
        Record_kicker4 = Kicker4
        Winner = Computer_tracker
        Tie = ""
        print("B")
        
    elif Score == Highscore and Minirank == Record_minirank and Minirank2 > Record_minirank2:
        Record_minirank2 = Minirank2
        Record_kicker = Kicker
        Record_kicker2 = Kicker2
        Record_kicker3 = Kicker3
        Record_kicker4 = Kicker4
        Winner = Computer_tracker
        Tie = ""
        print("C")
        
    elif Score == Highscore and Minirank == Record_minirank and Minirank2 == Record_minirank2 and Kicker > Record_kicker:
        Record_kicker = Kicker
        Record_kicker2 = Kicker2
        Record_kicker3 = Kicker3
        Record_kicker4 = Kicker4
        Winner = Computer_tracker
        Tie = ""
        print("D")
        
    elif Score == Highscore and Minirank == Record_minirank and Minirank2 == Record_minirank2 and Kicker == Record_kicker and Kicker2 > Record_kicker2:
        Record_kicker2 = Kicker2
        Record_kicker3 = Kicker3
        Record_kicker4 = Kicker4
        Winner = Computer_tracker
        Tie = ""
        print("E")
        
    elif Score == Highscore and Minirank == Record_minirank and Minirank2 == Record_minirank2 and Kicker == Record_kicker and Kicker2 == Record_kicker2 and Kicker3 > Record_kicker3:
        Record_kicker3 = Kicker3
        Record_kicker4 = Kicker4
        Winner = Computer_tracker
        Tie = ""
        print("F")
    elif Score == Highscore and Minirank == Record_minirank and Minirank2 == Record_minirank2 and Kicker == Record_kicker and Kicker2 == Record_kicker2 and Kicker3 == Record_kicker3 and Kicker4 > Record_kicker4:
        Record_kicker4 = Kicker4
        Winner = Computer_tracker
        Tie = ""
        print("G")
    elif Score == Highscore and Minirank == Record_minirank and Minirank2 == Record_minirank2 and Kicker == Record_kicker and Kicker2 == Record_kicker2 and Kicker3 == Record_kicker3 and Kicker4 == Record_kicker4:
        Tie = "Yes"
        print("H")
        
#Checks each of the 7 Ranking values, Highscore, Miniranks and the 4 kickers, and compares it to the record versions
#To my understanding, every one of these must be checked simulataneously like shown
#The last line is to ensure only a tying hand would tie, not a losing hand

    print()
    print()
def Bet():
    global Balance, Choice, Pot, Cycles
    if Choice == "All in" or Choice == "all in" or Choice == "e" or Choice == "A" or Choice == "a":
        Cycles = 4
        print()
    else:
        Choice = input("Check, Raise or Fold: ")
        if Choice == "Check" or Choice == "check" or Choice == "C" or Choice == "c" :
            print(Nums)
            for i in range(1,Computers):
                Computer_Decision(i)
                Computer_Check(i)
                
        elif Choice == "Raise" or Choice == "raise" or Choice == "R" or Choice == "r":
            Quantity = int(input("how much do you want to raise by? "))
            while Quantity > Balance:
                Quantity = int(input("you dont have that many chips, raise again. "))
            Balance = Balance - Quantity
            Pot = Pot + Quantity
            
            for i in range(1,Computers):
                Computer_Decision(i)
                Computer_Raise(i)
                
        elif Choice == "Fold" or Choice == "fold" or Choice == "F" or Choice == "f":
            print("you have folded")
            for i in range(0,Computers):
                Computer_fold(i)
            quit()
            
        elif Choice == "All in" or Choice == "all in" or Choice == "e" or Choice == "A" or Choice == "a":
            print("opponent calls, skipping all future betting rounds")
            Pot = Pot + Balance
            Balance = 0
        else:
            print("Try again")
            Bet()
        Cycles = Cycles + 1
        print()
        
#Allows Computers to spend their balance
#First checks that the Computer hasnt already requested to skip
#If Computer checks, nothing happens
#If Computer raises, currently all that happens is a line of code is written
#If Computer goes all in, betting is skipped





def Computer_Decision(i):
    global Rating, Value
    Rating = 0
    for j in range(0,len(Folds)):
        if i == Folds[j]:
            return
        
    Num_list = [Nums[2*i],Nums[(2*i)+1],Nums[-5],Nums[-4],Nums[-3],Nums[-2]]
    Suit_list = [Suits[2*i],Suits[(2*i)+1],Suits[-5],Suits[-4],Suits[-3],Suits[-2]]
    for i in range(0,len(Num_list)):
        if Num_list[i] == 1:
            Num_list[i] = 14

            
    if Cycles == 0:
        for i in range(2,6):
            Num_list.pop(2)
            Suit_list.pop(2)
        Num_list.sort()
            
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


            
    if Cycles == 1:
        Num_list.pop()
        Suit_list.pop()
        Num_list.sort()
        Suit_list.sort()
        print(Suit_list)
        Temp_list = list(dict.fromkeys(Num_list))
        for i in range(0,len(Temp_list)-3):
            Num = Temp_list[i]
            if Num + 3 == Temp_list[i+3]:
                print("EEEE")
        #4 straight
        for i in range(0,len(Temp_list)-2):
            Num = Temp_list[i]
            if Num + 2 == Temp_list[i+2]:
                print("F")
        #3 straight

        for i in range(0,len(Temp_list)-3):
            Num = Temp_list[i]
            if Num + 4 == Temp_list[i+3]:
                print("GG")
        #4 straight gapped

        for i in range(0,len(Suit_list)-3):
            if Suit_list[i] == Suit_list[i+3]:
                print("HHH")
        #4 Flush
        for i in range(0,len(Suit_list)-2):
            if Suit_list[i] == Suit_list[i+2]:
                print("I")
        #3 Flush

        
            
            
                    
                    


            
    if Cycles == 2:
        Num_list.sort()

    if Cycles == 3:
        Ranking_System(i)



    if Rating <= 20:
        Value = "Bad"
    elif Rating <= 40:
        Value = "OK"
    elif Rating <= 60:
        Value = "Good"
    elif Rating <= 80:
        Value = "Great"
    else:
        Value = "Fantastic"
    print(Num_list)
        
            


                      
def Computer_Check(i):
    for j in range(0,len(Folds)):
        if i == Folds[j]:
            return
    if Value == "Bad":
        print("Computer", i, "Checks")
    elif Value == "OK":
        print("Computer", i, "Checks")
    elif Value == "Good":
        print("Computer", i, "Checks")
    elif Value == "Great":
        print("Computer", i, "Checks")
    else:
        print("Computer", i, "Checks")




def Computer_Raise(i):
    print("Nower Rating is", Rating)
    for j in range(0,len(Folds)):
        if i == Folds[j]:
            return
    if Value == "Bad":
        print("Computer", i, "Folds")
        Computer_Fold(i)
    elif Value == "OK":
        print("Computer", i, "Folds")
        Computer_Fold(i)
    elif Value == "Good":
        print("Computer", i, "Folds")
        Computer_Fold(i)
    elif Value == "Great":
        print("Computer", i, "Calls")
    else:
        print("Computer", i, "Calls")



def Computer_Fold(i):
    Folds.append(i)
    
                      




for i in range(0,(2 * Computers) + 5):
    Cards_Test()  

print("You have", Balance, "Chips")
print("Your first card is the",Cards[0])
print("Your second card is the",Cards[1])
Bet()
print("The first card of the flop is the",Cards[-5])
print("The second card of the flop is the",Cards[-4])
print("The third card of the flop is the",Cards[-3])
Bet()
print("The turn is the",Cards[-2])
Bet()
print("The river is the",Cards[-1])
Bet()
print()
Nums[-4] = 2
Nums[-3] = 2

i = 0
for i in range(0,Computers):
    Ranking_System(i)


if Tie == "Yes":
    print("There is a tie")
elif Winner == 0:
    print("You win")
else:
    print("Computer number", Winner, "Wins")
if Winner == 0:
    Balance = Balance + Pot
    
Object = open("Balance.txt", "w")
Object.write(str(Balance))
Object.close()

#

