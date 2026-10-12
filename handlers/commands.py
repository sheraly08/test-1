from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram import F, Router
from handlers.keyboards import reply_keyboard, inline_keyboard
from database import db
router_commands = Router()

@router_commands.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Приветствуем в наше заведение 'Coffee House'\n"
                         "Для дополнительной информации нажмите на Помощь или /help",
                         reply_markup=reply_keyboard
                         )

@router_commands.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer("Нажмите на 'Меню' для более подробной информации")

@router_commands.message(Command('menu'))
async def cmd_menu(message: Message):
    await message.answer("Coffee House  — меню команд\n"
                         "/start — Запустить бота\n"
                         "/help - Помощь\n"
                         "/menu - Показать список команд\n" 
                         "/drinks - Посмотреть меню напитков\n"
                         "/add_product - Добавить напиток\n",
                         reply_markup=inline_keyboard
                         )

@router_commands.message(F.text == 'Старт')
async def start(message: Message):
    await cmd_start(message)

@router_commands.message(F.text == 'Помощь')
async def help(message: Message):
    await cmd_help(message)

@router_commands.message(F.text == "Меню")
async def menu(message: Message):
    await cmd_menu(message)

@router_commands.callback_query(F.data == "about")
async def cmd_about(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer("Добро пожаловать в Coffee House!\n"
                                  "Это уютное кафе, где каждый напиток создаётся с любовью"
                                    )


@router_commands.message(Command("drinks"))
async def drinks(message: Message):
    products = db.get_products_db()

    if not products:
        await message.answer("Меню пока пустое")
        return

    for product in products:
        await message.answer(
            f"Название: {product[0]}\n"
            f"Цена: {product[1]} сом\n"
            f"Описание: {product[2]}"
        )
    
@router_commands.message(F.text == 'пока')
async def cmd_stop(message: Message):
    await message.answer("До встречи!")
