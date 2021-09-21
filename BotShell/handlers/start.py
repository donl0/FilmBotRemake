from ..utils.dbcommands import update_general_history, update_user_history, update_all_watches, get_all_by_film_name, \
    user_info_by_id, create_user, get_message
from ..utils.keyboards import start_kerboard
from ..utils.states import OrderDataUser, FSMContext, State
from aiogram import Bot, Dispatcher
from aiogram import types
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

import re

from ..utils.text import telegram_markup


async def start_handlers(bot: Bot, dp: Dispatcher):
    @dp.message_handler(commands=['start'], state="*")
    async def start_handler(message: types.Message, state: FSMContext):
        print('ddd')
        user_name = message['from']['username']
        id_person = message['from']['id']

        # print('ddd')
        # await bot.send_photo(chat_id=id_person,photo='https://m.media-amazon.com/images/M/MV5BNzQzOTk3OTAtNDQ0Zi00ZTVkLWI0MTEtMDllZjNkYzNjNTc4L2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_UX182_CR0,0,182,268_AL_.jpg')
       # person_dataInf = cursor.execute(f"SELECT name from user_info WHERE id_tele='{id_person}'")
        create_data = {'name': user_name, 'id_tele': id_person}
        await create_user(create_data)
      #  name_check = (await user_info_by_id(id_person))
       # print('----------')
        #print(name_check)
        # print(person_dataInf)
        #if name_check == '':
         #   create_data = {'name':user_name, 'id_tele':id_person}
          #  await create_user(create_data)

        # x=await bot.get_chat_member('@test_anime1',user_id=id_person)
        # print(x['status'])
        # luke_k_1_new = InlineKeyboardMarkup(row_width=1)
        # next_user_butt = InlineKeyboardButton(text='👍 I Subscribed', callback_data='sus')
        # url_button1 = types.InlineKeyboardButton(text="➡️ Subscribe", url='https://t.me/test_anime1')
        next_step_keyboard = InlineKeyboardMarkup(row_width=3, resize_keyboard=True)
        item_searc_an = InlineKeyboardButton(text='🔍 Quick search', switch_inline_query_current_chat='')
        next_step_keyboard.row(item_searc_an)
       # await bot.send_message(chat_id=id_person,
        #                       text=f'👋 Hello and Welcome `{str(user_name)}` to GomoviesHD\! This bot will help you find almost any Movies or TV Shows you want to watch\. If you experiencing any problems or still have questions, you can ask them directly in our chat [GomoviesHD Chat](https://t.me/test_anime1) ❤️\n\n❗*IMPORTANT*\! When searching for Movies or TV Shows and typing name of the movie you *don''t need to write* year, season or series number\! Make sure title of the movie spelled correctly as it''s written on IMDb website\! Otherwise, bot can not help you to find anything\. Example below:\n\n✅ Correct: Wonder woman\n✅ Correct: The Witcher\n❌ Incorrect: Wonder woman 2020\n❌ Incorrect: The Witcher season 1 ',
         #                      reply_markup=await start_kerboard, parse_mode='MarkdownV2')
        await bot.send_message(chat_id=id_person,
                               text=telegram_markup(await get_message(100)),
                               reply_markup=await start_kerboard())
        await bot.send_message(chat_id=id_person,
                               text=telegram_markup(await get_message(101)),
                               reply_markup=next_step_keyboard)
        # luke_k_1_new.add(next_user_butt, url_button1)
        await OrderDataUser.to_start_menu.set()
        # await bot.send_message(chat_id=id_person, text='Hey\! friends\! Our bot is absolutely free and no ads\! But he has access only to subscribers of our [chat](https://t.me/test_anime1)\n\nSubscribe not to miss new items\! After subscribing, click "I have subscribed"\. Access will be opened automatically\.', reply_markup = luke_k_1_new, parse_mode='MarkdownV2')
        # await OrderDataUser.Subscribed1.set()
        '''
        x=await bot.get_chat_member('@test_anime1',user_id=id_person)
        if not x['status']=='left':
            await bot.get_chat_member('@test_anime1',user_id=id_person)
            next_step_keyboard = InlineKeyboardMarkup(row_width=3, resize_keyboard=True)
            item_searc_an = InlineKeyboardButton(text='🔍 Quick search', switch_inline_query_current_chat='')
            next_step_keyboard.row(item_searc_an)
            await bot.send_message(chat_id=id_person, text='👋 Hello and Welcome '+str(user_name)+' to GomoviesHD\! This bot will help you find almost any Movies or TV Shows you want to watch\. If you experiencing any problems or still have questions, you can ask them directly in our chat [GomoviesHD Chat](https://t.me/test_anime1)❤️\n\n❗IMPORTANT\! When searching for Movies or TV Shows and typing name of the movie you don''t need to write year, season or series number\! Make sure title of the movie spelled correctly as it’s written on IMDb website\! Otherwise, bot can not help you to find anything\. Example below:\n\n✅ Correct: Wonder woman\n✅ Correct: The Witcher\n❌ Incorrect: Wonder woman 2020\n❌ Incorrect: The Witcher season 1 ', reply_markup=start_kerboard, parse_mode='MarkdownV2')
            await bot.send_message(chat_id=id_person, text='Use menu below to navigate 👇 or click “🔍 Quick search” button and start typing the name of the movie want to watch!', reply_markup=next_step_keyboard)
            await OrderDataUser.to_start_menu.set()
            await state.finish()
        else:
            luke_k_1_new = InlineKeyboardMarkup(row_width=1)
            next_user_butt = InlineKeyboardButton(text='👍 I Subscribed', callback_data='sus')
            url_button1 = types.InlineKeyboardButton(text="➡️ Subscribe", url='https://t.me/test_anime1')
    
            luke_k_1_new.add(next_user_butt, url_button1)
    
            await bot.send_message(chat_id=id_person, text='Hey\! friends\! Our bot is absolutely free and no ads\! But he has access only to subscribers of our [chat](https://t.me/test_anime1)\n\nSubscribe not to miss new items\! After subscribing, click "I have subscribed"\. Access will be opened automatically\.', reply_markup = luke_k_1_new, parse_mode='MarkdownV2')
            await OrderDataUser.Subscribed1.set()
        '''


    '''
    @dp.message_handler(content_types=types.ContentTypes.TEXT, state='*')
    async def genres_adding(message: types.Message, state: FSMContext):
      #  user_data = await state.get_data()
        id_person= message['from']['id']
        print(message.text)
        #Subscribed1
        #await state.finish()
'''