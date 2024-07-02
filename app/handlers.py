from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

import app.keyboards as kb

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    # здороваемся, узнаем сразу ID и первое имя
    await message.reply(f'Банжорно. \nТвой ID: {message.from_user.id}\nИмя: {message.from_user.first_name}',
                        reply_markup=await kb.inline_cars())
    
@router.message(Command('down_list'))
async def get_help(message: Message):
    await message.answer('Загружаем список накладных!)))')

@router.message(Command('redy_list'))
async def get_help(message: Message):
    await message.answer('Список собранных накладных!)))')

@router.message(F.text == 'Обед')
async def get_otdjh(message: Message):
    await message.answer('Рано отдыхать - работай!!!)))')

@router.message(F.photo)
async def get_photo(message: Message):
    await message.answer(f'ID фото {message.photo[-1].file_id}')