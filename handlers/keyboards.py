from aiogram.types import (ReplyKeyboardMarkup,
                           KeyboardButton,
                           InlineKeyboardMarkup,
                           InlineKeyboardButton)


reply_keyboard = ReplyKeyboardMarkup(
    keyboard=[
    [KeyboardButton(text="Старт")],
    [KeyboardButton(text="Помощь"), KeyboardButton(text="Меню")]
])

inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
    [InlineKeyboardButton(text="О нас", callback_data="about")]
    ])