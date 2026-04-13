import random
import sys
import tkinter as tk
import os
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
Ratings = [0]
Rating = Cycles = Pot = Highscore = Winner = Computers = 0
Record_minirank = Record_minirank2 = Number_option = Num = 0
Record_kicker = Record_kicker2 = Record_kicker3 = Record_kicker4 = 0
Quantity = Count = Extra = 0
Max = Min = 0
Suit = Choice = Tie = ""

import threading

player_action_event = threading.Event()


def Amount_of_players():
    global Computers
    while True:
        tb_val = Textbox.get("1.0", "end")
        try:
            int(tb_val) > 0
            while int(tb_val) < 0 or int(tb_val) > 22:
                print("Value is out of range")
                tb_val = Textbox.get("1.0", "end")
                break
            if int(tb_val) < 20:
                print("In range",int(tb_val))
                Computers = int(tb_val)
                Playing()
                break
                
            break
        except ValueError:
            print("Error")
            tb_val = Textbox.get("1.0", "end")
            break


def Playing():
    global Textbox, Button3
    Button1.destroy()
    Button2.destroy()
    if Computers == 0:
        Textbox = tk.Text(root, height = 12, font = ("Arial", 16))
        Textbox.place(x=600, y=200)
        Button3 = tk.Button(root, text="Confirm", font=("Arial", 18), command = Amount_of_players)
        Button3.place(x=600, y=400)
    else:
        Textbox.destroy()
        Button3.destroy()
        Object = open("Balance.txt", "r").readlines()
        for i in range(0,Computers):
            if Object[i] == "0\n":
                Object[i] = "1000\n"
            Balance.append(int(Object[i]))
        Drawing()
    

    

    

