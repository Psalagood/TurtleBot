from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from keyboard.default import kb_menu
from utils.db_api.db_querries import select_all_users
import emoji
from utils.db_api.db_querries import select_all_turtles


async def turtles_list():
    resolt = await select_all_turtles()
    turtles = []
    for turtle in resolt:
        if turtle.status == 'WAIT':
            turtles.append(turtle.return_turtle_id())
    return turtles


async def get_turtles_db():
    turtles_lits_im = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text=f'Дело №{turtle}')] for turtle in await turtles_list()
    ], resize_keyboard=True)
    return turtles_lits_im