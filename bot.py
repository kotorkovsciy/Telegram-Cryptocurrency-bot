import asyncio
from aiogram.utils import executor
from create_bot import dp
from handlers import sendCurrentPrice, start, sendtimePrice
from scripts import MySQL_data, getCrypto

async def sendCrypto(wait_for):
    g = await MySQL_data.sql_read()
    print("ddf", g)
    for i in range(len(g)):
        await asyncio.sleep(wait_for)
        value = getCrypto.CryptoCurrency.getCurrentPrice(g[0], g[1])
        print(value)
        
        

async def on_startup(_):
    print('Бот вышел в онлайн')
    MySQL_data.sql_start()




sendtimePrice.register_handlers_sendtimePrice(dp)
start.register_handlers_common(dp)
sendCurrentPrice.register_handlers_sendCurrentPrice(dp)
loop = asyncio.get_event_loop()
loop.create_task(sendCrypto(10)) # поставим 10 секунд, в качестве теста
asyncio.run(executor.start_polling(dp, skip_updates=True, on_startup=on_startup))