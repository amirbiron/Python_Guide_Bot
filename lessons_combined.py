# -*- coding: utf-8 -*-
"""
כל השיעורים במקום אחד - 30 שיעורים מלאים ללימוד Python
"""

from lessons import LESSONS
from lessons_part2 import LESSONS_PART2
from lessons_part3 import LESSONS_PART3
from lessons_part4 import LESSONS_PART4
from lessons_part5 import LESSONS_PART5
from lessons_part6 import LESSONS_PART6

# איחוד כל השיעורים למילון אחד
ALL_LESSONS = {}
ALL_LESSONS.update(LESSONS)          # שיעורים 1-5
ALL_LESSONS.update(LESSONS_PART2)    # שיעורים 6-10
ALL_LESSONS.update(LESSONS_PART3)    # שיעורים 11-15
ALL_LESSONS.update(LESSONS_PART4)    # שיעורים 16-20
ALL_LESSONS.update(LESSONS_PART5)    # שיעורים 21-25
ALL_LESSONS.update(LESSONS_PART6)    # שיעורים 26-30

# סה"כ שיעורים
TOTAL_LESSONS = len(ALL_LESSONS)

def get_lesson(lesson_number):
    """מחזיר שיעור לפי מספר"""
    return ALL_LESSONS.get(lesson_number)

def get_all_lessons():
    """מחזיר את כל השיעורים"""
    return ALL_LESSONS

def get_lesson_titles():
    """מחזיר רשימת כותרות כל השיעורים"""
    return [lesson['title'] for lesson in ALL_LESSONS.values()]
