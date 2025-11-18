# -*- coding: utf-8 -*-
"""
שיעורים נוספים - חלק 6
שיעורים 26-30 - נושאים מתקדמים ומקצועיים
"""

LESSONS_PART6 = {
    26: {
        'title': '🗄️ שיעור 26: SQL ומסדי נתונים',
        'content': """
בואו נלמד איך לעבוד עם מסדי נתונים! 🗄️

🎯 <b>מה זה SQL?</b>
SQL (Structured Query Language) היא שפה לניהול מסדי נתונים!

📦 <b>SQLite - מסד נתונים מובנה:</b>
<code>import sqlite3

# יצירת חיבור:
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

# יצירת טבלה:
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE,
        age INTEGER
    )
''')

conn.commit()
conn.close()</code>

➕ <b>הוספת נתונים (INSERT):</b>
<code>import sqlite3

conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

# הוספה בסיסית:
cursor.execute('''
    INSERT INTO users (name, email, age)
    VALUES ('אמיר', 'amir@example.com', 25)
''')

# הוספה בטוחה (עם פרמטרים):
user_data = ('דני', 'danny@example.com', 30)
cursor.execute('''
    INSERT INTO users (name, email, age)
    VALUES (?, ?, ?)
''', user_data)

# הוספה מרובה:
users = [
    ('יוסי', 'yossi@example.com', 28),
    ('רונה', 'rona@example.com', 26),
    ('שרה', 'sara@example.com', 32)
]
cursor.executemany('''
    INSERT INTO users (name, email, age)
    VALUES (?, ?, ?)
''', users)

conn.commit()
conn.close()</code>

🔍 <b>שאילתות (SELECT):</b>
<code>import sqlite3

conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

# כל המשתמשים:
cursor.execute('SELECT * FROM users')
all_users = cursor.fetchall()
for user in all_users:
    print(user)

# משתמש ספציפי:
cursor.execute('SELECT * FROM users WHERE name = ?', ('אמיר',))
user = cursor.fetchone()
print(user)

# עמודות ספציפיות:
cursor.execute('SELECT name, email FROM users WHERE age > 25')
results = cursor.fetchall()

# עם ORDER BY:
cursor.execute('SELECT * FROM users ORDER BY age DESC')

# עם LIMIT:
cursor.execute('SELECT * FROM users LIMIT 5')

conn.close()</code>

✏️ <b>עדכון (UPDATE):</b>
<code>import sqlite3

conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

# עדכון בסיסי:
cursor.execute('''
    UPDATE users
    SET age = 26
    WHERE name = 'אמיר'
''')

# עדכון בטוח:
new_age = 27
user_name = 'אמיר'
cursor.execute('''
    UPDATE users
    SET age = ?
    WHERE name = ?
''', (new_age, user_name))

# עדכון כמה שורות:
cursor.execute('''
    UPDATE users
    SET age = age + 1
    WHERE age < 30
''')

print(f"עודכנו {cursor.rowcount} שורות")

conn.commit()
conn.close()</code>

🗑️ <b>מחיקה (DELETE):</b>
<code>import sqlite3

conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

# מחיקה ספציפית:
cursor.execute('DELETE FROM users WHERE name = ?', ('אמיר',))

# מחיקה לפי תנאי:
cursor.execute('DELETE FROM users WHERE age < 18')

# מחיקת הכל (זהירות!):
# cursor.execute('DELETE FROM users')

print(f"נמחקו {cursor.rowcount} שורות")

conn.commit()
conn.close()</code>

🔗 <b>JOIN - חיבור טבלאות:</b>
<code>import sqlite3

conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

# יצירת טבלת הזמנות:
cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        product TEXT,
        amount REAL,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
''')

# הוספת הזמנות:
orders = [
    (1, 'מחשב נייד', 3500),
    (1, 'עכבר', 50),
    (2, 'מקלדת', 150)
]
cursor.executemany('''
    INSERT INTO orders (user_id, product, amount)
    VALUES (?, ?, ?)
''', orders)

# INNER JOIN:
cursor.execute('''
    SELECT users.name, orders.product, orders.amount
    FROM users
    INNER JOIN orders ON users.id = orders.user_id
''')

for row in cursor.fetchall():
    print(f"{row[0]} הזמין {row[1]} ב-{row[2]}₪")

conn.commit()
conn.close()</code>

📊 <b>פונקציות אגרגציה:</b>
<code>import sqlite3

conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

# COUNT - ספירה:
cursor.execute('SELECT COUNT(*) FROM users')
total = cursor.fetchone()[0]
print(f"סך הכל משתמשים: {total}")

# AVG - ממוצע:
cursor.execute('SELECT AVG(age) FROM users')
avg_age = cursor.fetchone()[0]
print(f"גיל ממוצע: {avg_age:.1f}")

# MAX, MIN:
cursor.execute('SELECT MAX(age), MIN(age) FROM users')
max_age, min_age = cursor.fetchone()

# SUM:
cursor.execute('SELECT SUM(amount) FROM orders')
total_sales = cursor.fetchone()[0]

# GROUP BY:
cursor.execute('''
    SELECT user_id, COUNT(*), SUM(amount)
    FROM orders
    GROUP BY user_id
''')

conn.close()</code>

🎨 <b>Context Manager - ניהול חיבור טוב יותר:</b>
<code>import sqlite3

class Database:
    def __init__(self, db_name):
        self.db_name = db_name
    
    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        self.conn.row_factory = sqlite3.Row  # גישה לעמודות בשם
        return self.conn.cursor()
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.conn.commit()
        self.conn.close()

# שימוש:
with Database('mydatabase.db') as cursor:
    cursor.execute('SELECT * FROM users')
    for row in cursor.fetchall():
        print(f"{row['name']}: {row['email']}")
# החיבור נסגר אוטומטית!</code>

💪 <b>ORM - SQLAlchemy:</b>
<code># pip install sqlalchemy

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    age = Column(Integer)
    
    def __repr__(self):
        return f"<User(name='{self.name}', email='{self.email}')>"

# יצירת מנוע:
engine = create_engine('sqlite:///mydatabase.db')
Base.metadata.create_all(engine)

# יצירת session:
Session = sessionmaker(bind=engine)
session = Session()

# הוספה:
new_user = User(name='אמיר', email='amir@example.com', age=25)
session.add(new_user)
session.commit()

# שאילתה:
users = session.query(User).filter(User.age > 20).all()
for user in users:
    print(user)

# עדכון:
user = session.query(User).filter_by(name='אמיר').first()
user.age = 26
session.commit()

# מחיקה:
session.delete(user)
session.commit()

session.close()</code>

🔥 <b>דוגמה מקיפה - מערכת משתמשים:</b>
<code>import sqlite3
from typing import List, Optional, Dict

class UserDatabase:
    def __init__(self, db_name: str = 'users.db'):
        self.db_name = db_name
        self.init_db()
    
    def init_db(self):
        '''יצירת טבלה אם לא קיימת'''
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    age INTEGER,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            conn.commit()
    
    def add_user(self, username: str, email: str, age: int) -> bool:
        '''הוספת משתמש חדש'''
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO users (username, email, age)
                    VALUES (?, ?, ?)
                ''', (username, email, age))
                conn.commit()
                return True
        except sqlite3.IntegrityError:
            return False
    
    def get_user(self, username: str) -> Optional[Dict]:
        '''קבלת משתמש'''
        with sqlite3.connect(self.db_name) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute(
                'SELECT * FROM users WHERE username = ?',
                (username,)
            )
            row = cursor.fetchone()
            return dict(row) if row else None
    
    def get_all_users(self) -> List[Dict]:
        '''קבלת כל המשתמשים'''
        with sqlite3.connect(self.db_name) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM users')
            return [dict(row) for row in cursor.fetchall()]
    
    def update_user(self, username: str, **kwargs) -> bool:
        '''עדכון משתמש'''
        if not kwargs:
            return False
        
        set_clause = ', '.join([f"{k} = ?" for k in kwargs.keys()])
        values = list(kwargs.values()) + [username]
        
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(
                f'UPDATE users SET {set_clause} WHERE username = ?',
                values
            )
            conn.commit()
            return cursor.rowcount > 0
    
    def delete_user(self, username: str) -> bool:
        '''מחיקת משתמש'''
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(
                'DELETE FROM users WHERE username = ?',
                (username,)
            )
            conn.commit()
            return cursor.rowcount > 0

# שימוש:
db = UserDatabase()

# הוספה:
db.add_user('amir', 'amir@example.com', 25)
db.add_user('danny', 'danny@example.com', 30)

# קריאה:
user = db.get_user('amir')
print(user)

all_users = db.get_all_users()
for user in all_users:
    print(user['username'], user['email'])

# עדכון:
db.update_user('amir', age=26, email='new@example.com')

# מחיקה:
db.delete_user('danny')</code>

⚠️ <b>SQL Injection - זהירות!</b>
<code># ❌ מסוכן - פתוח ל-SQL Injection:
username = input("שם משתמש: ")
cursor.execute(f"SELECT * FROM users WHERE username = '{username}'")
# אם המשתמש יזין: ' OR '1'='1
# השאילתה תהיה: SELECT * FROM users WHERE username = '' OR '1'='1'

# ✅ בטוח - שימוש בפרמטרים:
cursor.execute("SELECT * FROM users WHERE username = ?", (username,))</code>

📚 <b>טיפים חשובים:</b>
• תמיד השתמש בפרמטרים (?) למניעת SQL Injection
• השתמש ב-transactions לפעולות מרובות
• סגור חיבורים תמיד (with/try-finally)
• צור אינדקסים לעמודות שמחפשים בהן הרבה
• גבה את מסד הנתונים!
• השתמש ב-ORM לפרויקטים גדולים
""",
        'exercise': {
            'question': 'איזו פקודה SQL משמשת לבחירת נתונים מטבלה?',
            'options': ['GET', 'SELECT', 'FETCH', 'RETRIEVE'],
            'correct_answer': 'SELECT',
            'explanation': 'נכון! 🎯 SELECT משמש לבחירת נתונים, למשל: SELECT * FROM users'
        }
    },
    
    27: {
        'title': '🎨 שיעור 27: GUI - ממשק גרפי עם Tkinter',
        'content': """
בואו ליצור תוכניות עם ממשק גרפי! 🖼️

🎯 <b>מה זה GUI?</b>
GUI (Graphical User Interface) הוא ממשק גרפי עם חלונות, כפתורים ועוד!

📦 <b>Tkinter - ספרייה מובנית:</b>
<code>import tkinter as tk

# יצירת חלון:
window = tk.Tk()
window.title("התוכנית הראשונה שלי")
window.geometry("400x300")

# הרצת החלון:
window.mainloop()</code>

🔘 <b>Label - תווית טקסט:</b>
<code>import tkinter as tk

window = tk.Tk()
window.title("שלום עולם")

# יצירת label:
label = tk.Label(window, text="שלום עולם!", font=("Arial", 24))
label.pack()

window.mainloop()</code>

🎯 <b>Button - כפתור:</b>
<code>import tkinter as tk

def on_click():
    label.config(text="לחצת על הכפתור!")

window = tk.Tk()
window.title("כפתור")

label = tk.Label(window, text="לחץ על הכפתור")
label.pack(pady=10)

button = tk.Button(window, text="לחץ כאן!", command=on_click)
button.pack()

window.mainloop()</code>

📝 <b>Entry - שדה קלט:</b>
<code>import tkinter as tk

def show_name():
    name = entry.get()
    label.config(text=f"שלום {name}!")

window = tk.Tk()
window.title("שם")

tk.Label(window, text="מה שמך?").pack()

entry = tk.Entry(window, width=30)
entry.pack(pady=10)

button = tk.Button(window, text="שלח", command=show_name)
button.pack()

label = tk.Label(window, text="")
label.pack(pady=10)

window.mainloop()</code>

☑️ <b>Checkbutton - תיבת סימון:</b>
<code>import tkinter as tk

def show_selection():
    result = f"Python: {python_var.get()}, JavaScript: {js_var.get()}"
    label.config(text=result)

window = tk.Tk()

python_var = tk.BooleanVar()
js_var = tk.BooleanVar()

tk.Checkbutton(
    window,
    text="Python",
    variable=python_var,
    command=show_selection
).pack()

tk.Checkbutton(
    window,
    text="JavaScript",
    variable=js_var,
    command=show_selection
).pack()

label = tk.Label(window, text="")
label.pack()

window.mainloop()</code>

🔘 <b>Radiobutton - בחירה יחידה:</b>
<code>import tkinter as tk

def show_choice():
    label.config(text=f"בחרת: {choice.get()}")

window = tk.Tk()

choice = tk.StringVar(value="Python")

tk.Radiobutton(
    window,
    text="Python",
    variable=choice,
    value="Python",
    command=show_choice
).pack()

tk.Radiobutton(
    window,
    text="JavaScript",
    variable=choice,
    value="JavaScript",
    command=show_choice
).pack()

label = tk.Label(window, text="")
label.pack()

window.mainloop()</code>

📋 <b>Listbox - רשימה:</b>
<code>import tkinter as tk

def show_selection():
    selection = listbox.curselection()
    if selection:
        item = listbox.get(selection[0])
        label.config(text=f"בחרת: {item}")

window = tk.Tk()

listbox = tk.Listbox(window, height=5)
listbox.pack()

items = ["תפוח", "בננה", "תפוז", "אבטיח", "ענבים"]
for item in items:
    listbox.insert(tk.END, item)

button = tk.Button(window, text="הצג", command=show_selection)
button.pack()

label = tk.Label(window, text="")
label.pack()

window.mainloop()</code>

📊 <b>Layout Managers:</b>

<b>1. pack() - פשוט:</b>
<code>import tkinter as tk

window = tk.Tk()

tk.Label(window, text="למעלה").pack(side=tk.TOP)
tk.Label(window, text="למטה").pack(side=tk.BOTTOM)
tk.Label(window, text="שמאל").pack(side=tk.LEFT)
tk.Label(window, text="ימין").pack(side=tk.RIGHT)

window.mainloop()</code>

<b>2. grid() - רשת:</b>
<code>import tkinter as tk

window = tk.K()

tk.Label(window, text="שם:").grid(row=0, column=0, sticky=tk.W)
tk.Entry(window).grid(row=0, column=1)

tk.Label(window, text="אימייל:").grid(row=1, column=0, sticky=tk.W)
tk.Entry(window).grid(row=1, column=1)

tk.Button(window, text="שלח").grid(row=2, column=0, columnspan=2)

window.mainloop()</code>

<b>3. place() - מיקום מדויק:</b>
<code>import tkinter as tk

window = tk.Tk()
window.geometry("400x300")

label = tk.Label(window, text="מרכז")
label.place(x=200, y=150, anchor=tk.CENTER)

button = tk.Button(window, text="פינה")
button.place(x=10, y=10)

window.mainloop()</code>

🎨 <b>Frame - מיכל:</b>
<code>import tkinter as tk

window = tk.Tk()

# Frame עליון:
top_frame = tk.Frame(window, bg="lightblue", height=100)
top_frame.pack(fill=tk.BOTH, expand=True)

tk.Label(top_frame, text="למעלה", bg="lightblue").pack()

# Frame תחתון:
bottom_frame = tk.Frame(window, bg="lightgreen", height=100)
bottom_frame.pack(fill=tk.BOTH, expand=True)

tk.Label(bottom_frame, text="למטה", bg="lightgreen").pack()

window.mainloop()</code>

💬 <b>MessageBox - חלונות הודעה:</b>
<code>import tkinter as tk
from tkinter import messagebox

def show_info():
    messagebox.showinfo("מידע", "זו הודעת מידע")

def show_warning():
    messagebox.showwarning("אזהרה", "זו הודעת אזהרה")

def show_error():
    messagebox.showerror("שגיאה", "זו הודעת שגיאה")

def ask_question():
    result = messagebox.askquestion("שאלה", "האם אתה בטוח?")
    print(result)  # 'yes' או 'no'

def ask_yesno():
    result = messagebox.askyesno("אישור", "להמשיך?")
    print(result)  # True או False

window = tk.Tk()

tk.Button(window, text="מידע", command=show_info).pack()
tk.Button(window, text="אזהרה", command=show_warning).pack()
tk.Button(window, text="שגיאה", command=show_error).pack()
tk.Button(window, text="שאלה", command=ask_question).pack()

window.mainloop()</code>

📁 <b>File Dialog - בחירת קבצים:</b>
<code>import tkinter as tk
from tkinter import filedialog

def open_file():
    filename = filedialog.askopenfilename(
        title="בחר קובץ",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )
    if filename:
        print(f"נבחר: {filename}")

def save_file():
    filename = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )
    if filename:
        print(f"שמירה ל: {filename}")

window = tk.Tk()

tk.Button(window, text="פתח קובץ", command=open_file).pack()
tk.Button(window, text="שמור קובץ", command=save_file).pack()

window.mainloop()</code>

🎨 <b>Menu - תפריט:</b>
<code>import tkinter as tk
from tkinter import messagebox

def new_file():
    messagebox.showinfo("חדש", "קובץ חדש")

def open_file():
    messagebox.showinfo("פתח", "פתיחת קובץ")

def exit_app():
    window.quit()

window = tk.Tk()

# יצירת תפריט:
menubar = tk.Menu(window)
window.config(menu=menubar)

# תפריט קובץ:
file_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="קובץ", menu=file_menu)
file_menu.add_command(label="חדש", command=new_file)
file_menu.add_command(label="פתח", command=open_file)
file_menu.add_separator()
file_menu.add_command(label="יציאה", command=exit_app)

# תפריט עזרה:
help_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="עזרה", menu=help_menu)
help_menu.add_command(label="אודות", command=lambda: messagebox.showinfo("אודות", "גרסה 1.0"))

window.mainloop()</code>

💪 <b>דוגמה מקיפה - מחשבון:</b>
<code>import tkinter as tk

class Calculator:
    def __init__(self, window):
        self.window = window
        self.window.title("מחשבון")
        self.window.geometry("300x400")
        
        self.result_var = tk.StringVar()
        self.result_var.set("0")
        
        # תצוגה:
        self.display = tk.Entry(
            window,
            textvariable=self.result_var,
            font=("Arial", 24),
            justify=tk.RIGHT,
            state="readonly"
        )
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="ew")
        
        # כפתורים:
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0)
        ]
        
        for (text, row, col) in buttons:
            if text == '=':
                cmd = self.calculate
            elif text == 'C':
                cmd = self.clear
            else:
                cmd = lambda x=text: self.add_char(x)
            
            btn = tk.Button(
                window,
                text=text,
                font=("Arial", 18),
                command=cmd
            )
            
            if text == 'C':
                btn.grid(row=row, column=col, columnspan=4, sticky="ew", padx=5, pady=5)
            else:
                btn.grid(row=row, column=col, sticky="ew", padx=5, pady=5)
        
        self.expression = ""
    
    def add_char(self, char):
        if self.expression == "0":
            self.expression = ""
        self.expression += str(char)
        self.result_var.set(self.expression)
    
    def calculate(self):
        try:
            result = eval(self.expression)
            self.result_var.set(str(result))
            self.expression = str(result)
        except:
            self.result_var.set("שגיאה")
            self.expression = ""
    
    def clear(self):
        self.expression = ""
        self.result_var.set("0")

# הרצה:
window = tk.Tk()
calc = Calculator(window)
window.mainloop()</code>

🎨 <b>עיצוב וצבעים:</b>
<code>import tkinter as tk

window = tk.Tk()

# צבעים:
label = tk.Label(
    window,
    text="טקסט צבעוני",
    bg="lightblue",     # צבע רקע
    fg="darkblue",      # צבע טקסט
    font=("Arial", 16, "bold"),
    padx=20,
    pady=10
)
label.pack()

# כפתור מעוצב:
button = tk.Button(
    window,
    text="לחץ כאן",
    bg="#4CAF50",
    fg="white",
    font=("Arial", 14),
    activebackground="#45a049",
    relief=tk.RAISED,
    borderwidth=3,
    cursor="hand2"
)
button.pack(pady=10)

window.mainloop()</code>

📚 <b>ספריות GUI נוספות:</b>
• <b>PyQt/PySide:</b> מקצועי מאוד
• <b>Kivy:</b> ל-mobile ו-desktop
• <b>wxPython:</b> native look
• <b>PySimpleGUI:</b> פשוט מאוד

💡 <b>טיפים חשובים:</b>
• mainloop() חייב להיות בסוף
• אל תערבב pack ו-grid באותו parent
• השתמש ב-Frame לארגון
• בדוק על מסכים שונים
• טפל בסגירת חלון
""",
        'exercise': {
            'question': 'איזו פונקציה מריצה את חלון ה-GUI?',
            'options': ['window.run()', 'window.start()', 'window.mainloop()', 'window.execute()'],
            'correct_answer': 'window.mainloop()',
            'explanation': 'נכון! 🎯 mainloop() מריצה את לולאת האירועים של החלון ושומרת עליו פתוח'
        }
    },
    
    28: {
        'title': '🔧 שיעור 28: Virtual Environments וניהול פרויקטים',
        'content': """
בואו נלמד לנהל פרויקטים כמו מקצוענים! 🚀

🎯 <b>מה זו סביבה וירטואלית?</b>
סביבה וירטואלית (venv) היא סביבה מבודדת לכל פרויקט עם החבילות שלו!

💡 <b>למה זה חשוב?</b>
• כל פרויקט עם החבילות שלו
• אין התנגשויות בין גרסאות
• קל לשתף את הפרויקט
• נקיון במערכת

📦 <b>יצירת venv:</b>
<code># Windows:
python -m venv myenv

# Mac/Linux:
python3 -m venv myenv

# עם שם אחר:
python -m venv my_project_env</code>

🔌 <b>הפעלת ה-venv:</b>
<code># Windows (CMD):
  myenv\\Scripts\\activate.bat

# Windows (PowerShell):
  myenv\\Scripts\\Activate.ps1

# Mac/Linux:
source myenv/bin/activate

# אחרי הפעלה תראה:
  (myenv) C:\\Users\\...></code>

📥 <b>התקנת חבילות ב-venv:</b>
<code># התקנה:
pip install requests
pip install pandas numpy matplotlib

# התקנת גרסה ספציפית:
pip install Django==4.2.0

# התקנה מ-requirements:
pip install -r requirements.txt</code>

📝 <b>requirements.txt - ניהול תלויות:</b>
<code># יצירת requirements.txt:
pip freeze > requirements.txt

# הקובץ ייראה כך:
requests==2.31.0
pandas==2.0.3
numpy==1.24.3
beautifulsoup4==4.12.2

# התקנה מהקובץ:
pip install -r requirements.txt</code>

🔍 <b>ניהול חבילות:</b>
<code># רשימת חבילות מותקנות:
pip list

# מידע על חבילה:
pip show requests

# חיפוש חבילה:
pip search django

# עדכון חבילה:
pip install --upgrade requests

# הסרת חבילה:
pip uninstall requests

# הסרת הכל:
pip freeze | xargs pip uninstall -y</code>

🚪 <b>יציאה מ-venv:</b>
<code># פשוט:
deactivate</code>

🗂️ <b>מבנה פרויקט טוב:</b>
<code>my_project/
│
├── venv/                  # הסביבה הוירטואלית
│
├── src/                   # קוד המקור
│   ├── __init__.py
│   ├── main.py
│   └── utils.py
│
├── tests/                 # בדיקות
│   ├── __init__.py
│   └── test_main.py
│
├── docs/                  # תיעוד
│   └── README.md
│
├── data/                  # נתונים
│   ├── raw/
│   └── processed/
│
├── requirements.txt       # תלויות
├── .gitignore            # Git
├── README.md             # תיעוד ראשי
└── setup.py              # התקנה</code>

📋 <b>.gitignore - מה לא לשמור ב-Git:</b>
<code># .gitignore
# סביבה וירטואלית:
venv/
env/
ENV/

# Python:
__pycache__/
*.py[cod]
*$py.class
*.so

# IDE:
.vscode/
.idea/
*.swp

# משתני סביבה:
.env
.env.local

# מערכת הפעלה:
.DS_Store
Thumbs.db

# בדיקות:
.coverage
htmlcov/
.pytest_cache/

# נתונים:
*.db
*.sqlite3

# לוגים:
*.log</code>

🔐 <b>.env - משתני סביבה:</b>
<code># קובץ .env:
DATABASE_URL=postgresql://user:pass@localhost/mydb
SECRET_KEY=your-secret-key-here
API_KEY=your-api-key
DEBUG=True

# שימוש בקוד (pip install python-dotenv):
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')
SECRET_KEY = os.getenv('SECRET_KEY')
API_KEY = os.getenv('API_KEY')
DEBUG = os.getenv('DEBUG') == 'True'</code>

📦 <b>setup.py - הפיכת הפרויקט לחבילה:</b>
<code># setup.py
from setuptools import setup, find_packages

setup(
    name='my_project',
    version='1.0.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='תיאור קצר של הפרויקט',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/my_project',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
    install_requires=[
        'requests>=2.31.0',
        'pandas>=2.0.0',
    ],
    entry_points={
        'console_scripts': [
            'my-command=my_project.main:main',
        ],
    },
)

# התקנה מקומית:
# pip install -e .</code>

🎨 <b>pyproject.toml - פורמט מודרני:</b>
<code># pyproject.toml
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "my_project"
version = "1.0.0"
description = "תיאור הפרויקט"
authors = [
    {name = "Your Name", email = "your.email@example.com"}
]
readme = "README.md"
requires-python = ">=3.8"
dependencies = [
    "requests>=2.31.0",
    "pandas>=2.0.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0",
    "black>=23.0",
    "flake8>=6.0",
]</code>

🔧 <b>Poetry - מנהל תלויות מתקדם:</b>
<code># התקנת Poetry:
# curl -sSL https://install.python-poetry.org | python3 -

# יצירת פרויקט חדש:
poetry new my_project

# הוספת תלויות:
poetry add requests pandas

# הוספת תלויות פיתוח:
poetry add --group dev pytest black

# התקנת התלויות:
poetry install

# הרצת סקריפט:
poetry run python main.py

# הפעלת shell:
poetry shell</code>

📊 <b>Makefile - אוטומציה:</b>
<code># Makefile
.PHONY: install test clean run

install:
	pip install -r requirements.txt

test:
	pytest tests/

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

run:
	python src/main.py

lint:
	flake8 src/
	black --check src/

format:
	black src/

# שימוש:
# make install
# make test
# make run</code>

🎯 <b>pre-commit - בדיקות אוטומטיות:</b>
<code># .pre-commit-config.yaml
repos:
  - repo: https://github.com/psf/black
    rev: 23.3.0
    hooks:
      - id: black
  
  - repo: https://github.com/PyCQA/flake8
    rev: 6.0.0
    hooks:
      - id: flake8

  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.4.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml

# התקנה:
# pip install pre-commit
# pre-commit install</code>

🔥 <b>דוגמה מקיפה - תבנית פרויקט:</b>
<code># מבנה:
awesome_project/
├── venv/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   └── utils/
│       ├── __init__.py
│       └── helpers.py
├── tests/
│   ├── __init__.py
│   ├── test_main.py
│   └── test_utils.py
├── docs/
│   └── README.md
├── .env.example
├── .gitignore
├── requirements.txt
├── requirements-dev.txt
├── setup.py
├── Makefile
├── README.md
└── LICENSE

# README.md:
# Awesome Project

## התקנה

```bash
# יצירת venv:
python -m venv venv

# הפעלה:
source venv/bin/activate  # Mac/Linux
  venv\\Scripts\\activate     # Windows

# התקנת תלויות:
pip install -r requirements.txt

# העתקת .env:
cp .env.example .env
# ערוך את .env עם הערכים שלך
```

## שימוש

```bash
python src/main.py
```

## בדיקות

```bash
pytest tests/
```

## רישיון

MIT License</code>

🌐 <b>pip-tools - ניהול תלויות מתקדם:</b>
<code># requirements.in (רק תלויות עיקריות):
requests
pandas
flask

# יצירת requirements.txt עם כל התלויות:
# pip install pip-tools
# pip-compile requirements.in

# זה יצור requirements.txt עם הכל:
requests==2.31.0
pandas==2.0.3
  numpy==1.24.3  # via pandas
flask==2.3.0
  click==8.1.3   # via flask
  # ועוד...

# עדכון:
# pip-compile --upgrade requirements.in

# סנכרון:
# pip-sync requirements.txt</code>

💡 <b>Best Practices:</b>
• תמיד עבוד ב-venv
• עדכן requirements.txt
• השתמש ב-.gitignore
• אל תשמור .env ב-Git
• תעד את הפרויקט (README)
• השתמש ב-semantic versioning (1.2.3)
• כתוב בדיקות
• השתמש ב-linters (flake8, black)

📚 <b>כלים נוספים:</b>
• <b>virtualenvwrapper:</b> ניהול venv מתקדם
• <b>pipenv:</b> משלב pip ו-venv
• <b>conda:</b> למדעני נתונים
• <b>tox:</b> בדיקות בסביבות מרובות
• <b>Docker:</b> לבידוד מלא
""",
        'exercise': {
            'question': 'איזו פקודה יוצרת קובץ requirements.txt?',
            'options': ['pip save', 'pip freeze > requirements.txt', 'pip export', 'pip list > requirements.txt'],
            'correct_answer': 'pip freeze > requirements.txt',
            'explanation': 'נכון! 🎯 pip freeze מציג את כל החבילות עם גרסאות, ו-> שומר את זה לקובץ'
        }
    },
    
    29: {
        'title': '🔄 שיעור 29: Git - בקרת גרסאות',
        'content': """
בואו נלמד את הכלי החשוב ביותר לכל מפתח! 🔄

🎯 <b>מה זה Git?</b>
Git הוא מערכת לבקרת גרסאות - מעקב אחרי שינויים בקוד!

💡 <b>למה Git חשוב?</b>
• שמירת היסטוריה של הקוד
• עבודה בצוות
• חזרה לגרסאות קודמות
• ניהול branches
• גיבוי בענן (GitHub, GitLab)

📦 <b>התקנת Git:</b>
<code># בדיקה אם מותקן:
git --version

# הגדרות ראשוניות:
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# בדיקת הגדרות:
git config --list</code>

🆕 <b>יצירת repository חדש:</b>
<code># יצירת תיקייה:
mkdir my_project
cd my_project

# אתחול Git:
git init

# הוספת README:
echo "# My Project" > README.md

# הוספה ל-staging:
git add README.md

# commit ראשון:
git commit -m "Initial commit"</code>

📝 <b>מעגל החיים של Git:</b>
<code># 1. עריכת קבצים (Working Directory)
# ערוך קובץ...

# 2. בדיקת סטטוס:
git status

# 3. הוספה ל-Staging Area:
git add filename.py
git add .  # הכל

# 4. Commit:
git commit -m "הוספתי פיצ׳ר חדש"

# ראה היסטוריה:
git log
git log --oneline
git log --graph --oneline</code>

🔍 <b>בדיקת שינויים:</b>
<code># שינויים שלא staged:
git diff

# שינויים ש-staged:
git diff --staged

# שינויים בין commits:
git diff commit1 commit2

# שינויים בקובץ ספציפי:
git diff filename.py</code>

↩️ <b>ביטול שינויים:</b>
<code># ביטול שינויים בקובץ (לפני add):
git checkout -- filename.py
# או:
git restore filename.py

# הסרה מ-staging (לפני commit):
git reset HEAD filename.py
# או:
git restore --staged filename.py

# ביטול commit אחרון (שמור שינויים):
git reset --soft HEAD~1

# ביטול commit אחרון (מחק שינויים):
git reset --hard HEAD~1

# ⚠️ זהירות עם --hard!</code>

🌿 <b>Branches - ענפים:</b>
<code># יצירת branch חדש:
git branch feature-login

# מעבר ל-branch:
git checkout feature-login
# או:
git switch feature-login

# יצירה ומעבר ביחד:
git checkout -b feature-login

# רשימת branches:
git branch
git branch -a  # כולל remote

# מחיקת branch:
git branch -d feature-login
git branch -D feature-login  # כפוי</code>

🔀 <b>Merge - מיזוג:</b>
<code># חזרה ל-main:
git checkout main

# מיזוג feature-login ל-main:
git merge feature-login

# אם יש קונפליקטים:
# 1. פתח את הקבצים עם <<<<<<<
# 2. ערוך ידנית
# 3. git add filename
# 4. git commit</code>

🌐 <b>עבודה עם GitHub:</b>
<code># הוספת remote:
git remote add origin https://github.com/username/repo.git

# בדיקת remotes:
git remote -v

# push לראשונה:
git push -u origin main

# push רגיל:
git push

# pull שינויים:
git pull

# fetch בלי merge:
git fetch origin</code>

📥 <b>Clone - שכפול repository:</b>
<code># שכפול:
git clone https://github.com/username/repo.git

# שכפול עם שם אחר:
git clone https://github.com/username/repo.git my_folder

# שכפול branch ספציפי:
git clone -b branch-name https://github.com/username/repo.git</code>

🏷️ <b>Tags - תיוגים:</b>
<code># יצירת tag:
git tag v1.0.0

# tag עם הודעה:
git tag -a v1.0.0 -m "גרסה 1.0.0"

# רשימת tags:
git tag

# push tags:
git push origin v1.0.0
git push origin --tags  # כל ה-tags

# מחיקת tag:
git tag -d v1.0.0
git push origin --delete v1.0.0</code>

🔄 <b>Stash - שמירה זמנית:</b>
<code># שמירה זמנית של שינויים:
git stash

# שמירה עם שם:
git stash save "עבודה על הלוגין"

# רשימת stashes:
git stash list

# החזרה של stash:
git stash apply
git stash apply stash@{0}

# החזרה ומחיקה:
git stash pop

# מחיקת stash:
git stash drop stash@{0}

# מחיקת הכל:
git stash clear</code>

🎯 <b>Git Workflow - זרימת עבודה:</b>
<code># 1. עדכון מהשרת:
git pull origin main

# 2. יצירת branch לפיצ׳ר:
git checkout -b feature-new-button

# 3. עבודה על הקוד...
# ערוך קבצים...

# 4. commit:
git add .
git commit -m "הוספתי כפתור חדש"

# 5. push ל-remote:
git push origin feature-new-button

# 6. פתיחת Pull Request ב-GitHub

# 7. אחרי אישור - merge ב-GitHub

# 8. עדכון local:
git checkout main
git pull origin main

# 9. מחיקת branch מקומי:
git branch -d feature-new-button</code>

📋 <b>.gitignore - דוגמה מלאה:</b>
<code># Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
dist/
*.egg-info/

# Virtual Environment
venv/
env/
ENV/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Environment Variables
.env
.env.local

# Database
*.db
*.sqlite3

# Logs
*.log

# Tests
.coverage
htmlcov/
.pytest_cache/

# Project Specific
data/
temp/
uploads/</code>

🔥 <b>דוגמה מקיפה - פרויקט מציאותי:</b>
<code># יצירת פרויקט:
mkdir awesome_app
cd awesome_app
git init

# יצירת README:
cat > README.md << EOL
# Awesome App

תיאור הפרויקט...

## התקנה
```bash
pip install -r requirements.txt
```
EOL

# יצירת .gitignore:
cat > .gitignore << EOL
venv/
__pycache__/
.env
*.db
EOL

# Commit ראשון:
git add .
git commit -m "Initial commit: project setup"

# יצירת GitHub repo ודחיפה:
git remote add origin https://github.com/username/awesome_app.git
git push -u origin main

# עבודה על פיצ׳ר:
git checkout -b feature-user-auth

# ... עבודה על הקוד ...

git add .
git commit -m "הוספתי מערכת התחברות"
git push origin feature-user-auth

# Pull Request ב-GitHub...

# אחרי merge:
git checkout main
git pull
git branch -d feature-user-auth</code>

🎨 <b>Git Aliases - קיצורי דרך:</b>
<code># הוספת aliases:
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.st status
git config --global alias.unstage 'reset HEAD --'
git config --global alias.last 'log -1 HEAD'
git config --global alias.visual 'log --graph --oneline --all'

# שימוש:
git co main  # במקום git checkout main
git ci -m "message"  # במקום git commit
git st  # במקום git status</code>

📚 <b>Git Best Practices:</b>
<code>✅ DO:
• commit הודעות ברורות ומתארות
• commits קטנים ולוגיים
• pull לפני push
• branch לכל פיצ׳ר
• .gitignore מסודר
• code review לפני merge

❌ DON'T:
• commit סיסמאות או מפתחות API
• commit קבצים בינאריים גדולים
• push ישירות ל-main
• commit קוד ששבור
• הודעות commit לא ברורות ("fix", "update")
• force push ל-main</code>

🔧 <b>Git Commands - סיכום מהיר:</b>
<code># בסיסי:
git init
git clone
git add
git commit
git status
git log

# Branches:
git branch
git checkout
git merge

# Remote:
git push
git pull
git fetch
git remote

# ביטול:
git reset
git revert
git checkout --

# אחר:
git stash
git tag
git diff</code>

💡 <b>טיפים חשובים:</b>
• commit לעיתים קרובות
• כתוב הודעות commit טובות
• השתמש ב-branches
• pull לפני שאתה מתחיל לעבוד
• למד להשתמש ב-Git GUI אם CLI קשה
• אל תפחד לנסות - אפשר תמיד לחזור אחורה!
""",
        'exercise': {
            'question': 'איזו פקודה משמשת לשמירת שינויים עם הודעה?',
            'options': ['git save', 'git commit -m "message"', 'git push', 'git add -m "message"'],
            'correct_answer': 'git commit -m "message"',
            'explanation': 'נכון! 🎯 git commit -m "message" שומר את השינויים ב-staging area עם הודעה'
        }
    },
    
    30: {
        'title': '🎓 שיעור 30: פרויקט מסכם - בניית API מלא',
        'content': """
בואו נבנה פרויקט מלא ומקצועי! 🚀

🎯 <b>הפרויקט: Todo API עם Flask</b>
API מלא לניהול משימות עם מסד נתונים, אימות, ותיעוד!

📦 <b>התקנה והגדרה:</b>
<code># יצירת פרויקט:
mkdir todo-api
cd todo-api

# venv:
python -m venv venv
source venv/bin/activate  # Mac/Linux
  venv\\Scripts\\activate     # Windows

# התקנת חבילות:
pip install flask flask-sqlalchemy flask-jwt-extended flask-cors

# יצירת requirements.txt:
pip freeze > requirements.txt</code>

🗂️ <b>מבנה הפרויקט:</b>
<code>todo-api/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   └── config.py
├── tests/
│   └── test_api.py
├── venv/
├── .env
├── .gitignore
├── requirements.txt
└── run.py</code>

⚙️ <b>app/config.py - הגדרות:</b>
<code>import os
from datetime import timedelta

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key')
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URL',
        'sqlite:///todo.db'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'jwt-secret-key')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)</code>

🗄️ <b>app/models.py - מודלים:</b>
<code>from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    todos = db.relationship('Todo', backref='user', lazy=True)
    
    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'created_at': self.created_at.isoformat()
        }

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    completed = db.Column(db.Boolean, default=False)
    priority = db.Column(db.String(20), default='medium')
    due_date = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'completed': self.completed,
            'priority': self.priority,
            'due_date': self.due_date.isoformat() if self.due_date else None,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }</code>

🛣️ <b>app/routes.py - Endpoints:</b>
<code>from flask import Blueprint, request, jsonify
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    get_jwt_identity
)
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

from .models import db, User, Todo

api = Blueprint('api', __name__)

# ========== Auth Routes ==========

@api.route('/register', methods=['POST'])
def register():
    '''רישום משתמש חדש'''
    data = request.get_json()
    
    if User.query.filter_by(username=data['username']).first():
        return jsonify({'error': 'שם משתמש כבר קיים'}), 400
    
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'error': 'אימייל כבר קיים'}), 400
    
    user = User(
        username=data['username'],
        email=data['email'],
        password_hash=generate_password_hash(data['password'])
    )
    
    db.session.add(user)
    db.session.commit()
    
    return jsonify({
        'message': 'משתמש נוצר בהצלחה',
        'user': user.to_dict()
    }), 201

@api.route('/login', methods=['POST'])
def login():
    '''התחברות'''
    data = request.get_json()
    
    user = User.query.filter_by(username=data['username']).first()
    
    if not user or not check_password_hash(user.password_hash, data['password']):
        return jsonify({'error': 'שם משתמש או סיסמה שגויים'}), 401
    
    access_token = create_access_token(identity=user.id)
    
    return jsonify({
        'access_token': access_token,
        'user': user.to_dict()
    })

# ========== Todo Routes ==========

@api.route('/todos', methods=['GET'])
@jwt_required()
def get_todos():
    '''קבלת כל המשימות'''
    user_id = get_jwt_identity()
    
    # פילטרים:
    completed = request.args.get('completed', type=lambda v: v.lower() == 'true')
    priority = request.args.get('priority')
    
    query = Todo.query.filter_by(user_id=user_id)
    
    if completed is not None:
        query = query.filter_by(completed=completed)
    if priority:
        query = query.filter_by(priority=priority)
    
    todos = query.all()
    
    return jsonify({
        'todos': [todo.to_dict() for todo in todos]
    })

@api.route('/todos', methods=['POST'])
@jwt_required()
def create_todo():
    '''יצירת משימה חדשה'''
    user_id = get_jwt_identity()
    data = request.get_json()
    
    todo = Todo(
        title=data['title'],
        description=data.get('description', ''),
        priority=data.get('priority', 'medium'),
        user_id=user_id
    )
    
    if 'due_date' in data:
        todo.due_date = datetime.fromisoformat(data['due_date'])
    
    db.session.add(todo)
    db.session.commit()
    
    return jsonify({
        'message': 'משימה נוצרה בהצלחה',
        'todo': todo.to_dict()
    }), 201

@api.route('/todos/<int:todo_id>', methods=['GET'])
@jwt_required()
def get_todo(todo_id):
    '''קבלת משימה ספציפית'''
    user_id = get_jwt_identity()
    
    todo = Todo.query.filter_by(id=todo_id, user_id=user_id).first()
    
    if not todo:
        return jsonify({'error': 'משימה לא נמצאה'}), 404
    
    return jsonify(todo.to_dict())

@api.route('/todos/<int:todo_id>', methods=['PUT'])
@jwt_required()
def update_todo(todo_id):
    '''עדכון משימה'''
    user_id = get_jwt_identity()
    
    todo = Todo.query.filter_by(id=todo_id, user_id=user_id).first()
    
    if not todo:
        return jsonify({'error': 'משימה לא נמצאה'}), 404
    
    data = request.get_json()
    
    if 'title' in data:
        todo.title = data['title']
    if 'description' in data:
        todo.description = data['description']
    if 'completed' in data:
        todo.completed = data['completed']
    if 'priority' in data:
        todo.priority = data['priority']
    if 'due_date' in data:
        todo.due_date = datetime.fromisoformat(data['due_date'])
    
    db.session.commit()
    
    return jsonify({
        'message': 'משימה עודכנה בהצלחה',
        'todo': todo.to_dict()
    })

@api.route('/todos/<int:todo_id>', methods=['DELETE'])
@jwt_required()
def delete_todo(todo_id):
    '''מחיקת משימה'''
    user_id = get_jwt_identity()
    
    todo = Todo.query.filter_by(id=todo_id, user_id=user_id).first()
    
    if not todo:
        return jsonify({'error': 'משימה לא נמצאה'}), 404
    
    db.session.delete(todo)
    db.session.commit()
    
    return jsonify({'message': 'משימה נמחקה בהצלחה'})

@api.route('/todos/<int:todo_id>/toggle', methods=['PATCH'])
@jwt_required()
def toggle_todo(todo_id):
    '''סימון משימה כהושלמה/לא הושלמה'''
    user_id = get_jwt_identity()
    
    todo = Todo.query.filter_by(id=todo_id, user_id=user_id).first()
    
    if not todo:
        return jsonify({'error': 'משימה לא נמצאה'}), 404
    
    todo.completed = not todo.completed
    db.session.commit()
    
    return jsonify({
        'message': f"משימה סומנה כ{'הושלמה' if todo.completed else 'לא הושלמה'}",
        'todo': todo.to_dict()
    })</code>

🏗️ <b>app/__init__.py - אתחול:</b>
<code>from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from .config import Config
from .models import db
from .routes import api

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # הרחבות:
    db.init_app(app)
    CORS(app)
    JWTManager(app)
    
    # Blueprints:
    app.register_blueprint(api, url_prefix='/api')
    
    # יצירת טבלאות:
    with app.app_context():
        db.create_all()
    
    # Route בסיסי:
    @app.route('/')
    def index():
        return {
            'message': 'Todo API',
            'version': '1.0.0',
            'endpoints': {
                'register': '/api/register',
                'login': '/api/login',
                'todos': '/api/todos'
            }
        }
    
    return app</code>

▶️ <b>run.py - הרצה:</b>
<code>from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)</code>

🧪 <b>tests/test_api.py - בדיקות:</b>
<code>import pytest
import json
from app import create_app
from app.models import db

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

def test_register(client):
    response = client.post('/api/register', json={
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'password123'
    })
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data['user']['username'] == 'testuser'

def test_login(client):
    # רישום:
    client.post('/api/register', json={
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'password123'
    })
    
    # התחברות:
    response = client.post('/api/login', json={
        'username': 'testuser',
        'password': 'password123'
    })
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'access_token' in data

# הרצה: pytest tests/</code>

📝 <b>.env:</b>
<code>SECRET_KEY=your-secret-key-here
JWT_SECRET_KEY=your-jwt-secret-key
DATABASE_URL=sqlite:///todo.db</code>

🎯 <b>שימוש ב-API:</b>
<code># רישום:
  curl -X POST http://localhost:5000/api/register \\
    -H "Content-Type: application/json" \\
  -d '{"username":"amir","email":"amir@example.com","password":"123456"}'

# התחברות:
  curl -X POST http://localhost:5000/api/login \\
    -H "Content-Type: application/json" \\
  -d '{"username":"amir","password":"123456"}'

# יצירת משימה (עם token):
  curl -X POST http://localhost:5000/api/todos \\
    -H "Content-Type: application/json" \\
    -H "Authorization: Bearer YOUR_TOKEN_HERE" \\
  -d '{"title":"ללמוד Python","priority":"high"}'

# קבלת משימות:
  curl http://localhost:5000/api/todos \\
  -H "Authorization: Bearer YOUR_TOKEN_HERE"</code>

🎉 <b>מזל טוב!</b>
בנית API מלא ומקצועי עם:
✅ אימות משתמשים (JWT)
✅ CRUD מלא
✅ מסד נתונים (SQLAlchemy)
✅ בדיקות
✅ מבנה נכון
✅ API RESTful

<b>המשך ללמוד ולבנות! 🚀</b>
""",
        'exercise': {
            'question': 'איזו ספרייה ב-Flask משמשת לעבודה עם מסד נתונים?',
            'options': ['Flask-Database', 'Flask-SQLAlchemy', 'Flask-ORM', 'Flask-DB'],
            'correct_answer': 'Flask-SQLAlchemy',
            'explanation': 'מעולה! 🎯 Flask-SQLAlchemy היא ה-ORM הפופולרי לעבודה עם מסדי נתונים ב-Flask'
        }
    }
}
