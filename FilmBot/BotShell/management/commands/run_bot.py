import asyncio
from asgiref.sync import sync_to_async
from django.core.management.base import BaseCommand

from aiogram import Bot, Dispatcher

from django.conf import settings

#from ...handlers.commands import cmd_handlers
#from ...handlers.text import text_handlers
from ...handlers.mainMenu import main_menu_handlers
#from ...handlers.callback import callback_handlers
#from ...handlers.registration import registration_handlers, new_date_handlers


import logging


async def bot_settings(loop=None):

   # logger_format = "%(asctime)s - %(levelname)s - %(name)s - %(message)s"

  #  if settings.DEBUG:
  #      logging.basicConfig(level=logging.DEBUG, format=logger_format)
  #  else:
    #    logging.basicConfig(level=logging.INFO, format=logger_format)

   # logger.info("Starting bot")

    bot = Bot(token=settings.TG_TOKEN, parse_mode='HTML', loop=loop)

    dp = Dispatcher(bot)

   # await cmd_handlers(bot, dp)
   # await text_handlers(bot, dp)
    await main_menu_handlers(bot, dp)
    #await callback_handlers(bot, dp)
    #await registration_handlers(bot, dp)
    #await new_date_handlers(bot, dp)

   # update_cache = sync_to_async(update_redis_cache)
    #await update_cache()

    return bot, dp


async def polling():
    bot, dp = await bot_settings()
    try:
       # dp.middleware.setup(AdminMiddleware())
        #dp.middleware.setup(CreateUserMiddleware())
        await dp.start_polling()
    finally:
        await bot.close()


class Command(BaseCommand):
    def handle(self, *args, **options):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        while True:
            asyncio.run(polling())

      #  if settings.POLLING:
       #     loop = asyncio.new_event_loop()
       #     asyncio.set_event_loop(loop)
       #     while True:
       #         asyncio.run(polling())
       # else:
        #    pass
