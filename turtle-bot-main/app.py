import time

async def on_startup(dp):

    from loader import db
    from utils.db_api.db_gino import on_startup
    print('Подключение к бд')
    await on_startup(dp)

    #print('Удаление таблиц')
    #await db.gino.drop_all()

    print('Создание таблиц')
    await db.gino.create_all()
    print('Ok!')

    from utils.notify_admins import on_startup_notify
    await on_startup_notify(dp)

    from utils.set_bot_commands import set_default_commands
    await set_default_commands(dp)

    print('Started bot')


if __name__ == "__main__":
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup)