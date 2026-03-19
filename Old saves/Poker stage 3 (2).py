import random
Suits = ["Hearts","Diamonds","Clubs","Spades"]
Balance = random.randint(1000,10000)
Flush = []
Blank = []
Cards = []
Record_temp = []
Player_tracker = 0
Highscore = 0
Score = 0
Pair_num = 0
Second_pair = 0
Triple_num = 0
Quad_num = 0
Temp = 0
Counter = 0
Winner = 0 
Minirank = 0
Record_minirank = 0
Minirank_2 = 0
Record_minirank_2 = 0
Check = ""
Flush_check = ""
Straight_check = ""
Choice = ""
Tie = ""
Computers = int(input("How many computers will be playing? "))

#Converts numbers into their poker value equivalent. Only used for displays
def King_maker():
    global Placeholder
    if Placeholder == "1":
        Placeholder = "Ace"
    elif Placeholder == "11":
        Placeholder = "Jack"
    elif Placeholder == "12":
        Placeholder = "Queen"
    elif Placeholder == "13":
        Placeholder = "King"

def Cards_test():
    global Placeholder
    for i in range(0,len(Cards)):
        if Placeholder == Cards[i]:
            suit_option = random.choice(Suits)
            number_option = random.randint(1,13)
            Placeholder = str(number_option)
            King_maker()
            Num2 = Placeholder
            Suit2 = suit_option
            Placeholder = Num2 + Suit2
            Cards_test()
    Cards.append(Placeholder)
    
#generates a hand for the real players    
def Player_Cards():
    global Balance
    global Placeholder
    global number_option1
    global number_option2
    global Suit1
    global Card1
    global Suit2
    global Card2
    while Balance % 10 > 0:
        Balance = random.randint(1000,10000)
#Generates a balance that looks nice. eventually this will be replaced.
        
    print("you have", Balance,"chips")
    suit_option = random.choice(Suits)
    number_option1 = random.randint(1,13)
#Generates a random suit and random number
    Placeholder = str(number_option1)
    King_maker()
    Num1 = Placeholder
#Sends the generated number off to become an ace, jack queen or king.
    Suit1 = suit_option
    Placeholder = Num1 + Suit1
    Cards.append(Placeholder)
        #Puts both suit and Number into one variable, helpful later
    print("your first card is the", Num1,"of", suit_option)

#repeats code to generate another player card

    suit_option = random.choice(Suits)
    number_option2 = random.randint(1,13)
    Placeholder = str(number_option2)
    King_maker()
    Num2 = Placeholder
    Suit2 = suit_option
    Placeholder = Num2 + Suit2
    Cards_test()
    
        
    print("your second card is the", Num2,"of", suit_option)
    Bet()
    Universal()
    Ranking_System()
    
#Allows players to spend their balance
def Bet():
    global Choice
    global Balance
    if Choice == "All in" or Choice == "all in" or Choice == "e":
        print()
#This skips the process of betting if all in was already requested
    else:
        Choice = input("Check, Raise or Fold: ")
        if Choice == "Check" or Choice == "check":
            print("both players check")
#Nothing happens, waits action from other players
#need ai stuff to happen here
        elif Choice == "Raise" or Choice == "raise":
            Quantity = int(input("how much do you want to raise by? "))
            while Quantity > Balance:
                Quantity = int(input("you dont have that many chips, raise again. "))
#adds to the pot, ensuring you cant spend what you dont have
            Balance = Balance - Quantity
        elif Choice == "Fold" or Choice == "fold":
            print("you have folded")
            quit()
#The player gives up
        elif Choice == "All in" or Choice == "all in" or Choice == "e":
            print("opponent calls, skipping all future betting rounds")
#The player skips to showdown
        else:
            print("program didnt get what it wanted, shutting down")
#failsafe
            quit()
        print()

