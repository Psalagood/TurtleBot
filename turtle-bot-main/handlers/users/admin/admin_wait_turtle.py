from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp
from utils.db_api import db_querries as commands
from aiogram.dispatcher.filters import Command
from states import turtle_register
from keyboard.default.turtles_from_bd import get_turtles_db
from keyboard.default.approve_reject import get_action_buttons
from aiogram.types.reply_keyboard import ReplyKeyboardRemove
import traceback

@dp.message_handler(Command('wait_turtle'), chat_type=types.ChatType.PRIVATE)
async def admin_wait_turtle_1(message: types.Message):
    try:
        user = await commands.select_user(message.from_user.id)
        if user == None:
            raise ZeroDivisionError ('Вы не зарегистрированы!')
        if user.role != 'ADMIN':
            raise ZeroDivisionError ('Команда доступна только администратору!')
        users_list_im = await get_turtles_db()
        if users_list_im['keyboard'] == []:
            raise KeyError ('Нет черепах в очереди на согласование!')
        await message.answer('Выберете черепаху для согласования', reply_markup=users_list_im)
        await turtle_register.turtle_id.set()
    except (KeyError, ZeroDivisionError) as ex:
        await message.answer(ex, reply_markup=ReplyKeyboardRemove())
    except Exception:
        await message.answer('Возникла ошибка в работе программы!', reply_markup=ReplyKeyboardRemove())



@dp.message_handler(state=turtle_register.turtle_id)
async def admin_wait_turtle_2(message: types.Message, state: FSMContext):
    try:
        answer = int(message.text.split('№')[1])
        await state.update_data(turtle_id=answer)
        await message.answer(
            await commands.report_single_turtle(
                turtle_id=answer,
                header='Описание черепахи:',
                show_issuer=True, show_reciever=True))
        # ReplyKeyboardRemove()
        keyboard_actions = await get_action_buttons()
        await message.answer('Что будем делать с черепахой (approve/reject)?', reply_markup=keyboard_actions)
        await turtle_register.action.set()
    except (IndexError, ValueError):
        await message.answer('Не удалось определить черепаху!', reply_markup=ReplyKeyboardRemove())
        await state.finish()
    except:
        await message.answer('Возникла ошибка в работе программы!', reply_markup=ReplyKeyboardRemove())
        await state.finish()
        print(traceback.format_exc())
        # await state.finish()

@dp.message_handler(state=turtle_register.action)
async def admin_wait_turtle_3(message: types.Message, state: FSMContext):
    try:
        await state.update_data(action=message.text)
        data = await state.get_data()
        await state.finish()
        reg_id = data.get("turtle_id")
        action = data.get("action")
        admin = await commands.select_user(int(message.from_user.id))
        turtle = await commands.select_turtle(reg_id)

        if action == 'Принять':
            await turtle.update(status='ACTIVE', admin_id=admin.user_id).apply()
            await dp.bot.send_message(
                text=await commands.report_single_turtle(
                    turtle_id=turtle.turtle_id,
                    header='Назначенную тебе черепаху одобрили!',
                    show_reciever=False, show_issuer=False),
                chat_id=turtle.user_id)

        elif action == 'Отклонить':
            await turtle.update(status='REJECTED', admin_id=admin.user_id).apply()
            await dp.bot.send_message(
                text=await commands.report_single_turtle(
                    turtle_id=turtle.turtle_id,
                    header='Назначенную тебе черепаху отклонили!',
                    show_reciever=False, show_issuer=False),
                chat_id=turtle.user_id)

        elif action == 'Отложить на потом':
            await message.answer('Черепаха еще закроет это дело, но потом.', reply_markup=ReplyKeyboardRemove())
            return
        else:
            raise ReferenceError ('Не понял, что делать с черепахой. Попробуйте еще раз')

        await message.answer('Статус черепахи изменен!', reply_markup=ReplyKeyboardRemove())

    except ReferenceError as ex:
        await message.answer(ex, reply_markup=ReplyKeyboardRemove())
        await state.finish()
    except:
        await message.answer('Возникла ошибка, не удалось обработать. Попробуйте еще раз', reply_markup=ReplyKeyboardRemove())
        await state.finish()