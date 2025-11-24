# -*- coding: utf-8 -*-
"""
שיעורים נוספים - חלק 7 (Critical Skills)
שיעורים 31-35 - מיומנויות קריטיות שכל מתכנת צריך
"""

LESSONS_PART7 = {
    31: {
        'title': '🐛 שיעור 31: Debugging - ניפוי שגיאות כמו מקצוען',
        'content': r'''
בואו נלמד לקרוא ולתקן שגיאות! 🔍

🎯 <b>למה Debugging חשוב?</b>
קוד תמיד משתבש! היכולת למצוא ולתקן באגים היא מיומנות קריטית!

⚠️ <b>סוגי שגיאות נפוצות:</b>

<b>1. SyntaxError - שגיאת תחביר:</b>
<code># ❌ שגוי:
if x > 5
    print("גדול")

# שגיאה: SyntaxError: expected ':'
# ✅ תיקון: צריך : אחרי if</code>

<b>2. IndentationError - שגיאת הזחה:</b>
<code># ❌ שגוי:
def my_function():
print("שלום")

# שגיאה: IndentationError
# ✅ תיקון: צריך הזחה אחרי def</code>

<b>3. NameError - משתנה לא קיים:</b>
<code># ❌ שגוי:
print(name)

# שגיאה: NameError: name 'name' is not defined
# ✅ תיקון: צריך להגדיר את name לפני</code>

<b>4. TypeError - טיפוס שגוי:</b>
<code># ❌ שגוי:
result = "5" + 5

# שגיאה: TypeError: can only concatenate str to str
# ✅ תיקון: צריך להמיר:
result = int("5") + 5  # או "5" + str(5)</code>

<b>5. IndexError - אינדקס לא קיים:</b>
<code># ❌ שגוי:
my_list = [1, 2, 3]
print(my_list[3])

# שגיאה: IndexError: list index out of range
# למה? בפייתון הספירה מ-0!
# my_list[0]=1, my_list[1]=2, my_list[2]=3
# ✅ תיקון: print(my_list[2])</code>

<b>6. KeyError - מפתח לא קיים:</b>
<code># ❌ שגוי:
user = {"name": "אמיר"}
print(user["age"])

# שגיאה: KeyError: 'age'
# ✅ תיקון: use .get()
print(user.get("age", "לא קיים"))</code>

<b>7. ValueError - ערך לא תקין:</b>
<code># ❌ שגוי:
number = int("abc")

# שגיאה: ValueError: invalid literal for int()
# ✅ תיקון: בדוק תקינות לפני
if text.isdigit():
    number = int(text)</code>

<b>8. ZeroDivisionError - חילוק באפס:</b>
<code># ❌ שגוי:
result = 10 / 0

# שגיאה: ZeroDivisionError
# ✅ תיקון: בדוק לפני
if divisor != 0:
    result = 10 / divisor</code>

🔍 <b>איך לקרוא Traceback:</b>
<code># קוד עם שגיאה:
def divide(a, b):
    return a / b

def calculate(x, y):
    result = divide(x, y)
    return result * 2

answer = calculate(10, 0)

# הפלט:
"""
Traceback (most recent call last):
  File "main.py", line 8, in <module>
    answer = calculate(10, 0)
  File "main.py", line 5, in calculate
    result = divide(x, y)
  File "main.py", line 2, in divide
    return a / b
ZeroDivisionError: division by zero
"""

# איך לקרוא:
# 1. התחל מלמטה - סוג השגיאה
# 2. קרא למעלה - מה קרה בכל שורה
# 3. מצא את הבעיה - שורה 2 בפונקציה divide</code>

🔧 <b>כלי Debugging:</b>

<b>1. Print Debugging:</b>
<code>def calculate_total(prices):
    print(f"Debug: קיבלתי {prices}")  # בדיקה
    total = 0
    for price in prices:
        print(f"Debug: מוסיף {price}")  # בדיקה
        total += price
    print(f"Debug: סכום סופי {total}")  # בדיקה
    return total

result = calculate_total([10, 20, 30])</code>

<b>2. assert - וידוא תנאים:</b>
<code>def divide(a, b):
    assert b != 0, "לא ניתן לחלק באפס!"
    assert isinstance(a, (int, float)), "a חייב להיות מספר"
    assert isinstance(b, (int, float)), "b חייב להיות מספר"
    return a / b

# אם התנאי לא מתקיים - AssertionError</code>

<b>3. breakpoint() - נקודת עצירה:</b>
<code>def complex_function(data):
    result = []
    for item in data:
        breakpoint()  # התוכנית תיעצר כאן!
        # אפשר לבדוק משתנים במצב debug
        processed = item * 2
        result.append(processed)
    return result</code>

<b>4. logging - תיעוד מתקדם:</b>
<code>import logging

logging.basicConfig(level=logging.DEBUG)

def process_data(data):
    logging.debug(f"התחלת עיבוד: {data}")
    try:
        result = data * 2
        logging.info(f"תוצאה: {result}")
        return result
    except Exception as e:
        logging.error(f"שגיאה: {e}")
        raise</code>

💡 <b>אסטרטגיות למציאת באגים:</b>

<b>1. חלק לחצאים (Binary Search):</b>
<code># אם יש 100 שורות קוד ולא יודע איפה השגיאה
# הוסף print באמצע (שורה 50)
# אם השגיאה לפני - חפש בין 1-50
# אם השגיאה אחרי - חפש בין 50-100
# חזור על זה עד שמצאת!</code>

<b>2. הרבּר ברווז (Rubber Duck Debugging):</b>
<code># הסבר את הקוד בקול רם לחפץ (כן, באמת!)
# הסבר שורה אחר שורה מה הקוד עושה
# לעתים קרובות תמצא את הבאג בזמן ההסבר</code>

<b>3. העתק-הדבק קטן:</b>
<code># צור קובץ חדש פשוט
# העתק רק את החלק הבעייתי
# נסה להריץ
# הסר קוד עד שאתה מוצא את השורה הבעייתית</code>

🎯 <b>דוגמאות מציאותיות:</b>

<b>באג 1: לולאה אינסופית</b>
<code># ❌ באג:
i = 0
while i < 10:
    print(i)
    # שכחנו i += 1 !

# ✅ תיקון:
i = 0
while i < 10:
    print(i)
    i += 1</code>

<b>באג 2: שינוי רשימה בלולאה</b>
<code># ❌ באג:
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)  # בעיה!

# ✅ תיקון:
numbers = [1, 2, 3, 4, 5]
numbers = [num for num in numbers if num % 2 != 0]</code>

<b>באג 3: Mutable default argument</b>
<code># ❌ באג:
def add_item(item, my_list=[]):
    my_list.append(item)
    return my_list

print(add_item(1))  # [1]
print(add_item(2))  # [1, 2] - מה?!

# ✅ תיקון:
def add_item(item, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(item)
    return my_list</code>

📚 <b>טיפים לכתיבת קוד עמיד באגים:</b>

✅ כתוב בדיקות (tests)
✅ השתמש ב-type hints
✅ תפוס חריגות (try/except)
✅ בדוק ערכים קיצוניים (0, None, רשימה ריקה)
✅ כתוב קוד פשוט וקריא
✅ הוסף הערות למקומות מורכבים
✅ השתמש ב-linter (pylint, flake8)

🔥 <b>דוגמה מקיפה - מציאת באג:</b>
<code># הקוד הזה אמור לחשב ממוצע ציונים
# אבל יש בו באג! תמצא אותו:

def calculate_average(grades):
    total = 0
    count = 0
    for grade in grades:
        if grade >= 0:  # רק ציונים חיוביים
            total += grade
            count += 1
    average = total / count  # ⚠️ מה אם count=0?
    return average

# בדיקה:
result = calculate_average([])  # 💥 ZeroDivisionError!

# ✅ תיקון:
def calculate_average(grades):
    total = 0
    count = 0
    for grade in grades:
        if grade >= 0:
            total += grade
            count += 1
    
    if count == 0:
        return 0  # או None, או raise ValueError
    
    return total / count</code>

⚡ <b>IDE Debugger - כלי מקצועי:</b>
<code># ב-VS Code / PyCharm:
# 1. לחץ ליד מספר השורה (נקודה אדומה)
# 2. הרץ במצב Debug (F5)
# 3. הקוד ייעצר בנקודה
# 4. בדוק משתנים בחלון הצד
# 5. המשך שורה-שורה (F10)
# 6. היכנס לפונקציה (F11)</code>

💪 <b>זכור:</b>
• כל מתכנת עושה באגים - זה חלק מהתהליך!
• ככל שתתרגל debugging, תהיה מהיר יותר
• לפעמים הפסקה קצרה עוזרת למצוא את הפתרון
• אל תפחד לבקש עזרה או לחפש ב-Google
• רוב הבאגים הם טעויות פשוטות
''',
        'exercise': {
            'question': """מה יקרה בקוד הזה?

my_list = [1, 2, 3]
print(my_list[3])""",
            'options': [
                'יודפס 3',
                'יודפס None',
                'IndexError - האינדקס לא קיים',
                'יודפס 4'
            ],
            'correct_answer': 'IndexError - האינדקס לא קיים',
            'explanation': 'נכון! 🎯 בפייתון הספירה מתחילה מ-0. הרשימה [1,2,3] יש לה אינדקסים 0,1,2. אין אינדקס 3, ולכן IndexError!'
        }
    },
    
    32: {
        'title': '⏰ שיעור 32: datetime - עבודה עם תאריכים וזמנים',
        'content': r'''
בואו נלמד לעבוד עם זמן! ⏰

🎯 <b>למה datetime חשוב?</b>
כמעט כל תוכנית צריכה לעבוד עם תאריכים - לוגים, events, תזמונים ועוד!

📅 <b>datetime - המודול הבסיסי:</b>
<code>from datetime import datetime, date, time, timedelta

# תאריך ושעה נוכחיים:
now = datetime.now()
print(now)  # 2024-11-18 14:30:45.123456

# רק תאריך:
today = date.today()
print(today)  # 2024-11-18

# רק שעה:
current_time = datetime.now().time()
print(current_time)  # 14:30:45.123456</code>

🔨 <b>יצירת תאריכים:</b>
<code>from datetime import datetime, date

# יצירה ידנית:
birthday = date(1998, 5, 15)
print(birthday)  # 1998-05-15

# עם שעה:
meeting = datetime(2024, 12, 25, 14, 30, 0)
print(meeting)  # 2024-12-25 14:30:00

# מ-string:
date_str = "2024-11-18"
parsed_date = datetime.strptime(date_str, "%Y-%m-%d")
print(parsed_date)</code>

📊 <b>פורמט תאריכים (strftime):</b>
<code>from datetime import datetime

now = datetime.now()

# פורמטים שונים:
print(now.strftime("%Y-%m-%d"))           # 2024-11-18
print(now.strftime("%d/%m/%Y"))           # 18/11/2024
print(now.strftime("%B %d, %Y"))          # November 18, 2024
print(now.strftime("%A"))                 # Monday
print(now.strftime("%H:%M:%S"))           # 14:30:45
print(now.strftime("%I:%M %p"))           # 02:30 PM
print(now.strftime("%d/%m/%Y %H:%M"))     # 18/11/2024 14:30

# עברית (צריך locale):
print(now.strftime("%d.%m.%Y בשעה %H:%M"))</code>

📝 <b>קודי פורמט נפוצים:</b>
<code>%Y - שנה (2024)
%y - שנה קצרה (24)
%m - חודש (01-12)
%B - שם חודש (January)
%b - שם חודש קצר (Jan)
%d - יום (01-31)
%A - יום בשבוע (Monday)
%a - יום קצר (Mon)
%H - שעה 24 (00-23)
%I - שעה 12 (01-12)
%M - דקות (00-59)
%S - שניות (00-59)
%p - AM/PM</code>

➕ <b>חישובים עם תאריכים (timedelta):</b>
<code>from datetime import datetime, timedelta

now = datetime.now()

# הוספה:
tomorrow = now + timedelta(days=1)
next_week = now + timedelta(weeks=1)
in_3_hours = now + timedelta(hours=3)

# חיסור:
yesterday = now - timedelta(days=1)
last_month = now - timedelta(days=30)

# שילוב:
future = now + timedelta(days=7, hours=2, minutes=30)

print(f"עכשיו: {now}")
print(f"מחר: {tomorrow}")
print(f"בעוד שבוע: {next_week}")</code>

📐 <b>הפרש בין תאריכים:</b>
<code>from datetime import datetime, date

# תאריכים:
birthday = date(1998, 5, 15)
today = date.today()

# הפרש:
age_delta = today - birthday
print(f"חי {age_delta.days} ימים")
print(f"בערך {age_delta.days // 365} שנים")

# עם שעות:
start = datetime(2024, 11, 18, 10, 0, 0)
end = datetime(2024, 11, 18, 15, 30, 0)

duration = end - start
print(f"משך: {duration}")  # 5:30:00
print(f"שעות: {duration.total_seconds() / 3600}")  # 5.5</code>

🔍 <b>השוואת תאריכים:</b>
<code>from datetime import datetime

date1 = datetime(2024, 11, 18)
date2 = datetime(2024, 12, 25)

if date1 < date2:
    print("date1 לפני date2")

if date1 == date2:
    print("אותו תאריך")

# מיון:
dates = [
    datetime(2024, 5, 15),
    datetime(2024, 1, 1),
    datetime(2024, 12, 31)
]
dates.sort()
print(dates)  # ממוינים מהקטן לגדול</code>

⏰ <b>Timezone - אזורי זמן:</b>
<code>from datetime import datetime
import pytz  # pip install pytz

# UTC:
utc_now = datetime.now(pytz.UTC)
print(utc_now)

# ישראל:
israel_tz = pytz.timezone('Asia/Jerusalem')
israel_now = datetime.now(israel_tz)
print(israel_now)

# המרה בין אזורי זמן:
ny_tz = pytz.timezone('America/New_York')
ny_time = israel_now.astimezone(ny_tz)
print(f"בישראל: {israel_now}")
print(f"בניו יורק: {ny_time}")</code>

📅 <b>calendar - עבודה עם לוח שנה:</b>
<code>import calendar
from datetime import date

# כמה ימים בחודש:
days_in_month = calendar.monthrange(2024, 2)[1]
print(f"בפברואר 2024: {days_in_month} ימים")  # 29 (שנה מעוברת)

# יום בשבוע:
day_of_week = calendar.weekday(2024, 11, 18)
print(day_of_week)  # 0=Monday, 6=Sunday

# הצגת חודש:
print(calendar.month(2024, 11))

# שנה מעוברת?
is_leap = calendar.isleap(2024)
print(f"2024 שנה מעוברת: {is_leap}")</code>

🎯 <b>דוגמאות מעשיות:</b>

<b>1. גיל מדויק:</b>
<code>from datetime import date

def calculate_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year
    
    # בדיקה אם עוד לא היה יום הולדת השנה:
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    
    return age

birthday = date(1998, 5, 15)
age = calculate_age(birthday)
print(f"גיל: {age}")</code>

<b>2. ספירה לאחור לאירוע:</b>
<code>from datetime import datetime, date

def countdown(event_date, event_name):
    today = date.today()
    days_left = (event_date - today).days
    
    if days_left > 0:
        return f"נשארו {days_left} ימים עד {event_name}!"
    elif days_left == 0:
        return f"{event_name} היום!"
    else:
        return f"{event_name} היה לפני {abs(days_left)} ימים"

new_year = date(2025, 1, 1)
print(countdown(new_year, "שנה חדשה"))</code>

<b>3. Log עם timestamp:</b>
<code>from datetime import datetime

def log_message(message, level="INFO"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] [{level}] {message}")

log_message("המערכת התחילה")
log_message("שגיאה בחיבור", "ERROR")</code>

<b>4. בדיקת שעות עבודה:</b>
<code>from datetime import datetime, time

def is_working_hours():
    now = datetime.now().time()
    start = time(9, 0)   # 09:00
    end = time(17, 0)    # 17:00
    
    return start <= now <= end

if is_working_hours():
    print("שעות עבודה - המערכת פעילה")
else:
    print("מחוץ לשעות עבודה")</code>

<b>5. פורמט ידידותי למשתמש:</b>
<code>from datetime import datetime

def format_relative_time(dt):
    now = datetime.now()
    diff = now - dt
    
    seconds = diff.total_seconds()
    
    if seconds < 60:
        return "עכשיו"
    elif seconds < 3600:
        minutes = int(seconds / 60)
        return f"לפני {minutes} דקות"
    elif seconds < 86400:
        hours = int(seconds / 3600)
        return f"לפני {hours} שעות"
    else:
        days = int(seconds / 86400)
        return f"לפני {days} ימים"

post_time = datetime(2024, 11, 17, 10, 0)
print(format_relative_time(post_time))</code>

🔥 <b>פרויקט מיני - תזכורות:</b>
<code>from datetime import datetime, timedelta

class Reminder:
    def __init__(self):
        self.reminders = []
    
    def add_reminder(self, message, when):
        """הוסף תזכורת"""
        self.reminders.append({
            'message': message,
            'time': when,
            'created': datetime.now()
        })
    
    def check_reminders(self):
        """בדוק תזכורות שהגיע זמנן"""
        now = datetime.now()
        due_reminders = []
        
        for reminder in self.reminders:
            if reminder['time'] <= now:
                due_reminders.append(reminder)
        
        # הסר תזכורות שהוצגו:
        for reminder in due_reminders:
            self.reminders.remove(reminder)
        
        return due_reminders

# שימוש:
rm = Reminder()

# תזכורת בעוד 5 שניות:
rm.add_reminder(
    "לבדוק אימיילים",
    datetime.now() + timedelta(seconds=5)
)

# תזכורת מחר בבוקר:
rm.add_reminder(
    "פגישה עם הלקוח",
    datetime.now().replace(hour=9, minute=0) + timedelta(days=1)
)

# בדיקה:
import time
while True:
    due = rm.check_reminders()
    for reminder in due:
        print(f"🔔 תזכורת: {reminder['message']}")
    time.sleep(1)</code>

⚡ <b>טיפים חשובים:</b>

• השתמש ב-datetime ולא ב-time (time מסובך יותר)
• תמיד שמור תאריכים ב-UTC במסד נתונים
• המר לאזור הזמן של המשתמש רק בתצוגה
• זהירות משנים מעוברות וחודשים עם ימים שונים
• השתמש ב-ISO 8601 לפורמט אחיד: YYYY-MM-DD

📚 <b>ספריות נוספות:</b>
• <b>arrow:</b> datetime מודרני וקל יותר
• <b>pendulum:</b> טיפול מתקדם באזורי זמן
• <b>dateutil:</b> פרסור גמיש של תאריכים
''',
        'exercise': {
            'question': """מה יודפס?

from datetime import date

birthday = date(2000, 1, 1)
today = date(2024, 1, 1)
diff = today - birthday

print(diff.days // 365)""",
            'options': ['23', '24', '25', 'שגיאה'],
            'correct_answer': '24',
            'explanation': 'נכון! 🎯 ההפרש הוא 24 שנים בדיוק. diff.days נותן את מספר הימים, וחילוק ב-365 נותן שנים (בערך)'
        }
    },
    
    33: {
        'title': '🎭 שיעור 33: Lambda, Map, Filter, Reduce - פונקציות מתקדמות',
        'content': r'''
בואו נלמד פונקציות חזקות לעיבוד נתונים! 🚀

🎯 <b>Lambda - פונקציות אנונימיות:</b>

<b>מה זה Lambda?</b>
פונקציה קטנה בשורה אחת, בלי שם!

<code># פונקציה רגילה:
def square(x):
    return x ** 2

# אותו דבר עם lambda:
square = lambda x: x ** 2

print(square(5))  # 25</code>

💡 <b>מבנה Lambda:</b>
<code>lambda פרמטרים: ביטוי

# דוגמאות:
add = lambda a, b: a + b
print(add(3, 5))  # 8

multiply = lambda x, y: x * y
print(multiply(4, 6))  # 24

is_even = lambda n: n % 2 == 0
print(is_even(4))  # True

# עם if-else:
max_val = lambda a, b: a if a > b else b
print(max_val(10, 20))  # 20</code>

🗺️ <b>Map - החלת פונקציה על רשימה:</b>

<code># בלי map:
numbers = [1, 2, 3, 4, 5]
squares = []
for n in numbers:
    squares.append(n ** 2)
print(squares)  # [1, 4, 9, 16, 25]

# עם map:
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
print(squares)  # [1, 4, 9, 16, 25]</code>

✨ <b>דוגמאות Map:</b>
<code># המרת מספרים ל-strings:
numbers = [1, 2, 3, 4, 5]
strings = list(map(str, numbers))
print(strings)  # ['1', '2', '3', '4', '5']

# אותיות גדולות:
words = ["hello", "world", "python"]
upper_words = list(map(str.upper, words))
print(upper_words)  # ['HELLO', 'WORLD', 'PYTHON']

# עם כמה רשימות:
nums1 = [1, 2, 3]
nums2 = [10, 20, 30]
sums = list(map(lambda x, y: x + y, nums1, nums2))
print(sums)  # [11, 22, 33]

# חישוב מורכב:
prices = [100, 200, 150]
with_tax = list(map(lambda p: p * 1.17, prices))
print(with_tax)  # [117.0, 234.0, 175.5]</code>

🔍 <b>Filter - סינון רשימה:</b>

<code># בלי filter:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = []
for n in numbers:
    if n % 2 == 0:
        evens.append(n)
print(evens)  # [2, 4, 6, 8, 10]

# עם filter:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6, 8, 10]</code>

✨ <b>דוגמאות Filter:</b>
<code># מספרים חיוביים:
numbers = [-3, -1, 0, 2, 5, -7, 10]
positive = list(filter(lambda x: x > 0, numbers))
print(positive)  # [2, 5, 10]

# מילים ארוכות:
words = ["hi", "hello", "hey", "goodbye"]
long_words = list(filter(lambda w: len(w) > 3, words))
print(long_words)  # ['hello', 'goodbye']

# הסרת None:
data = [1, None, 2, None, 3, None, 4]
clean = list(filter(None, data))
print(clean)  # [1, 2, 3, 4]

# סטודנטים שעברו:
grades = [95, 45, 78, 60, 85, 50]
passed = list(filter(lambda g: g >= 60, grades))
print(passed)  # [95, 78, 60, 85]</code>

🔄 <b>Reduce - צמצום לערך אחד:</b>

<code>from functools import reduce

# סכום:
numbers = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, numbers)
print(total)  # 15

# מכפלה:
product = reduce(lambda x, y: x * y, numbers)
print(product)  # 120

# מקסימום:
numbers = [3, 7, 2, 9, 1]
maximum = reduce(lambda x, y: x if x > y else y, numbers)
print(maximum)  # 9</code>

✨ <b>דוגמאות Reduce:</b>
<code>from functools import reduce

# שרשור strings:
words = ["Hello", " ", "World", "!"]
sentence = reduce(lambda x, y: x + y, words)
print(sentence)  # Hello World!

# מציאת המינימום:
numbers = [5, 2, 9, 1, 7]
minimum = reduce(lambda x, y: x if x < y else y, numbers)
print(minimum)  # 1

# ספירה:
items = ["apple", "banana", "apple", "orange", "apple"]
apple_count = reduce(
    lambda count, item: count + (1 if item == "apple" else 0),
    items,
    0  # ערך התחלתי
)
print(apple_count)  # 3</code>

🔥 <b>שילוב של Map, Filter, Reduce:</b>

<code>from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1. Filter - רק זוגיים
evens = filter(lambda x: x % 2 == 0, numbers)

# 2. Map - ריבוע
squares = map(lambda x: x ** 2, evens)

# 3. Reduce - סכום
result = reduce(lambda x, y: x + y, squares)

print(result)  # 220 (4+16+36+64+100)

# בשורה אחת:
result = reduce(
    lambda x, y: x + y,
    map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers))
)
print(result)  # 220</code>

💪 <b>דוגמאות מעשיות:</b>

<b>1. עיבוד נתוני משתמשים:</b>
<code>users = [
    {"name": "אמיר", "age": 25, "active": True},
    {"name": "דני", "age": 17, "active": False},
    {"name": "יוסי", "age": 30, "active": True},
    {"name": "רונה", "age": 22, "active": True},
]

# משתמשים פעילים בוגרים:
active_adults = list(filter(
    lambda u: u["active"] and u["age"] >= 18,
    users
))

# שמות בלבד:
names = list(map(lambda u: u["name"], active_adults))
print(names)  # ['אמיר', 'יוסי', 'רונה']</code>

<b>2. עיבוד מחירים:</b>
<code>products = [
    {"name": "מחשב", "price": 3000},
    {"name": "עכבר", "price": 50},
    {"name": "מקלדת", "price": 200},
    {"name": "מסך", "price": 1500},
]

# מוצרים עד 1000 ש״ח:
affordable = filter(lambda p: p["price"] <= 1000, products)

# עם מע״מ:
with_tax = map(lambda p: {
    "name": p["name"],
    "price": p["price"] * 1.17
}, affordable)

# סכום כולל:
from functools import reduce
total = reduce(
    lambda sum, p: sum + p["price"],
    with_tax,
    0
)

print(f"סכום: {total:.2f} ש״ח")</code>

<b>3. ניקוי וולידציה:</b>
<code># אימיילים:
emails = [
    "user@example.com",
    "invalid.email",
    "test@test.com",
    "",
    "admin@site.org"
]

# ולידציה:
valid_emails = list(filter(
    lambda e: "@" in e and "." in e.split("@")[1],
    emails
))

# lowercase:
clean_emails = list(map(str.lower, valid_emails))
print(clean_emails)</code>

⚡ <b>Lambda vs List Comprehension:</b>

<code># Map עם Lambda:
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))

# List Comprehension (יותר pythonic):
squares = [x ** 2 for x in numbers]

# Filter עם Lambda:
evens = list(filter(lambda x: x % 2 == 0, numbers))

# List Comprehension:
evens = [x for x in numbers if x % 2 == 0]

# Map + Filter:
even_squares = list(map(
    lambda x: x ** 2,
    filter(lambda x: x % 2 == 0, numbers)
))

# List Comprehension (יותר קריא):
even_squares = [x ** 2 for x in numbers if x % 2 == 0]</code>

💡 <b>מתי להשתמש במה?</b>

<b>Lambda:</b>
✅ פונקציה קטנה וחד-פעמית
✅ כ-argument לפונקציות אחרות
❌ לוגיקה מורכבת (השתמש ב-def)

<b>Map/Filter:</b>
✅ קוד functional
✅ עבודה עם iterators גדולים
❌ כשצריך index
❌ לוגיקה מורכבת

<b>List Comprehension:</b>
✅ יותר pythonic
✅ יותר קריא
✅ מהיר יותר
✅ תומך ב-nested loops

📚 <b>סיכום:</b>
<code># Lambda - פונקציה אנונימית:
f = lambda x: x * 2

# Map - החלה על הכל:
doubled = map(lambda x: x * 2, [1, 2, 3])

# Filter - סינון:
evens = filter(lambda x: x % 2 == 0, [1, 2, 3, 4])

# Reduce - צמצום:
from functools import reduce
sum_all = reduce(lambda x, y: x + y, [1, 2, 3, 4])

# List Comprehension (לעתים קרובות עדיף):
doubled = [x * 2 for x in [1, 2, 3]]
evens = [x for x in [1, 2, 3, 4] if x % 2 == 0]</code>
''',
        'exercise': {
            'question': """מה יודפס?

numbers = [1, 2, 3, 4, 5]
result = list(map(lambda x: x * 2, filter(lambda x: x > 2, numbers)))
print(result)""",
            'options': ['[2, 4, 6, 8, 10]', '[6, 8, 10]', '[3, 4, 5]', '[1, 2, 3]'],
            'correct_answer': '[6, 8, 10]',
            'explanation': 'מעולה! 🎯 filter מחזיר [3,4,5] (גדולים מ-2), ואז map מכפיל ב-2: [6,8,10]'
        }
    },
    
    34: {
        'title': '🔍 שיעור 34: מצא את הבאג! (Find the Bug)',
        'content': r'''
זמן לתרגל מציאת באגים! 🐛🔍

🎯 <b>למה חשוב לדעת למצוא באגים?</b>
80% מזמן המפתח הוא debug! ככל שתהיה טוב יותר במציאת באגים, תהיה מתכנת טוב יותר!

---

<b>🐛 באג #1: רשימה משותפת</b>

<code># הקוד הזה אמור ליצור 3 רשימות ריקות
# אבל... משהו לא עובד!

def create_lists():
    lists = [[]] * 3
    lists[0].append(1)
    print(lists)

create_lists()
# פלט: [[1], [1], [1]]
# ❌ למה כל הרשימות השתנו?!</code>

<b>💡 הבעיה:</b>
[[]] * 3 יוצר 3 הפניות לאותה רשימה!

<b>✅ תיקון:</b>
<code>def create_lists():
    lists = [[] for _ in range(3)]  # יוצר 3 רשימות שונות
    lists[0].append(1)
    print(lists)  # [[1], [], []]</code>

---

<b>🐛 באג #2: לולאה על רשימה משתנה</b>

<code># הקוד הזה אמור להסיר מספרים זוגיים
# אבל... הוא משאיר כמה!

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)

print(numbers)
# פלט: [1, 3, 5, 7, 8]
# ❌ למה 8 נשאר?!</code>

<b>💡 הבעיה:</b>
שינוי רשימה תוך כדי לולאה עליה גורם לדילוג על אלמנטים!

<b>✅ תיקון:</b>
<code>numbers = [1, 2, 3, 4, 5, 6, 7, 8]
numbers = [num for num in numbers if num % 2 != 0]
print(numbers)  # [1, 3, 5, 7]

# או:
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
numbers = list(filter(lambda x: x % 2 != 0, numbers))</code>

---

<b>🐛 באג #3: Mutable Default Argument</b>

<code># פונקציה שמוסיפה פריטים לרשימה
# אבל... הרשימה מתמלאת בפריטים ישנים!

def add_item(item, items=[]):
    items.append(item)
    return items

print(add_item("a"))  # ['a'] ✓
print(add_item("b"))  # ['a', 'b'] ❌ מה?!
print(add_item("c"))  # ['a', 'b', 'c'] ❌❌</code>

<b>💡 הבעיה:</b>
הרשימה הריקה נוצרת פעם אחת בהגדרת הפונקציה, לא בכל קריאה!

<b>✅ תיקון:</b>
<code>def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

print(add_item("a"))  # ['a']
print(add_item("b"))  # ['b']
print(add_item("c"))  # ['c']</code>

---

<b>🐛 באג #4: שכחת return</b>

<code># פונקציה שאמורה לחזיר את הסכום
# אבל... מחזירה None!

def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    # ❌ שכחנו return!

result = calculate_sum([1, 2, 3])
print(result)  # None</code>

<b>✅ תיקון:</b>
<code>def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total  # ✓

result = calculate_sum([1, 2, 3])
print(result)  # 6</code>

---

<b>🐛 באג #5: פסיק חסר</b>

<code># רשימה של tuples
# אבל משהו לא בסדר...

coordinates = [
    (1, 2),
    (3, 4)
    (5, 6)  # ❌ חסר פסיק!
]

# SyntaxError!</code>

<b>✅ תיקון:</b>
<code>coordinates = [
    (1, 2),
    (3, 4),  # ✓
    (5, 6)
]</code>

---

<b>🐛 באג #6: שימוש ב-= במקום ==</b>

<code># בדיקה אם x שווה ל-5
# אבל... x משתנה!

x = 10
if x = 5:  # ❌ השמה במקום השוואה!
    print("x is 5")

# SyntaxError</code>

<b>✅ תיקון:</b>
<code>x = 10
if x == 5:  # ✓ השוואה
    print("x is 5")
else:
    print("x is not 5")</code>

---

<b>🐛 באג #7: אינדקס מחוץ לטווח</b>

<code># גישה לאיבר אחרון
# אבל... קורסת!

my_list = [10, 20, 30]
last = my_list[3]  # ❌ אין אינדקס 3!

# IndexError!</code>

<b>💡 זכור:</b>
רשימה באורך 3 יש לה אינדקסים: 0, 1, 2

<b>✅ תיקון:</b>
<code>my_list = [10, 20, 30]
last = my_list[-1]  # ✓ האיבר האחרון
# או:
last = my_list[2]  # ✓ אינדקס 2</code>

---

<b>🐛 באג #8: שכחת indent</b>

<code># פונקציה שסוכמת מספרים
# אבל... שגיאה!

def sum_numbers(nums):
total = 0  # ❌ אין indent!
for num in nums:
    total += num
return total

# IndentationError!</code>

<b>✅ תיקון:</b>
<code>def sum_numbers(nums):
    total = 0  # ✓
    for num in nums:
        total += num
    return total</code>

---

<b>🐛 באג #9: Type Confusion</b>

<code># חיבור מספר ל-string
# אבל... שגיאה!

age = 25
message = "I am " + age + " years old"  # ❌

# TypeError!</code>

<b>✅ תיקון:</b>
<code>age = 25
message = "I am " + str(age) + " years old"  # ✓
# או:
message = f"I am {age} years old"  # ✓ יותר טוב!</code>

---

<b>🐛 באג #10: חילוק באפס</b>

<code># חישוב ממוצע
# אבל... קורסת על רשימה ריקה!

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

result = calculate_average([])  # ❌ ZeroDivisionError!</code>

<b>✅ תיקון:</b>
<code>def calculate_average(numbers):
    if len(numbers) == 0:
        return 0  # או None, או raise ValueError
    return sum(numbers) / len(numbers)

result = calculate_average([])  # 0</code>

---

🎯 <b>טיפים למציאת באגים:</b>

1. **קרא את הודעת השגיאה בעיון** - היא אומרת לך בדיוק מה הבעיה!
2. **הדפס משתנים** - print(variable) זה הכלי הטוב ביותר
3. **בדוק טיפוסים** - print(type(variable))
4. **פשט את הקוד** - הסר חלקים עד שמצאת את הבעיה
5. **השתמש ב-debugger** - breakpoint() או IDE debugger
6. **חפש ב-Google** - אתה לא הראשון עם הבעיה הזאת!

💪 <b>זכור:</b>
כל מתכנת עושה באגים - ההבדל הוא שמתכנתים טובים יודעים למצוא אותם מהר!
''',
        'exercise': {
            'question': """מצא את הבאג:

def double_items(items=[]):
    for i in range(len(items)):
        items[i] *= 2
    return items

list1 = double_items([1, 2, 3])
list2 = double_items([4, 5, 6])
print(list1, list2)

מה הבעיה?""",
            'options': [
                'לולאה לא נכונה',
                'חסר return',
                'Mutable default argument - הרשימה משותפת',
                'אין בעיה, הקוד תקין'
            ],
            'correct_answer': 'Mutable default argument - הרשימה משותפת',
            'explanation': 'נכון! 🎯 אם נקרא ל-double_items() בלי פרמטר, נשתמש באותה רשימה ריקה. הפתרון: items=None ולבדוק if items is None'
        }
    },
    
    35: {
        'title': '📝 שיעור 35: השלם את הקוד! (Code Completion)',
        'content': r'''
זמן להשלים קוד חסר! ✍️

🎯 <b>למה זה חשוב?</b>
כשאתה כותב קוד, אתה צריך להבין מה חסר ואיך להשלים. זה מפתח חשיבה!

---

<b>📝 תרגיל #1: השלם את הלולאה</b>

<code># הדפס את המספרים מ-1 עד 10

for i in _____(1, 11):
    print(i)</code>

<b>✅ תשובה:</b>
<code>for i in range(1, 11):
    print(i)</code>

---

<b>📝 תרגיל #2: השלם את הפונקציה</b>

<code># פונקציה שמחזירה את המקסימום בין שני מספרים

def get_max(a, b):
    if a > b:
        _____ a
    else:
        _____ b

print(get_max(10, 20))  # צריך להדפיס 20</code>

<b>✅ תשובה:</b>
<code>def get_max(a, b):
    if a > b:
        return a
    else:
        return b</code>

---

<b>📝 תרגיל #3: השלם את המילון</b>

<code># צור מילון של משתמש

user = {
    "name": "אמיר",
    "_____": 25,
    "email": "amir@example.com"
}

print(user["_____"])  # צריך להדפיס 25</code>

<b>✅ תשובה:</b>
<code>user = {
    "name": "אמיר",
    "age": 25,
    "email": "amir@example.com"
}

print(user["age"])</code>

---

<b>📝 תרגיל #4: השלם את try-except</b>

<code># תפוס שגיאת חילוק באפס

try:
    result = 10 / 0
_____ ZeroDivisionError:
    print("לא ניתן לחלק באפס!")</code>

<b>✅ תשובה:</b>
<code>try:
    result = 10 / 0
except ZeroDivisionError:
    print("לא ניתן לחלק באפס!")</code>

---

<b>📝 תרגיל #5: השלם את List Comprehension</b>

<code># צור רשימה של ריבועים של מספרים זוגיים

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [x**2 _____ x _____ numbers _____ x % 2 == 0]
print(squares)  # [4, 16, 36, 64, 100]</code>

<b>✅ תשובה:</b>
<code>squares = [x**2 for x in numbers if x % 2 == 0]</code>

---

<b>📝 תרגיל #6: השלם את הקלאס</b>

<code># קלאס של רכב

class Car:
    def _____(self, brand, year):
        self.brand = brand
        self.year = year
    
    def get_info(self):
        return f"{self.brand} from {self.year}"

my_car = Car("Toyota", 2020)
print(my_car.get_info())</code>

<b>✅ תשובה:</b>
<code>def __init__(self, brand, year):</code>

---

<b>📝 תרגיל #7: השלם את הקריאה לקובץ</b>

<code># קרא קובץ טקסט

_____ open("data.txt", "r") as file:
    content = file._____()
    print(content)</code>

<b>✅ תשובה:</b>
<code>with open("data.txt", "r") as file:
    content = file.read()
    print(content)</code>

---

<b>📝 תרגיל #8: השלם את ה-decorator</b>

<code># decorator שמודפס לפני ואחרי פונקציה

def logger(func):
    def wrapper():
        print("לפני")
        _____()
        print("אחרי")
    return _____

@logger
def say_hello():
    print("שלום!")

say_hello()</code>

<b>✅ תשובה:</b>
<code>def logger(func):
    def wrapper():
        print("לפני")
        func()
        print("אחרי")
    return wrapper</code>

---

<b>📝 תרגיל #9: השלם את הסינון</b>

<code># סנן מספרים גדולים מ-50

numbers = [23, 67, 12, 89, 45, 91, 34]
large_numbers = list(filter(_____ x: x > 50, numbers))
print(large_numbers)  # [67, 89, 91]</code>

<b>✅ תשובה:</b>
<code>large_numbers = list(filter(lambda x: x > 50, numbers))</code>

---

<b>📝 תרגיל #10: השלם את האימות</b>

<code># בדוק אם מספר בין 1 ל-100

def validate_number(num):
    _____ 1 <= num <= 100:
        return True
    _____:
        return False

print(validate_number(50))   # True
print(validate_number(150))  # False</code>

<b>✅ תשובה:</b>
<code>def validate_number(num):
    if 1 <= num <= 100:
        return True
    else:
        return False

# או פשוט:
def validate_number(num):
    return 1 <= num <= 100</code>

---

<b>📝 תרגיל #11: השלם את הלולאה המקוננת</b>

<code># הדפס משולש של כוכבים

for i in _____(1, 6):
    print("*" _____ i)</code>

<b>✅ תשובה:</b>
<code>for i in range(1, 6):
    print("*" * i)

# פלט:
# *
# **
# ***
# ****
# *****</code>

---

<b>📝 תרגיל #12: השלם את הפורמט</b>

<code># הדפס עם פורמט יפה

name = "אמיר"
age = 25
print(_____"שמי {name} ואני בן {age}"))</code>

<b>✅ תשובה:</b>
<code>print(f"שמי {name} ואני בן {age}")</code>

---

<b>📝 תרגיל מאתגר #13: מיון מתקדם</b>

<code># מיין רשימת tuples לפי האיבר השני

data = [(1, 5), (3, 2), (2, 8)]
data.sort(key=_____ x: x[___])
print(data)  # [(3, 2), (1, 5), (2, 8)]</code>

<b>✅ תשובה:</b>
<code>data.sort(key=lambda x: x[1])</code>

---

<b>📝 תרגיל מאתגר #14: List Comprehension מקונן</b>

<code># שטח מטריצה

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num _____ row _____ matrix _____ num _____ row]
print(flat)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]</code>

<b>✅ תשובה:</b>
<code>flat = [num for row in matrix for num in row]</code>

---

<b>📝 תרגיל מאתגר #15: Context Manager</b>

<code># פתיחה בטוחה של קובץ

_____ open("data.txt", "w") _____ file:
    file.write("Hello World!")
# הקובץ נסגר אוטומטית</code>

<b>✅ תשובה:</b>
<code>with open("data.txt", "w") as file:
    file.write("Hello World!")</code>

---

🎯 <b>סיכום - מה למדנו?</b>

• **range()** - ליצירת רצפים
• **return** - להחזרת ערך מפונקציה
• **for...in** - ללולאה על איטרבלים
• **if/else** - לתנאים
• **lambda** - לפונקציות אנונימיות
• **with** - לניהול משאבים
• **f-strings** - לפורמט טקסט
• **try/except** - לטיפול בשגיאות
• **__init__** - לבנאי של קלאס

💡 <b>טיפ:</b>
תרגול הוא המפתח! נסה להשלים קטעי קוד בעצמך לפני שאתה מסתכל על התשובה!
''',
        'exercise': {
            'question': """השלם את הקוד:

numbers = [1, 2, 3, 4, 5]
doubled = [x _____ 2 _____ x _____ numbers]
print(doubled)

מה צריך למלא במקום ה-___?""",
            'options': [
                '* for in',
                '+ for in',
                '* in for',
                '** for in'
            ],
            'correct_answer': '* for in',
            'explanation': 'נכון! 🎯 המבנה הנכון הוא: [x * 2 for x in numbers] - זה list comprehension שמכפיל כל מספר ב-2'
        }
    }
}
