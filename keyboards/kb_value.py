from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

cancel = KeyboardButton('Отмена')
btc = KeyboardButton('BTC')
eth = KeyboardButton('ETH')
ton = KeyboardButton('TON')

kb_symbol = ReplyKeyboardMarkup()
kb_symbol.add(btc).add(eth).add(ton).add(cancel)

rub = KeyboardButton('RUB')
usd = KeyboardButton('USD')
eur = KeyboardButton('EUR')

kb_valute = ReplyKeyboardMarkup()
kb_valute.add(rub).add(usd).add(eur).add(cancel)