from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from keyboard.default import kb_menu
from utils.db_api.db_querries import select_all_users
import emoji
from utils.db_api.db_querries import select_all_users


async def users_list(type):
    resolt = await select_all_users()
    users = []
    for user in resolt:
        if type == 'register' and user.status == 'WAIT':
            users.append(user.return_user_id())
        elif type == 'turtle' and user.status == 'ACTIVE':
            users.append(user.return_user_id())
    return users


async def get_users_db(type):
    users_lits_im = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text=f'{user[0]} {user[1]}, {user[2]}')] for user in await users_list(type)
    ], resize_keyboard=True)
    return users_lits_im

