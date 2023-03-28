from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


# KeyboardButton - створює одну кнопку
# ReplyKeyboardMarkup - створює клавіатуру
# ReplyKeyboardRemove - видаляє клавіатуру
# ReplyKeyboardMarkup створення клавіатури + адаптування resize_keyboard=True
# one_time_keyboard = True


# ===========================1 Keyboards============================
reg = KeyboardButton("Реєстрація ⚙️")
stikers = KeyboardButton("Стікери 👨‍👩‍👧‍👦")
applicant = KeyboardButton("Для абітурієнта 🧑‍💻")
others = KeyboardButton("Інше 📌")

kb_start = ReplyKeyboardMarkup(resize_keyboard=True)
kb_start.row(reg, stikers).row(others, applicant)
# ===========================2 Keyboards============================
reg = KeyboardButton("Розклад ⚙️")
stikers = KeyboardButton("Стікери 👨‍👩‍👧‍👦")
applicant = KeyboardButton("Для абітурієнта 🧑‍💻")
others = KeyboardButton("Інше 📌")

kb_start_user = ReplyKeyboardMarkup(resize_keyboard=True)
kb_start_user.row(reg, stikers).row(others, applicant)
# ===========================3 Keyboards============================
# ADMIN 1 reg
reg = KeyboardButton("Розклад ⚙️")
admin = KeyboardButton("Адмін 🔑")
stikers = KeyboardButton("Стікери 👨‍👩‍👧‍👦")
others = KeyboardButton("Інше 📌")
applicant = KeyboardButton("Для абітурієнта 🧑‍💻")

kb_start_admin = ReplyKeyboardMarkup(resize_keyboard=True)
kb_start_admin.row(reg, admin).row(others, stikers).add(applicant)
# ===========================4 Keyboards============================
about_author = KeyboardButton("Про бота 🖇")
commandsk = KeyboardButton("Донат 🫡")
helPa = KeyboardButton("Допомога 🛠")
time_work = KeyboardButton("Час роботи 📅")
addres = KeyboardButton("Адреса 📫")
menu = KeyboardButton("Меню 👥")
stats = KeyboardButton("Статистика 🧮")

kb_infs = ReplyKeyboardMarkup(resize_keyboard=True)
kb_infs.row(about_author, helPa).add(stats).row(addres, time_work).row(menu, commandsk)
# ===========================5 Keyboards============================
introduction = KeyboardButton("Вступ 📗")
specialty = KeyboardButton("Спеціальності 📜")
about_collage = KeyboardButton("Про коледж 🛡")
menu1 = KeyboardButton("Меню 👥")

kb_for_applicant = ReplyKeyboardMarkup(resize_keyboard=True)
kb_for_applicant.row(introduction, about_collage).row(menu1, specialty)
# ===========================6 Keyboards============================
spec012 = KeyboardButton("Дошкільна освіта")
spec013 = KeyboardButton("Початкова освіта")
spec014 = KeyboardButton("Трудове навчання")
spec014_12 = KeyboardButton("Образотворче 🎨")
spec015_39 = KeyboardButton("Цифрові технології")
spec029 = KeyboardButton("Діловодство")
back = KeyboardButton("🔙 Назад")

kb_speciality = ReplyKeyboardMarkup(resize_keyboard=True)
kb_speciality.add(spec012).insert(spec013).add(spec014).insert(spec015_39).row(
    spec014_12, spec029
).add(back)