def Drawing():
    global Ace, Ace2    
    # Load and resize the first card
    folder = "Spades"
    files = os.listdir(folder)
    path = os.path.join(folder, files[0])
    img1 = Image.open(path)
    img1 = img1.resize((150, 200), Image.Resampling.LANCZOS)
    Ace = ImageTk.PhotoImage(img1)
    label1 = tk.Label(root, image=Ace)  # Use root, not frame
    label1.image = Ace
    label1.place(x=100 , y=100 )
    
    # Load and resize the second card
    folder = "Spades"
    files = os.listdir(folder)
    path = os.path.join(folder, files[1])
    img2 = Image.open(path)
    img2 = img2.resize((150, 200), Image.Resampling.LANCZOS)
    Ace2 = ImageTk.PhotoImage(img2)
    label2 = tk.Label(root, image=Ace2)  # Use root, not frame
    label2.image = Ace2
    label2.place(x=200 , y=100)

    folder = "Spades"
    files = os.listdir(folder)
    path = os.path.join(folder, files[2])
    img1 = Image.open(path)
    img1 = img1.resize((150, 200), Image.Resampling.LANCZOS)
    Ace = ImageTk.PhotoImage(img1)
    label1 = tk.Label(root, image=Ace)  # Use root, not frame
    label1.image = Ace
    label1.place(x=300 , y=100)

    folder = "Spades"
    files = os.listdir(folder)
    path = os.path.join(folder, files[3])
    img1 = Image.open(path)
    img1 = img1.resize((150, 200), Image.Resampling.LANCZOS)
    Ace = ImageTk.PhotoImage(img1)
    label1 = tk.Label(root, image=Ace)  # Use root, not frame
    label1.image = Ace
    label1.place(x=400 , y=100)
    folder = "Spades"
    files = os.listdir(folder)
    path = os.path.join(folder, files[4])
    img1 = Image.open(path)
    img1 = img1.resize((150, 200), Image.Resampling.LANCZOS)
    Ace = ImageTk.PhotoImage(img1)
    label1 = tk.Label(root, image=Ace)  # Use root, not frame
    label1.image = Ace
    label1.place(x=500 , y=100)
    folder = "Spades"
    files = os.listdir(folder)
    path = os.path.join(folder, files[5])
    img1 = Image.open(path)
    img1 = img1.resize((150, 200), Image.Resampling.LANCZOS)
    Ace = ImageTk.PhotoImage(img1)
    label1 = tk.Label(root, image=Ace)  # Use root, not frame
    label1.image = Ace
    label1.place(x=600 , y=100)
    folder = "Spades"
    files = os.listdir(folder)
    path = os.path.join(folder, files[6])
    img1 = Image.open(path)
    img1 = img1.resize((150, 200), Image.Resampling.LANCZOS)
    Ace = ImageTk.PhotoImage(img1)
    label1 = tk.Label(root, image=Ace)  # Use root, not frame
    label1.image = Ace
    label1.place(x=700 , y=100)
    folder = "Spades"
    files = os.listdir(folder)
    path = os.path.join(folder, files[7])
    img1 = Image.open(path)
    img1 = img1.resize((150, 200), Image.Resampling.LANCZOS)
    Ace = ImageTk.PhotoImage(img1)
    label1 = tk.Label(root, image=Ace)  # Use root, not frame
    label1.image = Ace
    label1.place(x=800 , y=100)
    folder = "Spades"
    files = os.listdir(folder)
    path = os.path.join(folder, files[8])
    img1 = Image.open(path)
    img1 = img1.resize((150, 200), Image.Resampling.LANCZOS)
    Ace = ImageTk.PhotoImage(img1)
    label1 = tk.Label(root, image=Ace)  # Use root, not frame
    label1.image = Ace
    label1.place(x=900 , y=100)
    folder = "Spades"
    files = os.listdir(folder)
    path = os.path.join(folder, files[9])
    img1 = Image.open(path)
    img1 = img1.resize((150, 200), Image.Resampling.LANCZOS)
    Ace = ImageTk.PhotoImage(img1)
    label1 = tk.Label(root, image=Ace)  # Use root, not frame
    label1.image = Ace
    label1.place(x=1000 , y=100)
    folder = "Spades"
    files = os.listdir(folder)
    path = os.path.join(folder, files[10])
    img1 = Image.open(path)
    img1 = img1.resize((150, 200), Image.Resampling.LANCZOS)
    Ace = ImageTk.PhotoImage(img1)
    label1 = tk.Label(root, image=Ace)  # Use root, not frame
    label1.image = Ace
    label1.place(x=1100 , y=100)
    folder = "Spades"
    files = os.listdir(folder)
    path = os.path.join(folder, files[11])
    img1 = Image.open(path)
    img1 = img1.resize((150, 200), Image.Resampling.LANCZOS)
    Ace = ImageTk.PhotoImage(img1)
    label1 = tk.Label(root, image=Ace)  # Use root, not frame
    label1.image = Ace
    label1.place(x=1200 , y=100)
    folder = "Spades"
    files = os.listdir(folder)
    path = os.path.join(folder, files[12])
    img1 = Image.open(path)
    img1 = img1.resize((150, 200), Image.Resampling.LANCZOS)
    Ace = ImageTk.PhotoImage(img1)
    label1 = tk.Label(root, image=Ace)  # Use root, not frame
    label1.image = Ace
    label1.place(x=1300 , y=100)
    folder = "Hearts"
    files = os.listdir(folder)
    path = os.path.join(folder, files[0])
    img1 = Image.open(path)
    img1 = img1.resize((150, 200), Image.Resampling.LANCZOS)
    Ace = ImageTk.PhotoImage(img1)
    label1 = tk.Label(root, image=Ace)  # Use root, not frame
    label1.image = Ace
    label1.place(x=100 , y=200)
    folder = "Hearts"
    files = os.listdir(folder)
    path = os.path.join(folder, files[1])
    img1 = Image.open(path)
    img1 = img1.resize((150, 200), Image.Resampling.LANCZOS)
    Ace = ImageTk.PhotoImage(img1)
    label1 = tk.Label(root, image=Ace)  # Use root, not frame
    label1.image = Ace
    label1.place(x=200 , y=200)
    folder = "Hearts"
    files = os.listdir(folder)
    path = os.path.join(folder, files[2])
    img1 = Image.open(path)
    img1 = img1.resize((150, 200), Image.Resampling.LANCZOS)
    Ace = ImageTk.PhotoImage(img1)
    label1 = tk.Label(root, image=Ace)  # Use root, not frame
    label1.image = Ace
    label1.place(x=300 , y=200)
    folder = "Hearts"
    files = os.listdir(folder)
    path = os.path.join(folder, files[3])
    img1 = Image.open(path)
    img1 = img1.resize((150, 200), Image.Resampling.LANCZOS)
    Ace = ImageTk.PhotoImage(img1)
    label1 = tk.Label(root, image=Ace)  # Use root, not frame
    label1.image = Ace
    label1.place(x=400 , y=200)
    folder = "Hearts"
    files = os.listdir(folder)
    path = os.path.join(folder, files[4])
    img1 = Image.open(path)
    img1 = img1.resize((150, 200), Image.Resampling.LANCZOS)
    Ace = ImageTk.PhotoImage(img1)
    label1 = tk.Label(root, image=Ace)  # Use root, not frame
    label1.image = Ace
    label1.place(x=500 , y=200)
    folder = "Hearts"
    files = os.listdir(folder)
    path = os.path.join(folder, files[5])
    img1 = Image.open(path)
    img1 = img1.resize((150, 200), Image.Resampling.LANCZOS)
    Ace = ImageTk.PhotoImage(img1)
    label1 = tk.Label(root, image=Ace)  # Use root, not frame
    label1.image = Ace
    label1.place(x=600 , y=200)
    folder = "Hearts"
    files = os.listdir(folder)
    path = os.path.join(folder, files[6])
    img1 = Image.open(path)
    img1 = img1.resize((150, 200), Image.Resampling.LANCZOS)
    Ace = ImageTk.PhotoImage(img1)
    label1 = tk.Label(root, image=Ace)  # Use root, not frame
    label1.image = Ace
    label1.place(x=700 , y=200)
    folder = "Hearts"
    files = os.listdir(folder)
    path = os.path.join(folder, files[7])
    img1 = Image.open(path)
    img1 = img1.resize((150, 200), Image.Resampling.LANCZOS)
    Ace = ImageTk.PhotoImage(img1)
    label1 = tk.Label(root, image=Ace)  # Use root, not frame
    label1.image = Ace
    label1.place(x=800 , y=200)
    folder = "Hearts"
    files = os.listdir(folder)
    path = os.path.join(folder, files[8])
    img1 = Image.open(path)
    img1 = img1.resize((150, 200), Image.Resampling.LANCZOS)
    Ace = ImageTk.PhotoImage(img1)
    label1 = tk.Label(root, image=Ace)  # Use root, not frame
    label1.image = Ace
    label1.place(x=900 , y=200)
    folder = "Hearts"
    files = os.listdir(folder)
    path = os.path.join(folder, files[9])
    img1 = Image.open(path)
    img1 = img1.resize((150, 200), Image.Resampling.LANCZOS)
    Ace = ImageTk.PhotoImage(img1)
    label1 = tk.Label(root, image=Ace)  # Use root, not frame
    label1.image = Ace
    label1.place(x=1000 , y=200)
    folder = "Hearts"
    files = os.listdir(folder)
    path = os.path.join(folder, files[10])
    img1 = Image.open(path)
    img1 = img1.resize((150, 200), Image.Resampling.LANCZOS)
    Ace = ImageTk.PhotoImage(img1)
    label1 = tk.Label(root, image=Ace)  # Use root, not frame
    label1.image = Ace
    label1.place(x=1100 , y=200)
    folder = "Hearts"
    files = os.listdir(folder)
    path = os.path.join(folder, files[11])
    img1 = Image.open(path)
    img1 = img1.resize((150, 200), Image.Resampling.LANCZOS)
    Ace = ImageTk.PhotoImage(img1)
    label1 = tk.Label(root, image=Ace)  # Use root, not frame
    label1.image = Ace
    label1.place(x=1200 , y=200)
    folder = "Hearts"
    files = os.listdir(folder)
    path = os.path.join(folder, files[12])
    img1 = Image.open(path)
    img1 = img1.resize((150, 200), Image.Resampling.LANCZOS)
    Ace = ImageTk.PhotoImage(img1)
    label1 = tk.Label(root, image=Ace)  # Use root, not frame
    label1.image = Ace
    label1.place(x=1300 , y=200)
    folder = "Clubs"
    files = os.listdir(folder)
    path = os.path.join(folder, files[0])
    img1 = Image.open(path)
    img1 = img1.resize((150, 200), Image.Resampling.LANCZOS)
    Ace = ImageTk.PhotoImage(img1)
    label1 = tk.Label(root, image=Ace)  # Use root, not frame
    label1.image = Ace
    label1.place(x=100 , y=300)
    folder = "Clubs"
    files = os.listdir(folder)
    path = os.path.join(folder, files[1])
    img1 = Image.open(path)
    img1 = img1.resize((150, 200), Image.Resampling.LANCZOS)
    Ace = ImageTk.PhotoImage(img1)
    label1 = tk.Label(root, image=Ace)  # Use root, not frame
    label1.image = Ace
    label1.place(x=200 , y=300)
    folder = "Clubs"
    files = os.listdir(folder)
    path = os.path.join(folder, files[2])
    img1 = Image.open(path)
    img1 = img1.resize((150, 200), Image.Resampling.LANCZOS)
    Ace = ImageTk.PhotoImage(img1)
    label1 = tk.Label(root, image=Ace)  # Use root, not frame
    label1.image = Ace
    label1.place(x=300 , y=300)
    folder = "Clubs"
    files = os.listdir(folder)
    path = os.path.join(folder, files[3])
    img1 = Image.open(path)
    img1 = img1.resize((150, 200), Image.Resampling.LANCZOS)
    Ace = ImageTk.PhotoImage(img1)
    label1 = tk.Label(root, image=Ace)  # Use root, not frame
    label1.image = Ace
    label1.place(x=400 , y=300)
    folder = "Clubs"
    files = os.listdir(folder)
    path = os.path.join(folder, files[4])
    img1 = Image.open(path)
    img1 = img1.resize((150, 200), Image.Resampling.LANCZOS)
    Ace = ImageTk.PhotoImage(img1)
    label1 = tk.Label(root, image=Ace)  # Use root, not frame
    label1.image = Ace
    label1.place(x=500 , y=300)
    folder = "Clubs"
    files = os.listdir(folder)
    path = os.path.join(folder, files[5])
    img1 = Image.open(path)
    img1 = img1.resize((150, 200), Image.Resampling.LANCZOS)
    Ace = ImageTk.PhotoImage(img1)
    label1 = tk.Label(root, image=Ace)  # Use root, not frame
    label1.image = Ace
    label1.place(x=600 , y=300)
    folder = "Clubs"
    files = os.listdir(folder)
    path = os.path.join(folder, files[6])
    img1 = Image.open(path)
    img1 = img1.resize((150, 200), Image.Resampling.LANCZOS)
    Ace = ImageTk.PhotoImage(img1)
    label1 = tk.Label(root, image=Ace)  # Use root, not frame
    label1.image = Ace
    label1.place(x=700 , y=300)
    folder = "Clubs"
    files = os.listdir(folder)
    path = os.path.join(folder, files[7])
    img1 = Image.open(path)
    img1 = img1.resize((150, 200), Image.Resampling.LANCZOS)
    Ace = ImageTk.PhotoImage(img1)
    label1 = tk.Label(root, image=Ace)  # Use root, not frame
    label1.image = Ace
    label1.place(x=800 , y=300)
    folder = "Clubs"
    files = os.listdir(folder)
    path = os.path.join(folder, files[8])
    img1 = Image.open(path)
    img1 = img1.resize((150, 200), Image.Resampling.LANCZOS)
    Ace = ImageTk.PhotoImage(img1)
    label1 = tk.Label(root, image=Ace)  # Use root, not frame
    label1.image = Ace
    label1.place(x=900 , y=300)
    folder = "Clubs"
    files = os.listdir(folder)
    path = os.path.join(folder, files[9])
    img1 = Image.open(path)
    img1 = img1.resize((150, 200), Image.Resampling.LANCZOS)
    Ace = ImageTk.PhotoImage(img1)
    label1 = tk.Label(root, image=Ace)  # Use root, not frame
    label1.image = Ace
    label1.place(x=1000 , y=300)
    folder = "Clubs"
    files = os.listdir(folder)
    path = os.path.join(folder, files[10])
    img1 = Image.open(path)
    img1 = img1.resize((150, 200), Image.Resampling.LANCZOS)
    Ace = ImageTk.PhotoImage(img1)
    label1 = tk.Label(root, image=Ace)  # Use root, not frame
    label1.image = Ace
    label1.place(x=1100 , y=300)
    folder = "Clubs"
    files = os.listdir(folder)
    path = os.path.join(folder, files[11])
    img1 = Image.open(path)
    img1 = img1.resize((150, 200), Image.Resampling.LANCZOS)
    Ace = ImageTk.PhotoImage(img1)
    label1 = tk.Label(root, image=Ace)  # Use root, not frame
    label1.image = Ace
    label1.place(x=1200 , y=300)
    folder = "Clubs"
    files = os.listdir(folder)
    path = os.path.join(folder, files[12])
    img1 = Image.open(path)
    img1 = img1.resize((150, 200), Image.Resampling.LANCZOS)
    Ace = ImageTk.PhotoImage(img1)
    label1 = tk.Label(root, image=Ace)  # Use root, not frame
    label1.image = Ace
    label1.place(x=1300 , y=300)
    folder = "Diamonds"
    files = os.listdir(folder)
    path = os.path.join(folder, files[0])
    img1 = Image.open(path)
    img1 = img1.resize((150, 200), Image.Resampling.LANCZOS)
    Ace = ImageTk.PhotoImage(img1)
    label1 = tk.Label(root, image=Ace)  # Use root, not frame
    label1.image = Ace
    label1.place(x=100 , y=400)
    folder = "Diamonds"
    files = os.listdir(folder)
    path = os.path.join(folder, files[1])
    img1 = Image.open(path)
    img1 = img1.resize((150, 200), Image.Resampling.LANCZOS)
    Ace = ImageTk.PhotoImage(img1)
    label1 = tk.Label(root, image=Ace)  # Use root, not frame
    label1.image = Ace
    label1.place(x=200 , y=400)
    folder = "Diamonds"
    files = os.listdir(folder)
    path = os.path.join(folder, files[2])
    img1 = Image.open(path)
    img1 = img1.resize((150, 200), Image.Resampling.LANCZOS)
    Ace = ImageTk.PhotoImage(img1)
    label1 = tk.Label(root, image=Ace)  # Use root, not frame
    label1.image = Ace
    label1.place(x=300 , y=400)
    folder = "Diamonds"
    files = os.listdir(folder)
    path = os.path.join(folder, files[3])
    img1 = Image.open(path)
    img1 = img1.resize((150, 200), Image.Resampling.LANCZOS)
    Ace = ImageTk.PhotoImage(img1)
    label1 = tk.Label(root, image=Ace)  # Use root, not frame
    label1.image = Ace
    label1.place(x=400 , y=400)
    folder = "Diamonds"
    files = os.listdir(folder)
    path = os.path.join(folder, files[4])
    img1 = Image.open(path)
    img1 = img1.resize((150, 200), Image.Resampling.LANCZOS)
    Ace = ImageTk.PhotoImage(img1)
    label1 = tk.Label(root, image=Ace)  # Use root, not frame
    label1.image = Ace
    label1.place(x=500 , y=400)
    folder = "Diamonds"
    files = os.listdir(folder)
    path = os.path.join(folder, files[5])
    img1 = Image.open(path)
    img1 = img1.resize((150, 200), Image.Resampling.LANCZOS)
    Ace = ImageTk.PhotoImage(img1)
    label1 = tk.Label(root, image=Ace)  # Use root, not frame
    label1.image = Ace
    label1.place(x=600 , y=400)
    folder = "Diamonds"
    files = os.listdir(folder)
    path = os.path.join(folder, files[6])
    img1 = Image.open(path)
    img1 = img1.resize((150, 200), Image.Resampling.LANCZOS)
    Ace = ImageTk.PhotoImage(img1)
    label1 = tk.Label(root, image=Ace)  # Use root, not frame
    label1.image = Ace
    label1.place(x=700 , y=400)
    folder = "Diamonds"
    files = os.listdir(folder)
    path = os.path.join(folder, files[7])
    img1 = Image.open(path)
    img1 = img1.resize((150, 200), Image.Resampling.LANCZOS)
    Ace = ImageTk.PhotoImage(img1)
    label1 = tk.Label(root, image=Ace)  # Use root, not frame
    label1.image = Ace
    label1.place(x=800 , y=400)
    folder = "Diamonds"
    files = os.listdir(folder)
    path = os.path.join(folder, files[8])
    img1 = Image.open(path)
    img1 = img1.resize((150, 200), Image.Resampling.LANCZOS)
    Ace = ImageTk.PhotoImage(img1)
    label1 = tk.Label(root, image=Ace)  # Use root, not frame
    label1.image = Ace
    label1.place(x=900 , y=400)
    folder = "Diamonds"
    files = os.listdir(folder)
    path = os.path.join(folder, files[9])
    img1 = Image.open(path)
    img1 = img1.resize((150, 200), Image.Resampling.LANCZOS)
    Ace = ImageTk.PhotoImage(img1)
    label1 = tk.Label(root, image=Ace)  # Use root, not frame
    label1.image = Ace
    label1.place(x=1000 , y=400)
    folder = "Diamonds"
    files = os.listdir(folder)
    path = os.path.join(folder, files[10])
    img1 = Image.open(path)
    img1 = img1.resize((150, 200), Image.Resampling.LANCZOS)
    Ace = ImageTk.PhotoImage(img1)
    label1 = tk.Label(root, image=Ace)  # Use root, not frame
    label1.image = Ace
    label1.place(x=1100 , y=400)
    folder = "Diamonds"
    files = os.listdir(folder)
    path = os.path.join(folder, files[11])
    img1 = Image.open(path)
    img1 = img1.resize((150, 200), Image.Resampling.LANCZOS)
    Ace = ImageTk.PhotoImage(img1)
    label1 = tk.Label(root, image=Ace)  # Use root, not frame
    label1.image = Ace
    label1.place(x=1200 , y=400)
    folder = "Diamonds"
    files = os.listdir(folder)
    path = os.path.join(folder, files[12])
    img1 = Image.open(path)
    img1 = img1.resize((150, 200), Image.Resampling.LANCZOS)
    Ace = ImageTk.PhotoImage(img1)
    label1 = tk.Label(root, image=Ace)  # Use root, not frame
    label1.image = Ace
    label1.place(x=1300 , y=400)





