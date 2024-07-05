from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

# Обычная клавиатура 
# main = ReplyKeyboardMarkup(keyboard=[
#     [KeyboardButton(text='1. Загрузи накладные для работы')],
#     [KeyboardButton(text='2. Сборка по накладным'), KeyboardButton(text='3. Собранные накладные')],
# ],
#                            resize_keyboard=True,
#                            input_field_placeholder='Жмакни одну из клавиш')

# Клавиатура с callback
main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Загрузи накладные для работы', callback_data='down_list')],
    [InlineKeyboardButton(text='Сборка по накладным', callback_data='nakladnaya'), InlineKeyboardButton(text='Собранные накладные', callback_data='redy_list')],
],
                           resize_keyboard=True,
                           input_field_placeholder='Жмакни одну из клавиш')


settings = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='YA_COM', url='https://ya.com')],
    
    [InlineKeyboardButton(text='YA_COM', url='https://ya.com'), InlineKeyboardButton(text='YA_RU', url='https://ya.ru')],   
        
    [InlineKeyboardButton(text='YA_COM', url='https://ya.com'), InlineKeyboardButton(text='YA_RU', url='https://ya.ru'), 
     InlineKeyboardButton(text='YA_YA', url='https://yandex.ru')],   
        
    [InlineKeyboardButton(text='YA_COM', url='https://ya.com'), InlineKeyboardButton(text='YA_RU', url='https://ya.ru'), 
    InlineKeyboardButton(text='YA_YA', url='https://yandex.ru'), InlineKeyboardButton(text='YA_RU', url='https://ya.ru')]
    ])

# cars 
orders = ['0юГЛ-011339', '0юГЛ-011340', '0юГЛ-011341', '0юГЛ-011342', '0юГЛ-011343', '0юГЛ-011344', '0юГЛ-011345', '0юГЛ-011346', '0юГЛ-011347', '0юГЛ-011348', '0юГЛ-011349', '0юГЛ-011350', '0юГЛ-011351', '0юГЛ-011352', '0юГЛ-011353', '0юГЛ-011354', '0юГЛ-011355', '0юГЛ-011356', '0юГЛ-011357', '0юГЛ-011358', '0юГЛ-011359', '0юГЛ-011360', '0юГЛ-011361', '0юГЛ-011362', '0юГЛ-011363', '0юГЛ-011364', '0юГЛ-011365', '0юГЛ-011366', '0юГЛ-011367', '0юГЛ-011368', ]

# Меню внизу
# async def inline_cars():
#     keyboard = ReplyKeyboardBuilder()
#     for car in cars:
#         keyboard.add(KeyboardButton(text=car))
#     return keyboard.adjust(3).as_markup()

# Меню у сообщения
# async def inline_cars():
async def inline_orders():
    keyboard = InlineKeyboardBuilder()
    for order in orders:
        keyboard.add(InlineKeyboardButton(text=order, url='https://ya.com'))
    return keyboard.adjust(1).as_markup()