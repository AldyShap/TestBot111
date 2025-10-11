from aiogram.types import (InlineKeyboardButton,InlineKeyboardMarkup,
                           ReplyKeyboardMarkup, KeyboardButton)

ping_pong = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='ping', callback_data='pong')]
])