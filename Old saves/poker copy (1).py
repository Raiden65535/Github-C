import random
Suits = ["Hearts","Diamonds","Clubs", "Spades"]
Balance = random.randint(1000,10000)
Flush = []
Blank = []
Score = 0
Pair_num = 0
Triple_num = 0
Temp = 0
Counter = 0
Flush_check = ""
Straight_check = ""
while Balance % 10 > 0:
    Balance = random.randint(1000,10000)
    


print("you have", Balance,"chips")
suit_option = random.choice(Suits)
number_option1 = random.randint(1,13)
Num1 = str(number_option1)
if Num1 == "1":
    Num1 = "Ace"
elif Num1 == "11":
    Num1 = "Jack"
elif Num1 == "12":
    Num1 = "Queen"
elif Num1 == "13":
    Num1 = "King"
Suit1 = suit_option
Card1 = Num1 + Suit1


print("your first card is the", Num1,"of", suit_option)



suit_option = random.choice(Suits)
number_option2 = random.randint(1,13)
Num2 = str(number_option2)
if Num2 == "1":
    Num2 = "Ace"
elif Num2 == "11":
    Num2 = "Jack"
elif Num2 == "12":
    Num2 = "Queen"
elif Num2 == "13":
    Num2 = "King"
Suit2 = suit_option
Card2 = Num2 + Suit2
while Card2 == Card1:
    suit_option = random.choice(Suits)
    number_option2 = random.randint(1,13)
    Num2 = str(number_option2)
    if Num2 == "1":
        Num2 = "Ace"
    elif Num2 == "11":
        Num2 = "Jack"
    elif Num2 == "12":
        Num2 = "Queen"
    elif Num2 == "13":
        Num2 = "King"
    Suit2 = suit_option
    Card2 = Num2 + Suit2
    

print("your second card is the", Num2,"of", suit_option)


Choice = input("Check, Raise or Fold: ")
if Choice == "Check":
    print("both players check")
elif Choice == "Raise":
    Quantity = int(input("how much do you want to raise by? "))
    while Quantity > Balance:
        int(input("you dont have that many chips, raise again"))
    Balance = Balance - Quantity
elif Choice == "Fold":
    print("you have folded")
    quit()
elif Choice == "All in" or Choice == "e":
    print("opponent calls, skipping all future betting rounds")
else:
    print("program didnt get what it wanted, shutting down")
    quit()

    
    
print("")

suit_option = random.choice(Suits)
number_option3 = random.randint(1,13)
Num3 = str(number_option3)
if Num3 == "1":
    Num3 = "Ace"
elif Num3 == "11":
    Num3 = "Jack"
elif Num3 == "12":
     Num3 = "Queen"
elif Num3 == "13":
    Num3 = "King"
Suit3 = suit_option
Card3 = Num3 + Suit3
while Card3 == Card2 or Card3 == Card1:
    suit_option = random.choice(Suits)
    number_option3 = random.randint(1,13)
    Num3 = str(number_option3)
    if Num3 == "1":
        Num3 = "Ace"
    elif Num3 == "11":
        Num3 = "Jack"
    elif Num3 == "12":
         Num3 = "Queen"
    elif Num3 == "13":
        Num3 = "King"
    Suit3 = suit_option
    Card3 = Num3 + Suit3
    

print("the first card in the flop is the", Num3,"of", suit_option)


suit_option = random.choice(Suits)
number_option4 = random.randint(1,13)
Num4 = str(number_option4)
if Num4 == "1":
    Num4 = "Ace"
elif Num4 == "11":
    Num4 = "Jack"
elif Num4 == "12":
     Num4 = "Queen"
elif Num4 == "13":
    Num4 = "King"
Suit4 = suit_option
Card4 = Num4 + Suit4
while Card4 == Card3 or Card4 == Card2 or Card4 == Card1:
    suit_option = random.choice(Suits)
    number_option4 = random.randint(1,13)
    Num4 = str(number_option4)
    if Num4 == "1":
        Num4 = "Ace"
    elif Num4 == "11":
        Num4 = "Jack"
    elif Num4 == "12":
         Num4 = "Queen"
    elif Num4 == "13":
        Num4 = "King"
    Suit4 = suit_option
    Card4 = Num4 + Suit4
    
