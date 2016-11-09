import pyautogui as p
import time as t 
import webbrowser as w
w.open("http://youtube.com")
t.sleep(4)
p.position(434,653)
p.typewrite("pretty little liars",0.1)
p.keyDown('enter')
p.keyUp('enter')
t.sleep(2)
p.click(193,256)
t.sleep(2)
p.click(780,584)