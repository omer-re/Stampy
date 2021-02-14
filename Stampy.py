# -*- coding: utf-8 -*-
from PyPDF2 import PdfFileWriter, PdfFileReader
from tkinter import *
from tkinter.filedialog import *
import PyPDF2 as pypdf
from reportlab.pdfgen import canvas
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename, askdirectory
import sys, os
from tkinter import ttk
import time
from functools import partial

def get_input(root, display_text):
    col=1
    l1=ttk.Label(root, text="Enter text to stamp,",font='Helvetica 12', justify=LEFT).grid(row=2, column=col,stick="W",padx=20)
    l2=ttk.Label(root, text="English and numbers only please 🙂",font='Helvetica 12',foreground="#920", justify=LEFT).grid(row=3, column=col,stick="W",padx=20)
    e1 = Entry(root,textvariable = stamp_text,width=20, font=10,fg="blue",bd=3,selectbackground='violet')
    e1.grid(row=4, column=1,stick="N")
    return e1.get()

def ID_stamp():
    file=filename1.get()
    text=str(stamp_text.get())
    if (file==None or text==None):
        print("Invalid input")
    print("file path ={} \nStamp text= {}".format(filename1.get(),stamp_text.get()))
    c = canvas.Canvas('watermark.pdf')
    print("working")
    output_file = PdfFileWriter()
    input_file = PdfFileReader(open(file, "rb"))
    page_count = input_file.getNumPages()

    # get input dims
    (_,_,width,height)=input_file.getPage(0).mediaBox

    ######  Create new template with watermark ###
    c = canvas.Canvas('watermark.pdf')
    #if picture_path:
        #c.drawImage(picture_path, 15, 15)
    if text:
        c.setFontSize(22)
        c.setFillColorRGB(255,0,255)
        c.setFont('Courier-Bold', 14)
        c.drawString(15, (int(height)-20), text)
        c.save()
    watermark = PdfFileReader(open("watermark.pdf", "rb"))

    #########

    for page_number in range(page_count):
        input_page = input_file.getPage(page_number)
        input_page.mergePage(watermark.getPage(0))
        output_file.addPage(input_page)

        output_path = file.split('.pdf')[0] + '_watermarked' + '.pdf'
    print(output_path)
    with open(output_path, "wb") as outputStream:
        output_file.write(outputStream)
    time.sleep(1)
    root.quit()
    print("Done working")

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


root=Tk()
root.title('ID Stamper')
#root.iconbitmap( resource_path('./icon.ico'))
pdf_file=None

filename1=StringVar()
stamp_text=StringVar()


def load_pdf(filename):
    f = open(filename,'rb')
    return pypdf.PdfFileReader(f)

def load1():
    f = askopenfilename(filetypes=(('PDF File', '*.pdf'), ('All Files','*.*')))
    filename1.set(f)
    print(f)


button1=Button(root, text="Choose file", command=load1, font='Helvetica 14 bold',height = 4).grid(row=1, column=0)
Label(root, textvariable=filename1,width=20).grid(row=1, column=1, sticky=(N,S,E,W))

button2=Button(root, text="Stamp it", command=ID_stamp,font='Helvetica 14 bold', fg="red", height =4).grid(row=1, column=2,sticky=E)
stamp=get_input(root,"Enter text to stamp")


Label(root, text="""1. Choose your PDF file.\n2. Insert the text you'd like to stamp (ID, name, etc,).\n3. Hit the "Stamp it" button.""", font='Helvetica 12', justify=LEFT).grid(row=5, column=1, sticky="w")
Label(root, text="\n\n\nOmer Reuveni\nOmer@Solution-oriented.com", font='Helvetica 10',fg="blue", justify=LEFT).grid(row=6, column=0, sticky="w")


for child in root.winfo_children():
    child.grid_configure(padx=10,pady=10)

root.mainloop()