print("the second card in the flop is the", Num4,"of", suit_option)


suit_option = random.choice(Suits)
number_option5 = random.randint(1,13)
Num5 = str(number_option5)
if Num5 == "1":
    Num5 = "Ace"
elif Num5 == "11":
    Num5 = "Jack"
elif Num5 == "12":
     Num5 = "Queen"
elif Num5 == "13":
    Num5 = "King"
Suit5 = suit_option
Card5 = Num5 + Suit5
while Card5 == Card4 or Card5 == Card3 or Card5 == Card2 or Card5 == Card1:
    suit_option = random.choice(Suits)
    number_option5 = random.randint(1,13)
    Num5 = str(number_option5)
    if Num5 == "1":
        Num5 = "Ace"
    elif Num5 == "11":
        Num5 = "Jack"
    elif Num5 == "12":
         Num5 = "Queen"
    elif Num5 == "13":
        Num5 = "King"
    Suit5 = suit_option
    Card5 = Num5 + Suit5
    
print("the third card in the flop is the", Num5,"of", suit_option)

if Choice == "All in" or Choice == "e":
    print()
else:
    Choice = input("Check, Raise or Fold: ")
    if Choice == "Check":
        print("both players check")
    elif Choice == "Raise":
        Quantity = int(input("how much do you want to raise by? "))
        while Quantity > Balance:
            int(input("you dont have that many chips, raise again"))
        Balance = Balance - Quantity
    elif Choice == "Fold":
        print("you have folded")
        quit()
    elif Choice == "All in":
        print("opponent calls, skipping all future betting rounds")
    else:
        print("program didnt get what it wanted, shutting down")
        quit()

    
print("")

suit_option = random.choice(Suits)
number_option6 = random.randint(1,13)
Num6 = str(number_option6)
if Num6 == "1":
    Num6 = "Ace"
elif Num6 == "11":
    Num6 = "Jack"
elif Num6 == "12":
     Num6 = "Queen"
elif Num6 == "13":
    Num6 = "King"
Suit6 = suit_option
Card6 = Num6 + Suit6
while Card6 == Card5 or Card6 == Card4 or Card6 == Card3 or Card6 == Card2 or Card6 == Card1:
    suit_option = random.choice(Suits)
    number_option6 = random.randint(1,13)
    Num6 = str(number_option6)
    if Num6 == "1":
        Num6 = "Ace"
    elif Num6 == "11":
        Num6 = "Jack"
    elif Num6 == "12":
         Num6 = "Queen"
    elif Num6 == "13":
        Num6 = "King"
    Suit6 = suit_option
    Card6 = Num6 + Suit6
    
print("the turn is the", Num6,"of", suit_option)


if Choice == "All in" or Choice == "e":
    print()
else:
    Choice = input("Check, Raise or Fold: ")
    if Choice == "Check":
        print("both players check")
    elif Choice == "Raise":
        Quantity = int(input("how much do you want to raise by? "))
        while Quantity > Balance:
            int(input("you dont have that many chips, raise again"))
        Balance = Balance - Quantity
    elif Choice == "Fold":
        print("you have folded")
        quit()
    elif Choice == "All in":
        print("opponent calls, skipping all future betting rounds")
    else:
        print("program didnt get what it wanted, shutting down")
        quit()

print("")

suit_option = random.choice(Suits)
number_option7 = random.randint(1,13)
Num7 = str(number_option7)
if Num7 == "1":
    Num7 = "Ace"
elif Num7 == "11":
    Num7 = "Jack"
elif Num7 == "12":
     Num7 = "Queen"
elif Num7 == "13":
    Num7 = "King"
