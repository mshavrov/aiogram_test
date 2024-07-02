from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='1. Загрузи накладные для работы')],
    [KeyboardButton(text='2. Сборка по накладным'), KeyboardButton(text='3. Собранные накладные')],
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

cars = ['Купчино', 'Звёздная', 'Московская', 'Парк Победы', 'Электросила', 'Московские Ворота', 'Фрунзенская', 'Технологический Институт', 'Садовая', 'Невский Проспект', 'Горьковская', 'Петроградская', 'Черная речка', 'Пионерская', 'Удельная', 'Озерки', 'Проспект Просвящения', 'Парнас']

# Меню внизу
# async def inline_cars():
#     keyboard = ReplyKeyboardBuilder()
#     for car in cars:
#         keyboard.add(KeyboardButton(text=car))
#     return keyboard.adjust(3).as_markup()

# Меню у сообщения
async def inline_cars():
    keyboard = InlineKeyboardBuilder()
    for car in cars:
        keyboard.add(InlineKeyboardButton(text=car, url='https://ya.com'))
    return keyboard.adjust(3).as_markup()