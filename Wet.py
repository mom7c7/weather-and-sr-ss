import tkinter as ttk
from tkinter import Frame,Button,Label
import requests
root = ttk.Tk()
root.geometry('400x600')
root.resizable(0,0)
root.title('Weather App')
root.configure(bg='#339933')
URL = 'https://api.open-meteo.com/v1/forecast?latitude=35.8327&longitude=50.9915&hourly=temperature_2m&daily=sunrise,sunset&timezone=auto&forecast_days=3'
location = 'delhi technological university'
PARAMS = {'address' : location}
data = requests.get(url=URL,params=PARAMS)
info = data.json()
myday = None
frm1 = Frame(root,bg='#339933',width=400,height=50)
frm1.pack()
frm2 = Frame(root,bg='#339933',width=400,height=50)
frm2.pack()
frm3 = Frame(root,bg='#339933',width=400,height=50)
frm3.pack()
frm4 = Frame(root,bg='#339933',width=400,height=50)
frm4.pack()
frm5 = Frame(root,bg='#339933',width=400,height=50)
frm5.pack()
frm6 = Frame(root,bg='#339933',width=400,height=50)
frm6.pack()
frm7 = Frame(root,bg='#339933',width=400,height=50)
frm7.pack()
frm8 = Frame(root,bg='#339933',width=400,height=50)
frm8.pack()
frm9 = Frame(root,bg='#339933',width=400,height=50)
frm9.pack()
def mnp():
    global info
    root2 = ttk.Tk()
    root2.geometry('150x300')
    root2.resizable(0,0)
    root2.configure(bg='#339933')
    days = info["daily"]["time"]
    dayone = days[0].split('-')
    day1 = int(dayone[2])
    daytwo = days[1].split('-')
    day2 = int(daytwo[2])
    daythree = days[2].split('-')
    day3 = int(daythree[2]) 
    myday = None
    def getsrss1():
        global info,myday,day1
        srr = info["daily"]["sunrise"][0].split('T')
        sss = info["daily"]["sunset"][0].split('T')
        sr = srr[1]
        ss = sss[1]
        lbla.config(text=f'Sunrise = {sr}\n\nSunset = {ss}')
        myday = 0
        return myday
    def getsrss2():
        global info,myday,day2
        srr = info["daily"]["sunrise"][1].split('T')
        sss = info["daily"]["sunset"][1].split('T')
        sr = srr[1]
        ss = sss[1]
        lbla.config(text=f'Sunrise = {sr}\n\nSunset = {ss}')
        myday = 1
        return myday
    def getsrss3():
        global info,myday,day3
        srr = info["daily"]["sunrise"][2].split('T')
        sss = info["daily"]["sunset"][2].split('T')
        sr = srr[1]
        ss = sss[1]
        lbla.config(text=f'Sunrise = {sr}\n\nSunset = {ss}')
        myday = 2
        return myday   
    btna = Button(root2,text=day1,font=('MS UI Gothic',16),bg='#99FF99',activebackground='#003300',activeforeground='gray',command=getsrss1)
    btna.pack(side='top',pady=10)
    btnb = Button(root2,text=day2,font=('MS UI Gothic',16),bg='#99FF99',activebackground='#003300',activeforeground='gray',command=getsrss2)
    btnb.pack(side='top',pady=10)
    btnc = Button(root2,text=day3,font=('MS UI Gothic',16),bg='#99FF99',activebackground='#003300',activeforeground='gray',command=getsrss3)
    btnc.pack(side='top',pady=10)
    lbla = Label(root2,bg='#339933',font=('MS UI Gothic',16))
    lbla.pack()
    return myday
def zero():
    global myday
    if myday != 0 or myday != 1 or myday != 2:
        myday = 0
    if myday == 0:
        dot = 0
    elif myday == 1:
        dot = 24
    elif myday == 2:
        dot = 48
    temp = info["hourly"]["temperature_2m"][dot]
    lbl1.config(text=f'temp : {temp}')
