# -*- coding: utf-8 -*-
"""
המשך השיעורים - חלק 4 (אחרון!)
שיעורים 16-20
"""

LESSONS_PART4 = {
    16: {
        'title': '🎨 שיעור 16: מחלקות ואובייקטים (OOP) - חלק 1',
        'content': """
ברוכים הבאים לתכנות מונחה עצמים! 🏗️

🎯 <b>מה זו מחלקה (Class)?</b>
מחלקה היא כמו תבנית ליצירת אובייקטים. כמו שיש תבנית לעוגיות, יש מחלקה לאובייקטים!

📝 <b>מחלקה בסיסית:</b>
<code>class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        print(f"{self.name} נובח: וואף וואף!")

# יצירת אובייקט:
my_dog = Dog("רקס", 3)
print(my_dog.name)  # רקס
my_dog.bark()       # רקס נובח: וואף וואף!</code>

💡 <b>מרכיבי מחלקה:</b>
• __init__ - הבנאי, רץ כשיוצרים אובייקט חדש
• self - מתייחס לאובייקט עצמו
• attributes - מאפיינים (כמו name, age)
• methods - פונקציות של המחלקה

🎯 <b>מחלקה יותר מפורטת:</b>
<code>class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
    
    def introduce(self):
        print(f"שלום, אני {self.name}")
        print(f"אני בן {self.age}")
        print(f"אני גר ב{self.city}")
    
    def have_birthday(self):
        self.age += 1
        print(f"יום הולדת שמח! עכשיו אני בן {self.age}")

# שימוש:
person1 = Person("אמיר", 25, "תל אביב")
person1.introduce()
person1.have_birthday()</code>

🔧 <b>שינוי ו גישה למאפיינים:</b>
<code>class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
        self.mileage = 0
    
    def drive(self, km):
        self.mileage += km
        print(f"נסעתי {km} ק״מ")

my_car = Car("טויוטה", 2020)
print(my_car.mileage)  # 0
my_car.drive(100)
print(my_car.mileage)  # 100</code>

📊 <b>מאפייני מחלקה vs מאפייני אובייקט:</b>
<code>class Student:
    # מאפיין מחלקה - משותף לכולם:
    school = "תיכון הרצליה"
    
    def __init__(self, name, grade):
        # מאפייני אובייקט - ייחודי לכל אחד:
        self.name = name
        self.grade = grade

s1 = Student("דני", 10)
s2 = Student("רונה", 11)

print(s1.school)  # תיכון הרצליה
print(s2.school)  # תיכון הרצליה
print(s1.name)    # דני
print(s2.name)    # רונה</code>

🎨 <b>מתודות מיוחדות:</b>
<code>class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        return f"{self.title} מאת {self.author}"
    
    def __len__(self):
        return self.pages

book = Book("הארי פוטר", "ג.ק. רולינג", 350)
print(book)        # הארי פוטר מאת ג.ק. רולינג
print(len(book))   # 350</code>

💪 <b>דוגמה - חשבון בנק:</b>
<code>class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"הופקדו {amount}₪. יתרה: {self.balance}₪")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("אין מספיק כסף!")
        else:
            self.balance -= amount
            print(f"משכת {amount}₪. יתרה: {self.balance}₪")
    
    def get_balance(self):
        return f"יתרה: {self.balance}₪"

# שימוש:
account = BankAccount("אמיר", 1000)
account.deposit(500)
account.withdraw(200)
print(account.get_balance())</code>

🔒 <b>מאפיינים פרטיים:</b>
<code>class Secret:
    def __init__(self):
        self.public = "כולם רואים"
        self._protected = "מוגן"
        self.__private = "פרטי מאוד"
    
    def reveal_secret(self):
        return self.__private

s = Secret()
print(s.public)          # עובד
print(s._protected)      # עובד (אבל לא מומלץ)
# print(s.__private)     # שגיאה!
print(s.reveal_secret()) # עובד</code>

🎯 <b>property - getters ו-setters:</b>
<code>class Temperature:
    def __init__(self):
        self._celsius = 0
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273:
            print("טמפרטורה לא אפשרית!")
        else:
            self._celsius = value
    
    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32

temp = Temperature()
temp.celsius = 25
print(temp.fahrenheit)  # 77.0</code>

📚 <b>למה להשתמש ב-OOP?</b>
• ארגון קוד טוב יותר
• שימוש חוזר בקוד
• הסתרת מימוש
• קל יותר לתחזק
""",
        'exercise': {
            'question': 'מה ה-method שרץ אוטומטית כשיוצרים אובייקט חדש?',
            'options': ['__init__', '__new__', '__create__', '__start__'],
            'correct_answer': '__init__',
            'explanation': 'נכון! 🎯 __init__ הוא הבנאי (constructor) שרץ אוטומטית כשיוצרים אובייקט חדש'
        }
    },
    
    17: {
        'title': '🏗️ שיעור 17: ירושה והרחבה (OOP) - חלק 2',
        'content': """
בואו נלמד על ירושה - אחד הכוחות הגדולים של OOP! 👨‍👦

🎯 <b>מה זו ירושה (Inheritance)?</b>
ירושה מאפשרת למחלקה "לרשת" תכונות ממחלקה אחרת!

📝 <b>ירושה בסיסית:</b>
<code>class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} משמיע קול")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} נובח: וואף!")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} מיילל: מיאו!")

dog = Dog("רקס")
cat = Cat("מיטי")
dog.speak()  # רקס נובח: וואף!
cat.speak()  # מיטי מיילל: מיאו!</code>

💡 <b>הורה (Parent) ו-ילד (Child):</b>
• Animal = מחלקת הורה / Base class
• Dog, Cat = מחלקות ילד / Derived class
• הילד יורש את כל המאפיינים והמתודות של ההורה!

🔧 <b>super() - קריאה למחלקת ההורה:</b>
<code>class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
    
    def info(self):
        return f"{self.brand} {self.year}"

class Car(Vehicle):
    def __init__(self, brand, year, doors):
        super().__init__(brand, year)
        self.doors = doors
    
    def info(self):
        base_info = super().info()
        return f"{base_info} - {self.doors} דלתות"

car = Car("טויוטה", 2020, 4)
print(car.info())  # טויוטה 2020 - 4 דלתות</code>

🎯 <b>שכתוב מתודות (Override):</b>
<code>class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def calculate_bonus(self):
        return self.salary * 0.1

class Manager(Employee):
    def calculate_bonus(self):
        return self.salary * 0.2  # מנהלים מקבלים יותר!

emp = Employee("דני", 10000)
mgr = Manager("אמיר", 10000)
print(emp.calculate_bonus())  # 1000
print(mgr.calculate_bonus())  # 2000</code>

🔄 <b>ירושה מרובה:</b>
<code>class Flyer:
    def fly(self):
        print("טס באוויר!")

class Swimmer:
    def swim(self):
        print("שוחה במים!")

class Duck(Flyer, Swimmer):
    def __init__(self, name):
        self.name = name

duck = Duck("דונלד")
duck.fly()   # טס באוויר!
duck.swim()  # שוחה במים!</code>

💪 <b>דוגמה מקיפה - מערכת עובדים:</b>
<code>class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"שלום, אני {self.name} בן {self.age}"

class Employee(Person):
    def __init__(self, name, age, employee_id, department):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.department = department
    
    def introduce(self):
        base = super().introduce()
        return f"{base}, עובד #{self.employee_id} במחלקת {self.department}"

class Developer(Employee):
    def __init__(self, name, age, employee_id, languages):
        super().__init__(name, age, employee_id, "פיתוח")
        self.languages = languages
    
    def code(self):
        return f"כותב קוד ב-{', '.join(self.languages)}"

dev = Developer("אמיר", 25, "E001", ["Python", "JavaScript"])
print(dev.introduce())
print(dev.code())</code>

🎨 <b>isinstance() ו-issubclass():</b>
<code>class Animal:
    pass

class Dog(Animal):
    pass

rex = Dog()

print(isinstance(rex, Dog))     # True
print(isinstance(rex, Animal))  # True
print(isinstance(rex, str))     # False

print(issubclass(Dog, Animal))  # True
print(issubclass(Animal, Dog))  # False</code>

🔒 <b>מחלקות מופשטות (Abstract):</b>
<code>from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

rect = Rectangle(5, 10)
print(rect.area())       # 50
print(rect.perimeter())  # 30</code>

🎯 <b>Composition vs Inheritance:</b>
<code># Inheritance:
class Employee:
    def work(self):
        print("עובד...")

class Developer(Employee):
    pass

# Composition (לפעמים עדיף!):
class Engine:
    def start(self):
        print("מנוע מתניע")

class Car:
    def __init__(self):
        self.engine = Engine()  # יש לי מנוע!
    
    def start(self):
        self.engine.start()

car = Car()
car.start()</code>

🔥 <b>דוגמה - משחק:</b>
<code>class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health
    
    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} קיבל {damage} נזק. HP: {self.health}")

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=150)
        self.armor = 20
    
    def take_damage(self, damage):
        reduced = damage - self.armor
        if reduced < 0:
            reduced = 0
        super().take_damage(reduced)

class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=80)
        self.mana = 100
    
    def cast_spell(self):
        if self.mana >= 20:
            self.mana -= 20
            return "כישוף הוטל! 🔮"
        return "לא מספיק מאנה"

warrior = Warrior("גולם")
mage = Mage("מרלין")

warrior.take_damage(30)  # 150 - (30-20) = 140
print(mage.cast_spell())</code>

📚 <b>עקרונות OOP - SOLID:</b>
• Single Responsibility - כל מחלקה תעשה דבר אחד
• Open/Closed - פתוח להרחבה, סגור לשינוי
• Liskov Substitution - אפשר להחליף הורה בילד
• Interface Segregation - ממשקים קטנים ומוגדרים
• Dependency Inversion - תלות בהפשטה
""",
        'exercise': {
            'question': 'איזו מילת מפתח משמשת לקריאה למחלקת האב?',
            'options': ['parent()', 'super()', 'base()', 'inherit()'],
            'correct_answer': 'super()',
            'explanation': 'מצוין! 🌟 super() מאפשר לגשת למתודות ומאפיינים של מחלקת האב'
        }
    },
    
    18: {
        'title': '🔍 שיעור 18: List Comprehension וגנרטורים',
        'content': """
טכניקות מתקדמות וחזקות ליצירת רשימות! ⚡

🎯 <b>List Comprehension - מה זה?</b>
דרך מהירה וקריאה ליצור רשימות בשורה אחת!

📝 <b>List Comprehension בסיסי:</b>
<code># דרך רגילה:
squares = []
for x in range(10):
    squares.append(x ** 2)

# דרך מגניבה:
squares = [x ** 2 for x in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]</code>

💡 <b>מבנה:</b>
[ביטוי for פריט in רשימה]

🔍 <b>עם תנאי:</b>
<code># רק זוגיים:
evens = [x for x in range(20) if x % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# רק חיוביים:
numbers = [-2, -1, 0, 1, 2, 3]
positive = [x for x in numbers if x > 0]
print(positive)  # [1, 2, 3]</code>

🎨 <b>עם if-else:</b>
<code># "זוגי" או "אי-זוגי":
result = ["זוגי" if x % 2 == 0 else "אי-זוגי" for x in range(5)]
print(result)  # ['זוגי', 'אי-זוגי', 'זוגי', 'אי-זוגי', 'זוגי']

# כפל ב-2 אם זוגי, אחרת כפי ב-3:
numbers = [x * 2 if x % 2 == 0 else x * 3 for x in range(6)]
print(numbers)  # [0, 3, 4, 9, 8, 15]</code>

🔄 <b>לולאות מקוננות:</b>
<code># כל הזוגות:
pairs = [(x, y) for x in range(3) for y in range(3)]
print(pairs)
# [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)]

# מטריצה שטוחה:
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]
print(flat)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]</code>

📚 <b>עם פונקציות:</b>
<code># המרת טקסט לאותיות גדולות:
words = ["hello", "world", "python"]
upper_words = [word.upper() for word in words]
print(upper_words)  # ['HELLO', 'WORLD', 'PYTHON']

# אורכי מילים:
lengths = [len(word) for word in words]
print(lengths)  # [5, 5, 6]</code>

🎯 <b>Dictionary Comprehension:</b>
<code># ריבועים:
squares = {x: x**2 for x in range(5)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# הופכי מילון:
original = {"a": 1, "b": 2, "c": 3}
flipped = {v: k for k, v in original.items()}
print(flipped)  # {1: 'a', 2: 'b', 3: 'c'}

# עם תנאי:
scores = {"אמיר": 85, "דני": 95, "יוסי": 75}
passed = {name: score for name, score in scores.items() if score >= 80}
print(passed)  # {'אמיר': 85, 'דני': 95}</code>

🎨 <b>Set Comprehension:</b>
<code># מספרים ייחודיים:
numbers = [1, 2, 2, 3, 3, 3, 4]
unique_squares = {x**2 for x in numbers}
print(unique_squares)  # {1, 4, 9, 16}</code>

⚡ <b>גנרטורים (Generators):</b>
<code># List Comprehension - יוצר רשימה שלמה בזיכרון:
squares_list = [x**2 for x in range(1000000)]  # תופס הרבה זיכרון!

# Generator - מחשב ערך בכל פעם:
squares_gen = (x**2 for x in range(1000000))  # חסכוני בזיכרון!

# שימוש:
for square in squares_gen:
    if square > 100:
        break
    print(square)</code>

שימו לב לסוגריים! [] vs ()

🔥 <b>פונקציות גנרטור:</b>
<code>def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# שימוש:
for num in fibonacci(10):
    print(num)  # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34</code>

yield מחזיר ערך אבל שומר את המצב!

💪 <b>דוגמאות מעשיות:</b>
<code># סינון אימיילים:
emails = ["user@gmail.com", "test@yahoo.com", "admin@gmail.com"]
gmail_only = [e for e in emails if e.endswith("@gmail.com")]

# טרנספורמציה:
prices = [100, 200, 150, 300]
with_tax = [price * 1.17 for price in prices]

# קבלת ערכים מתוך מילון:
users = [
    {"name": "אמיר", "age": 25},
    {"name": "דני", "age": 17},
    {"name": "יוסי", "age": 30}
]
adults = [user["name"] for user in users if user["age"] >= 18]

# ניקוי טקסט:
text = "  שלום   עולם   "
words = [word.strip() for word in text.split() if word.strip()]</code>

🎯 <b>any() ו-all() עם comprehension:</b>
<code>numbers = [2, 4, 6, 8, 10]

# האם כולם זוגיים?
all_even = all(x % 2 == 0 for x in numbers)  # True

# האם יש לפחות אחד שלילי?
has_negative = any(x < 0 for x in numbers)  # False</code>

🔍 <b>zip() עם comprehension:</b>
<code>names = ["אמיר", "דני", "יוסי"]
ages = [25, 30, 28]

# יצירת מילון:
people = {name: age for name, age in zip(names, ages)}
print(people)  # {'אמיר': 25, 'דני': 30, 'יוסי': 28}</code>

📚 <b>מתי להשתמש?</b>
• List Comprehension - לרשימות קטנות עד בינוניות
• Generator - לכמויות גדולות של נתונים
• אם הקוד נעשה מסובך - עדיף לולאה רגילה!

⚠️ <b>אל תגזימו!</b>
<code># ❌ קשה לקריאה:
result = [x**2 for x in [y*2 for y in range(10) if y % 2 == 0] if x < 50]

# ✅ יותר ברור:
numbers = [y*2 for y in range(10) if y % 2 == 0]
result = [x**2 for x in numbers if x < 50]</code>
""",
        'exercise': {
            'question': 'מה יודפס?\n\nresult = [x*2 for x in range(5) if x % 2 == 0]\nprint(result)',
            'options': ['[0, 2, 4]', '[0, 4, 8]', '[2, 4, 6]', '[0, 2, 4, 6, 8]'],
            'correct_answer': '[0, 4, 8]',
            'explanation': 'נכון! 🎯 x לוקח ערכים 0,1,2,3,4. מתוכם רק 0,2,4 זוגיים. אחרי כפל ב-2: [0, 4, 8]'
        }
    },
    
    19: {
        'title': '🌐 שיעור 19: עבודה עם APIs ו-JSON',
        'content': """
בואו נלמד איך להתחבר לאינטרנט ולעבוד עם נתונים! 🚀

🎯 <b>מה זה API?</b>
API (Application Programming Interface) הוא דרך לתוכניות לדבר אחת עם השנייה!

📦 <b>התקנת requests:</b>
<code># בטרמינל:
pip install requests</code>

📡 <b>בקשת GET בסיסית:</b>
<code>import requests

response = requests.get("https://api.github.com")
print(response.status_code)  # 200 = הצלחה!
print(response.text)  # התשובה כטקסט</code>

💡 <b>קודי סטטוס נפוצים:</b>
• 200 - OK (הכל טוב!)
• 404 - Not Found (לא נמצא)
• 500 - Server Error (שגיאה בשרת)
• 401 - Unauthorized (אין הרשאה)

🎨 <b>עבודה עם JSON:</b>
<code>import requests

response = requests.get("https://api.github.com/users/octocat")
data = response.json()  # המרה ל-dict!

print(data["name"])
print(data["public_repos"])
print(data["followers"])</code>

📝 <b>JSON - מה זה?</b>
JSON הוא פורמט להעברת נתונים. נראה כמו dict ב-Python!

<code>import json

# Python → JSON:
data = {"name": "אמיר", "age": 25, "hobbies": ["קוד", "משחקים"]}
json_string = json.dumps(data, ensure_ascii=False)
print(json_string)

# JSON → Python:
loaded_data = json.loads(json_string)
print(loaded_data["name"])</code>

🔍 <b>בדיקת תקינות:</b>
<code>import requests

try:
    response = requests.get("https://api.example.com/data")
    response.raise_for_status()  # יזרוק שגיאה אם לא 200
    data = response.json()
    print(data)
except requests.exceptions.RequestException as e:
    print(f"שגיאה: {e}")</code>

📊 <b>שליחת פרמטרים:</b>
<code>import requests

# פרמטרים ב-URL:
params = {
    "q": "python",
    "sort": "stars",
    "order": "desc"
}

response = requests.get("https://api.github.com/search/repositories", params=params)
data = response.json()

print(f"נמצאו {data['total_count']} פרויקטים")</code>

📤 <b>POST - שליחת נתונים:</b>
<code>import requests

data = {
    "username": "user123",
    "email": "user@example.com"
}

response = requests.post("https://api.example.com/users", json=data)
print(response.status_code)
print(response.json())</code>

🔑 <b>Headers - כותרות:</b>
<code>import requests

headers = {
    "Authorization": "Bearer YOUR_TOKEN_HERE",
    "Content-Type": "application/json"
}

response = requests.get("https://api.example.com/data", headers=headers)
print(response.json())</code>

⏱️ <b>Timeout - זמן המתנה:</b>
<code>import requests

try:
    response = requests.get("https://api.example.com", timeout=5)
    print(response.json())
except requests.exceptions.Timeout:
    print("הבקשה לקחה יותר מדי זמן!")</code>

💾 <b>שמירת תשובה לקובץ:</b>
<code>import requests
import json

response = requests.get("https://api.github.com/users/octocat")
data = response.json()

with open("user_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)</code>

🌐 <b>דוגמה - מזג אוויר:</b>
<code>import requests

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric",
        "lang": "he"
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        
        temp = data["main"]["temp"]
        description = data["weather"][0]["description"]
        
        return f"טמפרטורה ב{city}: {temp}°C, {description}"
    except Exception as e:
        return f"שגיאה: {e}"

# שימוש:
# result = get_weather("Tel Aviv", "YOUR_API_KEY")
# print(result)</code>

🔥 <b>דוגמה - GitHub API:</b>
<code>import requests

def get_user_repos(username):
    url = f"https://api.github.com/users/{username}/repos"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        repos = response.json()
        
        print(f"פרויקטים של {username}:")
        for repo in repos[:5]:  # רק 5 הראשונים
            print(f"• {repo['name']} - ⭐ {repo['stargazers_count']}")
    
    except requests.exceptions.HTTPError as e:
        if response.status_code == 404:
            print("משתמש לא נמצא!")
        else:
            print(f"שגיאה: {e}")

# שימוש:
get_user_repos("octocat")</code>

📚 <b>עבודה עם JSON מקומי:</b>
<code>import json

# קריאה מקובץ:
with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# עיבוד:
for user in data["users"]:
    print(user["name"])

# כתיבה לקובץ:
new_data = {"message": "שלום עולם", "count": 42}
with open("output.json", "w", encoding="utf-8") as f:
    json.dump(new_data, f, ensure_ascii=False, indent=2)</code>

🎯 <b>Session - חיבורים מרובים:</b>
<code>import requests

# יעיל יותר לבקשות מרובות:
session = requests.Session()
session.headers.update({"Authorization": "Bearer TOKEN"})

response1 = session.get("https://api.example.com/endpoint1")
response2 = session.get("https://api.example.com/endpoint2")

session.close()</code>

⚡ <b>Async Requests - בקשות מקבילות:</b>
<code>import requests
from concurrent.futures import ThreadPoolExecutor

urls = [
    "https://api.github.com/users/user1",
    "https://api.github.com/users/user2",
    "https://api.github.com/users/user3"
]

def fetch_url(url):
    response = requests.get(url)
    return response.json()

with ThreadPoolExecutor(max_workers=3) as executor:
    results = list(executor.map(fetch_url, urls))

for result in results:
    print(result.get("name", "Unknown"))</code>

📚 <b>טיפים חשובים:</b>
• תמיד בדקו את status_code
• השתמשו ב-timeout
• קראו את התיעוד של ה-API
• שמרו API keys בטוח (לא בקוד!)
• טפלו בשגיאות נכון
• שמרו על rate limits (הגבלות בקשות)
""",
        'exercise': {
            'question': 'איזה קוד סטטוס HTTP מציין הצלחה?',
            'options': ['404', '500', '200', '401'],
            'correct_answer': '200',
            'explanation': 'מעולה! 🎉 200 OK הוא קוד הסטטוס שמציין שהבקשה הצליחה'
        }
    },
    
    20: {
        'title': '🎓 שיעור 20: טיפים מתקדמים וסיכום',
        'content': """
הגענו לשיעור האחרון! בואו נסכם ונלמד כמה טריקים מגניבים! 🎉

🎯 <b>Decorators - עיטורים לפונקציות:</b>
<code>def timer(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} לקח {end-start:.2f} שניות")
        return result
    return wrapper

@timer
def slow_function():
    import time
    time.sleep(2)
    print("סיימתי!")

slow_function()</code>

🔧 <b>Context Managers - with:</b>
<code>class FileManager:
    def __init__(self, filename):
        self.filename = filename
    
    def __enter__(self):
        self.file = open(self.filename, 'w')
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

with FileManager("test.txt") as f:
    f.write("שלום!")</code>

⚡ <b>*args ו-**kwargs - פרמטרים גמישים:</b>
<code>def flexible_function(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

flexible_function(1, 2, 3, name="אמיר", age=25)
# Args: (1, 2, 3)
# Kwargs: {'name': 'אמיר', 'age': 25}</code>

🎨 <b>enumerate וכמה טריקים:</b>
<code># enumerate עם start:
for i, item in enumerate(["א", "ב", "ג"], start=1):
    print(f"{i}. {item}")

# zip - איחוד רשימות:
names = ["אמיר", "דני"]
ages = [25, 30]
for name, age in zip(names, ages):
    print(f"{name}: {age}")

# reversed - הפוך:
for item in reversed([1, 2, 3]):
    print(item)  # 3, 2, 1</code>

💡 <b>Ternary Operator - תנאי בשורה:</b>
<code># במקום:
if x > 0:
    result = "חיובי"
else:
    result = "לא חיובי"

# אפשר:
result = "חיובי" if x > 0 else "לא חיובי"</code>

🔍 <b>Walrus Operator := (Python 3.8+):</b>
<code># השמה בתוך תנאי:
if (n := len(numbers)) > 10:
    print(f"יש {n} מספרים - הרבה!")

# בלולאה:
while (line := file.readline()):
    print(line)</code>

📊 <b>Counter - ספירה מהירה:</b>
<code>from collections import Counter

words = ["תפוח", "בננה", "תפוח", "תפוז", "בננה", "תפוח"]
counter = Counter(words)

print(counter.most_common(2))  # [('תפוח', 3), ('בננה', 2)]</code>

🎯 <b>defaultdict - מילון עם ברירת מחדל:</b>
<code>from collections import defaultdict

# רשימות אוטומטיות:
groups = defaultdict(list)
groups["fruits"].append("תפוח")
groups["fruits"].append("בננה")
print(groups)  # {'fruits': ['תפוח', 'בננה']}</code>

💪 <b>map, filter, reduce:</b>
<code># map - החלת פונקציה:
numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x**2, numbers))
print(squares)  # [1, 4, 9, 16]

# filter - סינון:
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4]

# reduce - צמצום לערך אחד:
from functools import reduce
total = reduce(lambda x, y: x + y, numbers)
print(total)  # 10</code>

🔥 <b>itertools - כלים מתקדמים:</b>
<code>from itertools import combinations, permutations, cycle

# צירופים:
items = [1, 2, 3]
print(list(combinations(items, 2)))  # [(1,2), (1,3), (2,3)]

# תמורות:
print(list(permutations([1, 2], 2)))  # [(1,2), (2,1)]

# חזרה אינסופית:
colors = cycle(['אדום', 'ירוק', 'כחול'])
for i, color in enumerate(colors):
    if i >= 5:
        break
    print(color)</code>

📚 <b>pathlib - עבודה עם קבצים מודרנית:</b>
<code>from pathlib import Path

# יצירת path:
path = Path("data/file.txt")

# בדיקות:
print(path.exists())
print(path.is_file())

# חלקים של הנתיב:
print(path.name)      # file.txt
print(path.suffix)    # .txt
print(path.parent)    # data

# קבלת כל הקבצים:
for file in Path(".").glob("*.py"):
    print(file)</code>

🎨 <b>dataclasses - מחלקות פשוטות:</b>
<code>from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
    city: str = "תל אביב"  # ערך ברירת מחדל

person = Person("אמיר", 25)
print(person)  # Person(name='אמיר', age=25, city='תל אביב')</code>

⚡ <b>טיפים לקוד טוב:</b>
<code># 1. השתמשו בשמות ברורים:
# ❌ x, y, z
# ✅ student_name, total_score, is_active

# 2. פונקציות קצרות:
# כל פונקציה - דבר אחד טוב

# 3. הערות רק למה, לא מה:
# ❌ x = x + 1  # מוסיף 1 ל-x
# ✅ x += 1  # קופץ לשורה הבאה

# 4. השתמשו ב-with:
with open("file.txt") as f:
    data = f.read()

# 5. list/dict comprehension לדברים פשוטים:
squares = [x**2 for x in range(10)]</code>

🎯 <b>Virtual Environments:</b>
<code># בטרמינל:
# יצירה:
python -m venv myenv

  # הפעלה (Windows):
  myenv\\Scripts\\activate

# הפעלה (Mac/Linux):
source myenv/bin/activate

# התקנת חבילות:
pip install requests

# שמירת תלויות:
pip freeze > requirements.txt

# התקנה מקובץ:
pip install -r requirements.txt</code>

📚 <b>לאן ממשיכים מכאן?</b>

🌟 <b>נושאים למידה:</b>
• Web Development (Flask, Django, FastAPI)
• Data Science (Pandas, NumPy, Matplotlib)
• Machine Learning (Scikit-learn, TensorFlow)
• Automation (Selenium, Beautiful Soup)
• Bots (Telegram, Discord, WhatsApp)
• Game Development (Pygame)
• Desktop Apps (Tkinter, PyQt)

📖 <b>משאבים מומלצים:</b>
• Python Docs - docs.python.org
• Real Python - realpython.com
• GitHub - חפש פרויקטים מעניינים
• Stack Overflow - תשאל שאלות
• YouTube - המון הדרכות בחינם

💪 <b>עצות אחרונות:</b>
1. תתרגלו כל יום - גם 30 דקות
2. תבנו פרויקטים משלכם
3. תקראו קוד של אחרים
4. תשאלו שאלות בקהילה
5. אל תתייאשו משגיאות - זה חלק מהתהליך!

🎉 <b>מזל טוב!</b>
סיימת את 20 השיעורים! עכשיו אתה מכיר את היסודות של Python.
הדרך מכאן היא לבנות פרויקטים ולהמשיך ללמוד.

זכור: כל מתכנת התחיל מאפס. אתה יכול! 💪

<b>Python הוא רק ההתחלה - העולם כולו מחכה לך! 🚀</b>
""",
        'exercise': {
            'question': 'איזו מהפעולות הבאות היא O(1) - הכי מהירה?',
            'options': ['חיפוש ברשימה', 'גישה לאלמנט במילון לפי מפתח', 'מיון רשימה', 'שכפול רשימה'],
            'correct_answer': 'גישה לאלמנט במילון לפי מפתח',
            'explanation': 'מצוין! 🏆 גישה למילון לפי מפתח היא O(1) - מהירה במיוחד! זה אחד היתרונות הגדולים של מילונים'
        }
    }
}
