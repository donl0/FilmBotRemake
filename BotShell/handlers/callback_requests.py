from ..utils.states import OrderDataUser, FSMContext, State
from aiogram import Bot, Dispatcher
from aiogram import types
from ..utils.text import telegram_markup
from ..utils.dbcommands import get_all_info, get_message, get_all_general_history, get_paper_count, get_trending_films, \
    get_likes_from_user, decrease_film_likes, increase_film_likes, add_new_liked_film_user, \
    remove_liked_film_user, get_dislikes_from_user, increase_film_dislikes, add_new_disliked_film_user, \
    decrease_film_dislikes, remove_disliked_film_user, get_favourite_user, add_new_favourite_film_user, \
    remove_new_favourite_film_user
from ..utils.scroll_keyboard import page_open
from ..utils.film_show import film_create
from ..utils.keyboards import main_m_keyboard, main_m_keyboard2
import re

from ..utils.tools import get_only_names, do_with_3_10_8_film_info, get_only_names2


async def callback_requests_handlers(bot: Bot, dp: Dispatcher):
    @dp.callback_query_handler(lambda c: True, state='*')
    async def callback_inline(call, state: FSMContext):
        user_data = await state.get_data()
        # if user_data['anime']==1:
        # print('DAAA')
        capt = call.message['caption']
        id_person = call.from_user['id']
        # print(call)
        # print(call.data)
        # print(call.message['caption'])
        '''
        next_step_keyboard = InlineKeyboardMarkup(row_width=3, resize_keyboard=True)
        item_film_like = InlineKeyboardButton(text='👍'+str(comm[9]), callback_data='like video')
        item_film_dislike = InlineKeyboardButton(text='👎🏿'+str(comm[10]), callback_data='dislike video')
        item_comm = InlineKeyboardButton(text='💬' +str(comm[12])+' comments', callback_data='comment video')
        item_fav = InlineKeyboardButton(text='❤️ My favorites', callback_data='add favourite')
        item_watch_f = InlineKeyboardButton(text='▶️ Watch now', callback_data='start watching')
        '''
        if call.data == 'like video':
            #   print(call)
           # cursor.execute(f"SELECT `id likes` FROM  user_info WHERE id_tele='{id_person}'")
         #   likes_list = await get_likes_from_user(id_person)  # то что лайкал чел
            capt = call.message['caption']
            phoneNum = re.compile(r'([\s\S]+)[(]\d+[)\n]')
            Fn = phoneNum.search(capt)
            film_name = Fn.group(1)
            film_name_sk = film_name.split('(')

            if len(film_name_sk) > 1:
                film_name = film_name_sk[0]

            likes_list = await get_likes_from_user(id_person)

            if not str(film_name) in await get_only_names(likes_list):  # если чел не лайкал этот фильм то
                # print(id_film)
                await bot.answer_callback_query(callback_query_id=call.id, text='You like that movie 😍',
                                                show_alert=False)
                await increase_film_likes(film_name)
                await add_new_liked_film_user(film_name, id_person)
                # увеличить количество лайков фильму, заебашить айди/название ф в персонажа
            #    cursor.execute(f"UPDATE films_list SET likes= likes+1 WHERE name_film = '{film_name}'")
               # cursor.execute(
               #     f"UPDATE user_info SET `id likes` = CONCAT(`id likes`,' {id_film}') WHERE id_tele='{id_person}';")
                #conn.commit()
            else:
                await decrease_film_likes(film_name)
                await remove_liked_film_user(film_name, id_person)
             #   cursor.execute(f"UPDATE films_list SET likes= likes-1 WHERE name_film = '{film_name}'")
              #  cursor.execute(f"SELECT `id likes` FROM  user_info WHERE id_tele='{id_person}'")
               # likes_list = cursor.fetchone()[0]
               # likes_list = likes_list.replace(' ' + str(id_film), '')
               # cursor.execute(f"UPDATE user_info SET `id likes` = '{likes_list}' WHERE id_tele='{id_person}';")
               # conn.commit()

                await bot.answer_callback_query(callback_query_id=call.id,
                                                text='Your like for that movie has been removed', show_alert=False)
            user_data = await state.get_data()
           # cursor.execute(f"SELECT name_film from `films_list` WHERE name_film='{user_data['film_name']}'")
            #film_inf = cursor.fetchone()[0]
            # print('film_info')
            # print(film_inf)
            print('--------------')
            print(user_data['film_name'])
            film_info = await film_create(film_name, id_person)
            #  print('-----film_info-------')
            #  print(film_info)
            #  print(film_info[4], film_info[0], film_info[1], film_info[3], film_info[2])

            # cursor.execute(f"SELECT favourite FROM `user_info` WHERE id_tele={id_person}")
            ## comm_list = cursor.fetchone()[0]
            # if not film_inf in comm_list:
            # await bot.edit_message_text()
            #    await bot.send_message(chat_id=id_person, text='Film information:', reply_markup=main_m_keyboard)
            # else:
            #    await bot.send_message(chat_id=id_person, text='Film information:', reply_markup=main_m_keyboard_2)
            await bot.edit_message_reply_markup(chat_id=id_person, message_id=call.message.message_id,
                                                reply_markup=film_info[7])
            # await bot.send_video(chat_id=id_person, video=film_info[4], caption='*'+film_info[0] +'('+str(film_info[1])+')*'+'\n\n_Genre: '+str(film_info[3])+'_\n'+str(film_info[8])+'\n\nIMDb: *'+str(film_info[2])+'*'+'\n_Dirctor: '+film_info[9]+'\nActors: '+film_info[10]+'_',reply_markup=film_info[7], parse_mode="Markdown")# as_html=True#parse_mode=ParseMode.MARKDOWN

        elif call.data == '11111':
            pass
        elif call.data == 'dislike video':
            #cursor.execute(f"SELECT `id dislikes` FROM  user_info WHERE id_tele='{id_person}'")
            #likes_list = cursor.fetchone()[0]
            dislike_list = await get_dislikes_from_user(id_person)
           # dislike_list = dislike_list.dislikes.all()
            capt = call.message['caption']

            phoneNum = re.compile(r'([\s\S]+)[(]\d+[)\n]')
            Fn = phoneNum.search(capt)
            film_name = Fn.group(1)
            film_name_sk = film_name.split('(')

            if len(film_name_sk) > 1:
                film_name = film_name_sk[0]
            #  print(Fn.group(1))
           # cursor.execute(f"SELECT id FROM films_list WHERE name_film = '{film_name}'")
           # id_film = cursor.fetchone()[0]
            #dislike_list = dislike_list.split(" ")
            print(dislike_list)
            print(film_name)
            if not film_name in await get_only_names(dislike_list):
                #  print(id_film)
                await bot.answer_callback_query(callback_query_id=call.id, text='You don’t like that movie 🤬',
                                                show_alert=False)
                # увеличить количество лайков фильму, заебашить айди/название ф в персонажа
                await increase_film_dislikes(film_name)
                await add_new_disliked_film_user(film_name, id_person)
               # cursor.execute(f"UPDATE films_list SET dislikes= dislikes+1 WHERE name_film = '{film_name}'")
               # cursor.execute(
               #     f"UPDATE user_info SET `id dislikes` = CONCAT(`id dislikes`,' {id_film}') WHERE id_tele='{id_person}';")
               # conn.commit()
            else:
                #cursor.execute(f"UPDATE films_list SET dislikes= dislikes-1 WHERE name_film = '{film_name}'")
               # cursor.execute(f"SELECT `id dislikes` FROM  user_info WHERE id_tele='{id_person}'")
                await decrease_film_dislikes(film_name)
                await remove_disliked_film_user(film_name, id_person)
               # likes_list = cursor.fetchone()[0]
               # likes_list = likes_list.replace(' ' + str(id_film), '')
               # cursor.execute(f"UPDATE user_info SET `id dislikes` = '{likes_list}' WHERE id_tele='{id_person}';")
                #conn.commit()

                await bot.answer_callback_query(callback_query_id=call.id,
                                                text='Your unlike for that movie has been removed', show_alert=False)
            user_data = await state.get_data()
            #cursor.execute(f"SELECT name_film from `films_list` WHERE name_film='{user_data['film_name']}'")
            #film_inf = cursor.fetchone()[0]
            # print('film_info')
            # print(film_inf)
            film_info = await film_create(film_name, id_person)
            #  print('-----film_info-------')
            #  print(film_info)
            #  print(film_info[4], film_info[0], film_info[1], film_info[3], film_info[2])

            # cursor.execute(f"SELECT favourite FROM `user_info` WHERE id_tele={id_person}")
            ## comm_list = cursor.fetchone()[0]
            # if not film_inf in comm_list:
            # await bot.edit_message_text()
            #    await bot.send_message(chat_id=id_person, text='Film information:', reply_markup=main_m_keyboard)
            # else:
            #    await bot.send_message(chat_id=id_person, text='Film information:', reply_markup=main_m_keyboard_2)
            await bot.edit_message_reply_markup(chat_id=id_person, message_id=call.message.message_id,
                                                reply_markup=film_info[7])
        elif call.data == 'add favourite':
        #    cursor.execute(f"SELECT favourite FROM `user_info` WHERE id_tele={id_person}")
         #   comm_list = cursor.fetchone()[0]
            favourite_list = await get_favourite_user(id_person)
            # print(capt)
            # print(comm_list)
            phoneNum = re.compile(r'([\s\S]+)[(]\d+[)\n]')
            Fn = phoneNum.search(capt)
            film_name = Fn.group(1)
            film_n_film_inf = film_name
            film_name_sk = film_name.split('(')

            if len(film_name_sk) > 1:
                film_name = film_name_sk[0]

            if not film_name in get_only_names2(favourite_list):

               # cursor.execute(
             #       f"UPDATE user_info SET `favourite` = CONCAT(`favourite`,',{film_name}') WHERE id_tele='{id_person}';")
               # conn.commit()
                await add_new_favourite_film_user(film_name, id_person)
                await bot.answer_callback_query(callback_query_id=call.id, text='Film added in favourite list',
                                                show_alert=False)
                film_info = await film_create(film_name, id_person)
                await bot.edit_message_reply_markup(chat_id=id_person, message_id=call.message.message_id,
                                            reply_markup=film_info[7])
            else:
                await remove_new_favourite_film_user(film_name, id_person)
                await bot.answer_callback_query(callback_query_id=call.id,
                                                text='Film deleted from favourite', show_alert=False)
                film_info = await film_create(film_name, id_person)
                await bot.edit_message_reply_markup(chat_id=id_person, message_id=call.message.message_id,
                                                    reply_markup=film_info[7])
        else:
            print(call.data)
            name_f = call.data.split('_')

            await state.update_data(film_name=name_f[1])
            # print(name_f[1])
            print(name_f[1])
           # cursor.execute(f"SELECT name_film from `films_list` WHERE instr(name_film, '{name_f[1]}')")
           # film_inf = cursor.fetchone()[0]
            # print('film_info')
            # print(film_inf)

            print(name_f[1])
            film_info = await film_create(name_f[1], id_person)
            print(film_info[3])
            print(len(film_info[3]))

            film_info_remake = do_with_3_10_8_film_info(film_info[3], film_info[10],film_info[8])
            film_info[3] = film_info_remake['film_info3']
            film_info[8] = film_info_remake['film_info8']
            film_info[10] = film_info_remake['film_info10']
            #cursor.execute(f"SELECT favourite FROM `user_info` WHERE id_tele={id_person}")
            #comm_list = cursor.fetchone()[0]

            await bot.send_message(chat_id=id_person, text=film_info[0] + '(' + str(film_info[1]) + ')',
                                   reply_markup=await main_m_keyboard(name_f[1], id_person))

            await bot.send_video(chat_id=id_person, video=film_info[4],
                                 caption='*' + str(film_info[0]) + '(' + str(film_info[1]) + ')*' + '\n\n_Genre: ' + str(
                                     film_info[3]) + '_\n' + str(film_info[8]) + '\nIMDb: *' + str(
                                     film_info[2]) + '*' + '\n_Dirctor: ' + str(film_info[9]) + '\nActors: ' + str(film_info[
                                             10]) + '_', reply_markup=film_info[7],
                                 parse_mode="Markdown")  # as_html=True#parse_mode=ParseMode.MARKDOWN
        # as_html=True#parse_mode=ParseMode.MARKDOWN

        # await OrderDataUser.sanding_films.set()
        # to_start_menu
        try:
            if user_data['anime'] == 1:
                print('DAAA')
            elif user_data['anime'] == 'tranding1':
                await OrderDataUser.tranding1.set()
            elif user_data['anime'] == 'popular1':
                await OrderDataUser.popular1.set()
            elif user_data['anime'] == 'sanding_films':
                await OrderDataUser.sanding_films.set()
            elif user_data['anime'] == 'resently1':
                await OrderDataUser.resently1.set()
            elif user_data['anime'] == 'top_all':
                await OrderDataUser.top_all.set()
            elif user_data['anime'] == 'Top IMDb':
                await OrderDataUser.top_all.set()
        except:
            print("user_data['anime'] not exist")