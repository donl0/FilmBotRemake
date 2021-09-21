from ..utils.dbcommands import update_general_history, update_user_history, update_all_watches, get_all_by_film_name
from ..utils.states import OrderDataUser, FSMContext, State
from aiogram import Bot, Dispatcher
from aiogram import types
import re

async def start_watching_handlers(bot: Bot, dp: Dispatcher):
    @dp.callback_query_handler(state='*', text='start watching')
    async def start_watching(call: types.CallbackQuery, state: FSMContext):
        capt = call.message['caption']
        id_person = call.from_user['id']
        phoneNum = re.compile(r'([\s\S]+)[(]\d+[)\n]')
        Fn = phoneNum.search(capt)
        film_name = Fn.group(1)
        film_name_sk = film_name.split('(')

        if len(film_name_sk) > 1:
            film_name = film_name_sk[0]
        # print('--------------------------------')
        # print(film_name_sk)
        # print(len(film_name_sk))
        # print('имяяяСС')
        # print(str(film_name)+'aa')
        await update_general_history(film_name)
        # cursor.execute(f"SELECT id FROM films_list WHERE name_film='{film_name}'")
        # id_film = cursor.fetchone()
        await update_user_history(film_name, id_person)
            # print(str(film_name)+' находится в '+ str(his_list))
        await update_all_watches(film_name)
        # print(film_name)
        info_film = await get_all_by_film_name(film_name)

        # print(info_film[0][2])
        # print(info_film[2])
        await bot.send_video(chat_id=id_person, video=info_film.video_link, caption='*' + info_film.film_name + '(' + str(
            info_film.year) + ')*\n\nEnjoy watching! Share @GomoviesHDbot with your family and friends ;) ',
                             parse_mode="Markdown")
        # await OrderDataUser.sanding_films.set()