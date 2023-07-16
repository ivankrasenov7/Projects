import tkinter
from tkinter import ttk
from tkinter import messagebox
import sqlite3

def enter_data():
    accepted = accept_var.get()

    if accepted == 'Accepted':
        first_name = first_name_entry.get()
        last_name = last_name_entry.get()

        if first_name and last_name:
            title = title_combobox.get()
            age = age_spinbox.get()
            nationality = nationality_combobox.get()

            registration_status = reg_status_var.get()
            numcourse = numcourses_spinbox.get()
            numsemesters = numsemesters_spinbox.get()

            print(f"First name: {first_name} Last name: {last_name}")
            print(f"Title: {title} Age: {age} Nationality {nationality}")
            print(f"Registration status {registration_status}, Numcourse {numcourse} Numsemesters {numsemesters}")
            print("---------------------------")

            conn = sqlite3.connect("dataset.db")

            table_create_query = ''' CREATE TABLE IF NOT EXISTS Student_Data (
            firstname TEXT, lastname TEXT, title TEXT, age INT, nationality TEXT,
            registration_status TEXT, numcourses INT, numsemester INT
            )
            
            '''
            conn.execute(table_create_query)
            data_insert_query = '''INSERT INTO Student_Data(firstname, lastname, title, age, nationality, registration_status,
            numcourses, numsemester) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            '''
            data_insert_tuple = (first_name, last_name, title, age, nationality, registration_status,
                                 numcourse, numsemesters)
            cursor = conn.cursor()
            cursor.execute(data_insert_query,data_insert_tuple)
            conn.commit()
            conn.close()


        else:
            tkinter.messagebox.showwarning(title="Error", message= "First name and Last name are required")
    else:
        tkinter.messagebox.showwarning(title="Error", message="You have not accepted the terms")

window = tkinter.Tk()
window.title("Entry form")

frame = tkinter.Frame(window)
frame.pack()

user_info_frame = tkinter.LabelFrame(frame, text="User Information")
user_info_frame.grid(row=0, column=0, padx=20, pady=10)

first_name_label = tkinter.Label(user_info_frame, text="First Name")
first_name_label.grid(row=0, column = 0)
last_name_label = tkinter.Label(user_info_frame, text="Last Name")
last_name_label.grid(row=0, column = 1)

first_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry = tkinter.Entry(user_info_frame)
last_name_entry.grid(row=1, column=1)

title_label = tkinter.Label(user_info_frame, text = "Title")
title_combobox = ttk.Combobox(user_info_frame, values=['MR', 'MRS', 'DR'])
title_label.grid(row=0, column=2)
title_combobox.grid(row=1, column=2)

age_label = tkinter.Label(user_info_frame, text="Age")
age_spinbox = tkinter.Spinbox(user_info_frame, from_=18, to=110)
age_label.grid(row =2, column=4)
age_spinbox.grid(row=3, column=0)

nationality_label = tkinter.Label(user_info_frame, text = "Nationality")
nationality_combobox = tkinter.Spinbox(user_info_frame, values=['Africa', 'Asia', 'Europe', 'Oceania', 'North America'])
nationality_label.grid(row=2, column=1)
nationality_combobox.grid(row=3, column=1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

course_frame = tkinter.LabelFrame(frame)
course_frame.grid(row=1, column=0, sticky='news', padx=20, pady=10)

registered_label = tkinter.Label(course_frame, text="Registration Status")

reg_status_var = tkinter.StringVar(value = "Not Registered")
registered_ckeck = tkinter.Checkbutton(course_frame, text="Currently Registered",
                                       variable = reg_status_var, onvalue="Registered", offvalue="Not Registered")

registered_label.grid(row=0, column=0)
registered_ckeck.grid(row=1, column=0)

numcourses_label = tkinter.Label(course_frame, text = '# Completed Courses')
numcourses_spinbox = tkinter.Spinbox(course_frame, from_=0, to="infinity")
numcourses_label.grid(row=0, column=1)
numcourses_spinbox.grid(row=1, column=1)

numsemesters_label = tkinter.Label(course_frame, text = '# Semesters')
numsemesters_spinbox = tkinter.Spinbox(course_frame, from_=0, to="infinity")
numsemesters_label.grid(row=0, column=2)
numsemesters_spinbox.grid(row=1, column=2)

for widget in course_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

terms_frame = tkinter.LabelFrame(frame, text = "Terms and Conditions")
terms_frame.grid(row=2, column=0, sticky='news', padx=20, pady=10)

accept_var = tkinter.StringVar(value='Not Accepted')
terms_check = tkinter.Checkbutton(terms_frame, text = 'I accept the terms and conditions',
                                  variable=accept_var, onvalue="Accepted", offvalue="Not accepted")

terms_check.grid(row=0, column=4)

button = tkinter.Button(frame, text= "Enter Data", command=enter_data)
button.grid(row=3, column=0, sticky='news', padx=20, pady=18)

window.mainloop()






