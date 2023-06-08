import traceback

from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp
from utils.db_api import db_querries as commands
from aiogram.dispatcher.filters import Command
from states import admin_register
from keyboard.default.users_from_bd import get_users_db
from keyboard.default.approve_reject import get_action_buttons
from aiogram.types.reply_keyboard import ReplyKeyboardRemove

@dp.message_handler(Command('wait_user'), chat_type=types.ChatType.PRIVATE)
async def admin_reg_user_1(message: types.Message):
    '''Одобрить/отклонить регистрацию пользователя'''
    try:
        user = await commands.select_user(message.from_user.id)
        if user == None:
            raise ZeroDivisionError ('Вы не зарегистрированы!')
        if user.role != 'ADMIN':
            raise ZeroDivisionError('Эта команда доступна только администратору!')
        users_list_im = await get_users_db('register')
        if users_list_im['keyboard'] == []:
            raise KeyError('Некого регистрировать!')
        await message.answer('Кого будем регистрировать?', reply_markup=users_list_im)
        await admin_register.user.set()
    except (KeyError, ZeroDivisionError) as ex:
        await message.answer(ex, reply_markup=ReplyKeyboardRemove())
    except Exception:
        await message.answer('Возникла ошибка в работе программы!', reply_markup=ReplyKeyboardRemove())


@dp.message_handler(state=admin_register.user)
async def admin_reg_user_2(message: types.Message, state: FSMContext):
    try:
        answer = int(message.text.split(',')[1][1:])
        pnp = await commands.select_user(answer)
        if pnp == None:
            raise ZeroDivisionError ('Нет такого пользователя!')
        await state.update_data(reg_id=answer)
        await message.answer(f'Telegram ID: {pnp.user_id}\n'
                             f'Имя пользователя: {pnp.username}\n'
                             f'Имя: {pnp.name}\n'
                             f'Фамилия: {pnp.surname}\n',
                             reply_markup=ReplyKeyboardRemove())
        keyboard_actions = await get_action_buttons()
        await message.answer('Что будем делать с пользователем (approve/reject)?', reply_markup=keyboard_actions)
        await admin_register.action.set()
    except ZeroDivisionError as ex:
        await message.answer(ex, reply_markup=ReplyKeyboardRemove())
        await state.finish()
    except Exception:
        await message.answer('Возникла ошибка, не удалось найти такого пользователя', reply_markup=ReplyKeyboardRemove())
        await state.finish()


@dp.message_handler(state=admin_register.action)
async def admin_reg_user_3(message: types.Message, state: FSMContext):
    try:
        await state.update_data(action=message.text)
        data = await state.get_data()
        await state.finish()
        reg_id = data.get("reg_id")
        action = data.get("action")
        pnp = await commands.select_user(reg_id)
        if action == 'Принять':
            await pnp.update(status='ACTIVE').apply()
            await dp.bot.send_message(chat_id=pnp.user_id, text='Тебе поменяли статус, теперь ты зарегистрирован.')
        elif action == 'Отклонить':
            await dp.bot.send_message(
                chat_id=pnp.user_id,
                text=f'Вероятнее всего данные которые ты ввёл не соответствуют действительности\n'
                    f'Админ решил, что ты никто и твоя жизнь ничего не стоит.'
                    f'Вы были удалены из БД. Введиту команду /start. И пройди регистрацию заново.\n'
                    f'В случае проблем обратись к администрации через команду /feedback.\n'
                    f'Обязательно укажи ФИО.')
            await commands.drop_user(pnp)
        elif action == 'Отложить на потом':
            await message.answer('Хатико ждал, и этот подождёт.', reply_markup=ReplyKeyboardRemove())
        else:
            raise ReferenceError ('Не понял, что делать с пользователем. Попробуйте еще раз')

        await message.answer('Статус пользователя изменен!', reply_markup=ReplyKeyboardRemove())
    except ReferenceError as ex:
        await message.answer(ex)
        await state.finish()
    except Exception:
        await message.answer('Возникла ошибка, попробуйте ещё раз', reply_markup=ReplyKeyboardRemove())
        await state.finish()
    finally:
        ReplyKeyboardRemove()