from os import stat
import sys
import asyncio
from aiogram import types, Dispatcher
from aiogram import types, Dispatcher 
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from keyboards.kb_value import kb_symbol, kb_valute
from keyboards.mainMenu import mainMenu
from scripts.getCrypto import CryptoCurrency
from aiogram.dispatcher.filters import Text

class CurrentPrice(StatesGroup):
    symbol = State()
    valute = State()

async def startCurrentPrice(message: types.Message):
    await CurrentPrice.symbol.set()
    await message.reply('Выбери крипту, если ее нет в списке, можешь написать ее сам.', reply_markup=kb_symbol)

async def getSymbol(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['symbol'] = message.text
    await message.reply('Напиши валюту, в которой хочешь узнать цену.', reply_markup=kb_valute)
    await CurrentPrice.next()

async def getValute(message: types.Message, state: FSMContext):
    
    async with state.proxy() as data:
        data['valute'] = message.text

        symbol = data['symbol'].upper()
        valute = data['valute'].upper()
        try:
            getCrypto = CryptoCurrency.getCurrentPrice(symbol, valute)
            price = round(getCrypto["data"][symbol]["quote"][valute]["price"])
            await message.answer(f'{price} {valute}', reply_markup=mainMenu)
        except: await message.answer(f'Произошла ошибка', reply_markup=mainMenu)

    await state.finish()

def register_handlers_sendCurrentPrice(dp : Dispatcher):
    dp.register_message_handler(startCurrentPrice, Text(equals="Узнать цену"), state=None)
    dp.register_message_handler(getSymbol, state=CurrentPrice.symbol)
    dp.register_message_handler(getValute, state=CurrentPrice.valute)