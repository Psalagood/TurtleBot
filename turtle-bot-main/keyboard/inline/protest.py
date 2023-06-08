from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboard.default import kb_menu
import emoji

protest = InlineKeyboardMarkup(row_width=3,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='Опротестовать',callback_data='Пока не готово. Страдай')
                                    ]
                                ])

agree_disagree = InlineKeyboardMarkup(row_width=3,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='Принять',callback_data='Пока не готово')
                                    ],
                                    [
                                        InlineKeyboardButton(text='Отклонить', callback_data='Пока не готово')
                                    ]
                                ])
