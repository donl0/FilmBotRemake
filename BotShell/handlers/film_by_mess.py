from ..utils.dbcommands import get_films_by_year, get_all_by_film_name
from ..utils.film_show import film_create
from ..utils.keyboards import main_m_keyboard, start_kerboard
from ..utils.states import OrderDataUser, FSMContext, State
from aiogram import Bot, Dispatcher
from aiogram import types
from ..utils.text import telegram_markup
from ..utils.tools import do_with_3_10_8_film_info


async def search_film_handlers(bot: Bot, dp: Dispatcher):
    @dp.message_handler(state = '*', content_types=types.ContentType.TEXT)
    async def film_film(message: types.Message, state: FSMContext):
        id_person = message['from']['id']
        mess=message.text
        await state.update_data(film_name=mess)
        #film_inf = await get_all_by_film_name(mess)
        # print('film_info')
        # print(film_inf)
       # print(mess)

        try:

            film_info = await film_create(mess, id_person)

            #  print('-----film_info-------')
            #  print(film_info)
            #  print(film_info[4], film_info[0], film_info[1], film_info[3], film_info[2])

            film_info_remake = do_with_3_10_8_film_info(film_info[3], film_info[10], film_info[8])
            film_info[3] = film_info_remake['film_info3']
            film_info[8] = film_info_remake['film_info8']
            film_info[10] = film_info_remake['film_info10']
            await bot.send_message(chat_id=id_person, text=film_info[0] + '(' + str(film_info[1]) + ')',
                                   reply_markup=await main_m_keyboard(mess, id_person))

            await bot.send_video(chat_id=id_person, video=film_info[4],
                                 caption='*' + film_info[0] + '(' + str(film_info[1]) + ')*' + '\n\n_Genre: ' + str(
                                     film_info[3]) + '_\n' + str(film_info[8]) + '\nIMDb: *' + str(
                                     film_info[2]) + '*' + '\n_Dirctor: ' + str(film_info[9]) + '\nActors: ' + str(
                                     film_info[
                                         10]) + '_', reply_markup=film_info[7],
                                 parse_mode="Markdown")  # as_html=True#parse_mode=ParseMode.MARKDOWN
        except:
            await bot.send_message(chat_id=message['from']['id'], text='🏠 You are back to main menu', reply_markup=await start_kerboard())
        #await state.finish()
            await OrderDataUser.to_start_menu.set()

        #await bot.send_message(chat_id=id_person, text="We don't have this film")