# 🐍 Python Learning Bot

בוט טלגרם מקיף ללימוד Python מההתחלה! 🚀

## ✨ תכונות

- 📚 **35 שיעורים מלאים** - מהיסודות ועד רמה מתקדמת
- 🎯 **תרגילים אינטראקטיביים** - אחרי כל שיעור
- 📊 **מעקב התקדמות** - שמירה במונגו של כל ההתקדמות
- 🎨 **ממשק נוח** - מקלדות אינליין מעוצבות
- 🇮🇱 **בעברית** - הסברים ברורים וכיפיים
- 💾 **MongoDB** - מסד נתונים מהיר ואמין

## 📋 נושאי הלימוד

### יסודות (שיעורים 1-5)
- מבוא ל-Python
- הדפסת טקסט (print)
- משתנים
- מספרים וחישובים
- עבודה עם טקסטים (Strings)

### מבני בקרה (שיעורים 6-8)
- תנאים (if/else)
- לולאת while
- לולאת for

### מבני נתונים (שיעורים 9-11)
- רשימות (Lists)
- Tuples ו-Sets
- מילונים (Dictionaries)

### פונקציות וקבצים (שיעורים 12-14)
- פונקציות
- עבודה עם קבצים
- טיפול בשגיאות (Try/Except)

### נושאים מתקדמים (שיעורים 15-20)
- מודולים וספריות
- מחלקות ואובייקטים (OOP)
- ירושה והרחבה
- List Comprehension וגנרטורים
- עבודה עם APIs ו-JSON
- טיפים מתקדמים וסיכום

### מקצוענים מודרניים (שיעורים 21-25)
- Web Scraping ואיסוף נתונים
- ביטויים רגולריים (Regex)
- Async/Await ותכנות אסינכרוני
- בדיקות אוטומטיות (unittest / pytest)
- Type Hints ו-Clean Code

### כלים לעבודה יומיומית (שיעורים 26-30)
- SQL ו-SQLAlchemy
- ממשקים גרפיים (Tkinter)
- סביבות וירטואליות וניהול פרויקטים
- Git ובקרת גרסאות
- פרויקט מסכם: בניית Todo API מלא

### מיומנויות קריטיות (שיעורים 31-35)
- Debugging וקריאת שגיאות
- datetime, calendar ואזורי זמן
- Lambda / Map / Filter / Reduce
- Find the Bug – תיקון קוד קיים
- Code Completion – השלמת קטעי קוד

## 🚀 התקנה והרצה

### דרישות מקדימות

- Python 3.8+
- חשבון MongoDB (Atlas או לוקלי)
- טוקן בוט מ-@BotFather בטלגרם

### שלב 1: שכפול הפרויקט

```bash
git clone <repository-url>
cd python-learning-bot
```

### שלב 2: יצירת סביבה וירטואלית

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### שלב 3: התקנת תלויות

```bash
pip install -r requirements.txt
```

### שלב 4: הגדרת משתני סביבה

צור קובץ `.env` בתיקיית הפרויקט:

```env
TELEGRAM_BOT_TOKEN=your_bot_token_here
MONGODB_URI=your_mongodb_connection_string
DB_NAME=python_learning_bot
```

#### איך לקבל טוקן בוט?

1. פתח את @BotFather בטלגרם
2. שלח `/newbot`
3. בחר שם לבוט
4. העתק את הטוקן שתקבל

#### איך להגדיר MongoDB Atlas?

