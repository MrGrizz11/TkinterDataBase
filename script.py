# MODULES
import tkinter

# WINDOW INIT
mainWindow = tkinter.Tk()

# TAKE SCREEN RESOLUTION
screenWidth = mainWindow.winfo_screenwidth()
screenHeight = mainWindow.winfo_screenheight()

# WINDOW CONFIGURE
mainWindow.title("Data Base")
mainWindow.geometry("1820x900")
#mainWindow.attributes('-fullscreen', True)
mainWindow.resizable(True, True)
mainWindow.state('zoomed')



# |||||     LOGIN PAGE     ||||| #


# FUNCTIONS
def open_menu():
    create_menu()


def login():
    #open_menu()
    credentials_situation_label.place(relx=0.5, rely=0.428)

    username = username_field.get()
    password = password_field.get()

    if username == "" and password == "":
        credentials_situation_label["text"] = "enter your credentials"
    elif username != "" and password == "":
        credentials_situation_label["text"] = "password field is empty"
    elif password != "" and username == "":
        credentials_situation_label["text"] = "username field is empty"
    elif username != "Grizz" or password != "12345678":
        credentials_situation_label["text"] = "incorrect credentials"
        password_field.delete(0, tkinter.END)
    elif username == "Grizz" and password == "12345678":
        open_menu()



# UI
def create_login_page():
    global password_field, username_field, credentials_situation_label


# $$ LEFT SIDE $$
    left_frame = tkinter.Frame(bg="#fff")
    left_frame.place(relheight=1, relwidth=1)

    left_label = tkinter.Label(left_frame, text="Welcome To Data Base",  font=("Century Gothic", 30), bg="#364F6B", fg="#fff")
    left_label.place(relwidth=0.5, relheight=1)


# $$ RIGHT SIDE $$
    right_frame = tkinter.Frame(bg="#fff")
    right_frame.place(relheight=1, relwidth=0.5, relx=0.5)


# USERNAME
    username_text = tkinter.Label(right_frame, text="username", font=("Century Gothic", 14), bg="#fff", fg="#364F6B")
    username_text.place(relx=0.25, rely=0.365, relwidth=0.1, relheight=0.02)

    username_field = tkinter.Entry(right_frame, font=("Century Gothic", 12), width=27, fg="#364F6B", exportselection=0, relief=tkinter.GROOVE, bd=2)
    username_field.place(relx=0.372, rely=0.36, relheight=0.029, relwidth=0.26)


# PASSWORD
    password_text = tkinter.Label(right_frame, text="password", font=("Century Gothic", 14), bg="#fff", fg="#364F6B")
    password_text.place(relx=0.25, rely=0.4049, relwidth=0.1, relheight=0.02)

    password_field = tkinter.Entry(right_frame, font=("Century Gothic", 11), fg="#364F6B", exportselection=0, relief=tkinter.GROOVE, bd=2, show="*")
    password_field.place(relx=0.372, rely=0.4, relheight=0.029, relwidth=0.26)


# LOGIN
    login_button = tkinter.Button(right_frame, font=("Century Gothic", 16), text="LOGIN", bg="#ffffff", fg="#364F6B", relief=tkinter.GROOVE, bd=2, padx=25, activebackground="#fff", activeforeground="#364F6B", command=login)
    login_button.place(relx=(0.5-0.14/2), rely=(0.5-0.04/2) + 0.1, relwidth=0.14, relheight=0.04)

    right_frame.bind('<Return>', login)
    login_button.bind('<Button-1>', login)


# CREDENTIALS CHECK
    credentials_situation_label = tkinter.Label(right_frame, font=("Century Gothic", 11), text="", bg="#fff", fg="#AF0069")




create_login_page()




# |||||      MENU PAGE     ||||| #


# FUNCTIONS
def myfunct():
    pass


# UI
def create_menu():

# FRAME
    menu_page = tkinter.Frame(bg="#fff")
    menu_page.place(relwidth=1, relheight=1)


