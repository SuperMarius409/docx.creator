import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import pandas as pd

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300, bg = 'lightsteelblue2', relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='Masina de teme', bg = 'lightsteelblue2')
label1.config(font=('helvetica', 20, 'bold'))
canvas1.create_window(150, 60, window=label1)

def getTxt ():
    global read_file
    
    import_file_path = filedialog.askopenfilename()
    read_file = pd.read_csv(import_file_path)
    
browseButtonTxt = tk.Button(text="      Creeaza Tema    ", command=getTxt, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 130, window=browseButtonTxt)

def convertToCsv ():
    global read_file
    
    export_file_path = filedialog.asksaveasfilename(defaultextension='.csv')
    read_file.to_csv (export_file_path, index = None)

saveAsButtonCsv = tk.Button(text='Convert Text to CSV', command=convertToCsv, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 180, window=saveAsButtonCsv)

def exitApplication():
       root.destroy()
     
exitButton = tk.Button (root, text='       Iesi din aplicatie     ',command=exitApplication, bg='brown', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 230, window=exitButton)

root.mainloop()