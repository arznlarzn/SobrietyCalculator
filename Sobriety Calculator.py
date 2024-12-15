from tkinter import *
from tkinter import messagebox
from tkcalendar import *
from datetime import datetime



class MyGUI:

    def __init__(self):



        self.root = Tk()
        self.root.title('Project 1')
        self.root.geometry('500x400')

        self.menubar = Menu(self.root)
        self.filemenu = Menu(self.menubar, tearoff = 0)
        self.filemenu.add_command(label="Close", command=self.on_closing)
        self.filemenu.add_command(label='Close Without Confirmation', command=exit)
        self.menubar.add_cascade(menu=self.filemenu, label="Menu")
        #This comman .config is the one that is needed to finalize and configure the menu to the window.
        self.root.config(menu = self.menubar)

        self.root.protocol('WM_DELETE_WINDOW', self.on_closing)

        self.title = Label(self.root, text='Sobriety Calculator', font=('Arial', 24))
        self.title.pack()
        #I am using the .place method for simplicity.
        self.info = Label(self.root, text='This is a sobriety calculator. Select your Sobriety\n date and it will calculate how many days it has been.', font=('Arial', 14))
        self.info.pack()
        self.calendar =Calendar(self.root, selectmode="day", year=2020, month=7, day=5)
        self.calendar.pack()
        self.button = Button(self.root, text="How many days has it been??", font=('Arial', 18), command=self.calculate_days)
        self.button.pack()
        self.answer = Label(self.root, text='Days Sober:', font=('Arial', 18))
        self.answer.pack()


        self.root.mainloop()

#Functions must be after the class itself.

    def on_closing(self):
        if messagebox.askyesno(title='Quit?', message="Do you really want to quit?"):
            self.root.destroy()

    def calculate_days(self):
        selected_date = self.calendar.get_date()
        selected_date = datetime.strptime(selected_date, '%m/%d/%y')
        current_date = datetime.now()
        delta = current_date - selected_date
        days_difference = delta.days
        self.answer.config(text=f"Days Sober: {days_difference}")

MyGUI()