def one():
    global myday
    if myday == 0:
        dot = 1
    elif myday == 1:
        dot = 25
    elif myday == 2:
        dot = 49
    temp = info["hourly"]["temperature_2m"][dot]
    lbl1.config(text=f'temp : {temp}')
def two():
    global myday
    if myday == 0:
        dot = 2
    elif myday == 1:
        dot = 26
    elif myday == 2:
        dot = 50
    temp = info["hourly"]["temperature_2m"][dot]
    lbl1.config(text=f'temp : {temp}')
def three():
    global myday
    if myday == 0:
        dot = 3
    elif myday == 1:
        dot = 27
    elif myday == 2:
        dot = 51
    temp = info["hourly"]["temperature_2m"][dot]
    lbl1.config(text=f'temp : {temp}')
def four():
    global myday
    if myday == 0:
        dot = 4
    elif myday == 1:
        dot = 28
    elif myday == 2:
        dot = 52
    temp = info["hourly"]["temperature_2m"][dot]
    lbl1.config(text=f'temp : {temp}')
def five():
    global myday
    if myday == 0:
        dot = 5
    elif myday == 1:
        dot = 29
    elif myday == 2:
        dot = 53
    temp = info["hourly"]["temperature_2m"][dot]
    lbl1.config(text=f'temp : {temp}')
def six():
    global myday
    if myday == 0:
        dot = 6
    elif myday == 1:
        dot = 30
    elif myday == 2:
        dot = 54
    temp = info["hourly"]["temperature_2m"][dot]
    lbl1.config(text=f'temp : {temp}')
def seven():
    global myday
    if myday == 0:
        dot = 7
    elif myday == 1:
        dot = 31
    elif myday == 2:
        dot = 55
    temp = info["hourly"]["temperature_2m"][dot]
    lbl1.config(text=f'temp : {temp}')
def eight():
    global myday
    if myday == 0:
        dot = 8
    elif myday == 1:
        dot = 32
    elif myday == 2:
        dot = 56
    temp = info["hourly"]["temperature_2m"][dot]
    lbl1.config(text=f'temp : {temp}')
def nine():
    global myday
    if myday == 0:
        dot = 9
    elif myday == 1:
        dot = 33
    elif myday == 2:
        dot = 57
    temp = info["hourly"]["temperature_2m"][dot]
    lbl1.config(text=f'temp : {temp}')
def ten():
    global myday
    if myday == 0:
        dot = 10
    elif myday == 1:
        dot = 34
    elif myday == 2:
        dot = 58
    temp = info["hourly"]["temperature_2m"][dot]
    lbl1.config(text=f'temp : {temp}')
def eleven():
    global myday
    if myday == 0:
        dot = 11
    elif myday == 1:
        dot = 35
    elif myday == 2:
        dot = 59
    temp = info["hourly"]["temperature_2m"][dot]
    lbl1.config(text=f'temp : {temp}')
def twelve():
    global myday
    if myday == 0:
        dot = 12
    elif myday == 1:
        dot = 36
    elif myday == 2:
        dot = 60
    temp = info["hourly"]["temperature_2m"][dot]
    lbl1.config(text=f'temp : {temp}')
def threteen():
    global myday
    if myday == 0:
        dot = 13
    elif myday == 1:
        dot = 37
    elif myday == 2:
        dot = 61
    temp = info["hourly"]["temperature_2m"][dot]
    lbl1.config(text=f'temp : {temp}')
def fourteen():
    global myday
    if myday == 0:
        dot = 14
    elif myday == 1:
        dot = 38
    elif myday == 2:
        dot = 62
    temp = info["hourly"]["temperature_2m"][dot]
    lbl1.config(text=f'temp : {temp}')
def fiveteen():
    global myday
    if myday == 0:
        dot = 15
    elif myday == 1:
        dot = 39
    elif myday == 2:
        dot = 63
    temp = info["hourly"]["temperature_2m"][dot]
    lbl1.config(text=f'temp : {temp}')
