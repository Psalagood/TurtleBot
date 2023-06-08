import traceback
from aiogram.dispatcher import FSMContext
from data.config import admins
from loader import dp
from aiogram.dispatcher.filters import Command
from aiogram import types
from states import start_feedback


@dp.message_handler(Command('feedback'))
async def feedback_start(message: types.Message):
    await message.answer(f'Ты можешь обратиться к администрации.'
                         f'Напиши своё сообщение, и будь уверен, всем насрать на него.')
    await start_feedback.comm.set()


@dp.message_handler(state=start_feedback.comm)
async def feedback_in(message: types.Message, state: FSMContext):
    try:
        await state.update_data(comm=message.text)
        data = await state.get_data()
        feed = 'У вас новое обращение от пользователей!:\n' + data.get("comm")
        await state.finish()
        await message.answer('Сообщение было отправлено, кто знает что с ним сделают. Или с тобой')
        for admin in admins:
            await dp.bot.send_message(chat_id=admin, text=feed)
    except Exception:
        await message.answer('Возникла ошибка, набери админу, спроси ну чо там с деньгами которые ты вложил в капитал прожиточного минимума')