#def Bet_Graphic():
    global Button4, Button5
    #Button4 = tk.Button(root, text="Check", font=("Arial", 30), command = Checking)
    #Button4.place(x=600, y=100)
    #Button5 = tk.Button(root, text="  Bet  ", font=("Arial", 30), command = Betting)
    #Button5.place(x=800, y=100)

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
        for i in range(2,(2 * Computers) + 5):
            Cards_Test()
        for i in range(0,Computers):
            Current_Bets.append(1)
        Bet()

def Trust_me_Bro():
    global Quantity, Textbox2
    while True:
        tb_val = Textbox2.get("1.0", "end")
        try:
            int(tb_val) > 0
            while int(tb_val) < 0 or int(tb_val) % 10 != 0: ##And greater than a blind
                print("Bet must be a positive multiple of 10")
                tb_val = Textbox2.get("1.0", "end")
                break
            if int(tb_val) > 0 and int(tb_val) % 10 == 0:
                print("In range",int(tb_val))
                Quantity = int(tb_val)
                Betting()
                break
                
            break
        except ValueError:
            print("Error")
            tb_val = Textbox2.get("1.0", "end")
            break





def Reraise_Graphic():
    global Button7, Button8, Button9
    print("In the reraise graphic")
    Label10 = tk.Label(root, text = str(Extra) + " to call", font = ("Arial", 20))
    Label10.place(x=1000, y=400)
    Button7 = tk.Button(root, text=" Call ", font=("Arial", 30), command = Calling)
    Button7.place(x=600, y=100)
    Button8 = tk.Button(root, text="  Raise  ", font=("Arial", 30), command = Raising)
    Button8.place(x=800, y=100)
    Button9 = tk.Button(root, text="  Fold  ", font=("Arial", 30), command = Folding)
    Button9.place(x=1000, y=100)
    print("UGh")

    

    
