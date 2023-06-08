import emoji
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

ak = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Пользователи в ожидании')
        ],
        [
            KeyboardButton(text='Согласование черепах'),
            KeyboardButton(text='Согласование сомбрерро')
        ],
        [
            KeyboardButton(text='Общая статистика')
        ],
        [
            KeyboardButton(text='Вернуться назад')
        ]
    ],
    resize_keyboard=True
)