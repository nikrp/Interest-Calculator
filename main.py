# Imports
from tkinter import *
from comp_interest_calulator import comp
from simp_interest_calculator import simple

# Window Settings
window = Tk()
window.title("Interest Calculator from Nikhil")
window.minsize(width=800, height=100)

# Interest Labels
yearLabel = Label(window, text="Time:")
yearLabel.grid(row=0, column=0)

yearLabel1 = Label(window, text="year(s)")
yearLabel1.grid(row=0, column=2)

amtLabel = Label(window, text="Initial Amount: $")
amtLabel.grid(row=1, column=0)

percentLabel = Label(window, text="Interest Rate:")
percentLabel.grid(row=2, column=0)

percentLabel1 = Label(window, text="%")
percentLabel1.grid(row=2, column=2)

# Interest Inputs
year = Entry(window)
year.grid(row=0, column=1)
year.insert(0, "0")

initialAmt = Entry(window)
initialAmt.grid(row=1, column=1)
initialAmt.insert(0, "0")

percent = Entry(window)
percent.grid(row=2, column=1)
percent.insert(0, "0")

# Interest Buttons
def calculate():
    answer = simple(window, int(year.get()), float(initialAmt.get()), float(percent.get()))
    simpleLabel = Label(window, text=f"SIMPLE INTEREST: {answer}", font=("Ariel", 10, "bold"))
    simpleLabel.grid(row=0, column=3, columnspan=3)
    answer1 = comp(window, int(year.get()), float(initialAmt.get()), float(percent.get()))
    compoundLabel = Label(window, text=f"COMPOUND INTEREST: {answer1}", font=("Ariel", 10, "bold"))
    compoundLabel.grid(row=1, column=3, columnspan=3)

calculateButton = Button(window, text="Calculate", font=("Ariel", 15, "bold"), command=calculate, bg="blue", fg="white")
calculateButton.grid(row=3, column=1)

# Loop to Keep Window Running
window.mainloop()