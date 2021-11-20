# Here we are importing the required libraries

from tkinter import *
import tkinter.messagebox

# Math library is imported as the calculator performs 
# mathematial operations
import math

# Root tk creates a window which we utilise to interact 
# with the user 
root = Tk()

# Creating fixed geometry of the
# tkinter window with dimensions 750x450
root.geometry("750x450+300+300")
root.title(" Scientific Calculator")

switch = None

''' The functions will be executed once we click on a buttons
    The following functions display the number once clicked
    The calculator also works if corresponding keys are pressed.
'''

# This function will insert 1 when button is clicked on calculator.
def btn1_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '1')

# This function will insert 2 when button is clicked on calculator.
def btn2_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '2')

# This function will insert 3 when button is clicked on calculator.
def btn3_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '3')

# This function will insert 4 when button is clicked on calculator.
def btn4_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '4')

# This function will insert 5 when button is clicked on calculator.
def btn5_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '5')

# This function will insert 6 when button is clicked on calculator.
def btn6_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '6')

# This function will insert 7 when button is clicked on calculator.
def btn7_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '7')

# This function will insert 8 when button is clicked on calculator.
def btn8_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '8')

# This function will insert 9 when button is clicked on calculator.
def btn9_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '9')

# This function will insert 0 when button is clicked on calculator.
def btn0_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '0')


def key_event(*args):
    if disp.get() == '0':
        disp.delete(0, END)

# This function will execute if + is clicked on calculator.
def btnp_clicked():
    pos = len(disp.get())
    disp.insert(pos, '+')

# This function will execute if - is clicked on calculator.
def btnm_clicked():
    pos = len(disp.get())
    disp.insert(pos, '-')

# This function will execute if * is clicked on calculator.
def btnml_clicked():
    pos = len(disp.get())
    disp.insert(pos, '*')

# This function will execute if / is clicked on calculator.
def btnd_clicked():
    pos = len(disp.get())
    disp.insert(pos, '/')


def btnc_clicked(*args):
    disp.delete(0, END)
    disp.insert(0, '0')

