# TO DO
# 3. import what we need not all library
# 6. improve aspect / clean code


from tkinter import *
from cards import *
import random


class CardGame:
    def __init__(self, master):
        self.master = master
        master.title("Card Game")
        master.configure(background='white', padx=30, pady=30)

        # import card images
        self.cardBackImg = PhotoImage(file="cards/card_back.png")

        self.cardRedImg = [
            PhotoImage(file="cards/ace_of_hearts.png"),
            PhotoImage(file="cards/ace_of_diamonds.png"),
            PhotoImage(file="cards/2_of_hearts.png"),
            PhotoImage(file="cards/2_of_diamonds.png"),
            PhotoImage(file="cards/3_of_hearts.png"),
            PhotoImage(file="cards/3_of_diamonds.png"),
            PhotoImage(file="cards/4_of_hearts.png"),
            PhotoImage(file="cards/4_of_diamonds.png"),
            PhotoImage(file="cards/5_of_hearts.png"),
            PhotoImage(file="cards/5_of_diamonds.png"),
            PhotoImage(file="cards/6_of_hearts.png"),
            PhotoImage(file="cards/6_of_diamonds.png"),
            PhotoImage(file="cards/7_of_hearts.png"),
            PhotoImage(file="cards/7_of_diamonds.png"),
            PhotoImage(file="cards/8_of_hearts.png"),
            PhotoImage(file="cards/8_of_diamonds.png"),
            PhotoImage(file="cards/9_of_hearts.png"),
            PhotoImage(file="cards/9_of_diamonds.png"),
            PhotoImage(file="cards/10_of_hearts.png"),
            PhotoImage(file="cards/10_of_diamonds.png"),
            PhotoImage(file="cards/jack_of_hearts.png"),
            PhotoImage(file="cards/jack_of_diamonds.png"),
            PhotoImage(file="cards/queen_of_hearts.png"),
            PhotoImage(file="cards/queen_of_diamonds.png"),
            PhotoImage(file="cards/king_of_hearts.png"),
            PhotoImage(file="cards/king_of_diamonds.png")
        ]
        self.cardBlackImg = [
            PhotoImage(file="cards/ace_of_spades.png"),
            PhotoImage(file="cards/ace_of_clubs.png"),
            PhotoImage(file="cards/2_of_spades.png"),
            PhotoImage(file="cards/2_of_clubs.png"),
            PhotoImage(file="cards/3_of_spades.png"),
            PhotoImage(file="cards/3_of_clubs.png"),
            PhotoImage(file="cards/4_of_spades.png"),
            PhotoImage(file="cards/4_of_clubs.png"),
            PhotoImage(file="cards/5_of_spades.png"),
            PhotoImage(file="cards/5_of_clubs.png"),
            PhotoImage(file="cards/6_of_spades.png"),
            PhotoImage(file="cards/6_of_clubs.png"),
            PhotoImage(file="cards/7_of_spades.png"),
            PhotoImage(file="cards/7_of_clubs.png"),
            PhotoImage(file="cards/8_of_spades.png"),
            PhotoImage(file="cards/8_of_clubs.png"),
            PhotoImage(file="cards/9_of_spades.png"),
            PhotoImage(file="cards/9_of_clubs.png"),
            PhotoImage(file="cards/10_of_spades.png"),
            PhotoImage(file="cards/10_of_clubs.png"),
            PhotoImage(file="cards/jack_of_spades.png"),
            PhotoImage(file="cards/jack_of_clubs.png"),
            PhotoImage(file="cards/queen_of_spades.png"),
            PhotoImage(file="cards/queen_of_clubs.png"),
            PhotoImage(file="cards/king_of_spades.png"),
            PhotoImage(file="cards/king_of_clubs.png")
        ]

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
        self.credit.insert(0, "CREDIT")

        # create CASH OUT button
        self.cashOut = Button(
            master, text="CASH OUT", command=lambda: self.cashOutTrigger()
        )
        self.cashOut.grid(pady=20, ipady=10)

        # create BET entry
        self.bet = Entry(master, justify=CENTER)
        self.bet.grid()
        self.bet.insert(0, "BET")

        # create INFO
        self.info = Entry(master,
                          justify=CENTER,
                          state=DISABLED,
                          disabledbackground="orange",
                          disabledforeground="white")
        self.info.grid(column=1, ipadx=20)

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
        self.credit.bind(
            "<FocusIn>", lambda event: self.clear_placeholder(event, self.credit,))  # so i didnt get error about the parameters of the function
        self.credit.bind(
            "<FocusOut>", lambda event: self.add_placeholder(event, self.credit,  "CREDIT"))  # if you change placeholder be sure to change `def click()` ifs too

        self.bet.bind(
            "<FocusIn>", lambda event: self.clear_placeholder(event, self.bet))
        self.bet.bind(
            "<FocusOut>", lambda event: self.add_placeholder(event, self.bet, "BET"))  # if you change placeholder be sure to change `def click()` ifs too

    # adds placeholder to the both entries
    def add_placeholder(self, event, whatEntry, placeholder):
        if not whatEntry.get() or whatEntry.get() == "0":
            whatEntry.delete(0, END)
            whatEntry.insert(0, placeholder)

    # clean placeholder to the both entries
    def clear_placeholder(self, event, whatEntry):
        if whatEntry.get() == "CREDIT" or whatEntry.get() == "BET":
            whatEntry.delete(0, END)

    def click(self, color):  # what happen when you click a color
        if len(self.credit.get()) == 0 or self.credit.get() == "CREDIT":
            print("Please insert coins first!")
            self.infoDisplay("Please insert coins first!", "orange")
        elif len(self.bet.get()) == 0 or self.bet.get() == "BET":
            print("Please bet first!")
            self.infoDisplay("Please bet first!", "orange")
        elif int(self.bet.get()) > int(self.credit.get()) and self.trigger is False:
            print("You don't have enough credit!")
            self.infoDisplay("You don't have enough credit!", "orange")
        else:
            chance = random.randint(1, 10)
            print(chance)
            self.takeCredit()
            self.flipCard(chance)
            self.checkWin(color, chance)
            self.disableBet()

    def cashOutTrigger(self):  # take coins out
        if len(self.credit.get()) == 0 or len(self.bet.get()) == 0:
            print("Please insert coins first!")
            self.infoDisplay("Please insert coins first!", "orange")
        elif self.trigger is False:
            print("Pick a color first!")
            self.infoDisplay("Pick a color first!", "orange")
        elif int(self.bet.get()) > 0:
            print("DONE!")
            self.infoDisplay("DONE!", "yellow")
            self.bet.configure(state=NORMAL)
            aux = int(self.credit.get())
            self.credit.delete(0, END)
            self.credit.insert(0, aux+int(self.bet.get()))
            self.bet.delete(0, END)
            self.trigger = False
        else:
            print("Try to win first!")
            self.infoDisplay("Try to win first!", "orange")

    def infoDisplay(self, outputText, color):  # display some usefull information
        self.info.configure(state=NORMAL)  # so we can modify it
        self.info.delete(0, END)
        self.info.insert(0, outputText)
        self.info.configure(
            disabledbackground=color,
            state=DISABLED  # return to the first state
        )

    def takeCredit(self):  # when you bet take credit
        if self.trigger is False:
            aux = int(self.credit.get())
            self.credit.delete(0, END)
            self.credit.insert(0, aux-int(self.bet.get()))

    def disableBet(self):  # so you cant edit bet after first shot
        if self.trigger is False:
            print("false output")
            self.bet.configure(state=NORMAL)
        else:
            print("true output")
            self.bet.configure(state=DISABLED)

    def flipCard(self, chance):  # change card according to the color
        # random choose one card from the lists
        cardsRandom = random.randint(0, len(self.cardRedImg))
        if 1 <= chance <= 5:
            self.cardWindow.configure(image=self.cardRedImg[cardsRandom])
            self.cardWindow.image = self.cardRedImg[cardsRandom]
        elif 6 <= chance <= 10:
            self.cardWindow.configure(image=self.cardBlackImg[cardsRandom])
            self.cardWindow.image = self.cardBlackImg[cardsRandom]

    def checkWin(self, color, chance):  # verify if is a win or a lose
        if color == "red" and 1 <= chance <= 5:
            print("You win!")
            self.infoDisplay("You win!", "green")
            self.bet.configure(state=NORMAL)
            self.trigger = True
            aux = int(self.bet.get())
            self.bet.delete(0, END)
            self.bet.insert(0, aux*2)
            self.bet.configure(state=DISABLED)
        elif color == "black" and 6 <= chance <= 10:
            print("You win!")
            self.infoDisplay("You win!", "green")
            self.bet.configure(state=NORMAL)
            self.trigger = True
            aux = int(self.bet.get())
            self.bet.delete(0, END)
            self.bet.insert(0, aux*2)
            self.bet.configure(state=DISABLED)
        else:
            print("You lose!")
            self.infoDisplay("You lose!", "tomato")
            self.bet.configure(state=NORMAL)
            self.bet.delete(0, END)
            self.trigger = False
            self.bet.configure(state=DISABLED)


root = Tk()
CardGame(root)
root.mainloop()
