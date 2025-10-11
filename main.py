import asyncio
from aiogram import Bot,Dispatcher
from confiq import BOT_TOKEN
from app.handlers import router

bot = Bot(BOT_TOKEN)
dp = Dispatcher()

async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception:
        print("Oh, something went wrong!!!")