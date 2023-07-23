import math
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random
import webview
from tkinter import filedialog
import subprocess
from tkinter import colorchooser # import colorchooser module
from tkinter import font # import font module
from tkinter import *
import re
from tkinter.font import Font
import sqlite3
from tkterminal import Terminal
from idlelib.percolator import Percolator
import pyperclip
from idlelib.colorizer import ColorDelegator as ic
import os
import sys
import webbrowser
def Cloud():
    webview.create_window('Qiwi',"https://qiwi.gg")
    webview.start()

tips = [
    "Terminal: Run in menu(Spustiť>Terminal)",
    "Run Calculator with command in menu: Spustiť>Launch Calculator",
    "Calculating Fast: Run Calculator and select the entry. Write math exam and click to button '='",
    "Change programming languague in syntax highlighting: Go to Nastavenia>Syntax and write num 1 for Python, 2 for HTML and 3 for C++."
]
def Tip():
    messagebox.showinfo("tip", random.choice(tips))
def Marks():
    gui = tk.Tk()

    def copy_to_clipboard(text):
        pyperclip.copy(text)
        messagebox.showinfo("Copy to Clipboard", "Mark copied to clipboard!")

    marks = ['ß', 'æ', 'œ', 'þ', 'ð', '¿', '¡', '§', '¶', '•', '£', '€', '¥', '¢', '‰', '†', '‡', '°', '±', 'µ',
            'א', 'ב', 'ג', 'ד', 'ה', 'ו', 'ז', 'ח', 'ט', 'י', 'כ', 'ך', 'ל', 'מ', 'ם', 'נ', 'ן', 'ס', 'ע', 'פ',
            'ף', 'צ', 'ץ', 'ק', 'ר', 'ש', 'ת', 'あ', 'い', 'う', 'え', 'お', 'か', 'き', 'く', 'け', 'こ', 'さ', 'し', 'す',
            'せ', 'そ', 'た', 'ち', 'つ', 'て', 'と', 'な', 'に', 'ぬ', 'ね', 'の', 'は', 'ひ', 'ふ', 'へ', 'ほ', 'ま', 'み', 'む',
            'め', 'も', 'や', 'ゆ', 'よ', 'ら', 'り', 'る', 'れ', 'ろ', 'わ', 'を', 'ん', 'ア', 'イ', 'ウ', 'エ', 'オ', 'カ', 'キ',
            'ク', 'ケ', 'コ', 'サ', 'シ', 'ス', 'セ', 'ソ', 'タ', 'チ', 'ツ', 'テ', 'ト', 'ナ', 'ニ', 'ヌ', 'ネ', 'ノ', 'ハ', 'ヒ', 'フ',
            'ヘ', 'ホ', 'マ', 'ミ', 'ム', 'メ', 'モ', 'ヤ', 'ユ', 'ヨ', 'ラ', 'リ', 'ル', 'レ', 'ロ', 'ワ', 'ヲ', 'ン', 'ا', 'ب', 'ت',
            'ث', 'ج', 'ح', 'خ', 'د', 'ذ', 'ر', 'ز', 'س', 'ش', 'ص', 'ض', 'ط', 'ظ', 'ع', 'غ', 'ف', 'ق', 'ك', 'ل', 'م', 'ن', 'ه', 'و', 'ي',
            '←', '↑', '→', '↓', '😀', '😃', '😄', '😊', '😎', '🙂', '😉', '😋', '😍', '😘', '😚', '😜', '😝', '😏', '😌', '😔', '😞', '😟', '😢', '😭',
            '­▓', '­░', '▒', '▓', '█', 'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С',
            'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я', '√', '≡', '≈', '≠', '▲', '■', '□', '●', '○', '♂', '♀']

    button_width = 2
    button_height = 1
    buttons_per_row = 45  # Number of buttons per row

    row_count = (len(marks) - 1) // buttons_per_row + 1
    column_count = buttons_per_row

    for i, x in enumerate(marks):
        btn = tk.Button(gui, text=x, command=lambda t=x: copy_to_clipboard(t), width=button_width, height=button_height)
        btn.grid(row=i // buttons_per_row, column=i % buttons_per_row, padx=5, pady=5)

    # Calculate window dimensions based on button size and number of buttons
    window_width = button_width * buttons_per_row + 15
    window_height = button_height * row_count + 15

    gui.geometry(f"{window_width}x{window_height}")

    gui.mainloop()
def terminal():
    terminal = Terminal(pady=5, padx=5)
    terminal.shell = True
    terminal.linebar = True
    terminal.pack(expand=True, fill='both')

def XediX():
    root = tk.Toplevel(roott)
    rew = 0
    menu = tk.Menu(root)
    text = tk.Text(root, height=20)
    text.pack()
    output = tk.Text(root, height=10)
    output.pack()
    style = ttk.Style()
    style.theme_use("winnative")
    style.map("TButton", background=[("pressed", "green"), ("active", "yellow")])
    style.theme_use("winnative")
    entrydd = Entry(root)
    command = entrydd.get()
    entrydd.pack()
    def run_command():
        out = subprocess.check_output(command, shell=True, text=True)
        output.insert('end', out)
    btn = Button(root, command=run_command, text="Run")
    btn.pack()
    cdg = ic()

    cdg.tagdefs["KEYWORD"] = {'foreground': '#AD1035'}
    cdg.tagdefs["BUILTIN"] = {'foreground': '#0000FF'}
    cdg.tagdefs["STRING"] = {'foreground': '#ff9c00'}
    cdg.tagdefs["COMMENT"] = {'foreground': '#7277CC', 'font': "TkFixedFont italic"}
    cdg.tagdefs["ERROR"] = {"background": "red"}
    cdg.tagdefs["DEFINITION"] = {'foreground':'#F0DC82'}
    cdg.tagdefs["LIBRARY"] = {'foreground': '#00FF00'}  # Pokud je již definováno+ľ
    
    Percolator(text).insertfilter(cdg)

    def opensite():
        webbrowser.open("github.com/mostypc123/XediX", 0, False)

    def fullscr():
        messagebox.showwarning("FullSreen nebol zapnutý", "FullSreen s adá vypnúť iba reštartom počítača. Bol odobraný s XediXu 3.1.1(e1).")

    def toggle_theme():
        if root['bg'] == 'black':
            root.config(bg='white')
            text.config(bg='white', fg='black')
        else:
            root.config(bg='black')
            text.config(bg='black', fg='white')
            output.config(bg='black', fg='white')

    def run_code():
        # Save the code to a temporary file
        code = text.get("1.0", tk.END)
        with open("temp.py", "w") as f:
            f.write(code)
        # Run the code with the chosen interpreter
        try:
            # Use sys.executable to get the path of the current interpreter
            result = os.system("python temp.py")
        except Exception as e:
            output.insert(tk.END, str(e) + "\n")
        else:
            messagebox.showinfo("output", "The output is in the terminal")
            output.insert(tk.END, result) #type: ignore

        # Check if a Tk instance already exists
        if not 'root' in globals():
            global root
            root = tk.Tk()


    def save_file():
        file = filedialog.asksaveasfile(defaultextension=".py")
        if file is not None:
            file.write(text.get("1.0", tk.END))
            file.close()

    def open_file():
        file = filedialog.askopenfile()
        if file is not None:
            text.delete("1.0", tk.END)
            text.insert(tk.END, file.read())
            file.close()

    def choose_color():
        color = colorchooser.askcolor()
        if color is not None: # check if a color is selected
            text.config(fg=color[1]) # change the text color to the selected color

    def choose_bg(): # define a function to choose background color
        bg = colorchooser.askcolor() # open the color chooser dialog
        if bg is not None: # check if a color is selected
            text.config(bg=bg[1]) # change the text background color to the selected color
    def choose_font(): # define a function to choose font
        fonts = list(font.families()) # get a list of available fonts
        font_menu = tk.Toplevel(root) # create a new window for font selection
        font_menu.title("Vybrať font") # set the title of the window
        font_var = tk.StringVar() # create a variable to store the selected font
        font_var.set(fonts[0]) # set the default font to the first one in the list
        font_list = tk.Listbox(font_menu, listvariable=font_var) # create a listbox to display the fonts
        font_list.pack() # pack the listbox
        def select_font(): # define a function to select the font from the listbox
            font_name = font_var.get() # get the selected font name
            text_font = font.Font(family=font_name) # create a font object with the selected name
            text.config(font=text_font) # change the text font to the selected one
            font_menu.destroy() # close the font selection window
        select_button = tk.Button(font_menu, text="Vybrať", command=select_font) # create a button to confirm the selection
        select_button.pack() # pack the button
    expression = tk.StringVar()
    def calculate():
        try:
            result = eval(expression.get())
            expression.set(str(result))
        except Exception as e:
            expression.set("Error")

    def clear():
        expression.set("")

    def append(char):
        current = expression.get()
        expression.set(current + char)

    def launch_calculator():
        clc = tk.Toplevel(root)
        clc.title("Calculator")

        entry = tk.Entry(clc, textvariable=expression, font=("Courier", 20))
        entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        buttons = [
            ("7", lambda: append("7")),
            ("8", lambda: append("8")),
            ("9", lambda: append("9")),
            ("/", lambda: append("/")),
            ("4", lambda: append("4")),
            ("5", lambda: append("5")),
            ("6", lambda: append("6")),
            ("*", lambda: append("*")),
            ("1", lambda: append("1")),
            ("2", lambda: append("2")),
            ("3", lambda: append("3")),
            ("-", lambda: append("-")),
            (".", lambda: append(".")),
            ("0", lambda: append("0")),
            ("=", calculate),
            ("+", lambda: append("+"))
        ]

        row = 1
        col = 0
        for button_text, command in buttons:
            button = tk.Button(clc, text=button_text, width=5, height=2, command=command)
            button.grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1

        clear_button = tk.Button(clc, text="C", width=5, height=2, command=clear)
        clear_button.grid(row=row, column=0, padx=5, pady=5)

        clc.mainloop()
    root.config(menu=menu)

    file_menu = tk.Menu(menu) 
    menu.add_cascade(label="Súbor", menu=file_menu)
    file_menu.add_command(label="Otvoriť", command=open_file)
    file_menu.add_command(label="Uložiť", command=save_file)

    run_menu = tk.Menu(menu)
    menu.add_cascade(label="Spustiť", menu=run_menu)
    run_menu.add_command(label="Spustiť kód", command=run_code)
    run_menu.add_command(label="App Marks", command=Marks)
    run_menu.add_command(label="Launch Calculator", command=launch_calculator)
    run_menu.add_command(label="Terminal", command=terminal)
    run_menu.add_command(label="Cloud", command=Cloud)

    color_menu = tk.Menu(menu)
    menu.add_cascade(label="Nastavenia", menu=color_menu)
    color_menu.add_command(label="Vybrať farbu písma", command=choose_color)
    color_menu.add_command(label="Vybrať farbu pozadia", command=choose_bg)
    color_menu.add_command(label='Toggle Dark/Light', command=toggle_theme)
    color_menu.add_command(label="Vybrať font", command=choose_font)
    color_menu.add_command(label="FullSreen", command=fullscr)

    root.config(menu=menu)

    help_menu = tk.Menu(menu)
    menu.add_cascade(label="Help", menu=help_menu)
    help_menu.add_command(label="Site", command=opensite)
    help_menu.add_command(label="Tips", command=Tip)

    menu.config(bg="black",fg="white")

    root.mainloop()
# Vytvorenie alebo pripojenie k databáze
conn = sqlite3.connect("users.db")
c = conn.cursor()

# Vytvorenie tabuľky pre používateľov, ak neexistuje
c.execute('''CREATE TABLE IF NOT EXISTS users (
                username TEXT PRIMARY KEY,
                password TEXT)''')

def login():
    username = username_entry.get()
    password = password_entry.get()

    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = c.fetchone()

    if user:
        roott.quit()
        messagebox.showinfo("Login Successful", f"Welcome, {username}!")
        XediX()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

def create_account():
    username = username_entry.get()
    password = password_entry.get()

    if username and password:
        try:
            c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            messagebox.showinfo("Account Created", "Your account has been created successfully.")
        except sqlite3.IntegrityError:
            messagebox.showerror("Account Creation Failed", "Username already exists.")
    else:
        messagebox.showerror("Account Creation Failed", "Username and password are required.")

roott = tk.Tk()
roott.title("XediX34.0.2.0")

# Nastavenie písma
font = Font(family="Helvetica", size=12)

# Nastavenie farieb
background_color = "#f0f0f0"
button_color = "#336699"
button_foreground_color = "white"

# Prihlasovacie okno
login_frame = tk.Frame(roott, bg=background_color)
login_frame.pack(pady=20)

username_label = tk.Label(login_frame, text="Username:", bg=background_color, font=font)
username_label.grid(row=0, column=0, padx=5, pady=5)
username_entry = tk.Entry(login_frame, font=font)
username_entry.grid(row=0, column=1, padx=5, pady=5)

password_label = tk.Label(login_frame, text="Password:", bg=background_color, font=font)
password_label.grid(row=1, column=0, padx=5, pady=5)
password_entry = tk.Entry(login_frame, show="•", font=font)
password_entry.grid(row=1, column=1, padx=5, pady=5)

login_button = tk.Button(login_frame, text="Login", command=login, bg=button_color, fg=button_foreground_color, font=font)
login_button.grid(row=2, column=0, padx=5, pady=5)

create_account_button = tk.Button(login_frame, text="Create Account", command=create_account, bg=button_color, fg=button_foreground_color, font=font)
create_account_button.grid(row=2, column=1, padx=5, pady=5)

medzeri = tk.Label(login_frame, text="\n                      ")

btnc = tk.Button(login_frame, text="Continue with no account", command=XediX)
btnc.grid()
tk.Button(roott, text="Tip", command=Tip).pack()
roott.mainloop()
# Zatvorenie spojenia s databázou po ukončení programu
conn.close()
