import asyncio

from aiogram import Bot, Dispatcher

from data.scripts.config import BotConfig
from handlers import general



async def main() -> None:
    bot = Bot(BotConfig().get_token())
    dp = Dispatcher()

    dp.include_router(general.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)



if __name__ == '__main__':
    asyncio.run(main())