from tkinter import *
from tkinter import filedialog
from PyPDF2 import PdfFileReader
from tkinter.messagebox import askquestion, showinfo
import pdf2docx

pdfWindow= Tk()
pdfWindow.title('My PDF Reader')
pdfWindow.geometry("550x550")
pdfWindow.config(bg='white')
page_data = None


pdfWindow.mainloop()