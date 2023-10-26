import math
from tkinter import *

calculator_layout = [
    "(", ")", "nCr", "nPr", "exp",
    "sin", "cos", "tan", "sqrt", "ln",
    "7", "8", "9", "/", "%",
    "4", "5", "6", "*", "fact",
    "1", "2", "3", "-", "π",
    ".", "0", "=", "+", ",", "C"
]

window = Tk()
window.title("SCIENTIFIC CALCULATER")
window.minsize(height=450, width=350)
# entry
entry = Entry()
entry.config(width=40, font=('Helvetica', 12))
entry.grid(row=0, column=0, columnspan=5, ipadx=8, ipady=8, sticky="nsew")


# Function to calculate square root
def sqrt(x):
    s = math.sqrt(x)
    return s


# Function to calculate nPr (permutation)
def nPr(n, r):
    if n >= r >= 0:
        return math.factorial(n) / math.factorial(n - r)
    else:
        return "Invalid input"


# Function to calculate nCr (combination)
def nCr(n, r):
    if n >= r >= 0:
        return math.factorial(n) / (math.factorial(r) * math.factorial(n - r))
    else:
        return "Invalid input"


# Function to calculate natural logarithm (ln)
def ln(x):
    return math.log(x)


# Function to calculate logarithm (log)
def log(x, base):
    return math.log(x, base)


# Function to calculate sine (sin)
def sin(x):
    return math.sin(x)


# Function to calculate cosine (cos)
def cos(x):
    return math.cos(x)


# Function to calculate tangent (tan)
def tan(x):
    return math.tan(x)

# function to calculate exponential
def exp(x,y):
    return math.pow(x,y)

# Function to calculate factorial (x!)
def fact(x):
    if x >= 0:
        return math.factorial(x)
    else:
        return "Invalid input"


def button_click(value):
    current = entry.get()
    if value == "π":
        current += math.pi
    else:
        current += value
    entry.delete(0, END)
    entry.insert(0, current)


def evaluate():
    expression = str(entry.get())
    try:
        result = eval(expression)
        entry.delete(0, END)
        entry.insert(0, result)
    except Exception:
        entry.delete(0, END)
        entry.insert(0, "Error")


def clear():
    entry.delete(0, END)


Row = 1
Col = 0
for b in calculator_layout:
    if b == "=":
        botn = Button(text=b, pady=20, padx=20, command=evaluate)
        botn.grid(row=Row, column=Col, sticky="nsew")
    elif b == "C":
        botn = Button(text=b, pady=20, padx=20, command=clear)
        botn.grid(row=Row, column=Col + 1, columnspan=3, sticky="nsew")
    else:
        botn = Button(text=b, pady=20, padx=20, command=lambda b1=b: button_click(b1))
        botn.grid(row=Row, column=Col, sticky="nsew")
    Col = Col + 1
    if Col > 4:
        Row = Row + 1
        Col = 0
window.mainloop()