def Calling():
    global Choice2, Button7, Button8, Button9
    print("Buttons to be killed")
    Choice2 = "Call"
    Button7.destroy()
    Button8.destroy()
    Button9.destroy()
    player_action_event.set()
    root.update()
    Player_raise()
    

def Raising():
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



def Tutorial():
    print("%")
    Tutorial = open("Tutorial.txt", "r")
    print(Tutorial.read())
    sys.exit()
    


print("Computers is", Computers)
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
    global Balance, Choice, Pot, Cycles, Quantity
    Ratings = [0]
    Current_Bets = []  
    print("Bet has been called") 
    if Choice == "All in" or Choice == "all in" or Choice == "e" or Choice == "A" or Choice == "a":
        Cycles = 4
        print()
    else:
        print("Choice is", Choice)
        if Choice == "Check" or Choice == "check" or Choice == "C" or Choice == "c" :
            for i in range(1,Computers):
                Computer_Decision(i)
            for i in range(1,Computers):
                Computer_Check(i)

                
        elif Choice == "Bet" or Choice == "bet" or Choice == "B" or Choice == "b":
            Balance[0] = Balance[0] - Quantity
            Pot = Pot + Quantity

            for i in range(1,Computers):
                Computer_Decision(i)
            for i in range(1,Computers):
                Computer_Bet(i)
                
        elif Choice == "Fold" or Choice == "fold" or Choice == "F" or Choice == "f":
            print("you have folded")
            for i in range(0,Computers):
                Computer_fold(i) #idk what the hell happened here but hey
            quit()
            
        elif Choice == "All in" or Choice == "all in" or Choice == "e" or Choice == "A" or Choice == "a":
            print("opponent calls, skipping all future betting rounds")
            Pot = Pot + Balance[0]
            Balance[0] = 0

        elif Choice == "End" or Choice == "end":
            with open("Player_count.txt", "w") as Object2:
                Object2.write("")
            sys.exit()

            
        else:
            print("Try again")
            quit()
            Bet()
        Cycles = Cycles + 1
        print()
        
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
                print("Triple")
                Triple_num = Num_list[i]
                Rating = (3*Num_list[i] + 50)
                #Triple
                
        for i in range(0,len(Num_list) - 1):
            if Num_list[i] == Num_list[i+1] and Num_list[i] != Triple_num:
                print("Pair")
                Pair_num = Num_list[i]
                Rating = (2*Num_list[i] + 40)
               #Pair
                
        for i in range(0,len(Num_list) - 3):
            if Num_list[i] == Num_list[i+3]:
                print("Quad")
                Rating = (4*Num_list[i] + 60)
                #Quad
                
        for i in range(0,len(Num_list) - 1):
            if Num_list[i] == Num_list[i+1] and Num_list[i] < Pair_num and Rating < ((3*Pair_num) + (2*Num_list[i]) + 30):
                print("Two pair")
                Rating = (3*Pair_num) + (2*Num_list[i]) + 30
                print("Rating from 2 pair is", Rating)
                #Two pair

        for i in range (0,len(Num_list) - 2):
            if Num_list[i] == Num_list[i+2] and Pair_num > 0 and Rating < (5*Triple_num) + (2*Pair_num) + 40:
                print("Full house!")
                Rating = (5*Triple_num) + (2*Pair_num) + 400

        print("Rating is", Rating)



        Temp_list = list(dict.fromkeys(Num_list))
        for i in range(0,len(Num_list)):
            if Num_list[i] == 14:
                Temp_list.insert(0,1)


            for i in range(0,len(Temp_list)-2):
                Num = Temp_list[i]
                if Num + 2 == Temp_list[i+2] and Rating < (2*Temp_list[i+2] + 40):
                    print("3 straight")
                    Rating = (2*Temp_list[i+2] + 40)
                    #3 straight

            for i in range(0,len(Temp_list)-3):
                Num = Temp_list[i]
                if Num + 4 == Temp_list[i+3] and Rating < (2*Temp_list[i+3] + 50):
                    print("4 straight gapped")
                    Rating = (2*Temp_list[i+3] + 50)
                    #4 straight gapped
                    
            for i in range(0,len(Temp_list)-3):
                Num = Temp_list[i]
                if Num + 3 == Temp_list[i+3] and Rating < (2*Temp_list[i+3] + 55):
                    print("4 straight")
                    Rating = (2*Temp_list[i+3] + 55)
                    #4 straight

            for i in range(0,len(Temp_list)-4):
                Num = Temp_list[i]
                if Num + 4 == Temp_list[i+4] and Rating < (2*Temp_list[i+4] + 70):
                    print("5 straight")
                    Rating = (2*Temp_list[i+4] + 70)
                    #5 straight


        for i in range(0,len(Suit_list)-2):
            if Suit_list[i] == Suit_list[i+2] and Rating < 40:
                print("3 flush")
                Rating = 40
                #3 Flush

        for i in range(0,len(Suit_list)-3):
            if Suit_list[i] == Suit_list[i+3] and Rating < 75:
                print("4 flush")
                Rating = 75
                #4 Flush
                
        for i in range(0,len(Suit_list)-4):
            if Suit_list[i] == Suit_list[i+4] and Rating < 90:
                print("5 flush")
                Rating = 90
                #5 Flush

    
            
    if Cycles == 3:
        Ranking_System(i)
        print(Score)
        Rating = Score * 10

    Bluff = random.randint(1,100)
    if Bluff < (Rating * 0.2) + 10:
        Bluffs.append(i)
                
    for j in range(0,len(Bluffs)):
        if i == Bluffs[j]:
            Rating = random.randint(70,100)

    Ratings.append(Rating)



