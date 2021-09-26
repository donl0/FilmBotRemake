from ..utils.dbcommands import get_message, delete_user_history, add_new_requests, get_user_requests
from ..utils.keyboards import clear_keyboard, my_prof_keyboard
from ..utils.states import OrderDataUser, FSMContext, State
from aiogram import Bot, Dispatcher
from aiogram import types
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

from ..utils.text import telegram_markup
from ..utils.tools import get_from_film_requests


async def profile_handlers(bot: Bot, dp: Dispatcher):
    @dp.message_handler(text=[telegram_markup(await get_message(80)), telegram_markup(await get_message(81)), telegram_markup(await get_message(81))], state=OrderDataUser.my_prof_st)
    async def clear_logic(message: types.Message):
        text = message.text
        id_person = message['from']['id']
        if text == telegram_markup(await get_message(80)):
            clear_keyboard = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
            item_accept_clear = InlineKeyboardButton(text=telegram_markup(await get_message(81)))
            item_reject_clear = InlineKeyboardButton(text=telegram_markup(await get_message(82)))
            clear_keyboard.add(item_accept_clear, item_reject_clear)
            await bot.send_message(chat_id=id_person, text=telegram_markup(await get_message(83)), reply_markup=clear_keyboard)
        elif text == telegram_markup(await get_message(81)):
            await delete_user_history(id_person)
            await bot.send_message(chat_id=id_person, text=telegram_markup(await get_message(84)), reply_markup=my_prof_keyboard)
        elif text == telegram_markup(await get_message(82)):
            await bot.send_message(chat_id=id_person, text=telegram_markup(await get_message(85)), reply_markup=my_prof_keyboard)

    @dp.message_handler(text=['➕ Add request', '📄 My requests'], state=OrderDataUser.box_state)
    async def help_section(message: types.Message, state: FSMContext):
        id_person = message['from']['id']
        text = message.text
        req = True
        if text == '➕ Add request':
            await bot.send_message(chat_id=id_person,
                                   text=telegram_markup(await get_message(93)))
            await OrderDataUser.request_list.set()

        # text=str(text)+'\n'
        # cursor.execute(f"UPDATE `user_info` SET `comments` = '\n{text}' WHERE `user_info`.`id` = {id_person};")

        elif text == '📄 My requests':
            requests = await get_from_film_requests(await get_user_requests((id_person)))
            if len(requests) == 0:
                await bot.send_message(chat_id=id_person, text=telegram_markup(await get_message(201)))
            else:
                string = ''
                print(requests)
                for i in range(len(requests[0])):
                   string += requests[1][i]+str(requests[0][i])+'\n'
                string += '\n\n'+str(telegram_markup(await get_message(202)))
                await bot.send_message(chat_id=id_person, text=string)
            # except:
            #    await bot.send_message(chat_id=id_person, text="Yoy didn't created any requests")

    @dp.message_handler(content_types=types.ContentTypes.TEXT, state=OrderDataUser.request_list)
    async def request_make(message: types.Message):
        id_person = message['from']['id']
        text = message.text
        if text == telegram_markup(await get_message(90)) or text == telegram_markup(await get_message(91)):
            await bot.send_message(chat_id=id_person, text='Enter another movie name.')
            await OrderDataUser.box_state.set()
        else:
            await add_new_requests(text, id_person)
            await bot.send_message(chat_id=id_person,
                                   text=telegram_markup(await get_message(203)))
            await OrderDataUser.box_state.set()
