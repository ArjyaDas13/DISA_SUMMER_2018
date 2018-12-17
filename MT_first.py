from Tkinter import *
import Tkinter
from meteor import *
from gtm import *
from bleu_new import *
from wer import *
from amber import *

top=Tk()
def window(main):
    main.title('MT Evaluator')
    main.update_idletasks()
    width=main.winfo_width()
    height=main.winfo_height()
    x=(main.winfo_screenwidth() // 2) - (width // 2)
    y=(main.winfo_screenheight() // 2) - (height // 2)
    main.geometry('{}x{}+{}+{}'.format(width,height,x,y))
L0 = Label(top, text="MT Evaluator",font="Times 24",fg="orange").grid(row=0,columnspan=4)
L1 = Label(top, text="Enter translated Sentence",).grid(row=1,column=0,sticky=W)
L2 = Label(top, text="Enter reference sentence",).grid(row=2,column=0,sticky=W)
L3 = Label(top, text="METEOR Score",).grid(row=3,column=0,sticky=W)
L4 = Label(top, text="WER Score",).grid(row=4,column=0,sticky=W)
L5 = Label(top, text="GTM Score",).grid(row=5,column=0,sticky=W)
L6 = Label(top, text="Amber Score",).grid(row=6,column=0,sticky=W)
L7 = Label(top, text="BLEU Aggregate Score",).grid(row=7,column=0,sticky=W)
L8 = Label(top, text="BLEU 1gram Score",).grid(row=8,column=0,sticky=W)
L9 = Label(top, text="BLEU  2gram Score",).grid(row=9,column=0,sticky=W)
L10 = Label(top, text="BLEU 3gram Score",).grid(row=10,column=0,sticky=W)
L11 = Label(top, text="BLEU 4gram Score",).grid(row=11,column=0,sticky=W)


E1 = Entry(top, bd =5,width=80)
E1.grid(row=1,column=1)
E2 = Entry(top, bd =5,width=80)
E2.grid(row=2,column=1)
E3 = Entry(top, bd =5,width=80)
E3.grid(row=3,column=1)
E4 = Entry(top, bd =5,width=80)
E4.grid(row=4,column=1)
E5 = Entry(top, bd =5,width=80)
E5.grid(row=5,column=1)
E6 = Entry(top, bd =5,width=80)
E6.grid(row=6,column=1)
E7 = Entry(top, bd =5,width=80)
E7.grid(row=7,column=1)
E8 = Entry(top, bd =5,width=80)
E8.grid(row=8,column=1)
E9 = Entry(top, bd =5,width=80)
E9.grid(row=9,column=1)
E10 = Entry(top, bd =5,width=80)
E10.grid(row=10,column=1)
E11 = Entry(top, bd =5,width=80)
E11.grid(row=11,column=1)


def getMeteor():
    hypot=Entry.get(E1).lower()
    refer=Entry.get(E2).lower()
    Entry.insert(E3,0,meteor(refer, hypot)) #wer takes parameters r and h as strings

def getWER():
    hypot=Entry.get(E1).lower()
    refer=Entry.get(E2).lower()
    Entry.insert(E4,0,wer(refer,hypot)) #wer takes parameters r and h as strings

def GetGTM():
    hypot=Entry.get(E1).lower()
    refer=Entry.get(E2).lower()
    Entry.insert(E5,0,gtm(refer,hypot)) #gtm takes parameters r and h as strings


def GetAmber():
    hypot=Entry.get(E1).lower()
    refer=Entry.get(E2).lower()
    Entry.insert(E6,0,amber(refer,hypot))


def GetBleuAgg():
    hypot=Entry.get(E1).lower()
    refer=Entry.get(E2).lower()
    Entry.insert(E7,0,Bleu(refer,hypot))

def GetBleu1():
    hypot=Entry.get(E1).lower()
    refer=Entry.get(E2).lower()
    Entry.insert(E8,0,Bleu1gram(refer,hypot)) #bleu takes parameters r and h as strings

def GetBleu2():
    hypot=Entry.get(E1).lower()
    refer=Entry.get(E2).lower()
    Entry.insert(E9,0,Bleu2gram(refer,hypot)) #bleu takes parameters r and h as strings

def GetBleu3():
    hypot=Entry.get(E1).lower()
    refer=Entry.get(E2).lower()
    Entry.insert(E10,0,Bleu3gram(refer,hypot)) #bleu takes parameters r and h as strings

def GetBleu4():
    hypot=Entry.get(E1).lower()
    refer=Entry.get(E2).lower()
    Entry.insert(E11,0,Bleu4gram(refer,hypot))

B=Button(top, text ="Submit",font="Arial 10",command = getMeteor).grid(row=3,column=3)
B=Button(top, text ="Submit",font="Arial 10",command = getWER).grid(row=4,column=3)
B=Button(top, text ="Submit",font="Arial 10",command = GetGTM).grid(row=5,column=3)
B=Button(top, text ="Submit",font="Arial 10",command = GetAmber).grid(row=6,column=3)
B=Button(top, text ="Submit",font="Arial 10",command = GetBleuAgg).grid(row=7,column=3)
B=Button(top, text ="Submit",font="Arial 10",command = GetBleu1).grid(row=8,column=3)
B=Button(top, text ="Submit",font="Arial 10",command = GetBleu2).grid(row=9,column=3)
B=Button(top, text ="Submit",font="Arial 10",command = GetBleu3).grid(row=10,column=3)
B=Button(top, text ="Submit",font="Arial 10",command = GetBleu4).grid(row=11,column=3)

def reset():
    E1.delete(0,END)
    E2.delete(0,END)
    E3.delete(0,END)
    E4.delete(0,END)
    E5.delete(0,END)
    E6.delete(0,END)
    E7.delete(0,END)
    E8.delete(0,END)
    E9.delete(0,END)
    E10.delete(0,END)
    E11.delete(0,END)

def process():
    hypot=Entry.get(E1).lower()
    refer=Entry.get(E2).lower()
    Entry.insert(E3,0,meteor(refer, hypot)) #wer takes parameters r and h as strings
    Entry.insert(E4,0,wer(refer,hypot)) #gtm takes parameters r and h as strings
    Entry.insert(E5,0,gtm(refer,hypot)) #bleu takes parameters r and h as strings
    Entry.insert(E6,0,amber(refer,hypot))
    Entry.insert(E7,0,Bleu(refer,hypot))
    Entry.insert(E8,0,Bleu1gram(refer,hypot)) #bleu takes parameters r and h as strings
    Entry.insert(E9,0,Bleu2gram(refer,hypot)) #bleu takes parameters r and h as strings
    Entry.insert(E10,0,Bleu3gram(refer,hypot)) #bleu takes parameters r and h as strings
    Entry.insert(E11,0,Bleu4gram(refer,hypot))



B=Button(top, text ="Submit",font="Arial 10",command = process).grid(row=14,columnspan=1)
B=Button(top, text ="Reset",font="Arial 10",command = reset).grid(row=14,columnspan=2)
window(top)
top.mainloop()
