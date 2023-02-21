from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from data_base.controller_db import *



#KeyboardButton - створює одну кнопку
#ReplyKeyboardMarkup - створює клавіатуру
#ReplyKeyboardRemove - видаляє клавіатуру 



#===========================1 Keyboards================================
def get_kb():
    h = kb_user_reg.get()
    kb_course = ReplyKeyboardMarkup(resize_keyboard=True) 
    for i in range(0,len(h)):
        kb_course.insert(h[i])
    return kb_course.add(KeyboardButton("Назад"))
#======================================================================



#===========================2 Keyboards================================
kb1 = KeyboardButton("Розклад пар 🥱")
kb2 = KeyboardButton("Розклад дзвінків ⌚️")
kb3 = KeyboardButton("Ч/З 🤨")
kb4 = KeyboardButton("Переєструватись 🤨")
kb5 = KeyboardButton("Меню 👥")

kb_client = ReplyKeyboardMarkup(resize_keyboard=True).row(kb1, kb2).row(kb5, kb3).add(kb4)
#======================================================================


    

