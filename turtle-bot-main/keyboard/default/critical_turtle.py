from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


async def get_critica():
    ct_keyboard = ReplyKeyboardMarkup(
            keyboard = [
                [
                    KeyboardButton(text=f'(minor) Дать фофан'),
                    KeyboardButton(text=f'(major) Пробить фанеру'),
                ],
                [KeyboardButton(text=f'(critical) Батин лещ')],
                [KeyboardButton(text=f'(letal) Разбить пакет с мусором об голову')],
                [KeyboardButton(text=f'(fatality) Посадить обновлять кубер')]
            ],
        resize_keyboard=True)
    return ct_keyboard