'''
Here when we use special mathematical functions we have to include exception handling.
Also, for changing into radians and degrees corresponding conditional statements are used.
'''
# This function will execute if sin is clicked on calculator.
def sin_clicked():
    # The function returns the sin value if there is no exception.
    try:
        ans = float(disp.get())
        if switch is True:
            ans = math.sin(math.radians(ans))
        else:
            ans = math.sin(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")

# This function will execute if cos is clicked on calculator.
def cos_clicked():
    # The function returns the cos value if there is no exception.
    try:
        ans = float(disp.get())
        if switch is True:
            ans = math.cos(math.radians(ans))
        else:
            ans = math.cos(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")

# This function will execute if tan is clicked on calculator.
def tan_clicked():
    # The function returns the tan value if there is no exception.
    try:
        ans = float(disp.get())
        if switch is True:
            ans = math.tan(math.radians(ans))
        else:
            ans = math.tan(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")

# This function will execute if sin^-1 is clicked on calculator.
def arcsin_clicked():
    # The function returns the sin^-1 value if there is no exception.
    try:
        ans = float(disp.get())
        if switch is True:
            ans = math.degrees(math.asin(ans))
        else:
            ans = math.asin(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")

# This function will execute if cos^-1 is clicked on calculator.
def arccos_clicked():
    # The function returns the cos^-1 value if there is no exception.
    try:
        ans = float(disp.get())
        if switch is True:
            ans = math.degrees(math.acos(ans))
        else:
            ans = math.acos(ans) 
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")

# This function will execute if tan^-1 is clicked on calculator.
def arctan_clicked():
    # The function returns the tan^-1 value if there is no exception.
    try:
        ans = float(disp.get())
        if switch is True:
            ans = math.degrees(math.atan(ans))
        else:
            ans = math.atan(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")

# This function will execute if ** is clicked on calculator.
def pow_clicked():
    pos = len(disp.get())
    disp.insert(pos, '**')

# This function will execute if Round is clicked on calculator.
def round_clicked():
    try:
        ans = float(disp.get())
        ans = round(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")

# This function will execute if ln is clicked on calculator.
def logarithm_clicked():
    try:
        ans = float(disp.get())
        ans = math.log10(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")

# This function will execute if fact is clicked on calculator.
def fact_clicked():
    try:
        ans = float(disp.get())
        ans = math.factorial(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")

# This function will execute if x^y is clicked on calculator.
def sqr_clicked():
    try:
        ans = float(disp.get())
        ans = math.sqrt(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")

# This function will execute if . is clicked on calculator.
def dot_clicked():
    pos = len(disp.get())
    disp.insert(pos, '.')

# This function will execute if symbol of pi is clicked on calculator.
def pi_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, str(math.pi))

# This function will execute if e is clicked on calculator.
def e_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, str(math.e))

# This function will execute if (in is clicked on calculator.
def bl_clicked():
    pos = len(disp.get())
    disp.insert(pos, '(')

# This function will execute if ) is clicked on calculator.
def br_clicked():
    pos = len(disp.get())
    disp.insert(pos, ')')

# This function will execute if del is clicked on calculator.
def del_clicked():
    # This funciton will delete the displaying elements
    pos = len(disp.get())
    display = str(disp.get())
    if display == '':
        disp.insert(0, '0')
    elif display == ' ':
        disp.insert(0, '0')
    elif display == '0':
        pass
    else:
        disp.delete(0, END)
        disp.insert(0, display[0:pos-1])

# This function will execute if conv is clicked on calculator.
def conv_clicked():
    # This function helps to convert radians to degrees and vice versa
    global switch
    if switch is None:
        switch = True
        conv_btn['text'] = "Deg"
    else:
        switch = None
        conv_btn['text'] = "Radi"

# This function will execute if ln is clicked on calculator.
def ln_clicked():
    try:
        ans = float(disp.get())
        ans = math.log(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")

# This function will execute if mod is clicked on calculator.
def mod_clicked():
    pos = len(disp.get())
    disp.insert(pos, '%')

# This function will execute if equal to is clicked on calculator.
def btneq_clicked(*args):
    try:
        ans = disp.get()
        ans = eval(ans)
        disp.delete(0, END)
        disp.insert(0, ans)

    except:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")


# Label

data = StringVar()

# This the function which takes input from the user 
# The default first entry box characteristics are specified  

disp = Entry(root, font="Helvetica 24 bold italic", fg="#456268", bg="#fcf8ec", bd=2, justify=RIGHT, insertbackground="#fcf8ec", cursor="arrow")

# The key events are specified, numeric as well as symbolic
# bind is used as it allows the input from keys pressed on keyboard as well.
disp.bind("<Return>", btneq_clicked)
disp.bind("<Escape>", btnc_clicked)
disp.bind("<Key-1>", key_event)
disp.bind("<Key-2>", key_event)
disp.bind("<Key-3>", key_event)
disp.bind("<Key-4>", key_event)
disp.bind("<Key-5>", key_event)
disp.bind("<Key-6>", key_event)
disp.bind("<Key-7>", key_event)
disp.bind("<Key-8>", key_event)
disp.bind("<Key-9>", key_event)
disp.bind("<Key-0>", key_event)
disp.bind("<Key-.>", key_event)
disp.insert(0, '0')
disp.focus_set()
# The all above specifeid feilds are shown on the screen
disp.pack(expand=TRUE, fill=BOTH)


'''The buttons are designed for the rows are the sizes are varied according to the font
# The font for all the buttons is Helvetica, font colour is white and the 
# background colour is varied to give a impression of gradient.
'''

# Buttons in row 1

btnrow1 = Frame(root)
btnrow1.pack(expand=TRUE, fill=BOTH)

pi_btn = Button(btnrow1, text="π", font="Helvetica 18", relief=GROOVE, bd=0, command=pi_clicked, fg="black", bg="#FFF8DC")
pi_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

fact_btn = Button(btnrow1, text=" ! ", font="Helvetica 18", relief=GROOVE, bd=0, command=fact_clicked, fg="black", bg="#FFF8DC")
fact_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

sin_btn = Button(btnrow1, text="sin", font="Helvetica 18", relief=GROOVE, bd=0, command=sin_clicked, fg="black", bg="#FFF8DC")
sin_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

cos_btn = Button(btnrow1, text="cos", font="Helvetica 18", relief=GROOVE, bd=0, command=cos_clicked, fg="black", bg="#FFF8DC")
cos_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

tan_btn = Button(btnrow1, text="tan", font="Helvetica 18", relief=GROOVE, bd=0, command=tan_clicked, fg="black", bg="#FFF8DC")
tan_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn1 = Button(btnrow1, text="1", font="Helvetica 23", relief=GROOVE, bd=0, command=btn1_clicked, fg="black", bg="#FFF8DC")
btn1.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn2 = Button(btnrow1, text="2", font="Helvetica 23", relief=GROOVE, bd=0,  command=btn2_clicked, fg="black", bg="#FFF8DC")
btn2.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn3 = Button(btnrow1, text="3", font="Helvetica 23", relief=GROOVE, bd=0, command=btn3_clicked, fg="black", bg="#FFF8DC")
btn3.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnp = Button(btnrow1, text="+", font="Helvetica 23", relief=GROOVE, bd=0, command=btnp_clicked, fg="black", bg="#FFF8DC")
btnp.pack(side=LEFT, expand=TRUE, fill=BOTH)

# Buttons in row 2

btnrow2 = Frame(root)
btnrow2.pack(expand=TRUE, fill=BOTH)

e_btn = Button(btnrow2, text="e", font="Helvetica 18", relief=GROOVE, bd=0, command=e_clicked, fg="white", bg="#5eaaa8")
e_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

sqr_btn = Button(btnrow2, text=" √x ", font="Helvetica 18", relief=GROOVE, bd=0, command=sqr_clicked, fg="white", bg="#5eaaa8")
sqr_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

sinh_btn = Button(btnrow2, text="sin−1", font="Helvetica 12 bold", relief=GROOVE, bd=0, command=arcsin_clicked, fg="white", bg="#5eaaa8")
sinh_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

cosh_btn = Button(btnrow2, text="cos-1", font="Helvetica 12 bold", relief=GROOVE, bd=0, command=arccos_clicked, fg="white", bg="#5eaaa8")
cosh_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

tanh_btn = Button(btnrow2, text="tan-1", font="Helvetica 12 bold", relief=GROOVE, bd=0, command=arctan_clicked, fg="white", bg="#5eaaa8")
tanh_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn4 = Button(btnrow2, text="4", font="Helvetica 23", relief=GROOVE, bd=0, command=btn4_clicked, fg="white", bg="#5eaaa8")
btn4.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn5 = Button(btnrow2, text="5", font="Helvetica 23", relief=GROOVE, bd=0, command=btn5_clicked, fg="white", bg="#5eaaa8")
btn5.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn6 = Button(btnrow2, text="6", font="Helvetica 23", relief=GROOVE, bd=0, command=btn6_clicked, fg="white", bg="#5eaaa8")
btn6.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnm = Button(btnrow2, text="-", font="Helvetica 23", relief=GROOVE, bd=0, command=btnm_clicked, fg="white", bg="#5eaaa8")
btnm.pack(side=LEFT, expand=TRUE, fill=BOTH)

# Buttons in row 3

btnrow3 = Frame(root)
btnrow3.pack(expand=TRUE, fill=BOTH)

conv_btn = Button(btnrow3, text="Radi", font="Helvetica 12 bold", relief=GROOVE, bd=0, command=conv_clicked, fg="white", bg="#276678")
conv_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

round_btn = Button(btnrow3, text=" Round", font="Helvetica 13 bold", relief=GROOVE, bd=0, command=round_clicked, fg="white", bg="#276678")
round_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

ln_btn = Button(btnrow3, text="ln", font="Helvetica 18", relief=GROOVE, bd=0, command=ln_clicked, fg="white", bg="#276678")
ln_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

logarithm_btn = Button(btnrow3, text="log", font="Helvetica 17", relief=GROOVE, bd=0, command=logarithm_clicked, fg="white", bg="#276678")
logarithm_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

pow_btn = Button(btnrow3, text="x^y", font="Helvetica 17", relief=GROOVE, bd=0, command=pow_clicked, fg="white", bg="#276678")
pow_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn7 = Button(btnrow3, text=" 7", font="Helvetica 23", relief=GROOVE, bd=0, command=btn7_clicked, fg="white", bg="#276678")
btn7.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn8 = Button(btnrow3, text="8", font="Helvetica 23", relief=GROOVE, bd=0, command=btn8_clicked, fg="white", bg="#276678")
btn8.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn9 = Button(btnrow3, text="9", font="Helvetica 23", relief=GROOVE, bd=0, command=btn9_clicked, fg="white", bg="#276678")
btn9.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnml = Button(btnrow3, text="*", font="Helvetica 23", relief=GROOVE, bd=0, command=btnml_clicked, fg="white", bg="#276678")
btnml.pack(side=LEFT, expand=TRUE, fill=BOTH)

# Buttons in row 4

btnrow4 = Frame(root)
btnrow4.pack(expand=TRUE, fill=BOTH)

mod_btn = Button(btnrow4, text="%", font="Helvetica 21", relief=GROOVE, bd=0, command=mod_clicked, fg="white", bg="#03506f")
mod_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

bl_btn = Button(btnrow4, text=" ( ", font="Helvetica 21", relief=GROOVE, bd=0, command=bl_clicked, fg="white", bg="#03506f")
bl_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

br_btn = Button(btnrow4, text=" ) ", font="Helvetica 21", relief=GROOVE, bd=0, command=br_clicked, fg="white", bg="#03506f")
br_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

dot_btn = Button(btnrow4, text=" • ", font="Helvetica 21", relief=GROOVE, bd=0, command=dot_clicked, fg="white", bg="#03506f")
dot_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnc = Button(btnrow4, text="AC", font="Helvetica 21", relief=GROOVE, bd=0, command=btnc_clicked, fg="white", bg="#03506f")
btnc.pack(side=LEFT, expand=TRUE, fill=BOTH)

del_btn = Button(btnrow4, text="clear", font="Helvetica 20", relief=GROOVE, bd=0, command=del_clicked, fg="white", bg="#03506f")
del_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn0 = Button(btnrow4, text="0", font="Helvetica 23", relief=GROOVE, bd=0, command=btn0_clicked, fg="white", bg="#03506f")
btn0.pack(side=LEFT, expand=TRUE, fill=BOTH)

btneq = Button(btnrow4, text="=", font="Helvetica 23", relief=GROOVE, bd=0, command=btneq_clicked, fg="white", bg="#03506f")
btneq.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnd = Button(btnrow4, text="/", font="Helvetica 23", relief=GROOVE, bd=0, command=btnd_clicked, fg="white", bg="#03506f")
btnd.pack(side=LEFT, expand=TRUE, fill=BOTH)

# This statement is responsible to keep the window open untill it is closed
root.mainloop()
