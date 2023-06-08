from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp
from utils.db_api import db_querries as commands
from aiogram.dispatcher.filters import Command
from states import admin_register, turtle_register, admin_get_user_stats
from keyboard.default.users_from_bd import get_users_db
from keyboard.default.turtles_from_bd import get_turtles_db
from keyboard.default.approve_reject import get_action_buttons
from aiogram.types.reply_keyboard import ReplyKeyboardRemove
import traceback
import emoji

@dp.message_handler(Command('users_stats'), chat_type=types.ChatType.PRIVATE)
async def admin_check_user_stat_1(message: types.Message):
    try:
        user = await commands.select_user(message.from_user.id)
        if user == None:
            raise ZeroDivisionError ('Вы не зарегистрированы!')
        if user.role != 'ADMIN':
            raise ZeroDivisionError('Эта команда доступна только администратору!')
        users_list_im = await get_users_db('turtle')
        if users_list_im['keyboard'] == []:
            raise KeyError('Нет пользователей, чьих черепах можно посмотреть!')
        await message.answer('Выберите пользователя', reply_markup=users_list_im)
        await admin_get_user_stats.user.set()
    except (KeyError, ZeroDivisionError) as ex:
        await message.answer(ex, reply_markup=ReplyKeyboardRemove())
    except Exception:
        await message.answer('Возникла ошибка в работе программы!', reply_markup=ReplyKeyboardRemove())

@dp.message_handler(state=admin_get_user_stats.user)
async def admin_check_user_stat_2(message: types.Message, state: FSMContext):
    try:
        await state.finish()
        pnp = int(message.text.split(',')[1][1:])
        crit = await commands.report_user_turtles(pnp)
        await message.answer(crit, reply_markup=ReplyKeyboardRemove())
    except:
        await message.answer('Что-то пошло не так, попробуйте еще раз!',reply_markup=ReplyKeyboardRemove())