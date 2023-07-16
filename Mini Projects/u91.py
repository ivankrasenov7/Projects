from tkinter import *
from datetime import date

root=Tk()
root.geometry("800x600")
root.title("ВЪЗРAСТОВ КАЛКУЛАТОР")
root.resizable(False, False)

# bg_image = PhotoImage(file="background.png")
# bg_label = Label(root, image=bg_image)
# bg_label.place(x=0, y=0, relwidth=1, relheight=1)

photo=PhotoImage(file="../age1.png")
photo=photo.subsample(2,2)
myimage=Label(image=photo)  
myimage.pack(padx=15, pady=15)

def getAstrologicalSign(month, day):
    signs = ["Козирог", "Водолей", "Риби", "Овен", "Телец", "Близнаци", "Рак", "Лъв", "Дева", "Везни", "Скорпион", "Стрелец"]
    if month == 12:
        astro_sign = 'Стрелец' if (day < 22) else 'Козирог'
    elif month == 1:
        astro_sign = 'Козирог' if (day < 20) else 'Водолей'
    elif month == 2:
        astro_sign = 'Водолей' if (day < 19) else 'Риби'
    elif month == 3:
        astro_sign = 'Риби' if (day < 21) else 'Овен'
    elif month == 4:
        astro_sign = 'Овен' if (day < 20) else 'Телец'
    elif month == 5:
        astro_sign = 'Телец' if (day < 21) else 'Близнаци'
    elif month == 6:
        astro_sign = 'Близнаци' if (day < 21) else 'Рак'
    elif month == 7:
        astro_sign = 'Рак' if (day < 23) else 'Лъв'
    elif month == 8:
        astro_sign = 'Лъв' if (day < 23) else 'Дева'
    elif month == 9:
        astro_sign = 'Дева' if (day < 23) else 'Везни'
    elif month == 10:
        astro_sign = 'Везни' if (day < 23) else 'Скорпион'
    elif month == 11:
        astro_sign = 'Скорпион' if (day < 22) else 'Стрелец'
    return signs[month-1]

def calculateAge():
    today=date.today()
    birthDate=date(int(yearEntry.get()),int(monthEntry.get()), int(dayEntry.get()))
    age = today.year - birthDate.year -((today.month,today.day)<(birthDate.month,birthDate.day))
    Label(text=f"{nameValue.get()}, вашата текуща възраст е {age} години", font=30).place(x=300,y=550)
    sign = getAstrologicalSign(int(monthEntry.get()), int(dayEntry.get()))
    Label(text=f"{nameValue.get()}, вашата текуща възраст е {age} години и вашият зодиакален знак е {sign}",
          font=30).place(x=150, y=550)


Label(text="Име", font=24).place(x=200, y=300)
Label(text="Година", font=24).place(x=200, y=350)
Label(text="Месец", font=24).place(x=200, y=400)
Label(text="Ден", font=24).place(x=200, y=450)

nameValue=StringVar()
yearValue=StringVar()
monthValue=StringVar()
dayValue=StringVar()

nameEntry=Entry(root, textvariable=nameValue, width=30, bd=5, font=20)
nameEntry.place(x=300, y=300)

yearEntry=Entry(root, textvariable=yearValue, width=30, bd=5, font=20)
yearEntry.place(x=300, y=350)

monthEntry=Entry(root, textvariable=monthValue, width=30, bd=5, font=20)
monthEntry.place(x=300, y=400)

dayEntry=Entry(root, textvariable=dayValue, width=30, bd=5, font=20)
dayEntry.place(x=300, y=450)

Button(text="Изчисли възрастта", font=20, bg="black", fg="white", width=11, height=2, command=calculateAge).place(x=300, y=500)




root.configure(bg="yellow")
root.mainloop()



