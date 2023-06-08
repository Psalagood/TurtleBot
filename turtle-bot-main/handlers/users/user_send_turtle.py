from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp
from utils.db_api import db_querries as commands
from aiogram.dispatcher.filters import Command
from states import turtle_add
from keyboard.default.users_from_bd import get_users_db
from aiogram.types.reply_keyboard import ReplyKeyboardRemove
from keyboard.default.critical_turtle import get_critica
import traceback


@dp.message_handler(Command('turtle'))
async def add_turtle_1(message: types.Message):
    '''Вызов запуливания черепахи'''
    try:
        user = await commands.select_user(message.from_user.id)
        if user.status != 'ACTIVE':
            raise ZeroDivisionError('Эта команда вам недоступна - ваш статус отличен от Active')
        users_list_im = await get_users_db('turtle')
        if users_list_im['keyboard'] == []:
            raise KeyError ('Некому запульнуть черепаху!')
        await message.answer('Выбери из списка ниже кому записать черепаху', reply_markup=users_list_im)
        await turtle_add.reciever.set()
    except (ZeroDivisionError, KeyError) as ex:
        await message.answer(ex, reply_markup=ReplyKeyboardRemove())
    except Exception:
        await message.answer('Возникла ошибка, не удалось найти такого пользователя', reply_markup=ReplyKeyboardRemove())


@dp.message_handler(state=turtle_add.reciever)
async def add_turtle_2(message: types.Message, state: FSMContext):
    '''Указываем комментарий, за что назначается черепаха'''
    await state.update_data(reciever=message.text)
    await message.answer("За что назначаем? Напиши комментарий.", reply_markup=ReplyKeyboardRemove())
    await turtle_add.reason.set()


@dp.message_handler(state=turtle_add.reason)
async def add_turtle_3(message: types.Message, state: FSMContext):
    '''Указываем критичность черепахи'''
    await state.update_data(reason=message.text)
    ct_keyboard = await get_critica()
    await message.answer("выбери критичность из списка ниже.", reply_markup=ct_keyboard)
    await turtle_add.crit.set()


@dp.message_handler(state=turtle_add.crit)
async def add_turtle_3(message: types.Message, state: FSMContext):
    '''Обрабатываем и добавляем черепаху'''
    try:
        await state.update_data(crit=message.text)
        data = await state.get_data()
        await state.finish()

        if not any(crit in message.text for crit in ['minor', 'major', 'critical', 'letal', 'fatality']):
            raise ReferenceError ('Уровень критичности не найден!')

        reciever = int(data.get("reciever").split(',')[1][1:])
        if await commands.select_user(reciever) == None:
            raise NameError ('Не удалось найти такого пользователя')
        reason = data.get("reason")
        if len(reason) >= 255:
            raise NameError ('Комментарий слишком длинный, надо не больше 255 символов!')
        crit = data.get("crit")
        turtle_id = await commands.generate_turtle_id()

        if await commands.get_user_role(message.from_user['id']) == 'ADMIN':
            admin_id = message.from_user['id']
            status = 'ACTIVE'
        else:
            admin_id = None
            status = 'WAIT'

        await commands.add_turtle(turtle_id=turtle_id,
            comm=reason,
            weight=crit,
            user_id=reciever,# Кому дали черепаху
            issuer_id=int(message.from_user['id']),# Кто дал черепаху
            admin_id=admin_id,# Кто одобрил/отклонил черепаху
            status=status)

        await message.answer(
            await commands.report_single_turtle(
                turtle_id=turtle_id,
                header='Зарегистрировал черепаху',
                show_reciever=True, show_issuer=False),
            reply_markup=ReplyKeyboardRemove())

        await dp.bot.send_message(
            text = await commands.report_single_turtle(
                turtle_id=turtle_id,
                header='Тебе прилетела черепаха. Её пока не одобрили' \
                        if status != 'ACTIVE' \
                        else 'Админ назначил тебе черепаху',
                show_reciever=False, show_issuer=False),
            chat_id=reciever)

    except (ReferenceError, NameError) as ex:
        await message.answer(ex, reply_markup=ReplyKeyboardRemove())
    except (IndexError, ValueError):
        await message.answer('Не удалось понять, что за пользователь')
    except Exception:
        await message.answer('Что-то пошло не так, создайте черепаху заново', reply_markup=ReplyKeyboardRemove())
        print(traceback.format_exc())
