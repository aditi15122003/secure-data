from tkinter import *
from tkinter import filedialog,messagebox
from PIL import Image,ImageTk
import os
from stegano import lsb

win = Tk()

win.geometry('900x900')
win.config(bg="#c2a146")
# button function
# open_img
def open_img():
    global open_file
    open_file = filedialog.askopenfilename(initialdir=os.getcwd(),
                                           title="Select file Type",
                                           filetypes=(('PNG file','*.png'),('JPG file','*.jpg'),('All file', '*.txt')))
    img = Image.open(open_file)
    img = ImageTk.PhotoImage(img)
    lf1.configure(image=img)
    lf1.image=img
    
    
def hide():
    global hide_msg
    password = code.get()
    if password == "1234":
        msg = text1.get(1.0 ,END)
        hide_msg = lsb.hide(str(open_file) ,msg)
        messagebox.showinfo("Sucesss", "Successfully Hidden")

    elif password == '':
        messagebox.showerror("Error" , "Please Enter the valid Password")
        
    else:
        messagebox.showerror("Error" , "Wrong Password")
        code.set('')
        
    
def save_img():
    hide_msg.save('Secret file.png')
    
    
def show():
    password = code.get()
    if password == "1234":
        show_msg = lsb.reveal(open_file)
        text1.delete(1.0 , END)
        text1.insert(END , show_msg)

# logo
logo = PhotoImage(file="logo.png")
Label(win, image=logo, bd=0).place(x=620, y=0)
# heding
Label(win,text="CyberSecurity",font="impack 30 bold" , bg="black" , fg="Yellow").place(x=600, y=200)
# frame
f1 = Frame(win, width=500, height=300 , bd=50, bg="#2e3632")
f1.place(x=50, y =300)
lf1 = Label(f1,bg="#2e3632")
lf1.place(x=0, y=0)

f2 = Frame(win, width=500, height=300 , bd=5, bg="White")
f2.place(x=1000, y =300)
text1 = Text(f2,font='Ariel 15 bold', wrap=WORD)
text1.place(x=0, y=0, width=310, height=210)
# Label for Secret Key
Label(win, text='Enter Secret Key', font='10', bg="black", fg="Yellow").place(x=700, y=650)

# Enterty widget for secret key
code = StringVar()
e = Entry(win,textvariable= code ,bd=2, font='impact 10 bold', show='*')
e.place(x=690,y=700)

# button
open_button = Button(win, text="Open Image", bg="#3e1442", fg="white", font="ariel 12 bold", cursor='hand2', command = open_img)
open_button.place(x=100, y=730)

save_button = Button(win, text="Save Image", bg="#4f1530", fg="white",cursor='hand2', font="ariel 12 bold", command=save_img)
save_button.place(x=400, y=730)


hide_button = Button(win, text="Hide Image", bg="#4f151c", fg="white",cursor='hand2', font="ariel 12 bold", command=hide)
hide_button.place(x=1000, y=730)

show_button = Button(win, text="Show Image", bg="#13472b", fg="white",cursor='hand2', font="ariel 12 bold" , command=show)
show_button.place(x=1400, y=730)
mainloop()