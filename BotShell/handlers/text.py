from aiogram import Bot, Dispatcher
from aiogram import types
from ..utils.text import telegram_markup
from ..utils.dbcommands import get_all_info, get_message
import inspect, os.path, sys


async def text_handlers(bot: Bot, dp: Dispatcher):
    @dp.message_handler(content_types = types.ContentTypes.TEXT)
    async def menu_keyboard(message: types.Message):
        id_person = message['from']['id']
     #   await film_create_text()
       # print(message)
      #  video = await get_all_info()
        #x = await message.answer_video(video)
       # print(x)
        #await message.answer_video(file_id)
       # await bot.send_message(id_person, video)
     #   x = await message.answer_video(video)
       # print(x)
       # video = 'C:\\Users\\danii\Desktop\\film_bot_remake\\FilmBot\\media\\videos\\Hyper_Light_Drifter_2021-07-24_14-19-13.mp4'
       # x = await message.answer_video(video)
        #await bot.send_video(chat_id=id_person, video='BAACAgIAAxkDAAKU4WEzrlfjnHBt2FMsI58iG8nJnPYjAAI_EQAC7leYSfeTNp385u26IAQ')
      #  filename = inspect.getframeinfo(inspect.currentframe()).filename
       # path = os.path.dirname(os.path.abspath(filename))
      #  path = os.path.dirname(os.path.abspath(sys.argv[0]))
       # path += video
     #   with open(path, 'rb') as video:
         #   x = await message.answer_video(video)
        x = await get_message(1)
        x = telegram_markup(x)
        print(x)
        await bot.send_message(id_person, x)
          #  print(x)