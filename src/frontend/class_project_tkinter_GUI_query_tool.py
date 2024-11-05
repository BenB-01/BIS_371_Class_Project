# SPDX-FileCopyrightText: 2024 Ben Burkert
#
# SPDX-License-Identifier: MIT

# import tkinter for GUI tools
import tkinter as tk
from tkinter import filedialog
# import class to interact with the database
from ..backend.DatabaseInteractor import DatabaseInteractor

db_interactor = DatabaseInteractor()
connection = db_interactor.connect()
cursor = connection.cursor()


# define query option buttons
def submitted_data_find():
    display_textbox.delete("1.0", tk.END)
    try:
        cursor.execute("SELECT Paper_Title, Activity_Date FROM Paper, Activity "
                       "WHERE Paper.Paper_ID = Activity.Paper_ID AND Activity.Activity_Type = 1 "
                       "ORDER BY Activity.Activity_Date")
    except Exception as err:
        print("There was an issue executing the submitted query.", err)
    rows = cursor.fetchall()
    for row in rows:
        display_textbox.insert("1.0", ("Submitted: " + row[0] + " Date: " '{:%Y-%m-%d}'.format(row[1]) + '\n'))


def accepted_data_find():
    display_textbox.delete("1.0", tk.END)
    try:
        cursor.execute("SELECT Paper_Title, Activity_Date FROM Paper, Activity "
                       "WHERE Paper.Paper_ID = Activity.Paper_ID AND Activity.Activity_Type = 2 "
                       "ORDER BY Activity.Activity_Date")
    except Exception as err:
        print("There was an issue executing the accepted query.", err)
    rows = cursor.fetchall()
    for row in rows:
        display_textbox.insert("1.0", ("Accepted: " + row[0] + " Date: " '{:%Y-%m-%d}'.format(row[1]) + '\n'))


def rejected_data_find():
    display_textbox.delete("1.0", tk.END)
    try:
        cursor.execute("SELECT Paper_Title, Activity_Date FROM Paper, Activity "
                       "WHERE Paper.Paper_ID = Activity.Paper_ID AND Activity.Activity_Type = 3 "
                       "ORDER BY Activity.Activity_Date")
    except Exception as err:
        print("There was an issue executing the rejected query.", err)
    rows = cursor.fetchall()
    for row in rows:
        display_textbox.insert("1.0", ("Rejected: " + row[0] + " Date: " '{:%Y-%m-%d}'.format(row[1]) + '\n'))


def rr_data_find():
    display_textbox.delete("1.0", tk.END)
    try:
        cursor.execute("SELECT Paper_Title, Activity_Date FROM Paper, Activity "
                       "WHERE Paper.Paper_ID = Activity.Paper_ID AND Activity.Activity_Type = 4 "
                       "ORDER BY Activity.Activity_Date")
    except Exception as err:
        print("There was an issue executing the R&R query.", err)
    rows = cursor.fetchall()
    for row in rows:
        display_textbox.insert("1.0", ("R&R: " + row[0] + " Date: " '{:%Y-%m-%d}'.format(row[1]) + '\n'))


# TKINTER WINDOW FORMATTING


# create the root window
window = tk.Tk()
window.title("Database query tool for activities ordered by date")

# frames:
display_frame = tk.Frame(master=window)
activity_buttons_frame = tk.Frame(master=window)

# frame formatting:
display_frame.pack(side=tk.TOP, fill=tk.BOTH)
activity_buttons_frame.pack(side=tk.TOP)

# textbox for displaying things
display_textbox = tk.Text(master=display_frame, width=113, height=25)
display_textbox.pack(side=tk.LEFT, fill=tk.Y)

# scrollbar for the display textbox
scrollbar = tk.Scrollbar(master=display_frame)
scrollbar.pack(side=tk.LEFT, fill=tk.Y)

# associate the scrollbar with the listbox
display_textbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=display_textbox.yview)

# Four buttons to query each activity type
submitted_button = tk.Button(text="Submitted", master=activity_buttons_frame, command=submitted_data_find)
accepted_button = tk.Button(text="Accepted", master=activity_buttons_frame, command=accepted_data_find)
rejected_button = tk.Button(text="Rejected", master=activity_buttons_frame, command=rejected_data_find)
rr_button = tk.Button(text="R&R", master=activity_buttons_frame, command=rr_data_find)

submitted_button.pack(side=tk.LEFT)
accepted_button.pack(side=tk.LEFT)
rejected_button.pack(side=tk.LEFT)
rr_button.pack(side=tk.LEFT)

display_textbox.insert("1.0", """Please select which activity type you would like a dated list of. \n
Your options are: \n -Submitted \n -Accepted \n -Rejected \n -R&R""")

# start main event manager
window.mainloop()
