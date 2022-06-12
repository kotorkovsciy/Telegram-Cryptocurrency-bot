from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

price = KeyboardButton('Узнать цену')
time = KeyboardButton('Оповощения')
mainMenu = ReplyKeyboardMarkup()
mainMenu.add(price).add(time)