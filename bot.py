# -*- coding: utf-8 -*-
"""
Python Learning Bot - בוט טלגרם ללימוד Python
"""

import logging
import sys
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)


def _ensure_ptb_py313_compatibility():
    """
    python-telegram-bot<=20.7 מפעיל Updater עם שדה פרטי חדש שלא הוגדר ב-__slots__.
    בפייתון 3.13 אין יותר __dict__ אוטומטי למחלקות עם __slots__, ולכן נוצרת AttributeError.
    הפונקציה מוודאת שקיים slot מתאים על-ידי החלפת המחלקה במחלקת משנה תואמת.
    """
    if sys.version_info < (3, 13):
        return

    try:
        import telegram.ext as telegram_ext
        import telegram.ext._applicationbuilder as applicationbuilder_module
        import telegram.ext._updater as updater_module
    except Exception:
        return

    base_updater = updater_module.Updater
    slot_name = "_Updater__polling_cleanup_cb"
    slots = getattr(base_updater, "__slots__", ())

    if isinstance(slots, tuple) and slot_name in slots:
        return

    class _PatchedUpdater(base_updater):  # type: ignore[misc, valid-type]
        __slots__ = (slot_name,)

    _PatchedUpdater.__module__ = base_updater.__module__
    _PatchedUpdater.__name__ = base_updater.__name__
    _PatchedUpdater.__qualname__ = base_updater.__qualname__

    updater_module.Updater = _PatchedUpdater
    telegram_ext.Updater = _PatchedUpdater
    applicationbuilder_module.Updater = _PatchedUpdater
    logging.getLogger(__name__).info(
        "Patched python-telegram-bot Updater for Python 3.13 compatibility."
    )

from config import TELEGRAM_BOT_TOKEN
from database import db
from lessons_combined import get_lesson, get_all_lessons, TOTAL_LESSONS
from keyboards import (
    main_menu_keyboard,
    lesson_menu_keyboard,
    exercise_keyboard,
    continue_learning_keyboard,
    lessons_list_keyboard,
    progress_keyboard
)

# הגדרת logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

_ensure_ptb_py313_compatibility()

# ========== פונקציות עזר ==========

def get_or_create_user(update: Update):
    """קבלת או יצירת משתמש"""
    user = update.effective_user
    user_data = db.get_user(user.id)
    
    if not user_data:
        user_data = db.create_user(
            user_id=user.id,
            username=user.username or "",
            first_name=user.first_name or ""
        )
    
    return user_data

def format_progress_bar(completed, total, length=10):
    """יצירת בר התקדמות"""
    filled = int((completed / total) * length)
    bar = "█" * filled + "░" * (length - filled)
    percentage = int((completed / total) * 100)
    return f"{bar} {percentage}%"