def sixteen():
    global myday
    if myday == 0:
        dot = 16
    elif myday == 1:
        dot = 40
    elif myday == 2:
        dot = 64
    temp = info["hourly"]["temperature_2m"][dot]
    lbl1.config(text=f'temp : {temp}')
def seventeen():
    global myday
    if myday == 0:
        dot = 17
    elif myday == 1:
        dot = 41
    elif myday == 2:
        dot = 65
    temp = info["hourly"]["temperature_2m"][dot]
    lbl1.config(text=f'temp : {temp}')
def eighteen():
    global myday
    if myday == 0:
        dot = 18
    elif myday == 1:
        dot = 42
    elif myday == 2:
        dot = 66
    temp = info["hourly"]["temperature_2m"][dot]
    lbl1.config(text=f'temp : {temp}')
def nineteen():
    global myday
    if myday == 0:
        dot = 19
    elif myday == 1:
        dot = 43
    elif myday == 2:
        dot = 67
    temp = info["hourly"]["temperature_2m"][dot]
    lbl1.config(text=f'temp : {temp}')
def twenty():
    global myday
    if myday == 0:
        dot = 20
    elif myday == 1:
        dot = 44
    elif myday == 2:
        dot = 68
    temp = info["hourly"]["temperature_2m"][dot]
    lbl1.config(text=f'temp : {temp}')
def twone():
    global myday
    if myday == 0:
        dot = 21
    elif myday == 1:
        dot = 45
    elif myday == 2:
        dot = 69
    temp = info["hourly"]["temperature_2m"][dot]
    lbl1.config(text=f'temp : {temp}')
def twotwo():
    global myday
    if myday == 0:
        dot = 22
    elif myday == 1:
        dot = 46
    elif myday == 2:
        dot = 70
    temp = info["hourly"]["temperature_2m"][dot]
    lbl1.config(text=f'temp : {temp}')
def twothree():
    global myday
    if myday == 0:
        dot = 23
    elif myday == 1:
        dot = 47
    elif myday == 2:
        dot = 71
    temp = info["hourly"]["temperature_2m"][dot]
    lbl1.config(text=f'temp : {temp}')