#Cards every player can use
#Mostly everything is the same as the player cards
def Universal():
    global Placeholder
    global number_option3
    global number_option4
    global number_option5
    global number_option6
    global number_option7
    global Suit3
    global Card3
    global Suit4
    global Card4
    global Suit5
    global Card5
    global Suit6
    global Card6
    global Suit7
    global Card7
    suit_option = random.choice(Suits)
    number_option3 = random.randint(1,13)
    Placeholder = str(number_option3)
    King_maker()
    Num3 = Placeholder
    Suit3 = suit_option
    Placeholder = Num3 + Suit3
    Cards_test()
        

    print("the first card in the flop is the", Num3,"of", suit_option)


    suit_option = random.choice(Suits)
    number_option4 = random.randint(1,13)
    Placeholder = str(number_option4)
    King_maker()
    Num4 = Placeholder
    Suit4 = suit_option
    Placeholder = Num4 + Suit4
    Cards_test()
    
    print("the second card in the flop is the", Num4,"of", suit_option)

    suit_option = random.choice(Suits)
    number_option5 = random.randint(1,13)
    Placeholder = str(number_option5)
    King_maker()
    Num5 = Placeholder
    Suit5 = suit_option
    Placeholder = Num5 + Suit5
    Cards_test()
        
    print("the third card in the flop is the", Num5,"of", suit_option)
    Bet()

    suit_option = random.choice(Suits)
    number_option6 = random.randint(1,13)
    Placeholder = str(number_option6)
    King_maker()
    Num6 = Placeholder
    Suit6 = suit_option
    Placeholder = Num6 + Suit6
    Cards_test()
        
    print("the turn is the", Num6,"of", suit_option)
    Bet()

    suit_option = random.choice(Suits)
    number_option7 = random.randint(1,13)
    Placeholder = str(number_option7)
    King_maker()
    Num7 = Placeholder
    Suit7 = suit_option
    Placeholder = Num7 + Suit7
    Cards_test()       
    print("the river is the", Num7,"of", suit_option)
    Bet()


def Ranking_System():
    global Second_pair
    global Pair_num
    global Triple_num
    global Quad_num
    global Counter
    global Flush_check
    global Straight_check
    global Record_temp
    global Score
    global Highscore
    global Minirank
    global Minirank_2
    global Record_minirank
    global Record_minirank2
    global Player_tracker
    global Winner
    global Placeholder
    global Tie
    global Check
    

    Unsorted_suits = []
    Unsorted_nums = []
    Suit_list = [Suit1,Suit2,Suit3,Suit4,Suit5,Suit6,Suit7]
    Num_list = [number_option1,number_option2,number_option3,number_option4,number_option5,number_option6,number_option7]
#Compiles all the numbers and suits together in their own respective lists
    for i in range(len(Suit_list)):
        Unsorted_suits.append(Suit_list[i])
        Unsorted_nums.append(Num_list[i])
#Creates 2 different versions of each list, one sorted, one unsorted. This becomes relevant with Straight flushes
    Num_list.sort()
    Suit_list.sort()
    print(Num_list)
    
#Num_list[i] == Num_list[i+1] checks the sorted list to see if they are the same value.
#Pair_num < Num_list[i] is so Triples, Full houses and double pairs are Evaluated correctly
#Counter < 1 is to ensure double pairs are evaluated correctly
    for i in range(0,6):
        if Num_list[i] == Num_list[i+1] and Pair_num < Num_list[i] and Counter < 1:
            Counter = Counter + 1
            Pair_num = Num_list[i]          
            Score = 2
#Pair_num == 1 / != is to evaluate things differently depending on if there are two 1s.
        if Num_list[i] == Num_list[i+1] and Num_list[i] != Pair_num and Counter > 0 and Pair_num == 1:
            Second_pair = Num_list[i]
#Second pair becomes Num_list[i] as it is guarenteed to be a lower value than the aces
            Counter = Counter + 1
            Score = 3
        if Num_list[i] == Num_list[i+1] and Num_list[i] != Pair_num and Counter > 0 and Pair_num != 1:
#Second pair now becomes what the previous Pair_num was, as immediately after Pair_num gets replaced with a higher number
            Second_pair = Pair_num
            Pair_num = Num_list[i]
            Counter = Counter + 1
            Score = 3
#The next line of code is outside the for loop as the results we want out of all 3 outcomes are the same for these variables       
#Minirank helps determine which hand wins if the type of hand is the same but the numbers are different
        Minirank = Pair_num
#Minirank_2 is essentially the same as Minirank, except is only needed when deeling with Pairs of Pairs
        Minirank_2 = Second_pair
        Placeholder = str(Pair_num)
        King_maker()
        Pair_number = Placeholder
             
#Same as checking for pairs, but now with [i+2]
    for i in range(0,5):
        if Num_list[i] == Num_list[i+2] and Score < 4:
            Triple_num = Num_list[i]
            Minirank = Triple_num
            Placeholder = str(Triple_num)
            King_maker()
            Triple_number = Placeholder
            if Triple_num == Pair_num:
                Pair_num = 0
