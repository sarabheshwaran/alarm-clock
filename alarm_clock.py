from tkinter import *
import datetime
import time
import winsound

def Alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        actual_time = datetime.datetime.now()
        cur_time = actual_time.strftime("%H:%M:%S")
        cur_date = actual_time.strftime("%d/%m/%Y")
        msg="Current Time: "+str(cur_time)
        print(msg)
        if cur_time == set_alarm_timer:
            print("Time to wake")
            winsound.PlaySound("Music.wav",winsound.SND_ASYNC)
            break

def get_alarm_time():
    alarm_set_time = f"{hour.get()}:{min.get()}:{sec.get()}"
    Alarm(alarm_set_time)

window = Tk()
window.title("ALARM")
window.geometry("500x150")
window.config(bg="white")
window.resizable(width=False,height=False)

time_format=Label(window, text= "Set time in 24 hour format!", fg="black",bg="white",font=("Arial",15)).place(x=20,y=120)
addTime = Label(window,text = "Hour     Min     Sec",font=60,fg="black",bg="white").place(x = 260)
setYourAlarm = Label(window,text = "Set Time for Alarm: ",fg="black",bg="white",relief = "solid",font=("Helevetica",15,"bold")).place(x=10, y=40)

hour = StringVar()
min = StringVar()
sec = StringVar()

hourTime= Entry(window,textvariable = hour,bg = "white",width = 4,font=(20)).place(x=250,y=40)
minTime= Entry(window,textvariable = min,bg = "white",width = 4,font=(20)).place(x=310,y=40)
secTime = Entry(window,textvariable = sec,bg = "white",width = 4,font=(20)).place(x=370,y=40)

submit = Button(window,text = "Set Your Alarm",fg="Black",bg="white",width = 15,command = get_alarm_time,font=(20)).place(x =100,y=80)

window.mainloop()