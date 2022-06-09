from aiogram.utils import executor
from create_bot import dp
from handlers import sendCurrentPrice, start
import asyncio
async def on_startup(_):
    print('Бот вышел в онлайн')

start.register_handlers_common(dp)
sendCurrentPrice.register_handlers_sendCurrentPrice(dp)
asyncio.run(executor.start_polling(dp, skip_updates=True, on_startup=on_startup))