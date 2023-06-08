from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp
from utils.db_api import db_querries as commands
from aiogram.dispatcher.filters import Command
from states import start_register
import traceback

@dp.message_handler(Command('start'))
async def user_registration_1(message: types.Message):
    try:
        user = await commands.select_user(message.from_user.id)
        if user:
            raise ZeroDivisionError ("Ты уже зарегистрирован. Проверь себя с помощью /profile")
    except ZeroDivisionError as ex:
        await message.answer(ex)
    except Exception:
        await message.answer("Есть ошибка в работе программы. Обратитесь к администратору")
    else:
        await message.answer("Напиши своё имя")
        await start_register.name.set()


@dp.message_handler(state=start_register.name)
async def user_registragtion_2(message: types.Message, state: FSMContext):
    try:
        await state.update_data(name=message.text)
        await message.answer("Фамилия?")
        await start_register.surname.set()
    except Exception:
        await message.answer("Есть ошибка в работе программы. Обратитесь к администратору")
        return


@dp.message_handler(state=start_register.surname)
async def user_registration_3(message: types.Message, state: FSMContext):
    try:
        await state.update_data(surname=message.text)
        data = await state.get_data()
        await state.finish()
        name = data.get("name")
        surname = data.get("surname")
        await commands.add_user(user_id=message.from_user.id,
                                username=message.from_user.username,
                                status='WAIT',
                                name=name,
                                surname=surname,
                                role='USER')
        await message.answer('Бот занес тебя в БД. Статус - ожидает подтверждения регистрации')
    except Exception:
        await message.answer("Есть ошибка в работе программы. Обратитесь к администратору")
        return