#This is so Full houses get evaluated fairly
            Score = 4


    Temp_list = Num_list
    Temp_list = list(dict.fromkeys(Temp_list))
#Removes duplicates from the list
    if Temp_list[0] == 1:
        Temp_list.append(14)
#Has the list act as if a 1 is the same as a 1 and a 14, like an ace would function
#To avoid an index error, we make it run a specfic amount. it doesnt run if there are only 4 values, as a straight needs 5 numbers.
    for i in range(0,len(Temp_list)-4):
        Num = Temp_list[i]
#A new value is needed because python didnt like Temp_list[i] + 4
        if Num + 4 == Temp_list[i+4]:
#After removing duplicates, if this condition is met it will be guarenteed the hand is a straight
            Straight_check = "Yes"
            Score = 5
            Minirank = Temp_list[i+4]
#Minirank gets assigned to the highest value in the straight
            

#Creats a new list and puts suits 1-5 in the list, then checks if its a flush.
#Then the list resets and checks for suits 2-6, then again with 3-7.
#Works because the suits are sorted together
    for i in range(0,3):
        Flush = []
        for j in range(i,i+5):
            Flush.append(Suit_list[j])
        if Flush[0] == Flush[4]:
            Flush_suit = Suit_list[4]
            Flush_check = "Yes"
            Score = 6


#Essentially empty, all the work for full house needed to go into Pair of pairs/ Triples.
    if Triple_num > 0 and Counter > 1:
        Score = 7
        Minirank = Triple_num

#The same as Triples or Pairs, but since full houses arent a problem, this becomes simple    
    for i in range(0,4):
        if Num_list[i] == Num_list[i+3] and Score < 8:
            Quad_num = Num_list[i]
            Placeholder = str(Quad_num)
            King_maker()
            Quad_number = Placeholder
            Score = 8
            Minirank = Quad_num

#All of this is to check the minirank for flushes
    if Score == 6:
        Temp_list = []
        Blank = []
        for i in range(0,7):
            if Flush_suit == Unsorted_suits[i]:
                Blank.append(i)
#Fills the list "blank" with numbers. These numbers represent which numbers in the unsorted list are part of the flush
        for i in range(0,len(Blank)):
            Temp_list.append(Unsorted_nums[Blank[i]])
#
#Temp_list has all the numbers from Num_list that are part of a flush
        Temp_list.sort(reverse=True)
        if Temp_list[-1] == 1:
            Temp_list.insert(0,14)
#Put the list in descending order, and have 1 act as both a 1 and 14
#Record_temp is the version of the list with the highest minirank
#It compares each number of Record_temp and Temp_list to see which one is weaker, i.e 13 10 9 7 6 would lose to 13 11 10 9 7
#The for loop must break after the condition is met so the Minirank is the highest different value
        if len(Record_temp) > 1:
            for i in range(0,len(Record_temp)):
                if Record_temp[i] > Temp_list[i]:
                    Minirank = 0
                    Check = "Yes"
                    break
                if Record_temp[i] < Temp_list[i]:
                    Record_minirank = Record_temp[i]
                    Minirank = Temp_list[i]
                    break
        if Check == "Yes" or Check == "":       
            Record_temp = []
            Record_temp = Temp_list
        i = 0
        

#Checks that there is both a Straight and Flush in the hand
    if Flush_check == "Yes" and Straight_check == "Yes":
        Temp_list = []
        Blank = []
        for i in range(0,7):
            if Flush_suit == Unsorted_suits[i]:
                Blank.append(i)
        for i in range(0,len(Blank)):
            Temp_list.append(Unsorted_nums[Blank[i]])
#Same thing as checking for the Minirank of the flush
            
        Temp_list.sort()
        Temp_list = list(dict.fromkeys(Temp_list))
        if Temp_list[0] == 1:
            Temp_list.append(14)
#Sorts and removes duplicates from the list, then has 1 act as 1 and 14 again
#Same code as the straight checking, now that we know all the cards have the same suit
        for i in range(0,len(Temp_list) - 4):
            Num = Temp_list[i]
            if Num + 4 == Temp_list[i+4]:
                Score = 9
                Minirank = Temp_list[i+4]
            if Temp_list[Length - 1] == 14 and Temp_list[Length - 2] == 13 and Temp_list[Length - 3] == 12:
                Score = 10
#Checking for a royal flush at the end 

