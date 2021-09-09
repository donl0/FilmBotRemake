from aiogram import Bot, Dispatcher
from aiogram import types
from ..utils.dbcommands import get_admin
from ..utils.film_fill import film_filler
#from ...FilmBot.settings import admin_id
# from ..utils.text import telegram_markup
from ..utils.dbcommands import get_all_info, get_message
import inspect, os.path, sys
#from django.conf import settings
#from ..management.commands.run_bot import settings
#from ...FilmBot.settings import admin_id


async def video_handlers(bot: Bot, dp: Dispatcher):
    @dp.message_handler(content_types=types.ContentType.VIDEO, state="*")
    async def film_create(message: types.Message):
        user_name = message['from']['username']
        id_person = message['from']['id']
        video = message.video.file_id
        # film_filler(message.caption, video)
        # await message.answer(text=message.caption+' было загружено!')
        admin_id = await get_admin()
       # admin_id = list(admin_id)
        print(admin_id)
        if id_person in admin_id:
            if message.caption[0] == '-':
                #   print('ЗАШЁЛ')
                await film_filler(message.caption, video)
                # film_name = film_pars(message.caption)[0]

                await message.answer(text=message.caption + ' was loaded!☺️!')
            else:
                await film_filler(message.caption, video)
                # film_name = film_pars(message.caption)[0]
                await message.answer(text='trailer for ' + message.caption + '  was loaded!')