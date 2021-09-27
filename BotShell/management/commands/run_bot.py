import asyncio
from django.core.management.base import BaseCommand

from aiogram import Bot, Dispatcher

from django.conf import settings

from ...handlers.comments import comments_handlers
from ...handlers.profile_requests import profile_handlers
from ...handlers.search_keyboard import search_keyboard_handlers
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
from ...handlers.film_by_mess import search_film_handlers
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from ...utils.loop_call import scheduler


async def bot_settings(loop=None):

    bot = Bot(token=settings.TG_TOKEN, parse_mode='HTML', loop=loop)

    dp = Dispatcher(bot, storage=MemoryStorage())

    await start_handlers(bot, dp)
    await video_handlers(bot, dp)
    await search_keyboard_handlers(bot, dp)
    await main_menu_handlers(bot, dp)
    await pages(bot, dp)
    await top_handlers(bot, dp)
    await movies_menu_handlers(bot, dp)
    await profile_handlers(bot, dp)
    await start_watching_handlers(bot, dp)
    await comments_handlers(bot, dp)
    await callback_requests_handlers(bot, dp)
    await genres_year_logic_handlers(bot, dp)


    await backs_handlers(bot, dp)


    await search_film_handlers(bot, dp)
    await inline_handlers(bot, dp)

    return bot, dp


async def polling():
    bot, dp = await bot_settings()
    asyncio.create_task(scheduler())
    try:
        await dp.start_polling()
    finally:
        await bot.close()


class Command(BaseCommand):
    def handle(self, *args, **options):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        while True:
            asyncio.run(polling())
