from tkinter import *
from tkinter import messagebox
import pyqrcode
import os

window = Tk()
window.title("QR Code Generator")
def generate():
    if len(subject.get()) != 0:
        global myQr
        myQr = pyqrcode.create(subject.get())
        qrImage = myQr.xbm(scale=6)
        global photo
        photo = BitmapImage(data=qrImage)
    else:
        messagebox.showinfo("Error!", "Please Enter The Subject")
    try:
        showCode()
    except:
        pass

def showCode():
    global photo
    notificationLabel.config(image=photo)
    subLabel.config(text="Showing QR Code for: " + subject.get())

def save():
  
    dir_path = "C:\\Users\\janan\\OneDrive\\Documents" 
    
    
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    
    try:
        if len(name.get()) != 0:
            qrImage = myQr.png(os.path.join(dir_path, name.get() + ".png"), scale=6)
        else:
            messagebox.showinfo("Error!", "File name cannot be empty!")
    except:
        messagebox.showinfo("Error!", "Please generate the code first")

lab1 = Label(window, text="Enter Subject", font=("Helvetica", 50),fg="white", bg="teal")
lab1.grid(row=0, column=0, sticky=N+S+E+W)

lab2 = Label(window, text="Enter file name", font=("Helvetica", 50),fg="white", bg="#3AAFA9")
lab2.grid(row=1, column=0, sticky=N+S+E+W)

subject = StringVar()
subjectEntry = Entry(window, textvariable=subject, font=("Helvetica", 50))
subjectEntry.grid(row=0, column=1, sticky=N+S+E+W)

name = StringVar()
nameEntry = Entry(window, textvariable=name, font=("Helvetica", 50))
nameEntry.grid(row=1, column=1, sticky=N+S+E+W)

# Create buttons with colors
createButton = Button(window, text="Create QR Code", font=("Helvetica", 30), width=15, command=generate, bg="teal", fg="black")
createButton.grid(row=0, column=3, sticky=N+S+E+W)

notificationLabel = Label(window)
notificationLabel.grid(row=2, column=1, sticky=N+S+E+W)

subLabel = Label(window, text="")
subLabel.grid(row=3, column=1, sticky=N+S+E+W)

showButton = Button(window, text="Save as PNG", font=("Helvetica", 30), width=15, command=save, bg="#3AAFA9", fg="black")
showButton.grid(row=1, column=3, sticky=N+S+E+W)

totalRows = 3
totalCols = 3

for row in range(totalRows + 1):
    window.grid_rowconfigure(row, weight=1)

for col in range(totalCols + 1):
    window.grid_columnconfigure(col, weight=1)


window.mainloop()
