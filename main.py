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

def file1():    
    if not textbox.edit_modified():      
        textbox.delete('1.0', END)
    else:        
        savefileas()
          
        textbox.delete('1.0', END)  
    
    textbox.edit_modified(0)
       
    pdfWindow.title('PYTHON GUIDES') 

#function to open text file
def openfile():
    
    if not textbox.edit_modified():       
        try:            
            path = filedialog.askopenfile(filetypes = (("Text files", "*.txt"), ("All files", "*.*"))).name
                       
            pdfWindow.title('Notepad - ' + path)          
            
            with open(path, 'r') as f:             
                content = f.read()
                textbox.delete('1.0', END)
                textbox.insert('1.0', content)
                                
                textbox.edit_modified(0)
             
        except:
            pass   
    
    else:       
        savefileas()      
        
        textbox.edit_modified(0)              
        openfile() 

# to save the current file
def savefile():    
    try:
        
        path = pdfWindow.title().split('-')[1][1:]   
    
    except:
        path = ''
    
    if path != '':
        
        with open(path, 'w') as f:
            content = textbox.get('1.0', END)
            f.write(content)
      
    else:
        savefileas()    
    
    textbox.edit_modified(0)

#to run save as file
def savefileas():    
    try:
        path = filedialog.asksaveasfile(filetypes = (("Text files", "*.txt"), ("All files", "*.*"))).name
        pdfWindow.title('Notepad - ' + path)
    
    except:
        return   
    
    with open(path, 'w') as f:
        f.write(textbox.get('1.0', END))

#functions  for choosing pdf file
def choose_pdf():
      filename = filedialog.askopenfilename(
            initialdir = "/",   # for Linux and Mac users
          # initialdir = "C:/",   for windows users
            title = "Select a File",
            filetypes = (("PDF files","*.pdf*"),("all files","*.*")))
      if filename:
          return filename
# functions to quit from app 
def quit_app():

    questionQuitOrNot = askquestion("QUIT?","Are you sure to quit")
    if(questionQuitOrNot=='yes'):
        pdfWindow.destroy()
    else:
        return
    
#functions to clear or close file
def clear_text():
    questionClearOrNot = askquestion("CLOSE IT?","If you close now your data will be lost",icon='warning')
    if(questionClearOrNot=='yes'):
       textbox.delete(1.0, END)
    else:
        return
   
# functions  to read the pdf file and extract text 
def read_pdf():
    
    try:
        filename = choose_pdf()
    
        reader = PdfFileReader(filename)
        pageObj = reader.getNumPages()
        for page_count in range(pageObj):
            page = reader.getPage(page_count)
            page_data = page.extractText()
            textbox.insert(END, page_data)
            
        
    except IndexError:
            print("index error")
    except  ValueError:
            print("error")
    except SyntaxError: 
            print("error")
        
#functions  copy the text to the clipboard
def copy_pdf_text():
    content = textbox.get(1.0, "end-1c")
    pdfWindow.withdraw()
    pdfWindow.clipboard_clear()
    pdfWindow.clipboard_append(content)
    pdfWindow.update()
    pdfWindow.destroy()

# to create text box for text display
textbox = Text(pdfWindow)

textbox.pack(expand=YES,fill=BOTH,side=LEFT)




#create a main menu
main_menu = Menu(pdfWindow)

# configing menu to main window
pdfWindow.config(menu=main_menu)

file_menu = Menu(main_menu,tearoff=0)
# to options for main menu
main_menu.add_cascade(label='File', menu=file_menu)
main_menu.add_command(label="Quit",command=quit_app)
# scrollbar for text window
scrollbar = Scrollbar(pdfWindow, orient=VERTICAL, command=textbox.yview)
scrollbar.pack(fill=Y, side=RIGHT)
textbox['yscrollcommand'] = scrollbar.set
# dropdown for file menu
file_menu.add_command(label='Open PDF File',command=read_pdf)
file_menu.add_command(label='Open File',command=openfile)
file_menu.add_command(label="Save", command=savefile)
file_menu.add_command(label="Save as...", command=savefileas)
file_menu.add_separator()
file_menu.add_command(label='Copy text to clipboard',command=copy_pdf_text)
file_menu.add_command(label="Close file",command=clear_text)

# loop for continuing prgram
pdfWindow.mainloop()