# ========== Command Handlers ==========

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """פקודת /start"""
    user_data = get_or_create_user(update)
    
    welcome_message = f"""
🎉 <b>ברוכים הבאים לבוט ללימוד Python!</b> 🐍

שלום {user_data['first_name']}! 👋

אני כאן כדי ללמד אותך Python מההתחלה ועד רמה מתקדמת!

📚 <b>מה יש לי להציע:</b>
• 20 שיעורים מקיפים
• הסברים ברורים וכיפיים בעברית
• תרגילים אינטראקטיביים
• מעקב אחר ההתקדמות שלך

💡 <b>איך זה עובד?</b>
כל שיעור מכיל הסבר מפורט, דוגמאות קוד, ותרגיל.
אחרי שתפתור את התרגיל, תוכל להמשיך לשיעור הבא!

🚀 <b>בואו נתחיל!</b>
"""
    
    await update.message.reply_text(
        welcome_message,
        reply_markup=main_menu_keyboard(),
        parse_mode='HTML'
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """פקודת /help"""
    help_text = """
❓ <b>עזרה - Python Learning Bot</b>

<b>פקודות זמינות:</b>
/start - התחלה מחדש
/help - הצגת עזרה זו
/progress - הצגת ההתקדמות שלך
/lesson [מספר] - מעבר לשיעור ספציפי

<b>איך להשתמש בבוט?</b>
1. לחץ על "התחל ללמוד" כדי להתחיל
2. קרא את השיעור בעיון
3. פתור את התרגיל
4. עבור לשיעור הבא!

<b>טיפים:</b>
• אפשר לחזור לשיעורים קודמים בכל זמן
• ההתקדמות שלך נשמרת אוטומטית
• אל תמהר - קח את הזמן שלך

💪 בהצלחה בלימוד!
"""
    
    await update.message.reply_text(
        help_text,
        parse_mode='HTML'
    )

async def progress_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """פקודת /progress"""
    user_data = get_or_create_user(update)
    progress = db.get_user_progress(user_data['user_id'])
    
    if not progress:
        await update.message.reply_text("עדיין לא התחלת ללמוד! 📚")
        return
    
    completed = progress['completed_lessons']
    current = progress['current_lesson']
    total_exercises = progress['total_exercises']
    
    progress_bar = format_progress_bar(completed, TOTAL_LESSONS)
    
    progress_text = f"""
📊 <b>ההתקדמות שלך</b>

{progress_bar}

📚 שיעורים שהשלמת: {completed}/{TOTAL_LESSONS}
📖 שיעור נוכחי: {current}
✍️ תרגילים שפתרת: {total_exercises}

{'🎉 כל הכבוד! סיימת את כל השיעורים!' if completed == TOTAL_LESSONS else '💪 המשך ככה!'}
"""
    
    await update.message.reply_text(
        progress_text,
        reply_markup=progress_keyboard(),
        parse_mode='HTML'
    )

async def lesson_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """פקודת /lesson [מספר]"""
    if not context.args:
        await update.message.reply_text("שימוש: /lesson [מספר]\nלדוגמה: /lesson 5")
        return
    
    try:
        lesson_number = int(context.args[0])
        if 1 <= lesson_number <= TOTAL_LESSONS:
            await show_lesson(update, context, lesson_number)
        else:
            await update.message.reply_text(f"שיעור צריך להיות בין 1 ל-{TOTAL_LESSONS}")
    except ValueError:
        await update.message.reply_text("אנא הזן מספר תקין")

# ========== Callback Handlers ==========

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """טיפול בלחיצות על כפתורים"""
    query = update.callback_query
    await query.answer()
    
    data = query.data
    
    # תפריט ראשי
    if data == "main_menu":
        await show_main_menu(query)
    
    # התחל ללמוד
    elif data == "start_learning":
        await start_learning(query, context)
    
    # התקדמות
    elif data == "my_progress":
        await show_progress(query)
    
    # רשימת שיעורים
    elif data == "lessons_list":
        await show_lessons_list(query, page=1)
    
    # דף ברשימת שיעורים
    elif data.startswith("lessons_page_"):
        page = int(data.split("_")[2])
        await show_lessons_list(query, page)
    
    # שיעור ספציפי
    elif data.startswith("lesson_"):
        lesson_number = int(data.split("_")[1])
        await show_lesson_callback(query, context, lesson_number)
    
    # תרגיל
    elif data.startswith("exercise_"):
        lesson_number = int(data.split("_")[1])
        await show_exercise(query, lesson_number)
    
    # תשובה לתרגיל
    elif data.startswith("answer_"):
        parts = data.split("_")
        lesson_number = int(parts[1])
        answer_index = int(parts[2])
        await check_answer(query, context, lesson_number, answer_index)
    
    # דילוג על תרגיל
    elif data.startswith("skip_"):
        lesson_number = int(data.split("_")[1])
        await skip_exercise(query, lesson_number)
    
    # השלמת כל השיעורים
    elif data == "completed_all":
        await show_completion(query)
    
    # עזרה
    elif data == "help":
        await show_help_callback(query)
    
    # התעלמות (למשל, מספר עמוד)
    elif data == "ignore":
        pass

# ========== פונקציות תצוגה ==========

async def show_main_menu(query):
    """הצגת תפריט ראשי"""
    menu_text = """
🏠 <b>תפריט ראשי</b>

בחר מה תרצה לעשות:
"""
    await query.edit_message_text(
        menu_text,
        reply_markup=main_menu_keyboard(),
        parse_mode='HTML'
    )

async def start_learning(query, context):
    """התחלת לימוד"""
    user = query.from_user
    user_data = db.get_user(user.id)
    
    if not user_data:
        user_data = db.create_user(
            user_id=user.id,
            username=user.username or "",
            first_name=user.first_name or ""
        )
    
    current_lesson = user_data.get('current_lesson', 1)
    await show_lesson_callback(query, context, current_lesson)

async def show_progress(query):
    """הצגת התקדמות"""
    user_data = db.get_user(query.from_user.id)
    if not user_data:
        await query.edit_message_text("עדיין לא התחלת ללמוד! 📚")
        return
    
    progress = db.get_user_progress(user_data['user_id'])
    completed = progress['completed_lessons']
    current = progress['current_lesson']
    total_exercises = progress['total_exercises']
    
    progress_bar = format_progress_bar(completed, TOTAL_LESSONS)
    
    progress_text = f"""
📊 <b>ההתקדמות שלך</b>

{progress_bar}

📚 שיעורים שהשלמת: {completed}/{TOTAL_LESSONS}
📖 שיעור נוכחי: {current}
✍️ תרגילים שפתרת: {total_exercises}

{'🎉 כל הכבוד! סיימת את כל השיעורים!' if completed == TOTAL_LESSONS else '💪 המשך ככה!'}
"""
    
    await query.edit_message_text(
        progress_text,
        reply_markup=progress_keyboard(),
        parse_mode='HTML'
    )

async def show_lessons_list(query, page=1):
    """הצגת רשימת שיעורים"""
    all_lessons = get_all_lessons()
    
    list_text = f"""
📖 <b>רשימת שיעורים</b>

סך הכל: {TOTAL_LESSONS} שיעורים

בחר שיעור:
"""
    
    await query.edit_message_text(
        list_text,
        reply_markup=lessons_list_keyboard(all_lessons, page),
        parse_mode='HTML'
    )

async def show_lesson_callback(query, context, lesson_number):
    """הצגת שיעור (מ-callback)"""
    lesson = get_lesson(lesson_number)
    
    if not lesson:
        await query.edit_message_text("שיעור לא נמצא!")
        return
    
    message_text = f"{lesson['title']}\n\n{lesson['content']}"
    
    # חלוקת הודעה אם היא ארוכה מדי
    if len(message_text) > 4000:
        # שלח בשני חלקים
        await query.edit_message_text(
            f"{lesson['title']}\n\n{lesson['content'][:3500]}...",
            reply_markup=lesson_menu_keyboard(lesson_number, TOTAL_LESSONS),
            parse_mode='HTML'
        )
    else:
        await query.edit_message_text(
            message_text,
            reply_markup=lesson_menu_keyboard(lesson_number, TOTAL_LESSONS),
            parse_mode='HTML'
        )

async def show_lesson(update, context, lesson_number):
    """הצגת שיעור (מפקודה)"""
    lesson = get_lesson(lesson_number)
    
    if not lesson:
        await update.message.reply_text("שיעור לא נמצא!")
        return
    
    message_text = f"{lesson['title']}\n\n{lesson['content']}"
    
    await update.message.reply_text(
        message_text,
        reply_markup=lesson_menu_keyboard(lesson_number, TOTAL_LESSONS),
        parse_mode='HTML'
    )

async def show_exercise(query, lesson_number):
    """הצגת תרגיל"""
    lesson = get_lesson(lesson_number)
    
    if not lesson:
        await query.edit_message_text("תרגיל לא נמצא!")
        return
    
    exercise = lesson['exercise']
    
    exercise_text = f"""
✍️ <b>תרגיל - שיעור {lesson_number}</b>

<b>שאלה:</b>
{exercise['question']}

בחר את התשובה הנכונה:
"""
    
    await query.edit_message_text(
        exercise_text,
        reply_markup=exercise_keyboard(lesson_number, exercise['options']),
        parse_mode='HTML'
    )

async def check_answer(query, context, lesson_number, answer_index):
    """בדיקת תשובה"""
    lesson = get_lesson(lesson_number)
    exercise = lesson['exercise']
    
    user_answer = exercise['options'][answer_index]
    correct_answer = exercise['correct_answer']
    is_correct = user_answer == correct_answer
    
    # שמירה במסד נתונים
    user = query.from_user
    db.save_exercise_attempt(user.id, lesson_number, user_answer, is_correct)
    
    if is_correct:
        # תשובה נכונה
        db.update_user_progress(user.id, lesson_number)
        
        result_text = f"""
✅ <b>נכון מאוד!</b> 🎉

{exercise['explanation']}

{'🏆 סיימת את כל השיעורים! כל הכבוד!' if lesson_number == TOTAL_LESSONS else ''}
"""
    else:
        # תשובה שגויה
        result_text = f"""
❌ <b>לא נכון...</b>

התשובה הנכונה היא: <b>{correct_answer}</b>

{exercise['explanation']}

💡 נסה לקרוא שוב את השיעור ולהבין את הנושא טוב יותר!
"""
    
    await query.edit_message_text(
        result_text,
        reply_markup=continue_learning_keyboard(lesson_number, TOTAL_LESSONS),
        parse_mode='HTML'
    )

async def skip_exercise(query, lesson_number):
    """דילוג על תרגיל"""
    skip_text = """
⏭️ <b>דילגת על התרגיל</b>

💡 זכור: כדאי לפתור את התרגילים כדי לוודא שהבנת את החומר!

תוכל תמיד לחזור ולפתור אותו מאוחר יותר.
"""
    
    await query.edit_message_text(
        skip_text,
        reply_markup=continue_learning_keyboard(lesson_number, TOTAL_LESSONS),
        parse_mode='HTML'
    )

async def show_completion(query):
    """הצגת מסך סיום"""
    completion_text = """
🎓 <b>מזל טוב!</b> 🎉

סיימת את כל 20 השיעורים של Python! 🐍

<b>מה למדת:</b>
• יסודות Python
• מבני נתונים
• לולאות ותנאים
• פונקציות ומחלקות
• עבודה עם קבצים
• APIs ו-JSON
• טכניקות מתקדמות

<b>לאן ממשיכים מכאן?</b>
• תבנה פרויקטים משלך
• תלמד ספריות מתקדמות
• תתרגל כל יום
• תצטרף לקהילת Python

<b>זכור:</b> הדרך ללמידה היא ארוכה, אבל התחלת נהדר! 💪

Python הוא רק ההתחלה - העולם כולו מחכה לך! 🚀

תודה שלמדת איתי! ❤️
"""
    
    await query.edit_message_text(
        completion_text,
        reply_markup=main_menu_keyboard(),
        parse_mode='HTML'
    )

async def show_help_callback(query):
    """הצגת עזרה (מ-callback)"""
    help_text = """
❓ <b>עזרה - Python Learning Bot</b>

<b>איך להשתמש בבוט?</b>
1. לחץ על "התחל ללמוד" כדי להתחיל
2. קרא את השיעור בעיון
3. פתור את התרגיל
4. עבור לשיעור הבא!

<b>פקודות זמינות:</b>
/start - התחלה מחדש
/help - הצגת עזרה זו
/progress - הצגת ההתקדמות שלך
/lesson [מספר] - מעבר לשיעור ספציפי

<b>טיפים:</b>
• אפשר לחזור לשיעורים קודמים בכל זמן
• ההתקדמות שלך נשמרת אוטומטית
• אל תמהר - קח את הזמן שלך

💪 בהצלחה בלימוד!
"""
    
    await query.edit_message_text(
        help_text,
        reply_markup=main_menu_keyboard(),
        parse_mode='HTML'
    )

# ========== Error Handler ==========

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """טיפול בשגיאות"""
    logger.error(f"Exception while handling an update: {context.error}")
    
    try:
        if update and update.effective_message:
            await update.effective_message.reply_text(
                "אופס! משהו השתבש 😅\nנסה שוב או צור קשר עם התמיכה."
            )
    except:
        pass

# ========== Main ==========

def main():
    """הרצת הבוט"""
    logger.info("Starting Python Learning Bot...")
    
    # יצירת Application
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    
    # רישום handlers
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("progress", progress_command))
    application.add_handler(CommandHandler("lesson", lesson_command))
    application.add_handler(CallbackQueryHandler(button_callback))
    
    # רישום error handler
    application.add_error_handler(error_handler)
    
    # הרצת הבוט
    logger.info("Bot is running!")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
