#-*-encoding:utf8
from tkinter import *
from tkinter import filedialog
#create header
from tkinter.filedialog import askopenfilename
import logging

root=Tk()
root.title("Text Editor")
root.geometry("825x500")

#Edit Text Area
lnlabel = Label(root,width = 2,bg = 'antique white', text= "")
lnlabel.pack(side = LEFT,fill = Y)
lnlabel.config(text="1")

lnlabel2 = Label(root,width = 2,height=500,bg = 'black', text= "")
lnlabel2.pack(fill = X)


textpad = Text(root,undo = True)
textpad.pack(expand = YES,fill = BOTH)

scroll = Scrollbar(textpad)
textpad.config(yscrollcommand = scroll.set)
scroll.config(command = textpad.yview)
scroll.pack(side = RIGHT,fill = Y)

###################################
textpad2 = Text(root,undo = True)
textpad2.pack(expand = YES,fill = BOTH)

scroll = Scrollbar(textpad2)
textpad2.config(yscrollcommand = scroll.set)
scroll.config(command = textpad2.yview)
scroll.pack(side = RIGHT,fill = Y)

textpad.place(height = 500, width = 400, x = 20,y = 0)
textpad2.place(height = 500, width = 400, x = 425,y = 0)
textpad2.config(state=DISABLED)
#create menu
menubar = Menu(root)
root.config(menu = menubar)



#######################     File Menu Functions     ########################
def new():
    root.title('Untitled')
    filename = None
    textpad.delete(1.0, END)

def save():
    global filename
    try:
        f = open(filename, 'w')
        msg = textpad.get(1.0, END)
        f.write(msg)
        f.close()
    except:
        saveas()

def openfile():
    new()
    name = askopenfilename(filetypes=(("Text File", "*.txt"), ("All Files", "*.*")),
                           title="Choose a file.")
    print(name)
    # Using try in case user types in unknown file or closes without choosing a file.
    try:
        with open(name, 'r') as UseFile:
            text = UseFile.read();
            print(UseFile.read())
            print(text)
            textpad.insert(1.0, text)
    except:
        logging.exception("message")
        print("No file exists")

def saveas():
    t = textpad.get("1.0", "end-1c")
    savelocation = filedialog.asksaveasfilename()
    savelocation = savelocation + ".txt"
    file1 = open(savelocation, "w+")
    file1.write(t)
    file1.close()

#######################     Edit Menu Functions     ########################
def cut():
  textpad.event_generate('<<Cut>>')

def copy():
  textpad.event_generate('<<Copy>>')

def paste():
  textpad.event_generate('<<Paste>>')

def redo():
  textpad.event_generate('<<Redo>>')

def undo():
  textpad.event_generate('<<Undo>>')

def selectAll():
  textpad.tag_add('sel','1.0',END)

def search():
  topsearch = Toplevel(root)
  topsearch.geometry('300x30+200+250')
  label1 = Label(topsearch,text='Find')
  label1.grid(row=0, column=0,padx=5)
  entry1 = Entry(topsearch,width=20)
  entry1.grid(row=0, column=1,padx=5)
  button1 = Button(topsearch,text='Find')
  button1.grid(row=0, column=2)


#######################     Status Menu Functions     ########################
def Word_Count():
    textpad2.config(state="normal")
    selected_text = textpad.selection_get()
    count = 0

    for i in range(0,len(selected_text)-1):
        print(selected_text[i])
        if selected_text[i] ==" " and selected_text[i+1] != " ":
            count = count + 1
    if selected_text[0] == " ":
        textpad2.insert(1.0,count)
    else:
        textpad2.insert(1.0, count + 1)
    textpad2.insert(1.0, "  ")
    textpad2.config(state=DISABLED)

def Letter_Count():
    textpad2.config(state="normal")
    selected_text = textpad.selection_get()
    count = 0

    for i in range(0,len(selected_text)-1):
        
        if selected_text[i+1] != " ":
            count = count + 1
   
    textpad2.insert(1.0, count+1)
    textpad2.insert(1.0, "  ")
    textpad2.config(state=DISABLED)
def Word_Count2():
    textpad2.config(state=ENABLED)
def Word_Count3():
    textpad2.config(state=ENABLED)




#File Menu
filemenu = Menu(menubar)
filemenu.add_command(label = 'New', accelerator ='ctrl + N', command = new)
filemenu.add_command(label = 'Open', accelerator ='ctrl + O', command = openfile)
filemenu.add_command(label = 'Save', accelerator ='ctrl + S', command = save)
filemenu.add_command(label = 'Save As', accelerator ='ctrl + Shift + s', command = saveas)
menubar.add_cascade(label='File', menu=filemenu)

#Edit Menu
editmenu = Menu(menubar)
editmenu.add_command(label = 'Undo',accelerator = 'ctrl + z')
editmenu.add_command(label = 'Redo',accelerator = 'ctrl + y')
editmenu.add_command(label = 'Copy',accelerator = 'ctrl + c',command = copy)
editmenu.add_command(label = 'Cut',accelerator = 'ctrl + x',command = cut)
editmenu.add_command(label = 'Paste',accelerator = 'ctrl + v',command = paste)
editmenu.add_command(label = 'Find',accelerator = 'ctrl + F',command = search)
editmenu.add_command(label = 'Select All',accelerator = 'ctrl + A')
menubar.add_cascade(label = 'Edit',menu = editmenu)

#Status Menu
statusmenu = Menu(menubar)
statusmenu.add_command(label = 'Word Count',accelerator = 'ctrl + w',command = Word_Count)
statusmenu.add_command(label = 'Letter Count',accelerator = 'ctrl + e',command = Letter_Count)
statusmenu.add_command(label = 'Word Count2',accelerator = 'ctrl + r',command = Word_Count2)
statusmenu.add_command(label = 'Word Count3',accelerator = 'ctrl + t',command = Word_Count3)
menubar.add_cascade(label = 'Status',menu = statusmenu)

root.mainloop()
