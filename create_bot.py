import os
from aiogram import Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher
from dotenv import load_dotenv
load_dotenv()

TOKEN_CRYPTO = os.getenv('TOKEN_CRYPTO') # API-TOKEN брать здесь https://pro.coinmarketcap.com/account
bot = Bot(token=os.getenv('TOKEN_BOT')) # API-TOKEN вашего телеграм бота https://t.me/BotFather
dp = Dispatcher(bot, storage=MemoryStorage())