btnx = Button(frm1,text='Choose Day',bg='#99FF99',width=20,font=('MS UI Gothic',16),activebackground='#003300',activeforeground='gray',command=mnp)
btnx.pack(fill='x',pady=10)
mnp()
btn0 = Button(frm2,font=('MS UI Gothic',16),text='00',activebackground='#003300',activeforeground='gray',bg='#99FF99',command=zero)
btn0.pack(side='left',padx=10,pady=10)
btn1 = Button(frm2,font=('MS UI Gothic',16),text='01',activebackground='#003300',activeforeground='gray',bg='#99FF99',command=one)
btn1.pack(side='left',padx=10,pady=10)
btn2 = Button(frm2,font=('MS UI Gothic',16),text='02',activebackground='#003300',activeforeground='gray',bg='#99FF99',command=two)
btn2.pack(side='left',padx=10,pady=10)
btn3 = Button(frm2,font=('MS UI Gothic',16),text='03',activebackground='#003300',activeforeground='gray',bg='#99FF99',command=three)
btn3.pack(side='left',padx=10,pady=10)
btn4 = Button(frm2,font=('MS UI Gothic',16),text='04',activebackground='#003300',activeforeground='gray',bg='#99FF99',command=four)
btn4.pack(side='left',padx=10,pady=10)
btn5 = Button(frm2,font=('MS UI Gothic',16),text='05',activebackground='#003300',activeforeground='gray',bg='#99FF99',command=five)
btn5.pack(side='left',padx=10,pady=10)
btn6 = Button(frm3,font=('MS UI Gothic',16),text='06',activebackground='#003300',activeforeground='gray',bg='#99FF99',command=six)
btn6.pack(side='left',padx=10,pady=10)
btn7 = Button(frm3,font=('MS UI Gothic',16),text='07',activebackground='#003300',activeforeground='gray',bg='#99FF99',command=seven)
btn7.pack(side='left',padx=10,pady=10)
btn8 = Button(frm3,font=('MS UI Gothic',16),text='08',activebackground='#003300',activeforeground='gray',bg='#99FF99',command=eight)
btn8.pack(side='left',padx=10,pady=10)
btn9 = Button(frm3,font=('MS UI Gothic',16),text='09',activebackground='#003300',activeforeground='gray',bg='#99FF99',command=nine)
btn9.pack(side='left',padx=10,pady=10)
btn10 = Button(frm3,font=('MS UI Gothic',16),text='10',activebackground='#003300',activeforeground='gray',bg='#99FF99',command=ten)
btn10.pack(side='left',padx=10,pady=10)
btn11 = Button(frm3,font=('MS UI Gothic',16),text='11',activebackground='#003300',activeforeground='gray',bg='#99FF99',command=eleven)
btn11.pack(side='left',padx=10,pady=10)
btn12 = Button(frm4,font=('MS UI Gothic',16),text='12',activebackground='#003300',activeforeground='gray',bg='#99FF99',command=twelve)
btn12.pack(side='left',padx=10,pady=10)
btn13 = Button(frm4,font=('MS UI Gothic',16),text='13',activebackground='#003300',activeforeground='gray',bg='#99FF99',command=threteen)
btn13.pack(side='left',padx=10,pady=10)
btn14 = Button(frm4,font=('MS UI Gothic',16),text='14',activebackground='#003300',activeforeground='gray',bg='#99FF99',command=fourteen)
btn14.pack(side='left',padx=10,pady=10)
btn15 = Button(frm4,font=('MS UI Gothic',16),text='15',activebackground='#003300',activeforeground='gray',bg='#99FF99',command=fiveteen)
btn15.pack(side='left',padx=10,pady=10)
btn16 = Button(frm4,font=('MS UI Gothic',16),text='16',activebackground='#003300',activeforeground='gray',bg='#99FF99',command=sixteen)
btn16.pack(side='left',padx=10,pady=10)
btn17 = Button(frm4,font=('MS UI Gothic',16),text='17',activebackground='#003300',activeforeground='gray',bg='#99FF99',command=seventeen)
btn17.pack(side='left',padx=10,pady=10)
btn18 = Button(frm5,font=('MS UI Gothic',16),text='18',activebackground='#003300',activeforeground='gray',bg='#99FF99',command=eighteen)
btn18.pack(side='left',padx=10,pady=10)
btn19 = Button(frm5,font=('MS UI Gothic',16),text='19',activebackground='#003300',activeforeground='gray',bg='#99FF99',command=nineteen)
btn19.pack(side='left',padx=10,pady=10)
btn20 = Button(frm5,font=('MS UI Gothic',16),text='20',activebackground='#003300',activeforeground='gray',bg='#99FF99',command=twenty)
btn20.pack(side='left',padx=10,pady=10)
btn21 = Button(frm5,font=('MS UI Gothic',16),text='21',activebackground='#003300',activeforeground='gray',bg='#99FF99',command=twone)
btn21.pack(side='left',padx=10,pady=10)
btn22 = Button(frm5,font=('MS UI Gothic',16),text='22',activebackground='#003300',activeforeground='gray',bg='#99FF99',command=twotwo)
btn22.pack(side='left',padx=10,pady=10)
btn23 = Button(frm5,font=('MS UI Gothic',16),text='23',activebackground='#003300',activeforeground='gray',bg='#99FF99',command=twothree)
btn23.pack(side='left',padx=10,pady=10)
lbl1 = Label(frm6,text='Click On Hour Button',font=('MS UI Gothic',16),bg='#339933')
lbl1.pack()
root.mainloop()