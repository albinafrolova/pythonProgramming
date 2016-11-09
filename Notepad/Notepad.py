from tkinter import*

def newfile(event=None):
    global filename
    filename=None
    if messagebox.askokcancel("Save","Do you want to save this file?"):
        savefile()
        text.delete(1.0,END)
        wn.title("Untitled.txt") 
    else:
        text.delete(1.0,END)
        wn.title("Untitled.txt")
def openfile(event=None):
    global filename
    filename = filedialog.askopenfilename()
    wn.title(filename)
    file = open(filename,"r",encoding="utf-8")
    text.insert(1.0,file.read())
def savefile(event=None):
    global filename
    filename = filedialog.asksaveasfilename()
    file = open(filename,"w",encoding="utf-8")
    content=text.get(1.0,END)
    file.write(content)
    file.close()
def cutfile():
    text.event_generate("<<Cut>>")
def copyfile():
    text.event_generate("<<Copy>>")
def pastefile():
    text.event_generate("<<Paste>>")
def undofile():
    text.event_generate("<<Undo>>")
def redofile():
    text.event_generate("<<Redo>>")
def click(event):
    popupmenu.tk_popup(event.x_root, event.y_root, 0)
def close():
    if messagebox.askokcancel("Exit","Do you want to exit?"):
        wn.destroy()
    else:
        pass
def show_info():
    messagebox.showinfo("About", "This application is done by Albina")
wn = Tk()
wn.title("Notepad")
wn.geometry("250x250")

newfile_img = PhotoImage(file = "icons/new_file.gif")
openfile_img = PhotoImage(file = "icons/open_file.gif")
save_img = PhotoImage(file = "icons/save.gif")
undo_img = PhotoImage (file = "icons/undo.gif")
redo_img = PhotoImage (file = "icons/redo.gif")
about_img = PhotoImage (file = "icons/about.gif")
search_img = PhotoImage (file = "icons/onfind.gif")
cut_img = PhotoImage (file="icons/cut.gif")

menubar = Menu(wn)
wn.config(menu=menubar)

filemenu = Menu(menubar)
filemenu.add_command(label="New File", image = newfile_img, compound =LEFT,accelerator="Ctrl+N",command=newfile)
filemenu.add_command(label="Open",image = openfile_img, compound =LEFT, accelerator="Ctrl+O", command=openfile)
filemenu.add_command(label="Save",image= save_img,compound =LEFT,accelerator="Ctrl+S",command=savefile)
filemenu.add_command(label="About",image=about_img,compound=LEFT,command = show_info)
menubar.add_cascade(label="File", menu=filemenu)
filerecent = Menu(filemenu)
filerecent.add_command(label="Recents...")
filerecent.add_command(label="file.123")
filemenu.add_separator()
filemenu.add_cascade(label="Recents", menu=filerecent)
filemenu.add_checkbutton(label="Checked")

editmenu = Menu(menubar)
editmenu.add_command(label="Undo Tryng", image = undo_img, compound =LEFT,accelerator="Ctrl+Z",command=undofile)
editmenu.add_command(label="Redo",image = redo_img, compound =LEFT, accelerator="Ctrl+Shift+Z",command=redofile)
editmenu.add_command(label="About", image = about_img, compound = LEFT, accelerator="Ctrl+A")
editmenu.add_command(label="Search",image= search_img,compound =LEFT,accelerator="Ctrl+P")
menubar.add_cascade(label="Edit", menu=editmenu)

formatmenu = Menu(menubar)
formatmenu.add_command(label="Text", compound = LEFT, accelerator ="Ctrl+T")
menubar.add_cascade(label="Format", menu = formatmenu)
formatfont = Menu(formatmenu)
formatfont.add_command(label="Italics")
formatfont.add_command(label="Bold")
formatfont.add_command(label="Undrelined")
formatmenu.add_cascade(label = "Font", menu = formatfont)
formatmenu.add_command(label="Indent",compound = LEFT, accelerator="Ctrl+I")

optionsmenu = Menu(menubar)
optionsmenu.add_command(label="Sort files", compound=LEFT, accelerator="Ctrl+G")
optionsmenu.add_command(label="Hide all folders", compound=LEFT, accelerator="Ctrl+L")
menubar.add_cascade(label="Options", menu=optionsmenu)

helpmenu = Menu(menubar)
helpmenu.add_command(label="Notepad help",image=about_img,compound=LEFT,accelerator="Ctrl+H")
menubar.add_cascade(label="Help",menu=helpmenu)

frame = Frame(wn)
newfile_btn = Button(frame, image=newfile_img,command=newfile)
newfile_btn.grid(row = 0, column = 0)
openfile_btn = Button(frame,image = openfile_img,command=openfile)
openfile_btn.grid( row = 0, column = 1)
saveimg_btn = Button(frame, image = save_img,command=savefile)
saveimg_btn.grid( row = 0, column = 2)
undoimg_btn = Button (frame, image = undo_img,command=undofile)
undoimg_btn.grid (row = 0, column = 3)
redoimg_btn = Button (frame, image = redo_img,command=redofile)
redoimg_btn.grid (row = 0, column = 4)
cutimg_btn = Button (frame, image = cut_img,command=cutfile)

cutimg_btn.grid (row = 0, column = 5)
frame.pack()
text = Text(wn, bg = "light blue", undo=True)
text.pack()

wn.protocol("WM_DELETE_WINDOW",close)
text.bind("<Button-3>", click)
text.bind("<Control-n>",newfile)
text.bind("<Control-o>",openfile)
text.bind("<Control-s>",savefile)
text.bind("<Control-x>",cutfile)
text.bind("<Control-z>",undofile)
text.bind("<Control-Shift-z>",redofile)
text.bind("<Control-v>",copyfile)


popupmenu = Menu(text)
popupmenu.add_command(label="Cut",accelerator="Ctrl+X",command=cutfile)
popupmenu.add_command(label="Copy",accelerator="Ctrl+V",command=copyfile)
popupmenu.add_command(label="Paste",accelerator="Ctrl+C",command=pastefile)
                 

