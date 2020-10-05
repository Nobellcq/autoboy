import win32api 
import win32gui 
import win32con 
import time 
import ctypes
import pyHook
import threading
import pythoncom

import sys
sys.path.append("../")
from appJar import gui

app=gui("Grid Demo", "200x100")
flag=0   #标记 0：未开始点击，1：开始    2：停止


def getCursor():
     return win32api.GetCursorPos()
   

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

def onKeyboardEvent(event):
	# 监听键盘事件
	'''
	print "MessageName:", event.MessageName
	print "Message:", event.Message
	print "Time:", event.Time
	print "Window:", event.Window
	print "WindowName:", event.WindowName
	print "Ascii:", event.Ascii, chr(event.Ascii)
	print "Key:", event.Key
	print "KeyID:", event.KeyID
	print "ScanCode:", event.ScanCode
	print "Extended:", event.Extended
	print "Injected:", event.Injected
	print "Alt", event.Alt
	print "Transition", event.Transition
	print "---"
	'''
	global flag
	if event.Key=='S':     #S开始
		flag=1
	elif event.Key=='E':   #E结束
		flag=2
	return True

def createKeyboardListen():
	# 创建一个“钩子”管理对象
	hm = pyHook.HookManager()
	# 监听所有键盘事件
	hm.KeyDown = onKeyboardEvent
	# 设置键盘“钩子”
	hm.HookKeyboard()
	# 开始监听
	
	pythoncom.PumpMessages() 

def UI():
    app=gui("Grid Demo", "250x100")
    app.setSticky("news")
    app.setExpand("both")
    app.setFont(30)
    app.addLabel("l1", getCursor()[0], 1, 1)
    app.setLabelBg("l1", "LightYellow")
    app.go()

def Listener():
        #开一个循环，其实就是一个监听，等待flag的变化
    while(1):
            time.sleep(0.05)    #每隔1秒鼠标点1次
            app.setLabel("l1","x:"+str(getCursor()[0])+"  "+"y:"+str(getCursor()[1]))
            print(str(getCursor()[0])+"  "+str(getCursor()[1]))
'''
            if flag==1:
            elif flag==2:
                    break
   '''             
   
    
def main():

    #单独开一个线程用于监听键盘按键
    t=threading.Thread(target=createKeyboardListen,args=())
    t.start()
    
    t1=threading.Thread(target=Listener,args=())
    t1.start()

    #构建ui

    app.setSticky("news")
    app.setExpand("both")
    app.setFont(15)
    app.addLabel("l1", getCursor()[0], 1, 1)
    app.setLabelBg("l1", "LightYellow")
    app.setLabel("l1","ss")
    app.go()
    


    
main()

