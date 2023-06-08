from aiogram import types
from loader import dp
from handlers.users.user_send_turtle import add_turtle_1
from handlers.users.admin.admin_wait_turtle import admin_wait_turtle_1
from handlers.users.admin.admin_wait_user import admin_reg_user_1
from handlers.users.admin.admin_get_stats import admin_check_user_stat_1

# from handlers.users.user_registration import stitistics
from keyboard.default import ak, kb_menu
from handlers.users.user_feedback import feedback_start


@dp.message_handler(text=['Обратная связь'])
async def buttons_feedback(message: types.Message):
    await feedback_start(message)

@dp.message_handler(text=['Отправить черепаху'])
async def buttons_add_turtle(message: types.Message):
    await add_turtle_1(message)

@dp.message_handler(text=['Отправить сомбреро'])
async def buttons_add_like(message: types.Message):
    await message.answer(f'Poka ne gotovo')

@dp.message_handler(text=['Моя статистика'])
async def buttons_statistics(message: types.Message):
    #await stitistics(message)
    pass

@dp.message_handler(text=['Админ панель'])
async def buttons_admin_panel(message: types.Message):
    await message.answer('Меню администраторов.', reply_markup=ak)

@dp.message_handler(text=['Пользователи в ожидании'])
async def buttons_user_wait(message: types.Message):
    await admin_reg_user_1(message)

@dp.message_handler(text=['Согласование черепах'])
async def buttons_approve_turtle(message: types.Message):
    await admin_wait_turtle_1(message)

@dp.message_handler(text=['Согласование сомбрерро'])
async def buttons_approve_sombrerro(message: types.Message):
    # await user_registration_1(message)
    await message.answer('Пока не готово!')

@dp.message_handler(text=['Общая статистика'])
async def buttons_all_user_stat(message: types.Message):
    await admin_check_user_stat_1(message)

@dp.message_handler(text=['Вернуться назад'])
async def buttons_back_to_menu(message: types.Message):
    await message.answer('Главное меню.',reply_markup=kb_menu)

@dp.message_handler(text=['Опротестовать'])
async def buttons_back_to_menu(message: types.Message):
    await message.answer('Пока не готово. Страдай')
