from aiogram import types
from loader import dp
from utils.db_api import db_querries as commands
import traceback

@dp.message_handler(text='/profile')
async def profile(message: types.Message):
    try:
        user = await commands.select_user(message.from_user.id)
        await message.answer(f'ID: {user.user_id}\n'
                             f'Логин телеграмм: - {user.username}\n'
                             f'Статус пользователя: - {user.status}\n'
                             f'Зарегистрирован: - {user.created_at.strftime(format="%d.%m.%Y %H:%M")}\n'
                             f'Имя: - {user.name}\n'
                             f'Фамилия: - {user.surname}\n'
                             f'Роль: - {user.role}\n'
                             )
    except AttributeError:
        await message.answer('Ты не зарегистрирован, введи команду /start')
    except:
        print(traceback.format_exc())

@dp.message_handler(text='/stats')
async def stitistics(message: types.Message):
    try:
        user_message = await commands.report_user_turtles(message.from_user.id)
        await message.answer(user_message)
    except AttributeError:
        await message.answer('Ты не зарегистрирован, введи команду /start')

@dp.message_handler(text='/delete')
async def command_delete(message: types.Message):
    try:
        user = await commands.select_user(message.from_user.id)
        if user.status == 'WAIT':
            await commands.drop_user(user)
            await message.answer('Вы удалились из БД. Зарегистрируйтесь повторно с помощью /start')
        else:
            await message.answer('Удаление со статусом "ACTIVE" не разрешено')
    except AttributeError:
        await message.answer('Ты не зарегистрирован, введи команду /start')