#If no hand has been made, finds the highest value card as your Minirank, ensuring 1 is at max value
    if Score == 0 and Num_list[0] == 1:
        print("Ace high")
        Minirank = 1
        Score = 1
    elif Score == 0:
        Num8 = Num_list[6]
        Minirank = Num8
        if Num8 == 11:
            Num8 = "Jack"
        elif Num8 == 12:
             Num8 = "Queen"
        elif Num8 == 13:
            Num8 = "King"
        print(Num8, "high")
        Score = 1
        

    if Score == 10:
        print("A royal flush")
    elif Score == 9:
        print("A straight flush")
    elif Score == 8:
        print("Quad ",Quad_number,"s", sep = "")
    elif Score == 7:
        print("A full house")
    elif Score == 6:
        print("A flush")
    elif Score == 5:
        print("A straight")
    elif Score == 4:
        print("Triple ",Triple_number,"s", sep = "")
    elif Score == 3:
        print("Pair of pairs with ",Pair_number,"s", sep = "")
    elif Score == 2:
        print("Pair of ",Pair_number,"s", sep = "")
        
#Pair_numBER and such is used as that uses Jack/Queen etc while Pair_num is just 11/12
#, sep = "" is to remove the space between the number and the s, so 5s instead of 5 s
    

    if Minirank == 1:
        Minirank = 14
    if Score > 3 and Score != 7:
        Minirank_2 = 0
#Light adjustments so everything is valued correctly
    Player_tracker = Player_tracker + 1
    if Score > Highscore:                                                      
        Highscore = Score
        Record_minirank = Minirank
        Record_minirank2 = Minirank_2
        Winner = Player_tracker
        Tie = ""
#If the Score is higher than the record, all the values of the winnning player get stored as the record
#This logic applies for the Next 2 elif statements, but they check minirank
    elif Score == Highscore and Minirank > Record_minirank:
        Record_minirank = Minirank
        Record_minirank2 = Minirank_2
        Winner = Player_tracker
        Tie = ""
    elif Score == Highscore and Minirank == Record_minirank and Minirank_2 > Record_minirank2:
        Record_minirank2 = Minirank_2
        Winner = Player_tracker
        Tie = ""
    elif Score == Highscore and Minirank == Record_minirank and Minirank_2 == Record_minirank2:
        Tie = "Yes"
#This last elif statement ensure the computer can handle a tie, which can happen in poker
#The other conditions have Tie = "" to ensure if p1 and p2 tie, but p3 has a stronger hand, p3 still wins
        
    
    
    Score = 0
    Counter = 0
    Pair_num = 0
    Triple_num = 0
    Quad_num = 0
    Minirank = 0
    Minirank_2 = 0
    Check = ""
    Straight_check = ""
    Flush_check = ""
#Reset all temp values except lists as they already get reset in the lists and the record variables
    print()
    


Player_Cards()
print()

#The computers cards, They replace the old num1 and Num2 with new ones.
#Designed to work with any amount of computers, and ensures cards arent repeated
#Other then that, its the same as the Player cards
def Computer_cards():
    global Placeholder
    global number_option1
    global number_option2
    global Suit1
    global Card1
    global Suit2
    global Card2
    suit_option = random.choice(Suits)
    number_option1 = random.randint(1,13)
    Placeholder = str(number_option1)
    King_maker()
    Num1 = Placeholder
    Suit1 = suit_option
    Card1 = Num1 + Suit1
    for i in range(0,len(Cards)):
        while Card1 == Cards[i]:
            print("E")
            suit_option = random.choice(Suits)
            number_option1 = random.randint(1,13)
            Placeholder = str(number_option1)
            King_maker()
            Num1 = Placeholder
            Suit1 = suit_option
            Card1 = Num1 + Suit1
    Cards.append(Card1)


    print("Computers first card is the", Num1,"of", suit_option)

    suit_option = random.choice(Suits)
    number_option2 = random.randint(1,13)
    Num2 = str(number_option2)
    Placeholder = str(number_option2)
    King_maker()
    Num2 = Placeholder
    Suit2 = suit_option
    Placeholder = Num2 + Suit2
    Cards_test()
    
    
    print("Computers second card is the", Num2,"of", suit_option)

for i in range(0,Computers):
    Computer_cards()
    Ranking_System()


if Tie == "Yes":
    print("There is a tie")
else:
    print("Player number", Winner,"Wins")



            






