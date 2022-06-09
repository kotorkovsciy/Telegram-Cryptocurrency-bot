from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

price = KeyboardButton('Узнать цену')
mainMenu = ReplyKeyboardMarkup()
mainMenu.add(price)