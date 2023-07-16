from tkinter import *
from tkinter import ttk, messagebox
import googletrans
import textblob
from google.cloud import translate_v2 as translate



root = Tk()
root.title("This is a Google Translate Page")
root.geometry("1200x500")

def label_change():
    c=combo1.get()
    c1=combo2.get()
    label1.configure(text=c)
    label2.configure(text=c1)
    root.after(1000, label_change)

def translate_now():
    global language
    try:
        text_ = text1.get(1.0, END)
        c2=combo1.get()
        c3=combo2.get()
        if(text_):
            words=textblob.TextBlob(text_)
            lan=words.detect_language()
            for i, j in language.items():
                if(j==c3):
                    lan_=i
            words=words.translate(from_lang=lan, to=str(lan_))
            text2.delete(1.0,END)
            text2.insert(END,words)
    except Exception as e:
        messagebox.showerror("googletrans", "please, try again")


# icon
image_icon = PhotoImage(file="../translate.png")
root.iconphoto(True, image_icon)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = int((screen_width - root.winfo_reqwidth()) / 2)
y = int((screen_height - root.winfo_reqheight()) / 2)
root.geometry("+{}+{}".format(x, y))

arrow_image=PhotoImage(file="../t2.png")
image_label=Label(root, image=arrow_image, width=150)
image_label.place(x=460, y=50)



language = googletrans.LANGUAGES
languageV = list(language.values())
lan1 = list(language.keys())

combo1 = ttk.Combobox(root, values=languageV, font= "Roboto 15", state = "readonly")
combo1.place(x=110, y=20)
combo1.set("Български")

label1 = Label(root, text="Bulgarian", font = "Arial 32 bold", bg= "darkgrey", width=18, bd=5,  relief=GROOVE)
label1.place(x=10, y=50)


f = Frame(root, bg="black", bd=5)
f.place(x=10, y=118, width=440, height=210)

text1 = Text(f, font="Roboto 20", bg="darkgrey", relief=GROOVE, wrap=WORD, state="normal")
text1.place(x=0, y=0, width=430, height=200)

scrollbar1 = Scrollbar(f)
scrollbar1.pack(side="right", fill="y")

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)



combo2 = ttk.Combobox(root, values=languageV, font="Roboto 15", state="readonly")
combo2.place(x=750, y= 20)
combo2.set("Select language")

label2 = Label(root, text="Случаен език", font = "segoe 32 bold", bg= "darkgrey", width=18, bd=5, relief=GROOVE)
label2.place(x=620, y=50)

f1=Frame(root, bg="black", bd=5)
f1.place(x=620, y=118, width=440, height=210)

text2 = Text(f1, font="Roboto 20", bg="darkgrey", relief=GROOVE, wrap=WORD, state="normal")
text2.place(x=0, y=0, width=430, height=200)

scrollbar2 = Scrollbar(f1)
scrollbar2.pack(side="right", fill="y")

scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)

translate=Button(root, text="Translate", font="Roboto 15", activebackground="purple", cursor="hand2", bd=5,
                 bg="red", fg="white", command=translate_now)
translate.place(x=480, y=300)


label_change()

# root.configure(bg="Yellow")
root.mainloop()








