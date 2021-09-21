from ..utils.film_show import film_create
from ..utils.keyboards import main_m_keyboard
from ..utils.states import OrderDataUser, FSMContext, State
from aiogram import Bot, Dispatcher
from aiogram import types
from ..utils.text import telegram_markup
from ..utils.tools import do_with_3_10_8_film_info


async def backs_handlers(bot: Bot, dp: Dispatcher):
    @dp.back_handler1(text='⬅  Back', state = OrderDataUser.comment_v)
    async def comm_back(message: types.Message, state: FSMContext):
        user_data = await state.get_data()
        id_person = message['from']['id']
        print('SRABOTAL')
        #await state.update_data(film_name=mess)
        film_info = film_create(user_data['film_name'], id_person)
        film_info_remake = do_with_3_10_8_film_info(film_info[3], film_info[10], film_info[8])
        film_info[3] = film_info_remake['film_info3']
        film_info[8] = film_info_remake['film_info8']
        film_info[10] = film_info_remake['film_info10']
        #  print('-----film_info-------')
        #  print(film_info)
        #  print(film_info[4], film_info[0], film_info[1], film_info[3], film_info[2])

        # film_info[3]=film_info[3].replace(", "," #")

        await bot.send_message(chat_id=id_person, text=film_info[0] + '(' + str(film_info[1]) + ')',
                               reply_markup=await main_m_keyboard(user_data['film_name'], id_person))

        await bot.send_video(chat_id=id_person, video=film_info[4],
                             caption='*' + film_info[0] + '(' + str(film_info[1]) + ')*' + '\n\n_Genre: ' + str(
                                 film_info[3]) + '_\n' + str(film_info[8]) + '\nIMDb: *' + str(
                                 film_info[2]) + '*' + '\n_Dirctor: ' + film_info[9] + '\nActors: ' + film_info[
                                         10] + '_', reply_markup=film_info[7],
                             parse_mode="Markdown")  # as_html=True#parse_mode=ParseMode.MARKDOWN
        '''
        try:
           # cursor.execute(f"SELECT name_film from `films_list` WHERE name_film='{user_data['film_name']}'")
           # film_inf = cursor.fetchone()[0]
            # print('film_info')
            # print(film_inf)
            film_info = film_create(user_data['film_name'], id_person)
            film_info_remake = do_with_3_10_8_film_info(film_info[3], film_info[10], film_info[8])
            film_info[3] = film_info_remake['film_info3']
            film_info[8] = film_info_remake['film_info8']
            film_info[10] = film_info_remake['film_info10']
            #  print('-----film_info-------')
            #  print(film_info)
            #  print(film_info[4], film_info[0], film_info[1], film_info[3], film_info[2])


                #film_info[3]=film_info[3].replace(", "," #")


            await bot.send_message(chat_id=id_person, text=film_info[0] +'('+str(film_info[1])+')', reply_markup=await main_m_keyboard1(user_data['film_name'], id_person))


            await bot.send_video(chat_id=id_person, video=film_info[4], caption='*'+film_info[0] +'('+str(film_info[1])+')*'+'\n\n_Genre: '+str(film_info[3])+'_\n'+str(film_info[8])+'\nIMDb: *'+str(film_info[2])+'*'+'\n_Dirctor: '+film_info[9]+'\nActors: '+film_info[10]+'_',reply_markup=film_info[7], parse_mode="Markdown")# as_html=True#parse_mode=ParseMode.MARKDOWN
    # as_html=True#parse_mode=ParseMode.MARKDOWN
        except:
            await bot.send_message(chat_id=message['from']['id'], text='🏠 You are back to main menu', reply_markup=start_kerboard)
        #await state.finish()
            await OrderDataUser.to_start_menu.set()
        '''
        try:
            if user_data['anime']==1:
                await OrderDataUser.to_start_menu.set()
            elif user_data['anime']=='tranding1':
                await OrderDataUser.tranding1.set()
            elif user_data['anime']=='popular1':
                await OrderDataUser.popular1.set()
            elif user_data['anime']=='sanding_films':
                await OrderDataUser.sanding_films.set()
            elif user_data['anime']=='resently1':
                await OrderDataUser.resently1.set()
            elif user_data['anime']=='top_all':
                await OrderDataUser.top_all.set()
            elif user_data['anime']=='Top IMDb':
                await OrderDataUser.top_all.set()
        except:
            print("user_data['anime'] not exist")