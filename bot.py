import asyncio
from aiogram.utils import executor
from create_bot import dp, bot
from handlers import sendCurrentPrice, start, sendtimePrice
from scripts import getCrypto
from scripts.MySQL_data import SQL_DB

async def sendCrypto(wait_for, bot):
    while True:
        await asyncio.sleep(wait_for)
        records = await SQL_DB.sql_read()
        for row in records:
            await asyncio.sleep(wait_for)
            value = getCrypto.CryptoCurrency.getCurrentPrice(row[0], row[1])["data"][row[0]]["quote"][row[1]]["price"]
            await bot.send_message(row[2], f"{row[0]}: {round(value)} {row[1]}")
        
async def on_startup(_):
    print('Бот вышел в онлайн')

sendtimePrice.register_handlers_sendtimePrice(dp)
start.register_handlers_common(dp)
sendCurrentPrice.register_handlers_sendCurrentPrice(dp)

if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    a = SQL_DB.sql_read(name_table="time")
    loop.create_task(sendCrypto(a, bot))
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
