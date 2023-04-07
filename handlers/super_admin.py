# import
import asyncio

# from import
from aiogram import types
from aiogram.dispatcher import Dispatcher
from aiogram.utils.exceptions import MessageIsTooLong
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards import *
from data_base.controller_db import *
from config import super_admin_admin, super_admin_ura
from create_bot import bot
from handlers.reg import passwords


class FSMSuperA(StatesGroup):
    group = State()
    id_student = State()
    id_teachers = State()
    id_student_delete = State()
    id_teachers_delete = State()


# ===========================Список груп============================
# Клавіаура адміна
async def admin_kb(msg: types.Message):
    if (
        await admin_exists_sql(msg.from_user.id)
        or msg.from_user.id == super_admin_admin
        or msg.from_user.id == super_admin_ura
    ):
        await msg.answer("Клавіатура адміна", reply_markup=kb_admin)


# Клавіаура власника
async def super_admin_kb(msg: types.Message):
    if msg.from_user.id == super_admin_admin or msg.from_user.id == super_admin_ura:
        await msg.answer("Клавіатура власника", reply_markup=sadmin)


# Клавіаура користувача
async def user_kb(msg: types.Message):
    if (
        await user_exists_sql(msg.from_user.id)
        or msg.from_user.id == super_admin_admin
        or msg.from_user.id == super_admin_ura
    ):
        await msg.answer("Клавіатура юзера", reply_markup=kb_client)


# Показати таблицю користувачів
async def super_admin_user(msg: types.Message):
    if msg.from_user.id == super_admin_admin or msg.from_user.id == super_admin_ura:
        try:
            booled = await user_all_sql()
            if booled:
                await msg.answer("Немає користувачів")
            elif not booled:
                spisok = list_all_user.get()
                await msg.answer(spisok)
        except MessageIsTooLong:
            for x in range(0, len(spisok), 4096):
                await bot.send_message(msg.chat.id, spisok[x : x + 4096])
    else:
        dels = await msg.answer("У тебе немає прав, для перегляду бази данних")
        await asyncio.sleep(4)
        await msg.delete()
        await dels.delete()


# Показати таблицю викладачів
async def super_admin_teach(msg: types.Message):
    if msg.from_user.id == super_admin_admin or msg.from_user.id == super_admin_ura:
        try:
            booled = await teach_all_sql()
            if booled:
                await msg.answer("Немає користувачів")
            elif not booled:
                spisok = list_all_teach.get()
                await msg.answer(spisok)
        except MessageIsTooLong:
            for x in range(0, len(spisok), 4096):
                await bot.send_message(msg.chat.id, spisok[x : x + 4096])
    else:
        dels = await msg.answer("У тебе немає прав, для перегляду бази данних")
        await asyncio.sleep(4)
        await msg.delete()
        await dels.delete()


# Показати користувачів за групою
async def super_admin_user_for_group(msg: types.Message, state: FSMContext):
    if msg.from_user.id == super_admin_admin or msg.from_user.id == super_admin_ura:
        await msg.answer(
            "Введіть групу для перегляду таблиці за цією групою",
            reply_markup=await get_kb(),
        )
        await FSMSuperA.group.set()
    else:
        dels = await msg.answer("У тебе немає прав, для перегляду бази данних")
        await asyncio.sleep(4)
        await msg.delete()
        await dels.delete()


async def super_admin_user_for_group1(msg: types.Message, state: FSMContext):
    if msg.from_user.id == super_admin_admin or msg.from_user.id == super_admin_ura:
        if msg.text == "Назад":
            await msg.answer("Меню", reply_markup=sadmin)
            await state.finish()
        else:
            if await group_exists_sql(msg.text):
                try:
                    booled = await user_for_group_sql(msg.text)
                    if booled:
                        await msg.answer("Немає користувачів", reply_markup=sadmin)
                        await state.finish()
                    elif not booled:
                        spisok = list_all_user_for_group.get()
                        await msg.answer(spisok)
                        await msg.answer("Done!", reply_markup=sadmin)
                        await state.finish()
                except MessageIsTooLong:
                    for x in range(0, len(spisok), 4096):
                        await bot.send_message(msg.chat.id, spisok[x : x + 4096])
                        await msg.answer("Done!", reply_markup=sadmin)
                        await state.finish()
            else:
                await state.finish()
                dels = await msg.answer(
                    "☹️ Немає такої групи, звяжіться з адміністратором",
                    reply_markup=sadmin,
                )
                await asyncio.sleep(4)
                await msg.delete()
                await dels.delete()
    else:
        dels = await msg.answer("У тебе немає прав, для перегляду бази данних")
        await asyncio.sleep(4)
        await msg.delete()
        await dels.delete()


