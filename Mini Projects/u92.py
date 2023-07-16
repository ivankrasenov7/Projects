import tkinter
from tkinter import *

root=Tk()
root.title("Калкулатор за кредити")
root.geometry("500x400")

def Calculation():
    grammar=int(grammarEntry.get())
    listening=int(listeningEntry.get())
    speaking=int(speakingEntry.get())
    total=(grammar+listening+speaking)
    Label(text=f"{total}", font="arial 15 bold").place(x=250,y=170)

    average=int(total/3)
    Label(text=f"{average}%", font="arial 15 bold").place(x=250,y=210)

    if(average)>50:
        grade="PASS"
    else:
        grade="FAIL"
    # Label(text=f"{average}%", font="arial 17 bold", fg="red").place(x=250,y=250)
    Label(text=grade, font="arial 17 bold", fg="red").place(x=250, y=250)



sub1=Label(root, text="Граматика",font="arial 10")
sub2=Label(root, text="Слушане", font="arial 10")
sub3=Label(root, text="Говорене", font="arial 10")
total=Label(root, text="Общо Кредити", font="arial 10")
avg=Label(root, text="Резултат", font="arial 10")
grade=Label(root, text="Финален резултат", font="arial 10")

sub1.place(x=50,y=20)
sub2.place(x=50,y=70)
sub3.place(x=50,y=120)
total.place(x=50,y=170)
avg.place(x=50,y=210)
grade.place(x=50,y=250)

grammarValue=StringVar()
listeningValue=StringVar()
speakingValue=StringVar()

grammarEntry=Entry(root, textvariable=grammarValue, font="arial 15", width=15)
listeningEntry=Entry(root, textvariable=listeningValue, font="arial 15", width=15)
speakingEntry=Entry(root, textvariable=speakingValue, font="arial 15", width=15)

grammarEntry.place(x=250, y=20)
listeningEntry.place(x=250, y=70)
speakingEntry.place(x=250,y=120)

Button(text="Калкулирай", font="arial 15", bg="white" ,fg="red", bd=10,command=Calculation).place(x=50,y=300)
Button(text="Изход", font="arial 15", bg="white", fg="black", bd=10,command=lambda: exit()).place(x=350,y=300)




root.configure(bg="green")
root.mainloop()