Suit7 = suit_option
Card7 = Num7 + Suit7
while Card7 == Card6 or Card7 == Card5 or Card7 == Card4 or Card7 == Card3 or Card7 == Card2 or Card7 == Card1:
    suit_option = random.choice(Suits)
    number_option7 = random.randint(1,13)
    Num7 = str(number_option7)
    if Num7 == "1":
        Num7 = "Ace"
    elif Num7 == "11":
        Num7 = "Jack"
    elif Num7 == "12":
         Num7 = "Queen"
    elif Num7 == "13":
        Num7 = "King"
    Suit7 = suit_option
    Card7 = Num7 + Suit7
    
print("the river is the", Num7,"of", suit_option)
print()




Unsorted_suits = []
Unsorted_nums = []

Suit_list = [Suit1,Suit2,Suit3,Suit4,Suit5,Suit6,Suit7]
Num_list = [number_option1,number_option2,number_option3,number_option4,number_option5,number_option6,number_option7]
for i in range(len(Suit_list)):
    Unsorted_suits.append(Suit_list[i])
    Unsorted_nums.append(Num_list[i])
Num_list.sort()
Suit_list.sort()



for i in range(0,6):
    if Num_list[i] == Num_list[i+1] and Pair_num < Num_list[i] and Counter < 1:
        Counter = Counter + 1
        Pair_num = Num_list[i]
        Score = 2
    if Num_list[i] == Num_list[i+1] and Num_list[i] != Pair_num and Counter > 0:
        Counter = Counter + 1
        Score = 3
         

for i in range(0,5):
    if Num_list[i] == Num_list[i+2] and Score < 4:
        Triple_num = Num_list[i]
        if Triple_num == Pair_num:
            Pair_num = 0
        Score = 4


Temp_list = Num_list
Temp_list = list(dict.fromkeys(Temp_list))
if Temp_list[0] == 1:
    Temp_list.append(14)
Length = len(Temp_list)
for i in range(0,Length - 4):
    Num = Temp_list[i]
    if Num + 4 == Temp_list[i+4]:
        Straight_check = "Yes"
        Score = 5


    
for i in range(0,3):
    Flush = []
    for j in range(i,i+5):
        Flush.append(Suit_list[j])
    if Flush[0] == Flush[4]:
        Flush_suit = Suit_list[4]
        Flush_check = "Yes"
        Score = 6


if Triple_num > 0 and Counter > 1:
    Score = 7

    
for i in range(0,4):
    if Num_list[i] == Num_list[i+3] and Score < 8:
        Score = 8


if Flush_check == "Yes" and Straight_check == "Yes":
    Temp_list = []
    for i in range(0,7):
        if Flush_suit == Unsorted_suits[i]:
            Blank.append(i)
    for i in range(0,len(Blank)):
        Temp_list.append(Unsorted_nums[Blank[i]])
    Temp_list.sort()
    Temp_list = list(dict.fromkeys(Temp_list))
    Length = len(Temp_list)
    if Temp_list[0] == 1:
        Temp_list.append(14)
    Length = len(Temp_list)
    for i in range(0,Length - 4):
        Num = Temp_list[i]
        if Num + 4 == Temp_list[i+4]:
            Score = 9
        if Temp_list[Length - 1] == 14 and Temp_list[Length - 2] == 13:
            Score = 10

print(Num_list)


if Score == 0 and Num_list[0] == 1:
    print("You have ace high")
elif Score == 0:
    Num8 = Num_list[6]
    if Num8 == 11:
        Num8 = "Jack"
    elif Num8 == 12:
         Num8 = "Queen"
    elif Num8 == 13:
        Num8 = "King"
    print("You have", Num8, "high")

if Score == 10:
    print("We have a royal flush")
elif Score == 9:
    print("We have a straight flush")
elif Score == 8:
    print("We have a quad")
elif Score == 7:
    print("We have a full house")
elif Score == 6:
    print("We have a flush")
elif Score == 5:
    print("We have a straight")
elif Score == 4:
    print("We have a triple")
elif Score == 3:
    print("We have a pair of pairs")
elif Score == 2:
    print("We have a pair")




    

