# ====================================


# Показати таблицю груп
async def super_admin_groupa(msg: types.Message):
    if msg.from_user.id == super_admin_admin or msg.from_user.id == super_admin_ura:
        try:
            booled = await groupa_all_sql()
            if booled:
                await msg.answer("Немає груп")
            elif not booled:
                spisok = list_all_groupa.get()
                await msg.answer(spisok)
        except MessageIsTooLong:
            for x in range(0, len(spisok), 4096):
                await bot.send_message(msg.chat.id, spisok[x : x + 4096])
    else:
        dels = await msg.answer("У тебе немає прав, для перегляду бази данних")
        await asyncio.sleep(4)
        await msg.delete()
        await dels.delete()


# Показати таблицю адмінів
async def super_admin_admins(msg: types.Message):
    if msg.from_user.id == super_admin_admin or msg.from_user.id == super_admin_ura:
        booled = await admin_all_sql()
        if booled:
            await msg.answer("Немає адмінів")
        elif not booled:
            spisok = list_all_admin.get()
            await msg.answer(spisok)
    else:
        dels = await msg.answer("У тебе немає прав, для перегляду бази данних")
        await asyncio.sleep(4)
        await msg.delete()
        await dels.delete()


# ========================================================================================


# Показати студента за id
async def super_admin_user_for_id(msg: types.Message, state: FSMContext):
    if msg.from_user.id == super_admin_admin or msg.from_user.id == super_admin_ura:
        await msg.answer("Введіть ID студента")
        await FSMSuperA.id_student.set()
    else:
        dels = await msg.answer("У тебе немає прав, для перегляду бази данних")
        await asyncio.sleep(4)
        await msg.delete()
        await dels.delete()


async def super_admin_user_for_id1(msg: types.Message, state: FSMContext):
    if msg.from_user.id == super_admin_admin or msg.from_user.id == super_admin_ura:
        try:
            booled, text = await studen_for_id_sql(msg.text)
            if booled:
                await msg.answer("Немає студента")
                await state.finish()
            elif not booled:
                await msg.answer(text)
                await msg.answer("Done!")
                await state.finish()
        except MessageIsTooLong:
            for x in range(0, len(text), 4096):
                await bot.send_message(msg.chat.id, text[x : x + 4096])
                await msg.answer("Done!")
                await state.finish()
    else:
        dels = await msg.answer("У тебе немає прав, для перегляду бази данних")
        await asyncio.sleep(4)
        await msg.delete()
        await dels.delete()


# Показати викладача за id
async def super_admin_teach_for_id(msg: types.Message, state: FSMContext):
    if msg.from_user.id == super_admin_admin or msg.from_user.id == super_admin_ura:
        await msg.answer("Введіть ID викладача")
        await FSMSuperA.id_teachers.set()
    else:
        dels = await msg.answer("У тебе немає прав, для перегляду бази данних")
        await asyncio.sleep(4)
        await msg.delete()
        await dels.delete()


async def super_admin_teach_for_id1(msg: types.Message, state: FSMContext):
    if msg.from_user.id == super_admin_admin or msg.from_user.id == super_admin_ura:
        try:
            booled, text = await teach_for_id_sql(msg.text)
            if booled:
                await msg.answer("Немає викладача")
                await state.finish()
            elif not booled:
                await msg.answer(text)
                await msg.answer("Done!")
                await state.finish()
        except MessageIsTooLong:
            for x in range(0, len(text), 4096):
                await bot.send_message(msg.chat.id, text[x : x + 4096])
                await msg.answer("Done!")
                await state.finish()
    else:
        dels = await msg.answer("У тебе немає прав, для перегляду бази данних")
        await asyncio.sleep(4)
        await msg.delete()
        await dels.delete()


