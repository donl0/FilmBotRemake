from ..utils.dbcommands import year_genre_filter, get_films_by_genres, get_paper_count, get_films_by_year, \
    get_all_by_contain_film
from ..utils.states import OrderDataUser, FSMContext, State
from aiogram import Bot, Dispatcher
from aiogram import types

async def inline_handlers(bot: Bot, dp: Dispatcher):
    @dp.inline_handler(lambda query: len(query.query) > 0, state='*')
    async def query_text(query):
        # print('INL')
        film_name_by_inline = query.query  # То что вводит пользователь при обращении
        try:
            film_info = await get_all_by_contain_film(film_name_by_inline)
            #film_name_by_inline = film_name_by_inline.replace("'", "''")
            #sql = cursor.execute(

             #   f"SELECT name_film, year, rating, link, id , photo FROM films_list WHERE (instr(name_film, '{film_name_by_inline}'));")
        except:
            print("ну ошибка типо")

       # film_list = cursor.fetchall()
        results = []
        # print(film_list)
        for i in range(0, len(film_info)):
            single_msg = types.InlineQueryResultArticle(
               # id=film_list[i][4],
                id=film_info[i].film_name,
                title=film_info[i].film_name,
                input_message_content=types.InputTextMessageContent(message_text=film_info[i].film_name),
                # добавляем ссылку на фильм в чат
                description='Year: ' + str(film_info[i].year) + ' \n' + 'Rating: ' + str(film_info[i].rating),
                thumb_url=film_info[i].photo,
            )
            results.append(single_msg)

        await bot.answer_inline_query(query.id, results)