def Computer_Check(i):
    for j in range(0,len(Folds)):
        if i == Folds[j]:
            return
    if Ratings[i] <= 20:
        print("Computer", i, "Checks")
    elif Ratings[i] <= 40:
        print("Computer", i, "Checks")
    elif Ratings[i] <= 60:
        print("Computer", i, "Checks")
    elif Ratings[i] <= 80:
        print("Computer", i, "Checks")
    else:
        Computer_Raise(i)
        




def Computer_Bet(i):
    global Count, Extra, Pot
    Balance[i] = Balance[i] - Quantity
    Pot = Pot + Quantity

    for j in range(0,len(Folds)):
        if i == Folds[j]:
            return
    if Ratings[i] <= 20:
        print("Computer", i, "Folds")
        Computer_Fold(i)
    elif Ratings[i] <= 40:
        print("Computer", i, "Folds")
        Computer_Fold(i)
    elif Ratings[i] <= 60:
        print("Computer", i, "Folds")
        Computer_Fold(i)
    elif Ratings[i] <= 80:
        print("Computer", i, "Calls")
    else:
        Computer_Raise(i)



def Computer_Fold(i):
    print("Computer", i, "Folds")
    Folds.append(i)
 


def Computer_Raise(i):
    global Pot, Counting, Max
    Max = 0
    if Quantity > 0:
        Current_Bets[0] = Quantity
    Replacement = i
    Extra = random.randint(100,100)
    Condition = False
    def step():
        nonlocal Replacement

        # --- First for-loop ---
        for j in range(Replacement, Computers):
            if j in Folds or Current_Bets[j] == Max:
                break
            elif Ratings[j] < 20:
                Computer_Fold(j)
                break
            elif Ratings[j] > 80:
                print("Going into ReRaise")
                Computer_Reraise(j)
                Replacement = j
                break
            else:
                Balance[j] = Max - Current_Bets[j]
                Current_Bets[j] = Max
                # POT

        # --- Player action check ---
        if Current_Bets[0] != Max:
            print("Inside the if")
            player_action_event.clear()
            Reraise_Graphic()
            # ❗ NO root.update() ANYWHERE
            # GUI remains fully responsive
            root.after(1, wait_for_player)
            return
        
        # Continue immediately to second half
        second_half()

    # --- WAIT LOOP for player without freezing ---
    def wait_for_player():
        if not player_action_event.is_set():
            root.after(10, wait_for_player)
            return

        print("After gate closed")
        second_half()

    # --- Second for-loop ---
    def second_half():
        nonlocal Replacement

        for j in range(1, Replacement):
            if j in Folds or Current_Bets[j] == Max:
                break
            elif Ratings[j] < 20:
                Computer_Fold(j)
                break
            elif Ratings[j] > 80:
                Computer_Reraise(j)
                Replacement = j
                break
            else:
                print("Balance is", Balance[j])
                print("J is", j)
                Balance[j] = Max - Current_Bets[j]
                Current_Bets[j] = Max
                # POT

        # End condition of original while-loop
        if Max != Min:
            root.after(1, step)   # continue looping without freezing
            return

        # If finished, do final pot calculation
        finish()

    def finish():
        for j in range(0, len(Current_Bets)):
            Pot = Pot + Current_Bets[j]

        if Quantity == 0:
            print("Computer", Replacement, "Bets", Extra)
        else:
            print("Computer", Replacement, "Raises by", Extra)

    # Start first step
    step()

    if Quantity == 0:
        print("Computer", Replacement, "Bets ", Extra)
    else:
        print("Computer", Replacement, "Raises by ", Extra)