# Видалити користувача за id
async def super_admin_delete_user(msg: types.Message, state: FSMContext):
    if msg.from_user.id == super_admin_admin or msg.from_user.id == super_admin_ura:
        await msg.answer("Введіть ID студента")
        await FSMSuperA.id_student_delete.set()
    else:
        dels = await msg.answer("У тебе немає прав, для перегляду бази данних")
        await asyncio.sleep(4)
        await msg.delete()
        await dels.delete()


async def super_admin_delete_user1(msg: types.Message, state: FSMContext):
    if msg.from_user.id == super_admin_admin or msg.from_user.id == super_admin_ura:
        exits = await user_exists_sql(msg.text)
        if exits:
            await delete_teach_for_id_sql(msg.text)
            await msg.answer("Студента видаленно")
            await state.finish()
        elif not exits:
            await msg.answer("Немає користувача з таким ID")
            await state.finish()
    else:
        dels = await msg.answer("У тебе немає прав, для перегляду бази данних")
        await asyncio.sleep(4)
        await msg.delete()
        await dels.delete()


# Видалити викладача за id
async def super_admin_delete_teach(msg: types.Message, state: FSMContext):
    if msg.from_user.id == super_admin_admin or msg.from_user.id == super_admin_ura:
        await msg.answer("Введіть ID викладача")
        await FSMSuperA.id_student_delete.set()
    else:
        dels = await msg.answer("У тебе немає прав, для перегляду бази данних")
        await asyncio.sleep(4)
        await msg.delete()
        await dels.delete()


async def super_admin_delete_teach1(msg: types.Message, state: FSMContext):
    if msg.from_user.id == super_admin_admin or msg.from_user.id == super_admin_ura:
        exits = await teachers_exists_sql(msg.text)
        if exits:
            await delete_teach_for_id_sql(msg.text)
            await msg.answer("Викладача видаленно")
            await state.finish()
        elif not exits:
            await msg.answer("Немає користувача з таким ID")
            await state.finish()
    else:
        dels = await msg.answer("У тебе немає прав, для перегляду бази данних")
        await asyncio.sleep(4)
        await msg.delete()
        await dels.delete()


async def password(msg: types.Message):
    if msg.from_user.id == super_admin_admin or msg.from_user.id == super_admin_ura:
        await msg.answer(f"PASSWORD : {passwords}")
    else:
        dels = await msg.answer("У тебе немає прав, для перегляду бази данних")
        await asyncio.sleep(4)
        await msg.delete()
        await dels.delete()


async def update_db(msg: types.Message):
    if msg.from_user.id == super_admin_admin:
        await update_user_db_sql()


# ===========================реєстратор============================
def register_handler_sadmin(dp: Dispatcher):
    dp.register_message_handler(password, text="p")
    dp.register_message_handler(update_db, text="update")
    dp.register_message_handler(admin_kb, text="Адмін 🔑")
    dp.register_message_handler(super_admin_kb, text="власник")
    dp.register_message_handler(user_kb, text="студент")
    dp.register_message_handler(super_admin_user, text="таблиця студентів")
    dp.register_message_handler(super_admin_teach, text="таблиця викладачів")
    dp.register_message_handler(super_admin_groupa, text="таблиця групи")
    dp.register_message_handler(super_admin_admins, text="таблиця адмінів")

    dp.register_message_handler(
        super_admin_user_for_group, text="таблиця за групою", state=None
    )
    dp.register_message_handler(super_admin_user_for_group1, state=FSMSuperA.group)

    dp.register_message_handler(
        super_admin_user_for_id, text="Студент за ID", state=None
    )
    dp.register_message_handler(super_admin_user_for_id1, state=FSMSuperA.id_student)

    dp.register_message_handler(
        super_admin_teach_for_id, text="Викладач за ID", state=None
    )
    dp.register_message_handler(super_admin_teach_for_id1, state=FSMSuperA.id_teachers)

    dp.register_message_handler(
        super_admin_delete_user, text="Видалити студента", state=None
    )
    dp.register_message_handler(
        super_admin_delete_user1, state=FSMSuperA.id_student_delete
    )

    dp.register_message_handler(
        super_admin_delete_teach1, text="Видалити викладача", state=None
    )
    dp.register_message_handler(
        super_admin_delete_teach1, state=FSMSuperA.id_teachers_delete
    )
