from aiogram import Bot, Dispatcher
from config import TOKEN
from app.handlers import router
from app.callback import router1
import asyncio
from database.db import DataBase

async def main():

    bot = Bot(TOKEN)
    dp = Dispatcher()
    dp.include_routers(router, router1)
    dp.startup.register(DataBase.on_startup)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

try:
    print("Bot online...")
    if __name__ == "__main__":
        asyncio.run(main())
except KeyboardInterrupt:
    print("Bot offline...")