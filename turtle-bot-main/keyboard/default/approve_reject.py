from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


async def get_action_buttons():
    actions = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text=f'{key}')] for key in ['Принять', 'Отклонить', 'Отложить на потом']
    ], resize_keyboard=True)
    return actions