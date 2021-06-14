from tkinter import *
import sqlite3
from Canton_Class import nat_doses, swiss_pop, equi_distr
from Canton_data import cantons

window = Tk()
window.title('Covid Vaccination')
window.iconbitmap('vax.ico')
window.geometry('400x350')
window.config(background='#41B77F')

# Create a Choice function for the mode
i = 0
total = 0

def choice():
    for i in range(len(nat_doses)):
        if mode_name.get() == 'manual':
            for canton in cantons:
                print(canton)
                number = float(input('Please, enter a rate = '))
                doses = number * nat_doses[i] * (canton.pop/swiss_pop)
                canton.receive(doses)
                canton.use(doses)
                print(canton)

        elif mode_name.get() == 'equity':
            equi_distr(cantons, i)
            for canton in cantons:
                print(canton)
    mode_name.delete(0, END)

# Create a frame
frame = Frame(window, bg='#41B77F')

# Create a sub-frame
sub_frame = Frame(window, bg='#41B77F')

# Add a Title and subtitle
label_title = Label(frame, text="Welcome to the vaccination site", font=("Courrier",19), bg='#41B77F', fg='white')
label_title.pack()
label_subtitle = Label(frame, text="Please enter a mode", font=("Courrier",15), bg='#41B77F', fg='white')
label_subtitle.pack()

# Center frame in the window
frame.pack(expand=YES)
sub_frame.pack(expand=YES)

# Create Text Boxes
mode_name = Entry(sub_frame, width=30)
mode_name.pack(expand=YES)

# Create Choose Button
choose_btn = Button(sub_frame, text="Choose", command=choice)
choose_btn.pack(expand=YES,padx=2,pady=2)

window.mainloop()