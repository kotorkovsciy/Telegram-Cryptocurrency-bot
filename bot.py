import asyncio
from aiogram.utils import executor
from create_bot import dp
from handlers import sendCurrentPrice, start, sendtimePrice
from scripts import getCrypto
from scripts.MySQL_data import SQL_DB

async def sendCrypto(wait_for):
    while True:
        await asyncio.sleep(wait_for)
        num = list(await SQL_DB.sql_quantity())
        records = await SQL_DB.sql_read()
        print("ddf", num[0])
        for row in records:
            await asyncio.sleep(wait_for)
            value = getCrypto.CryptoCurrency.getCurrentPrice(row[0], row[1])
            print(value)
        
        

async def on_startup(_):
    print('Бот вышел в онлайн')




sendtimePrice.register_handlers_sendtimePrice(dp)
start.register_handlers_common(dp)
sendCurrentPrice.register_handlers_sendCurrentPrice(dp)

if __name__ == '__main__':
  loop = asyncio.new_event_loop()
  asyncio.set_event_loop(loop)
  loop.create_task(sendCrypto(10))
  executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
