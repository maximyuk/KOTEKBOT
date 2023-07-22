from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from data_base import Database

# Головна клавіатура для не зареєстрованих
async def start_all_kb() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()

    keyboard = [
        "Реєстрація 📝",
        "Не зайнята кнопка",
        "Інше 📌",
        "Для абітурієнта 🧑‍💻",
    ]

    for button in keyboard:
        builder.add(KeyboardButton(text=button))

    return builder.adjust(2).as_markup(resize_keyboard=True)


# Головна клавіатура для студентів
async def start_student_kb() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()

    keyboard = [
        "Студент 👨‍🎓",
        "Налаштування ⚙️",
        "Інше 📌",
        "Розклад 📚",
    ]

    for button in keyboard:
        builder.add(KeyboardButton(text=button))

    return builder.adjust(2).as_markup(resize_keyboard=True)

# Головна клавіатура для викладачів
async def start_teacher_kb() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()

    keyboard = [
        "Викладач 👩‍🏫",
        "Налаштування ⚙️",
        "Інше 📌",
        "Розклад 📚",
    ]

    for button in keyboard:
        builder.add(KeyboardButton(text=button))

    return builder.adjust(2).as_markup(resize_keyboard=True)

# Головна клавіатура для адмінів
async def start_admin_kb() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()

    keyboard = [
        "Панель 📁",
        "Адмін 🔑",
        "Інше 📌",
        "Розклад 📚",
    ]

    for button in keyboard:
        builder.add(KeyboardButton(text=button))

    return builder.adjust(2).as_markup(resize_keyboard=True)


# 📌 other
async def other_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    keyboard = [
        "Про бота 🖇",
        "Про мене 👀",
        "Розробка 🧩",
        "Статистика 🧮",
        "Допомога 🛠",
        "Час роботи 📅",
        "Фото кота 🖼",
        "Стікери 👨‍👩‍👧‍👦",
        "Сховати ❌",
        "Донат 🫡",
    ]

    for button in keyboard:
        builder.add(InlineKeyboardButton(text=button, callback_data=button))

    return builder.adjust(2).as_markup(resize_keyboard=True)


# 🧑‍💻 applicant
async def applicant_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    keyboard = [
        "Вступ 📗",
        "Про коледж 🛡",
        "Адреса 📫",
        "Контакти 📘",
        "Реквізити 💳",
        "Офіційний сайт 🌎",
        "Сховати ❌",
        "Спеціальності 📜",
    ]

    for button in keyboard:
        builder.add(InlineKeyboardButton(text=button, callback_data=button))

    return builder.adjust(2).as_markup(resize_keyboard=True)


# Клавіатура розкладу (для зареєстрованих)
async def schedule_kb(user_id: int) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    db = await Database.setup()
    
    keyboard = [
        "Розклад студ. 🧑‍🎓",
        "Розклад викл. 👨‍🏫",
        "Сховати ❌",
    ]

    if await db.student_exists_sql(user_id):
        keyboard.insert(0, "Розклад дзвінків ⌚️")
        keyboard.insert(0, "Розклад пар 👀")
        keyboard.insert(4, "Ч/З тиждень ✏️")

        for button in keyboard:
            builder.add(InlineKeyboardButton(text=button, callback_data=button))

        return builder.adjust(2).as_markup(resize_keyboard=True)

    if await db.teacher_exists_sql(user_id):
        keyboard.insert(0, "Розклад дзвінків ⌛️")
        keyboard.insert(0, "Розклад занять 👀")
        keyboard.insert(4, "Ч/З тиждень ✒️")
        
        for button in keyboard:
            builder.add(InlineKeyboardButton(text=button, callback_data=button))

        return builder.adjust(2).as_markup(resize_keyboard=True)
    
    if await db.admin_exists_sql(user_id):
        keyboard.insert(2, "Ч/З тиждень ✒️")
        keyboard.insert(2, "Розклад дзвінків ⌛️")

        for button in keyboard:
            builder.add(InlineKeyboardButton(text=button, callback_data=button))

        return builder.adjust(2).as_markup(resize_keyboard=True)

