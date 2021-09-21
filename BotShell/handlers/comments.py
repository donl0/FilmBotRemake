import re
from ..utils.states import OrderDataUser, FSMContext, State
from aiogram import Bot, Dispatcher
from aiogram import types
from ..utils.dbcommands import get_comments_film, create_comment, inc_comments
from ..utils.keyboards import comm_keyboard
from ..utils.tools import get_comments


async def comments_handlers(bot: Bot, dp: Dispatcher):
    @dp.callback_query_handler(state='*', text='comment video')
    async def show_comments(call: types.CallbackQuery, state: FSMContext):
        # print(State)
        capt = call.message['caption']
        id_person = call.from_user['id']
        # comment_v
        maska = re.compile(r'([\s\S]+)[(]\d+[)\n]')
        Fn = maska.search(capt)
        film_name = Fn.group(1)
        film_name_sk = film_name.split('(')

        if len(film_name_sk) > 1:
            film_name = film_name_sk[0]
        send_mes = ''
        all_comments = get_comments(await get_comments_film(film_name))
        print('------')
        print(all_comments)
        try:
            all_comments = get_comments(await get_comments_film(film_name))
            print()
        # print(all_comments)

            for comment in all_comments:
                #  print(i)
                send_mes+=str(comment)+'\n++++++++++++++++++++++++\n'

            await bot.send_message(chat_id=id_person, text='Comments for <b>' + str(film_name) + '</b>', parse_mode="HTML")
            await bot.send_message(chat_id=id_person, text=str(send_mes), reply_markup=comm_keyboard, parse_mode="HTML")
        except:
            send_mes = 'There are no comments for that movie yet, be the 1st one to write it.'
            await bot.send_message(chat_id=id_person, text=str(send_mes), reply_markup=comm_keyboard, parse_mode="HTML")
            # `{str(user_name)}`
        # all_comments=all_comments.replace('^','\n')
        # await bot.send_message(chat_id=id_person, text='Comments\n---------------\n'+str(all_comments), reply_markup=comment_keyboard)
        # film_name='*'+str(film_name)+'*'


        # await bot.send_message(chat_id=id_person, text='Comment for this film haven''t added', reply_markup=comm_keyboard)
        await state.update_data(capt=film_name)

        await state.update_data(way='comment_way')
        # await OrderDataUser.comment_v.set()

    @dp.message_handler(text='💬 Comments', state='*')
    async def show_comments2(message: types.Message, state: FSMContext):
        id_person = message['from']['id']
        user_data = await state.get_data()
        film_name = user_data['film_name']
        send_mes = ''
        try:
            all_comments = get_comments(await get_comments_film(film_name))

            # print(all_comments)
            for comment in all_comments:
                #  print(i)
                send_mes += str(comment) + '\n++++++++++++++++++++++++'
            await bot.send_message(chat_id=id_person, text='Comments for <b>' + str(film_name) + '</b>',
                                   parse_mode="HTML")
            await bot.send_message(chat_id=id_person, text=str(send_mes), reply_markup=comm_keyboard, parse_mode="HTML")
        except:
            send_mes = 'There are no comments for that movie yet, be the 1st one to write it.'
            await bot.send_message(chat_id=id_person, text=str(send_mes), reply_markup=comm_keyboard, parse_mode="HTML")
            # all_comments=all_comments.replace('^','\n')
        # await bot.send_message(chat_id=id_person, text='Comments\n---------------\n'+str(all_comments), reply_markup=comment_keyboard)


        # await bot.send_message(chat_id=id_person, text='Comment for this film haven''t added', reply_markup=comm_keyboard)
        await state.update_data(capt=film_name)

        await state.update_data(way='comment_way')

    @dp.callback_query_handler(state='*', text='add comment')
    async def send_com(call: types.CallbackQuery, state: FSMContext):
        id_person = call.from_user['id']
        name_u = call.message.chat['username']
        await bot.send_message(chat_id=id_person, text='Send your comment')
        await OrderDataUser.comment_v.set()

    @dp.message_handler(text='💬 Leave a comment', state='*')
    async def send_com2(message: types.Message, state: FSMContext):
        id_person = message['from']['id']
        user_data = await state.get_data()
        film_inf = user_data['film_name']
        await bot.send_message(chat_id=id_person,
                               text='❗IMPORTANT! The comment must be at least 5 to 250 characters long. Advertising links, swearing, insulting other users fully prohibited. The punishment will lead to ban. \n\nPlease type your comment below👇')
        await OrderDataUser.comment_v.set()

    @dp.message_handler(state=OrderDataUser.comment_v, content_types=types.ContentType.TEXT)
    async def send_com_finished(message: types.Message, state: FSMContext):
        user_data = await state.get_data()
        mess = message.text
        id_person = message['from']['id']
        await create_comment(user_data['film_name'], id_person, mess)
        await bot.send_message(chat_id=id_person, text='Your comment saved')
        await inc_comments(user_data['film_name'])

        await OrderDataUser.tranding1.set()