def Computer_Reraise(j):
        global Max, Min, Extra
        Extra = random.randint(100,100) + Extra
        Current_Bets[j] = Current_Bets[j] + Extra
        Max = max(Current_Bets)
        Min = min(Current_Bets)
        print("Max is", Max)
        print("Min is", Min)
        Current_Bets[j] = Max
        
def Player_raise(): 
    global Max, Choice2
    print("In player raise")
    if Choice2 == "Call" or Choice2 == "call" or Choice2 == "C" or Choice2 == "c" :
        print("You call")
        Balance[0] = Balance[0] - (Max - Current_Bets[0])
        Current_Bets[0] = Max
    elif Choice2 == "Raise" or Choice2 == "raise" or Choice2 == "R" or Choice2 == "r":
        Extra = int(input("How much do you want to raise by? "))
        while Extra > Balance[0] or (Extra + Current_Bets[0]) < Max:
            Extra = int(input("Insufficient, raise again "))
        Balance[0] = Balance[0]  - Extra
        Current_Bets[0] = Current_Bets[0] + Extra
        Max = Current_Bets[0]
    elif Choice2 == "Fold" or Choice2 == "fold" or Choice2 == "F" or Choice2 == "f":
        print("You have folded")
        Computer_Fold(i)
        quit()

    
for i in range(0,51):
    Cards_Test()
for i in range(0,Computers):
    Current_Bets.append(1)


root.geometry("1800x1500")
root.title("Poker")
Label = tk.Label(root, text = "Hello.", font = ("Arial", 20))
Label.pack(padx = 20, pady = 20)

Button1 = tk.Button(root, text="Start", font=("Arial", 18), command = Playing)
Button1.pack()
                 
Button2 = tk.Button(root, text="Secondary", font=("Arial", 18), command = Tutorial)
Button2.pack()

    
root.mainloop()

print("Line 893, Computers is", Computers)




print("You have", Balance, "Chips")
print("Your first card is the",Cards[0])
print("Your second card is the",Cards[1])
#Bet()
print("The first card of the flop is the",Cards[-5])
print("The second card of the flop is the",Cards[-4])
print("The third card of the flop is the",Cards[-3])
#Bet()
print("The turn is the",Cards[-2])
#Bet()
print("The river is the",Cards[-1])
#Bet()
print()


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
    Balance[Winner] = Balance[Winner] + Pot
    
with open("Balance.txt", "w") as f:
    for i in range(0,len(Balance)):
        f.write(str(Balance[i]) + "\n")

print("Ratings is", Ratings)