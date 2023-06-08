from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_test = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Comming later"),
            KeyboardButton(text="Comming later")
        ],
        [
            KeyboardButton(text="Comming later"),
            KeyboardButton(text="Comming later")
        ],
        [
            KeyboardButton(text="/start"),
            KeyboardButton(text="/menu"),
            KeyboardButton(text="/help")
        ],
    ],
    resize_keyboard=True
)