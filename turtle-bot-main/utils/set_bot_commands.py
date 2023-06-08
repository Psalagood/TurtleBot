from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand('menu', 'Перейти в главное меню.'),
        types.BotCommand('start', 'Регистрация у бота'),
        types.BotCommand('stats', 'Проверить свою статистику'),
        types.BotCommand('profile', 'Получить информацию о своем профиле'),
        types.BotCommand('info', 'Получить общую информацию о боте'),
        types.BotCommand('help', 'Помощь'),
        # types.BotCommand('turtle', 'Отправить черепаху'),
        # types.BotCommand('wait_user', 'Подтвердить регистрацию пользователя (админ)'),
        # types.BotCommand('wait_turtle', 'Подтвердить черепаху (админ)'),
        # types.BotCommand('delete', 'Удалиться из бота (только для статусов "WAIT" или "REJECTED")')
    ])

