from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

# ♻️ update
async def update_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.add(InlineKeyboardButton(text="⬅️ Назад", callback_data="other_inline"))
    builder.add(InlineKeyboardButton(text="Оновити ♻️", callback_data="Статистика 🧮"))

    return builder.as_markup()