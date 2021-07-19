from tkinter import *
from tkinter import messagebox

ws = Tk()
ws.title("made by Gabriel Tsen")
ws.geometry('300x100')

def AskMe():
    res = messagebox.askquestion('askquestion', 'Do you like cats?')
    if res == 'yes':
        messagebox.showinfo('Response', 'You like Cats')
    elif res == 'no':
        messagebox.showinfo('Response', 'You must be a dog fan.')
    else:
        messagebox.showwarning('error', 'Something went wrong!')


Button(ws, text='Click me', padx=100, pady=50, command=AskMe).pack(pady=20)

ws.mainloop()