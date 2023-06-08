from aiogram import types
from keyboard.default import kb_menu

from loader import dp

@dp.message_handler(text=["menu", "/menu"])
async def menu(message: types.Message):
    await message.answer('Перейти в главное меню.', reply_markup=kb_menu)

@dp.message_handler(text=['/help'])
async def command_help(message: types.Message):
    all_commands_info = \
'''
/menu - перейти в главное меню
/start - регистрация у бота
/profile - получить информацию из бд о вас
/stats - получить вашу статистику
/delete - удалиться из БД (только со статусом "WAIT" или "REJECTED")
/turtle - отправить черепаху
/info - информация о разрабах
'''
    await message.answer(all_commands_info)

@dp.message_handler(text=['/myInfo', 'myinfo', 'info', 'iam', '/info'])
async def command_start(message: types.Message):
    await message.answer(f'Hola! {message.from_user.full_name}!\n' 
                            f'You ID: {message.from_user.id}\n'
                            #f'You register date: {message.user.created_at}\n'
                            #f'You status: {message.from_user.status}\n'
                         f'\nФункционал бота постоянно дорабатывается'
                         f'\nПо любым вопросам прошу обращаться:\n'
                         f'-Воронко Александр\n'
                         f'-Сережкин Олег\n'
                         f'-Гребенюк Алексей')