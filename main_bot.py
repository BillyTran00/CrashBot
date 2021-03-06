import tkinter as tk
import betting as bet
from tkinter import messagebox
import threading as t


class Main:

    def __init__(self):
        self.stake = bet.Bot()
        self.roobet = bet.Roobet()

    def quitBot(self, canvas):
        self.stake.stopBot()
        self.roobet.stopBot()
        canvas.quit()

    def startBotStake(self, lossStreak, baseBetAmount=0.03):

        if str.isdigit(lossStreak):
            if int(lossStreak) <= 0:
                tk.messagebox.showwarning(title="Warning", message="Please Enter an Integer Higher than 0")
            else:
                botThread = t.Thread(target=(self.stake.runBot), args=(int(lossStreak), float(baseBetAmount), ))
                botThread.start()

        else:
            tk.messagebox.showwarning(title="Warning", message="Please Enter an Integer")

    def startBotRoobet(self, lossStreak=3, baseBetAmount=0.02):

        if str.isdigit(lossStreak):
            if int(lossStreak) <= 0:
                tk.messagebox.showwarning(title="Warning", message="Please Enter an Integer Higher than 0")
            else:
                botThread = t.Thread(target=(self.roobet.runBot), args=(int(lossStreak), float(baseBetAmount), ))
                botThread.start()

        else:
            tk.messagebox.showwarning(title="Warning", message="Please Enter an Integer")
        
    def draw(self, canvas): 
            
        #Set up Canvas
        canvas.title("Crash Bot")
        canvas.minsize(width=250, height=250)
        canvas.resizable(0, 0)

        #Make bottom frame
        bottomFrame = tk.Frame(canvas,width=100, height=100)
        bottomFrame.grid(row=1, column=0)

        #Description
        tk.Label(canvas, text=" Enter the Desired Loss Streak ").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(canvas, text=" Enter the Base Bet Amount ").grid(row=1, column=0, padx=10, pady=10)

        #Entry Field
        desiredLossField = tk.Entry(bottomFrame, width=10)
        desiredLossField.grid(row=0, column=0, padx=5, pady=5)
        baseBetField = tk.Entry(bottomFrame, width=10)
        baseBetField.grid(row=2, column=0, padx=15, pady=15)

        #Button
        tk.Button(bottomFrame, text="Stake",
                command=lambda: self.startBotStake(desiredLossField.get(), baseBetField.get())).grid(row=0, column=1)
        tk.Button(bottomFrame, text="Roobet",
                command=lambda: self.startBotRoobet(desiredLossField.get(), baseBetField.get())).grid(row=0, column=2, padx=4)
        
        tk.Button(bottomFrame, text="Quit",
                command=lambda: self.quitBot(canvas)).grid(row=2, column=2, pady=5)


#Set Up

canvas = tk.Tk()
program = Main()

program.draw(canvas)
canvas.mainloop()
