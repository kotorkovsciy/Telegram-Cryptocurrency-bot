import asyncio
from aiogram import types, Dispatcher
from aiogram import types, Dispatcher 
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from keyboards.kb_value import kb_symbol, kb_valute
from keyboards.mainMenu import mainMenu
from scripts.getCrypto import CryptoCurrency
from aiogram.dispatcher.filters import Text
from scripts.MySQL_data import SQL_DB
class TimerCurrentPrice(StatesGroup):
    symbol = State()
    valute = State()
    id_user = State()

async def startCurrentPrice(message: types.Message, state: FSMContext):
    await TimerCurrentPrice.symbol.set()       
    await message.reply('Выбери крипту, если ее нет в списке, можешь написать ее сам.', reply_markup=kb_symbol)

async def getSymbol(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['symbol'] = message.text
    await message.reply('Напиши валюту, в которой хочешь узнать цену.', reply_markup=kb_valute)
    await TimerCurrentPrice.next()

async def getValute(message: types.Message, state: FSMContext): 
    async with state.proxy() as data:
        data['valute'] = message.text
    await message.reply('Подверди', reply_markup=kb_valute)
    await TimerCurrentPrice.next()

async def getUserID(message: types.Message, state: FSMContext):
    if message.text.lower() == "да":
        async with state.proxy() as data:
            data['id_user'] = message.from_user.id
        await SQL_DB.sql_add_command(state)
        await state.finish()
    elif message.text.lower() == "нет":
        await state.finish()

def register_handlers_sendtimePrice(dp : Dispatcher):
    dp.register_message_handler(startCurrentPrice, Text(equals="Оповощения"), state=None)
    dp.register_message_handler(getSymbol, state=TimerCurrentPrice.symbol)
    dp.register_message_handler(getValute, state=TimerCurrentPrice.valute)
    dp.register_message_handler(getUserID, state=TimerCurrentPrice.id_user)
