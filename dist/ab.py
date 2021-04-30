from tkinter import *


window=Tk()

lbl=Label(window, text="HELLO WORLD", fg='purple', font=("Helvetica", 11))
lbl.place(x=20, y=20)

window.title('Keeping Awake')
window.geometry("150x70+10+20")
window.mainloop()
