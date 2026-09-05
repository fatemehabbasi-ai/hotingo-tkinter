import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

window = tk.Tk()
window.title("App")

windoww = 800
windowh = 300

screenw = window.winfo_screenwidth()
screenh = window.winfo_screenheight()

startx = int((screenw / 2) - (windoww / 2))
starty = int((screenh / 2) - (windowh / 2))

window.geometry(
    '{}x{}+{}+{}'.format(
        windoww, windowh, startx, starty
    )
)

login_frame = tk.Frame(window)
main_frame = tk.Frame(window)

sidebar = tk.Frame(main_frame, bg="#5c7cfa", width=150, height=400)
sidebar.pack(side=tk.LEFT, fill="y")

content_frame = tk.Frame(main_frame)
content_frame.pack(side=tk.RIGHT, fill="both", expand=True)

dashboard_frame = tk.Frame(content_frame)
reservations_frame = tk.Frame(content_frame)
about_frame = tk.Frame(content_frame)


def login():
    login_frame.pack_forget()
    main_frame.pack(fill="both", expand=True)
    show_dashboard()
    
login_frame.pack(fill="both", expand=True)

def show_dashboard():
    dashboard_frame.pack_forget()
    reservations_frame.pack_forget()
    about_frame.pack_forget()

    dashboard_frame.pack(fill="both", expand=True)


    
def show_reservations():
    dashboard_frame.pack_forget()
    reservations_frame.pack_forget()
    about_frame.pack_forget()

    reservations_frame.pack(fill="both", expand=True)

def show_about():
    dashboard_frame.pack_forget()
    reservations_frame.pack_forget()
    about_frame.pack_forget()

    about_frame.pack(fill="both", expand=True)

def logout():
    answer = messagebox.askyesno(
        "Logout",
        "Do you really want to log out?"
    )

    if answer:
        main_frame.pack_forget()
        login_frame.pack(fill="both", expand=True)

tree = ttk.Treeview(reservations_frame, columns=("id", "guest", "room"), show="headings")
tree.heading("id", text="Reservation ID")
tree.heading("guest", text="Guest ID")
tree.heading("room", text="Room ID")
tree.pack()

tree.insert("", "end", values=(1, 12, 345))
tree.insert("", "end", values=(2, 8, 210))

def get_selected():
    selected_item = tree.focus()          
    values = tree.item(selected_item, "values")   
    print(values)

def add_reservation():
    guest=guest_entry.get()
    guest_entry.delete(0, tk.END)
    room=room_entry.get()
    room_entry.delete(0, tk.END)
    tree.insert("", "end", values=(len(tree.get_children()) + 1, guest, room))
    

reserve = tk.Button(reservations_frame,text="Reserve",command=add_reservation)
reserve.pack(fill="x")
        
label = ttk.Label(login_frame, text="HotinGo Login")
label.grid(row=0, column=1, columnspan=2)

user_label = ttk.Label(login_frame, text="Username:")
user_label.grid(row=1, column=1)

user_name = tk.Entry(login_frame)
user_name.grid(row=1, column=2)

password_label = ttk.Label(login_frame, text="Password:")
password_label.grid(row=2, column=1)

password = tk.Entry(login_frame, show="*")
password.grid(row=2, column=2)

login_button = ttk.Button(
    login_frame,
    text="Login",
    command=login
)
login_button.grid(row=3, column=2)

dashboard_btn = tk.Button(sidebar, text="Dashboard", command=show_dashboard)
dashboard_btn.pack(fill="x")

dashboard_label = ttk.Label(dashboard_frame, text="Welcome to Dashboard", font=("Arial", 14, "bold"))
dashboard_label.grid(row=0, column=0, columnspan=3, pady=10)

vacant_card = tk.Frame(dashboard_frame, bg="#eee", padx=20, pady=10)
vacant_card.grid(row=1, column=0, padx=10, pady=10)
vacant_title = tk.Label(vacant_card, text="Vacant", bg="#eee")
vacant_title.pack()
vacant_value = tk.Label(vacant_card, text="350", bg="#eee", font=("Arial", 20, "bold"))
vacant_value.pack()

booked_card = tk.Frame(dashboard_frame, bg="#eee", padx=20, pady=10)
booked_card.grid(row=1, column=1, padx=10, pady=10)
booked_title = tk.Label(booked_card, text="Booked", bg="#eee")
booked_title.pack()
booked_value = tk.Label(booked_card, text="350", bg="#eee", font=("Arial", 20, "bold"))
booked_value.pack()

hotel= tk.Frame(dashboard_frame, bg="#eee", padx=20, pady=10)
hotel.grid(row=1, column=2, padx=10, pady=10)
hvalue_title = tk.Label(hotel, text="Hotel value", bg="#eee")
hvalue_title.pack()
hotel_value = tk.Label(hotel, text="350", bg="#eee", font=("Arial", 20, "bold"))
hotel_value.pack()

about_label = ttk.Label(about_frame, text="About HotinGo", font=("Arial", 14, "bold"))
about_label.pack(pady=20)

about_text = ttk.Label(
    about_frame,
    text="HotinGo is a simple hotel management project\nYou can reserve coming soon.",
    justify="center"
)
about_text.pack(pady=10)

form_frame = tk.Frame(reservations_frame)
form_frame.pack(pady=10)

guest_label = ttk.Label(form_frame, text="Guest ID:")
guest_label.grid(row=0, column=0, padx=5, pady=5)

guest_entry = tk.Entry(form_frame)
guest_entry.grid(row=0, column=1, padx=5, pady=5)

room_label = ttk.Label(form_frame, text="Room ID:")
room_label.grid(row=1, column=0, padx=5, pady=5)

room_entry = tk.Entry(form_frame)
room_entry.grid(row=1, column=1, padx=5, pady=5)


reservations_btn = tk.Button(sidebar, text="Reservations", command=show_reservations)
reservations_btn.pack(fill="x")

about_btn = tk.Button(sidebar, text="About", command=show_about)
about_btn.pack(fill="x")

logout_btn = tk.Button(sidebar, text="Logout", command=logout)
logout_btn.pack(fill="x")





window.mainloop()