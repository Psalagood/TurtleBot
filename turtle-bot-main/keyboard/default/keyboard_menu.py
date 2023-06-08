from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            # KeyboardButton(text="Отправить сомбреро"),
            KeyboardButton(text="Отправить черепаху")
        ],
        [
            KeyboardButton(text="Моя статистика")
        ],
        [
            KeyboardButton(text="Обратная связь")
        ],
        [
            KeyboardButton(text="Админ панель")
        ],
    ],
    resize_keyboard=True
)