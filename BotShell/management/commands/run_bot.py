import asyncio
from asgiref.sync import sync_to_async
from django.core.management.base import BaseCommand

from aiogram import Bot, Dispatcher

from django.conf import settings

#from ...handlers.commands import cmd_handlers
#from ...handlers.text import text_handlers
from ...handlers.comments import comments_handlers
from ...handlers.film_by_mess import search_film_handlers
from ...handlers.genres_year_search_logic import genres_year_logic_handlers
from ...handlers.inline import inline_handlers
from ...handlers.page_logic_other import pages
from ...handlers.other_backs import backs_handlers
from ...handlers.start import start_handlers
from ...handlers.mainMenu import main_menu_handlers
from ...handlers.top_movies import top_handlers
from ...handlers.video import video_handlers
from ...handlers.moviesMenu import movies_menu_handlers
from ...handlers.start_watching_callback import start_watching_handlers
from ...handlers.callback_requests import callback_requests_handlers
from aiogram.contrib.fsm_storage.memory import MemoryStorage
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

    dp = Dispatcher(bot, storage=MemoryStorage())

   # await cmd_handlers(bot, dp)
   # await text_handlers(bot, dp)
    await start_handlers(bot, dp)
    await video_handlers(bot, dp)
    await main_menu_handlers(bot, dp)
    await pages(bot, dp)
    await top_handlers(bot, dp)
    await movies_menu_handlers(bot, dp)
    await start_watching_handlers(bot, dp)
    await comments_handlers(bot, dp)
    await callback_requests_handlers(bot, dp)
    await genres_year_logic_handlers(bot, dp)


    await backs_handlers(bot, dp)


    await search_film_handlers(bot, dp)
    await inline_handlers(bot, dp)
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
