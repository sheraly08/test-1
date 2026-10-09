from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from database import db


class Add_product(StatesGroup):
    name = State()
    price = State()
    description = State()

router_add_product = Router()

@router_add_product.message(Command("add_product"))
async def start(message: Message, state: FSMContext):
    await message.answer("Введите название напитка: ")
    await state.set_state(Add_product.name)

@router_add_product.message(Add_product.name)
async def add_product_name(message: Message, state: FSMContext):
    if message.text is None:
        await message.answer("Введите название напитка текстом.")
        return

    await state.update_data(name=message.text)
    await message.answer("Введите цену напитка:")
    await state.set_state(Add_product.price)

@router_add_product.message(Add_product.price)
async def add_product_price(message: Message, state: FSMContext):
    await state.update_data(price=message.text)
    await message.answer('Введите описание напитка: ')
    await state.set_state(Add_product.description)

@router_add_product.message(Add_product.description)
async def add_product_description(message: Message, state: FSMContext):
    await state.update_data(description=message.text)

    data = await state.get_data()

    db.add_product_db(
    name=data["name"],
    price=data["price"],
    description=data["description"]
    )

    await message.answer(f"Данные напитка: \n"
                         f"Название: {data['name']}\n"
                         f"Цена: {data['price']}\n"
                         f"Описание: {data['description']}"
                         )
    
    

    await state.clear()
    
    