1. היכנס ל-[MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
2. צור חשבון חינם
3. צור Cluster חדש (Free Tier)
4. לחץ על "Connect" → "Connect your application"
5. העתק את ה-Connection String
6. החלף `<password>` בסיסמה שלך

### שלב 5: הרצה לוקלית

```bash
python bot.py
```

הבוט אמור להיות זמין בטלגרם! 🎉

## 🌐 דפלוי ל-Render

### שלב 1: צור חשבון ב-Render

הירשם ב-[Render.com](https://render.com) (חינם!)

### שלב 2: חבר את הפרויקט

1. לחץ על "New +"
2. בחר "Web Service"
3. חבר את ה-GitHub repository
4. או השתמש בקובץ `render.yaml` שמצורף

### שלב 3: הגדר Environment Variables

בהגדרות ה-Service הוסף:
- `TELEGRAM_BOT_TOKEN`
- `MONGODB_URI`
- `DB_NAME`

### שלב 4: Deploy!

Render יבנה וירוץ את הבוט אוטומטית! 🚀

הבוט ירוץ 24/7 בחינם (עם הגבלות של Free Tier).

## 📁 מבנה הפרויקט

```
python-learning-bot/
│
├── bot.py                    # הבוט הראשי
├── config.py                 # הגדרות
├── database.py               # ניהול MongoDB
├── keyboards.py              # מקלדות טלגרם
│
├── lessons.py                # שיעורים 1-5
├── lessons_part2.py          # שיעורים 6-10
├── lessons_part3.py          # שיעורים 11-15
├── lessons_part4.py          # שיעורים 16-20
├── lessons_part5.py          # שיעורים 21-25
├── lessons_part6.py          # שיעורים 26-30
├── lessons_part7.py          # שיעורים 31-35
├── lessons_combined.py       # איחוד כל השיעורים
│
├── requirements.txt          # תלויות Python
├── .env.example             # דוגמה למשתני סביבה
├── .gitignore               # קבצים להתעלם
├── render.yaml              # הגדרות Render
└── README.md                # הקובץ הזה
```

## 🎮 שימוש בבוט

### פקודות זמינות

- `/start` - התחלת הבוט
- `/help` - הצגת עזרה
- `/progress` - הצגת ההתקדמות שלך
- `/lesson [מספר]` - מעבר לשיעור ספציפי

### דוגמאות שימוש

```
/start              # להתחיל
/lesson 5           # מעבר לשיעור 5
/progress           # בדיקת התקדמות
```

### זרימת הלימוד

1. 🏠 **תפריט ראשי** - בחר "התחל ללמוד"
2. 📖 **קריאת שיעור** - קרא בעיון את החומר
3. ✍️ **פתרון תרגיל** - בדוק את הבנתך
4. ✅ **קבלת משוב** - למד מהטעויות
5. ⏭️ **המשך לשיעור הבא** - המשך לשיעור הבא

## 🛠️ טכנולוגיות

- **Python 3.10+** - שפת התכנות
- **python-telegram-bot 20.7** - ספריית הבוט
- **MongoDB** - מסד נתונים
- **pymongo** - Driver למונגו
- **python-dotenv** - ניהול משתני סביבה

## 📊 מסד הנתונים

### אוספים (Collections)

#### `users`
```json
{
  "user_id": 123456789,
  "username": "username",
  "first_name": "שם",
  "created_at": "2024-01-01T00:00:00",
  "current_lesson": 1,
  "completed_lessons": [1, 2, 3],
  "total_exercises_completed": 3
}
```

#### `progress`
```json
{
  "user_id": 123456789,
  "lesson_number": 1,
  "answer": "תשובה",
  "is_correct": true,
  "timestamp": "2024-01-01T00:00:00"
}
```

## 🔧 פיתוח

### הוספת שיעור חדש

1. פתח את `lessons_part4.py` (או צור חלק 5)
2. הוסף שיעור חדש למילון:

```python
21: {
    'title': '🎯 שיעור 21: נושא חדש',
    'content': """
    תוכן השיעור כאן...
    """,
    'exercise': {
        'question': 'שאלה?',
        'options': ['אפשרות 1', 'אפשרות 2', 'אפשרות 3', 'אפשרות 4'],
        'correct_answer': 'אפשרות 1',
        'explanation': 'הסבר...'
    }
}
```

3. עדכן את `TOTAL_LESSONS` ב-`lessons_combined.py`

### הרצת בדיקות

```bash
# בדיקת תחביר
python -m py_compile bot.py

# הרצה עם debug
python bot.py
```

## 🐛 פתרון בעיות נפוצות

### הבוט לא עונה

1. ✅ בדוק שהטוקן נכון
2. ✅ וודא שהאינטרנט פעיל
3. ✅ בדוק logs לשגיאות

### שגיאת חיבור ל-MongoDB

1. ✅ בדוק את ה-Connection String
2. ✅ וודא שה-IP מורשה ב-Atlas
3. ✅ בדוק שם משתמש וסיסמה

### הבוט נופל אחרי זמן מה

- זה נורמלי ב-Render Free Tier (ישנים אחרי 15 דקות)
- שדרג ל-Paid Plan או השתמש בשירות אחר

## 📝 רישיון

MIT License - חופשי לשימוש!

## 🤝 תרומה

רוצה לתרום? מעולה! 

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 💬 יצירת קשר

יש שאלות? פתח Issue או צור קשר!

## 🎓 קרדיטים

נוצר על ידי אמיר חיים עם ❤️

---

**מזל טוב על הבחירה ללמוד Python! 🐍**

זכור: כל מומחה התחיל כמתחיל. המפתח הוא תרגול קבוע! 💪

**תהנה מהלימוד! 🚀**