# SHOWCASE
    showcase_button = tkinter.Button(menu_page, text="SHOWCASE", bd=0, font=("Century Gothic", 40), fg="#fff", bg="#364F6B", activebackground="#3B5475", activeforeground="#fff")
    showcase_button.place(relwidth=0.3, relheight=0.22, rely=0.09, relx=0.08)


# STOCK
    stock_button = tkinter.Button(menu_page, text="STOCK", bd=0, font=("Century Gothic", 40), fg="#fff", bg="#364F6B", activebackground="#3B5475", activeforeground="#fff", command=create_stock)
    stock_button.place(relwidth=0.3, relheight=0.22, rely=0.39, relx=0.08)


# HISTORY
    history_button = tkinter.Button(menu_page, text="HISTORY", bd=0, font=("Century Gothic", 40), fg="#fff", bg="#364F6B", activebackground="#3B5475", activeforeground="#fff")
    history_button.place(relwidth=0.3, relheight=0.22, rely=0.69, relx=0.08)


# SELL
    sell_button = tkinter.Button(menu_page, text="SELL", bd=0, font=("Century Gothic", 70), fg="#fff", bg="#364F6B", activebackground="#3B5475", activeforeground="#fff")
    sell_button.place(relwidth=0.494, relheight=0.82, rely=0.09, relx=0.425)





# |||||      EDIT PAGE     ||||| #

# VAR

# FUNCTIONS

def add_caterogy():
    global add_to_main_categoy_button, list_box_frame
    add_to_main_category_button.destroy()
    add_category_name_input = tkinter.Entry(list_box_frame, bd=1, bg="#f0f0f0", fg="#5c5c5c", font=("Ba hnschrift", 16))
    add_category_name_input.place(relwidth=0.8, relheight=0.035, relx=0.1, rely=0.025)


# UI
def create_stock():
    global list_box_frame
# FULL FRAME
    stock_page = tkinter.Frame(bg="#fff")
    stock_page.place(relwidth=1, relheight=1)


# TOP FRAME
    top_nav_frame = tkinter.Frame(bg="#364F6B")
    top_nav_frame.place(relheight=0.06, relwidth=1)

    stock_text = tkinter.Label(top_nav_frame, bg="#364F6B", fg="#fff", text="STOCK", font=("Century Gothic", 24))
    stock_text.place(relwidth=1, relheight=1)


# LIST FRAME
    list_box_frame = tkinter.Frame(stock_page, bg="#f0f0f0")
    list_box_frame.place(relwidth=0.2, relheight=0.94, rely=0.06, relx=0)


# 1 LIST
    list_box_stock = tkinter.Listbox(list_box_frame, bg="#f0f0f0", bd=0, relief=tkinter.FLAT, highlightthickness=0, activestyle=tkinter.NONE, font=("Century Gothic", 16), selectbackground="#d0d0d0", selectforeground="#000000")
    list_box_stock.place(relheight=0.985, relwidth=0.95, relx=0.05, rely=0.015)

    #list_box_stock.insert(1, "▸ Mărfuri fără TVA")
# ▾


# SPOT INFO LABEL
# ADD TO MAIN LIST BUTTON
    # global add_to_main_category_button
    # add_to_main_category_button = tkinter.Button(list_box_frame, text="+", bd=1, font=("Century Gothic", 18), fg="#5c5c5c", bg="#e3e3e3", activebackground="#e3e3e3", activeforeground="#5c5c5c", command=add_caterogy)
    # add_to_main_category_button.place(relwidth=0.8, relheight=0.035, relx=0.1, rely=0.025)


#### TESTING #####



#### TESTING #####


# SCROLLBAR
    scrollbar_list_stock = tkinter.Scrollbar(stock_page, bg="#f0f0f0")
    scrollbar_list_stock.place(relheight=0.94, rely=0.06, relx=0.2)

# SCROLLBAR CONFIG
    scrollbar_list_stock.config(command=list_box_stock.yview)
    list_box_stock.config(yscrollcommand=scrollbar_list_stock.set)


mainWindow.mainloop()
