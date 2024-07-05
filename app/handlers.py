from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

import app.keyboards as kb

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    # здороваемся, узнаем сразу ID и первое имя
    await message.reply(f'Привет {message.from_user.first_name} {message.from_user.last_name}!\nТвой ID: {message.from_user.id} \nТвой  ник:  @{message.from_user.username}',
                        reply_markup=kb.main)
                        # reply_markup=await kb.inline_orders())
    
@router.message(Command('down_list'))
async def get_help(message: Message):
    await message.answer('Загружаем список накладных!)))')

@router.message(Command('nakladnaya'))
async def get_help(message: Message):
    await message.answer('Одна !)))')

@router.message(Command('redy_list'))
async def get_help(message: Message):
    await message.answer('Список собранных накладных!)))')

@router.message(F.text == 'Обед')
async def get_otdjh(message: Message):
    await message.answer('Иди ты найху! \n\n работай!!!')

@router.message(F.photo)
async def get_photo(message: Message):
    await message.answer(f'ID фото {message.photo[-1].file_id}')
    

@router.callback_query(F.data == 'down_list')
async def down_list(callback:CallbackQuery):
    await callback.answer('Загружаем список накладных для сборки!')
    await callback.message.edit_text("Список накладных для сборки.", reply_markup=await kb.inline_orders())
    

@router.callback_query(F.data == 'nakladnaya')
async def down_list(callback:CallbackQuery):
    await callback.answer('')
    await callback.message.answer("Открываем список накладных")
    

@router.callback_query(F.data == 'redy_list')
async def down_list(callback:CallbackQuery):
    await callback.answer('')
    await callback.message.answer("Список готовых накладных...")
