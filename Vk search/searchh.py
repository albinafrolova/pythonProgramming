from tkinter import*
import log
import vk_requests

window=Tk()
window.title("Search user")
window.geometry("250x200")

def push():
    qq=entry_lab1.get()
    print(qq)
    print(api.users.search(q=qq))

def push2():
    qq=entry_lab2.get()
    countt=entry_lab3.get()
    print(api.users.search(q=qq, count=countt))
  

frame = Frame(window)

button = Button (frame, text = "Search ID",command=push)
button.grid(row=2, column=1)

entry_lab1 = Entry(frame)
entry_lab1.grid(row=1, column=1)

label_lab=Label(frame,text="ID:")
label_lab.grid(row=0, column=1)

button = Button (frame, text = "Search", command=push2)
button.grid(row=4, column=3)

entry_lab3 = Entry(frame)
entry_lab3.grid(row=3, column=3)

label_lab=Label(frame,text="Count")
label_lab.grid(row=2,column=3)

entry_lab2 = Entry(frame)
entry_lab2.grid(row=1, column=3)

label_lab=Label(frame,text="Name/Surname:")
label_lab.grid(row=0, column=3)
frame.pack()


api=vk_requests.create_api(app_id=5562874, login=log.login, password=log.password)
