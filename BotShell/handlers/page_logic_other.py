from ..utils.dbcommands import get_paper_count
from ..utils.film_show import film_create
from ..utils.scroll_keyboard import next_page_info1, previous_page_info1
from ..utils.states import OrderDataUser, FSMContext, State
from aiogram import Bot, Dispatcher
from aiogram import types


async def pages(bot: Bot, dp: Dispatcher):
    @dp.callback_query_handler(state=OrderDataUser.resently1, text='next_page')
    async def del_adv(call: types.CallbackQuery, state: FSMContext):
        user_data = await state.get_data()
        id_person = call.from_user['id']

        user_data['counter'] = user_data['counter'] + 1

        # all_list=next_page_info(user_data['counter'], user_data['film_list'], user_data['len_list'], id_person)

        paper_count = await get_paper_count(id_person)
        all_list = await next_page_info1(user_data['counter'], user_data['film_list'], user_data['len_list'], paper_count,
                                   id_person)
        print('-------------')
        print(user_data['film_list'])
        print(all_list)
        print(all_list[1])
        await bot.edit_message_text(chat_id=id_person, message_id=call.message.message_id, text=all_list[1],
                                    reply_markup=all_list[2])
        await state.update_data(counter=all_list[0])

    @dp.callback_query_handler(state=OrderDataUser.resently1, text='previous_page')
    async def del_adv(call: types.CallbackQuery, state: FSMContext):
        user_data = await state.get_data()

        id_person = call.from_user['id']

        # user_data['counter']=user_data['counter']-1
        # all_list=previous_page_info(user_data['counter'], user_data['film_list'], user_data['len_list'], id_person)

        paper_count = await get_paper_count(id_person)
        user_data['counter'] = user_data['counter'] - 1
        all_list = await previous_page_info1(user_data['counter'], user_data['film_list'], user_data['len_list'], paper_count,
                                       id_person)

        await state.update_data(counter=all_list[0])
        await bot.edit_message_text(chat_id=id_person, message_id=call.message.message_id, text=all_list[1],
                                    reply_markup=all_list[2])

    @dp.callback_query_handler(state=OrderDataUser.favorite_st, text='next_page')
    async def del_adv(call: types.CallbackQuery, state: FSMContext):
        user_data = await state.get_data()
        id_person = call.from_user['id']

        user_data['counter'] = user_data['counter'] + 1

        # all_list=next_page_info(user_data['counter'], user_data['film_list'], user_data['len_list'], id_person)

        paper_count = await get_paper_count(id_person)
        all_list = await next_page_info1(user_data['counter'], user_data['film_list'], user_data['len_list'], paper_count,
                                   id_person)

        await bot.edit_message_text(chat_id=id_person, message_id=call.message.message_id, text=all_list[1],
                                    reply_markup=all_list[2])
        await state.update_data(counter=all_list[0])

    @dp.callback_query_handler(state=OrderDataUser.favorite_st, text='previous_page')
    async def del_adv(call: types.CallbackQuery, state: FSMContext):
        user_data = await state.get_data()

        id_person = call.from_user['id']

        user_data['counter'] = user_data['counter'] - 1
        # all_list=previous_page_info(user_data['counter'], user_data['film_list'], user_data['len_list'], id_person)

        paper_count = await get_paper_count(id_person)
        # user_data['counter']=user_data['counter']-1
        all_list = await previous_page_info1(user_data['counter'], user_data['film_list'], user_data['len_list'], paper_count,
                                       id_person)

        await state.update_data(counter=all_list[0])
        await bot.edit_message_text(chat_id=id_person, message_id=call.message.message_id, text=all_list[1],
                                    reply_markup=all_list[2])


    @dp.callback_query_handler(state=OrderDataUser.search_by_all, text='next_page')
    async def next_p1(call: types.CallbackQuery, state: FSMContext):
        user_data = await state.get_data()
        id_person = call.from_user['id']

        user_data['counter'] = user_data['counter'] + 1
        paper_count = await get_paper_count(id_person)
        all_list = await next_page_info1(user_data['counter'], user_data['film_list'], user_data['len_list'], paper_count,
                                   id_person)
        await bot.edit_message_text(chat_id=id_person, message_id=call.message.message_id, text=all_list[1],
                                    reply_markup=all_list[2])
        await state.update_data(counter=all_list[0])

    @dp.callback_query_handler(state=OrderDataUser.search_by_all, text='previous_page')
    async def del_adv(call: types.CallbackQuery, state: FSMContext):
        user_data = await state.get_data()

        id_person = call.from_user['id']
        paper_count = await get_paper_count(id_person)
        user_data['counter'] = user_data['counter'] - 1
        all_list = await previous_page_info1(user_data['counter'], user_data['film_list'], user_data['len_list'], paper_count,
                                       id_person)
        await state.update_data(counter=all_list[0])
        await bot.edit_message_text(chat_id=id_person, message_id=call.message.message_id, text=all_list[1],
                                    reply_markup=all_list[2])

    @dp.callback_query_handler(state=OrderDataUser.search_director, text='next_page')
    async def del_adv(call: types.CallbackQuery, state: FSMContext):
        user_data = await state.get_data()
        id_person = call.from_user['id']

        user_data['counter'] = user_data['counter'] + 1
        paper_count = await get_paper_count(id_person)
        all_list = await next_page_info1(user_data['counter'], user_data['film_list'], user_data['len_list'], paper_count,
                                   id_person)
        await bot.edit_message_text(chat_id=id_person, message_id=call.message.message_id, text=all_list[1],
                                    reply_markup=all_list[2])
        await state.update_data(counter=all_list[0])

    @dp.callback_query_handler(state=OrderDataUser.search_director, text='previous_page')
    async def del_adv(call: types.CallbackQuery, state: FSMContext):
        user_data = await state.get_data()

        id_person = call.from_user['id']
        paper_count = await get_paper_count(id_person)
        user_data['counter'] = user_data['counter'] - 1
        all_list = await previous_page_info1(user_data['counter'], user_data['film_list'], user_data['len_list'], paper_count,
                                       id_person)
        await state.update_data(counter=all_list[0])
        await bot.edit_message_text(chat_id=id_person, message_id=call.message.message_id, text=all_list[1],
                                    reply_markup=all_list[2])

    @dp.callback_query_handler(state=OrderDataUser.search_stars, text='next_page')
    async def del_adv(call: types.CallbackQuery, state: FSMContext):
        user_data = await state.get_data()
        id_person = call.from_user['id']

        user_data['counter'] = user_data['counter'] + 1
        paper_count = await get_paper_count(id_person)
        all_list = await next_page_info1(user_data['counter'], user_data['film_list'], user_data['len_list'], paper_count,
                                   id_person)
        await bot.edit_message_text(chat_id=id_person, message_id=call.message.message_id, text=all_list[1],
                                    reply_markup=all_list[2])
        await state.update_data(counter=all_list[0])

    @dp.callback_query_handler(state=OrderDataUser.search_stars, text='previous_page')
    async def del_adv(call: types.CallbackQuery, state: FSMContext):
        user_data = await state.get_data()

        id_person = call.from_user['id']
        paper_count = await get_paper_count(id_person)
        user_data['counter'] = user_data['counter'] - 1
        all_list = await previous_page_info1(user_data['counter'], user_data['film_list'], user_data['len_list'], paper_count,
                                       id_person)
        await state.update_data(counter=all_list[0])
        await bot.edit_message_text(chat_id=id_person, message_id=call.message.message_id, text=all_list[1],
                                    reply_markup=all_list[2])

    @dp.callback_query_handler(state=OrderDataUser.by_name1, text='next_page')
    async def del_adv(call: types.CallbackQuery, state: FSMContext):
        user_data = await state.get_data()
        id_person = call.from_user['id']

        user_data['counter'] = user_data['counter'] + 1
        paper_count = await get_paper_count(id_person)
        all_list = await next_page_info1(user_data['counter'], user_data['film_list'], user_data['len_list'], paper_count,
                                   id_person)
        await bot.edit_message_text(chat_id=id_person, message_id=call.message.message_id, text=all_list[1],
                                    reply_markup=all_list[2])
        await state.update_data(counter=all_list[0])

    @dp.callback_query_handler(state=OrderDataUser.by_name1, text='previous_page')
    async def del_adv(call: types.CallbackQuery, state: FSMContext):
        user_data = await state.get_data()

        id_person = call.from_user['id']
        paper_count = await get_paper_count(id_person)
        user_data['counter'] = user_data['counter'] - 1
        all_list = await previous_page_info1(user_data['counter'], user_data['film_list'], user_data['len_list'], paper_count,
                                       id_person)
        await state.update_data(counter=all_list[0])
        await bot.edit_message_text(chat_id=id_person, message_id=call.message.message_id, text=all_list[1],
                                    reply_markup=all_list[2])

    @dp.callback_query_handler(state=OrderDataUser.history1, text='next_page')
    async def del_adv(call: types.CallbackQuery, state: FSMContext):
        user_data = await state.get_data()
        id_person = call.from_user['id']

        user_data['counter'] = user_data['counter'] + 1

        #  all_list=next_page_info(user_data['counter'], user_data['film_list'], user_data['len_list'], id_person)

        paper_count = await get_paper_count(id_person)
        all_list = await next_page_info1(user_data['counter'], user_data['film_list'], user_data['len_list'], paper_count,
                                   id_person)

        await bot.edit_message_text(chat_id=id_person, message_id=call.message.message_id, text=all_list[1],
                                    reply_markup=all_list[2])
        await state.update_data(counter=all_list[0])

    @dp.callback_query_handler(state=OrderDataUser.history1, text='previous_page')
    async def del_adv(call: types.CallbackQuery, state: FSMContext):
        user_data = await state.get_data()

        id_person = call.from_user['id']

        user_data['counter'] = user_data['counter'] - 1
        # all_list=previous_page_info(user_data['counter'], user_data['film_list'], user_data['len_list'], id_person)

        paper_count = await get_paper_count(id_person)
        #  user_data['counter']=user_data['counter']-1
        all_list = await previous_page_info1(user_data['counter'], user_data['film_list'], user_data['len_list'], paper_count,
                                       id_person)

        await state.update_data(counter=all_list[0])
        await bot.edit_message_text(chat_id=id_person, message_id=call.message.message_id, text=all_list[1],
                                    reply_markup=all_list[2])


    @dp.callback_query_handler(state=OrderDataUser.popular1, text='next_page')
    async def del_adv(call: types.CallbackQuery, state: FSMContext):
        user_data = await state.get_data()
        id_person = call.from_user['id']

        user_data['counter'] = user_data['counter'] + 1

        # all_list=next_page_info(user_data['counter'], user_data['film_list'], user_data['len_list'], id_person)

        paper_count = await get_paper_count(id_person)
        all_list = await ext_page_info1(user_data['counter'], user_data['film_list'], user_data['len_list'], paper_count,
                                   id_person)

        await bot.edit_message_text(chat_id=id_person, message_id=call.message.message_id, text=all_list[1],
                                    reply_markup=all_list[2])
        await state.update_data(counter=all_list[0])

    @dp.callback_query_handler(state=OrderDataUser.popular1, text='previous_page')
    async def del_adv(call: types.CallbackQuery, state: FSMContext):
        user_data = await state.get_data()

        id_person = call.from_user['id']

        user_data['counter'] = user_data['counter'] - 1
        # all_list=previous_page_info(user_data['counter'], user_data['film_list'], user_data['len_list'], id_person)

        paper_count = await get_paper_count(id_person)
        # user_data['counter']=user_data['counter']-1
        all_list = await previous_page_info1(user_data['counter'], user_data['film_list'], user_data['len_list'], paper_count,
                                       id_person)

        await state.update_data(counter=all_list[0])
        await bot.edit_message_text(chat_id=id_person, message_id=call.message.message_id, text=all_list[1],
                                    reply_markup=all_list[2])

    @dp.callback_query_handler(state=OrderDataUser.top_all, text='next_page')
    async def del_adv(call: types.CallbackQuery, state: FSMContext):
        user_data = await state.get_data()
        id_person = call.from_user['id']

        user_data['counter'] = user_data['counter'] + 1

        # all_list=next_page_info(user_data['counter'], user_data['film_list'], user_data['len_list'], id_person)

        paper_count = await get_paper_count(id_person)
        all_list = await next_page_info1(user_data['counter'], user_data['film_list'], user_data['len_list'], paper_count,
                                   id_person)

        await bot.edit_message_text(chat_id=id_person, message_id=call.message.message_id, text=all_list[1],
                                    reply_markup=all_list[2])
        await state.update_data(counter=all_list[0])

    @dp.callback_query_handler(state=OrderDataUser.top_all, text='previous_page')
    async def del_adv(call: types.CallbackQuery, state: FSMContext):
        user_data = await state.get_data()

        id_person = call.from_user['id']

        user_data['counter'] = user_data['counter'] - 1
        # all_list=previous_page_info(user_data['counter'], user_data['film_list'], user_data['len_list'], id_person)

        paper_count = await get_paper_count(id_person)
        # user_data['counter']=user_data['counter']-1
        all_list = await previous_page_info1(user_data['counter'], user_data['film_list'], user_data['len_list'], paper_count,
                                       id_person)

        await state.update_data(counter=all_list[0])
        await bot.edit_message_text(chat_id=id_person, message_id=call.message.message_id, text=all_list[1],
                                    reply_markup=all_list[2])

        @dp.callback_query_handler(state=OrderDataUser.resently1, text='next_page')
        async def del_adv(call: types.CallbackQuery, state: FSMContext):
            user_data = await state.get_data()
            id_person = call.from_user['id']

            user_data['counter'] = user_data['counter'] + 1

            # all_list=next_page_info(user_data['counter'], user_data['film_list'], user_data['len_list'], id_person)

            paper_count = await get_paper_count(id_person)
            all_list = await next_page_info1(user_data['counter'], user_data['film_list'], user_data['len_list'], paper_count,
                                       id_person)

            await bot.edit_message_text(chat_id=id_person, message_id=call.message.message_id, text=all_list[1],
                                        reply_markup=all_list[2])
            await state.update_data(counter=all_list[0])

        @dp.callback_query_handler(state=OrderDataUser.resently1, text='previous_page')
        async def del_adv(call: types.CallbackQuery, state: FSMContext):
            user_data = await state.get_data()

            id_person = call.from_user['id']

            # user_data['counter']=user_data['counter']-1
            # all_list=previous_page_info(user_data['counter'], user_data['film_list'], user_data['len_list'], id_person)

            paper_count = await get_paper_count(id_person)
            user_data['counter'] = user_data['counter'] - 1
            all_list = await previous_page_info1(user_data['counter'], user_data['film_list'], user_data['len_list'],
                                           paper_count, id_person)

            await state.update_data(counter=all_list[0])
            await bot.edit_message_text(chat_id=id_person, message_id=call.message.message_id, text=all_list[1],
                                        reply_markup=all_list[2])
