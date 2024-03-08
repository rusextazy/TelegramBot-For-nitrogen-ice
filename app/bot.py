#from app.middlewares.subscription_checker import CheckSubscription
#from app.callbacks import subscription_check, price
import asyncio
import logging

from aiogram import Bot, Dispatcher
from app.utils.config import Config, load_config
from app.handlers.user import commands, message
from app.callbacks import price
from app.handlers.admin import admin_panel, admin_text, admin_newsletter

logger = logging.getLogger(__name__)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')

    logger.info('БОТ ЗАПУЩЕН')

    config: Config = load_config()

    bot = Bot(token=config.tg_bot.token,
              parse_mode='HTML')
    dp = Dispatcher()

    # dp.message.middleware(CheckSubscription())
    # dp.include_router(subscription_check.router)
    dp.include_router(commands.router)
    dp.include_router(message.router)
    dp.include_router(price.router)
    dp.include_router(admin_panel.router)
    dp.include_router(admin_text.router)
    dp.include_router(admin_newsletter.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
