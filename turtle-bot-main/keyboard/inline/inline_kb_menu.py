from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboard.default import kb_menu
import emoji

ikb_menu = InlineKeyboardMarkup(row_width=3,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='Пользователи в ожидании',callback_data='Пользователи в ожидании')
                                    ],
                                    [
                                        InlineKeyboardButton(text='Согласование черепах',callback_data='1')
                                    ],
                                    [
                                        InlineKeyboardButton(text='Согласование сомбрерро',callback_data='poka ne gotovo')
                                    ],
                                    [
                                        InlineKeyboardButton(text='Общая статистика',callback_data='poka ne gotovo')
                                    ]
                                ])
