# TODO
# 1. when you bet credit = credit - bet
# 2. add labet credit and bet

from tkinter import *
import random


class Table:
    def __init__(self, master):
        self.master = master
        master.title("Card Game")
        master.configure(background='white', padx=30, pady=30)

        # import card images
        self.cardBackImg = PhotoImage(file="cards/card_back.png")
        self.cardRedImg = PhotoImage(file="cards/ace_of_hearts.png")
        self.cardBlackImg = PhotoImage(file="cards/ace_of_spades.png")

        # create card window
        self.cardWindow = Label(
            master, image=self.cardBackImg, width=222, height=323, bg="white"
        )
        # we need to keep a reference to the image in order to display it http://effbot.org/pyfaq/why-do-my-tkinter-images-not-appear.htm
        self.cardWindow.image = self.cardBackImg
        self.cardWindow.grid()

        # create RED button
        redButtonImg = PhotoImage(file="buttons/redButton.png")
        self.redButton = Button(
            master, image=redButtonImg, bg="white", borderwidth=0, command=lambda: self.click("red")
        )
        self.redButton.image = redButtonImg
        self.redButton.grid()

        # create BLACK button
        blackButtonImg = PhotoImage(file="buttons/blackButton.png")
        self.blackButton = Button(
            master, image=blackButtonImg, bg="white", command=lambda: self.click("black")
        )
        self.blackButton.image = blackButtonImg
        self.blackButton.grid()

        # create CREDIT text
        self.credit = Entry(master, justify=CENTER)
        self.credit.grid()

        # create CASH OUT button
        self.cashOut = Button(
            master, text="CASH OUT", command=lambda: self.cashOutTrigger()
        )
        self.cashOut.grid(pady=20, ipady=10)

        # create BET button
        self.bet = Entry(master, justify=CENTER)
        self.bet.grid()

        # make grid system
        count = 0
        components = [
            self.redButton, self.cardWindow, self.blackButton,
            self.credit, self.cashOut, self.bet
        ]
        for row in range(0, 2):
            for column in range(0, 3):
                components[count].grid(row=row, column=column)
                count += 1
        self.trigger = False

    def click(self, color):
        if len(self.credit.get()) == 0 or len(self.bet.get()) == 0:
            print("Please insert coins first!")
        elif int(self.bet.get()) > int(self.credit.get()):
            print("You don't have enough credit!")
        else:
            print("What button was pressed?", color)
            chance = random.randint(1, 10)
            print(chance)
            self.flipCard(chance)
            self.checkWin(color, chance)

    def cashOutTrigger(self):
        if self.trigger == False:
            print("Pick a color first!")
        elif int(self.bet.get()) > 0:
            aux = int(self.credit.get())
            self.credit.delete(0, END)
            self.credit.insert(0, aux+int(self.bet.get()))
            self.bet.delete(0, END)
            self.bet.insert(0, 0)
            self.trigger = False
        else:
            print("Try to win first!")

    def flipCard(self, chance):
        if 1 <= chance <= 5:
            self.cardWindow.configure(image=self.cardRedImg)
            self.cardWindow.image = self.cardRedImg
        elif 6 <= chance <= 10:
            self.cardWindow.configure(image=self.cardBlackImg)
            self.cardWindow.image = self.cardBlackImg

    def checkWin(self, color, chance):
        if color == "red" and 1 <= chance <= 5:
            print("You win!")
            self.trigger = True
            aux = int(self.bet.get())
            self.bet.delete(0, END)
            self.bet.insert(0, aux*2)
        elif color == "black" and 6 <= chance <= 10:
            print("You win!")
            self.trigger = True
            aux = int(self.bet.get())
            self.bet.delete(0, END)
            self.bet.insert(0, aux*2)
        else:
            print("You lose!")
            self.bet.delete(0, END)
            self.bet.insert(0, 0)
            self.trigger = False


root = Tk()
Table(root)
root.mainloop()
