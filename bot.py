import asyncio
import logging
from init import dp, bot

from register_handlers import register_handlers


logging.basicConfig(level=logging.INFO)



async def main():
    register_handlers()

    
    try:
        await dp.start_polling(bot, skip_updates=True)
    finally:
        await dp.storage.close()
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())