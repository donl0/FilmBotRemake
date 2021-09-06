from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

from ..utils.text import telegram_markup
from ..utils.dbcommands import get_all_info, get_message

#стартовая клавиатура
async def start_kerboard():
    start_kerboard = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    item_search = InlineKeyboardButton(text=telegram_markup(await get_message(0)), switch_inline_query_current_chat='')
    item_popul = InlineKeyboardButton(text='🔥 Popular')

    #item_Trend = InlineKeyboardButton(text='🔥 Trending')
    item_my_prof=InlineKeyboardButton(text='📂 My profile')
    #item_markers=InlineKeyboardButton(text='🧡 Favourite')
    item_markers=InlineKeyboardButton(text='❤️ My favorites')
    item_movies = InlineKeyboardButton(text='🎬 Movies')
    item_tv_shows = InlineKeyboardButton(text='🍿 TV Shows')

    #👨‍💻 Help
    #item_requests = InlineKeyboardButton(text='📦 Request')  📮 Request
    item_requests = InlineKeyboardButton(text='📮 Request')
    item_inf = InlineKeyboardButton(text='👨‍💻 Help')
    start_kerboard.add(item_search, item_popul, item_movies, item_tv_shows, item_my_prof, item_markers,  item_requests, item_inf)
    return start_kerboard
#📁📂🗂
#после movie
movie_keyboard = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
item_back = InlineKeyboardButton(text='⬅ Back')
item_pop = InlineKeyboardButton(text='Trending')
item_recently_added = InlineKeyboardButton(text='Recently added')
#item_top_rating = InlineKeyboardButton(text='Top rating')
item_top_rating = InlineKeyboardButton(text='Top rated')
#random film
item_watched_list = InlineKeyboardButton(text='History')
#item_random = InlineKeyboardButton(text='Random film')
#item_filter = InlineKeyboardButton(text='🎚Filter')
item_Genres = InlineKeyboardButton(text='Browse by Genre')
item_Years = InlineKeyboardButton(text='Browse by Year')
#item_watched_list = InlineKeyboardButton(text='History')
#recently added top rating



movie_keyboard.insert(item_back).add(item_pop, item_recently_added, item_top_rating, item_watched_list, item_Genres, item_Years)


#keyb_s_1
search_keyboard = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
item_what_others = InlineKeyboardButton(text='🕵️‍♂️ What others search')
item_filter_search2 = InlineKeyboardButton(text='⚙️ Search filter')

search_keyboard.insert(item_back).add(item_what_others, item_filter_search2)

#keyboard_comm
comm_keyboard = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
item_add_c = InlineKeyboardButton(text='💬 Leave a comment')
item_back_c = InlineKeyboardButton(text='⬅  Back')
comm_keyboard.add(item_back_c,item_add_c)



#genres
filter_keyboard = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
item_Genres = InlineKeyboardButton(text='Genres')
item_Years = InlineKeyboardButton(text='Years')
filter_keyboard.insert(item_back).add(item_Genres,item_Years)


#profile
my_prof_keyboard = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

item_history_clear = InlineKeyboardButton(text='🗑️ Clear all watch history')
my_prof_keyboard.add(item_back).add(item_history_clear)

clear_keyboard = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
item_accept_clear = InlineKeyboardButton(text='Yes, I do.')
item_reject_clear = InlineKeyboardButton(text='No, I changed my mind')
clear_keyboard.add(item_accept_clear, item_reject_clear)

#again or g main menu
again_keyboard = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

item_back_m_m = InlineKeyboardButton(text='⤴️ Back')
item_Again_ = InlineKeyboardButton(text='🔁 Again')

again_keyboard.add(item_back_m_m,item_Again_ )

#fim k
main_m_keyboard = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

item_back1 = InlineKeyboardButton(text='⬅️ Back')
item_main_m1 = InlineKeyboardButton(text='🏠 Main menu')
item_watch_n1 = InlineKeyboardButton(text='▶️ Watch now')
item_u_Comments = InlineKeyboardButton(text='💬 Comments')
item_u_fav = InlineKeyboardButton(text='❤️ Favorite')
main_m_keyboard.add(item_back1, item_main_m1).add(item_watch_n1).add(item_u_Comments, item_u_fav)

main_m_keyboard_2 = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

item_back1 = InlineKeyboardButton(text='⬅️ Back')
item_main_m1 = InlineKeyboardButton(text='🏠 Main menu')
item_watch_n1 = InlineKeyboardButton(text='▶️ Watch now')
item_u_Comments = InlineKeyboardButton(text='💬 Comments')
item_u_fav = InlineKeyboardButton(text='🚫 Remove')
main_m_keyboard_2.add(item_back1, item_main_m1).add(item_watch_n1).add(item_u_Comments, item_u_fav)



#Genre list
Genre_keyboard = ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
item_Anime = InlineKeyboardButton(text='Anime')
item_Action = InlineKeyboardButton(text='Action')
item_Adventure = InlineKeyboardButton(text='Adventure')
item_Animation = InlineKeyboardButton(text='Animation')
item_Biography = InlineKeyboardButton(text='Biography')
item_Comedy = InlineKeyboardButton(text='Comedy')
item_Crime = InlineKeyboardButton(text='Crime')
item_Documentary = InlineKeyboardButton(text='Documentary')
item_Drama = InlineKeyboardButton(text='Drama')
item_Family = InlineKeyboardButton(text='Family')
item_Fantasy = InlineKeyboardButton(text='Fantasy')
item_Game_Show = InlineKeyboardButton(text='Game Show')
item_Horror = InlineKeyboardButton(text='Horror')
item_Music = InlineKeyboardButton(text='Music')
item_Musical = InlineKeyboardButton(text='Musical')
item_Mystery = InlineKeyboardButton(text='Mystery')
item_News = InlineKeyboardButton(text='News')
item_Reality_TV = InlineKeyboardButton(text='Reality-TV')
item_Romance = InlineKeyboardButton(text='Romance')
item_Sci_Fi = InlineKeyboardButton(text='Sci-Fi')
item_Sport = InlineKeyboardButton(text='Sport')
item_Superhero = InlineKeyboardButton(text='Superhero')
item_Talk_Show = InlineKeyboardButton(text='Talk Show')
item_Thriller = InlineKeyboardButton(text='Thriller')
item_War = InlineKeyboardButton(text='War')
item_Western = InlineKeyboardButton(text='Western')
#Genre_keyboard.insert(item_back).add(item_Anime, item_Action, item_Adventure, item_Animation, item_Biography, item_Comedy, item_Crime, item_Drama, item_Family, item_Family, item_Game_Show, item_Horror,item_Music, item_Mystery, item_News, item_Reality_TV, item_Romance, item_Sci_Fi, item_Sport, item_Talk_Show, item_Thriller, item_War, item_Western)
Genre_keyboard.insert(item_back).add(item_Action, item_Adventure, item_Animation, item_Biography, item_Comedy, item_Crime, item_Drama, item_Family, item_Fantasy, item_Horror,item_Music, item_Mystery, item_Romance, item_Sci_Fi, item_Thriller, item_War, item_Western)
#info about bot
info_keyb = ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
item_question = InlineKeyboardButton(text='⚠️ FAQ')
item_adv = InlineKeyboardButton(text='📈 Advertise')
item_copyright = InlineKeyboardButton(text='📄 DMCA')
item_about_pr = InlineKeyboardButton(text='✉️ About us')
info_keyb.add(item_back).add(item_question).add(item_adv).add(item_copyright,item_about_pr)
#⚠️ FAQ
question_keyb = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
item_sound_or_freez = InlineKeyboardButton(text='No audio or video freezes')
item_space = InlineKeyboardButton(text='My phone run out of space')
item_dont_f = InlineKeyboardButton(text="I couldn’t find Movie or TV Show")

question_keyb.add(item_back, item_sound_or_freez,item_space, item_dont_f)

#box
box_keyboard = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
item_create_req = InlineKeyboardButton(text='➕ Add request')
item_my_req = InlineKeyboardButton(text='📄 My requests')
box_keyboard.row(item_back).row(item_create_req, item_my_req)



#TOP
top_keyboard = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
item_day = InlineKeyboardButton(text='Top of the day')
item_mounth = InlineKeyboardButton(text='Top of the month')
item_imdb = InlineKeyboardButton(text='Top IMDb')
top_keyboard.row(item_back).row(item_day, item_mounth).add(item_imdb)


#searching with filtrs
comment_keyboard = InlineKeyboardMarkup(row_width=3, resize_keyboard=True)
item_add_comm = InlineKeyboardButton(text='Add comment', callback_data='add comment')
comment_keyboard.add(item_add_comm)

#searching with filtrs
next_step_keyboard = InlineKeyboardMarkup(row_width=3, resize_keyboard=True)
item_start_search = InlineKeyboardButton(text='Next step', callback_data='next_step')
next_step_keyboard.add(item_start_search)

next_step_keyboard_years = InlineKeyboardMarkup(row_width=3, resize_keyboard=True)
item_start_search = InlineKeyboardButton(text='find movies', callback_data='next_step_years')
next_step_keyboard_years.add(item_start_search)


#watch_keyboard = InlineKeyboardMarkup(row_width=3, resize_keyboard=True)
#item_watch = InlineKeyboardButton(text='Watch', callback_data='watch')
#watch_keyboard.add(item_watch)

item_back = InlineKeyboardButton(text='⬅ Back')
just_back_k=ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
just_back_k.add(item_back)



just_back_yrarf_keybard =  ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
item_year_f = InlineKeyboardButton(text='Choose year')
just_back_yrarf_keybard.add(item_back).row(item_year_f)

just_back_ganre_keybard =  ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
item_ganre_f = InlineKeyboardButton(text='Choose genre')
just_back_ganre_keybard.add(item_back).row(item_ganre_f)

#keyboard for years
years_keyboard = ReplyKeyboardMarkup(row_width=4, resize_keyboard=True)
item_2021 = InlineKeyboardButton(text="2021")
item_2020 = InlineKeyboardButton(text="2020")
item_2019 = InlineKeyboardButton(text="2019")
item_2018 = InlineKeyboardButton(text="2018")
item_2017 = InlineKeyboardButton(text="2017")
item_2016 = InlineKeyboardButton(text="2016")
item_2015 = InlineKeyboardButton(text="2015")
item_2014 = InlineKeyboardButton(text="2014")
item_2013 = InlineKeyboardButton(text="2013")
item_2012 = InlineKeyboardButton(text="2012")
item_2011 = InlineKeyboardButton(text="2011")
item_2010 = InlineKeyboardButton(text="2010")
item_2009 = InlineKeyboardButton(text="2009")
item_2008 = InlineKeyboardButton(text="2008")
item_2007 = InlineKeyboardButton(text="2007")
item_2006 = InlineKeyboardButton(text="2006")
item_2005 = InlineKeyboardButton(text="2005")
item_2004 = InlineKeyboardButton(text="2004")
item_2003 = InlineKeyboardButton(text="2003")
item_2002 = InlineKeyboardButton(text="2002")
item_2001 = InlineKeyboardButton(text="2001")
item_2000 = InlineKeyboardButton(text="2000")
item_1999 = InlineKeyboardButton(text="1999")
item_1998 = InlineKeyboardButton(text="1998")
item_1997 = InlineKeyboardButton(text="1997")
item_1996 = InlineKeyboardButton(text="1996")
item_1995 = InlineKeyboardButton(text="1995")
item_1994 = InlineKeyboardButton(text="1994")
item_1993 = InlineKeyboardButton(text="1993")
item_1992 = InlineKeyboardButton(text="1992")
item_1991 = InlineKeyboardButton(text="1991")
item_1990 = InlineKeyboardButton(text="1990")

#years_keyboard.insert(item_back).add(item_2021, item_2020, item_2019, item_2018, item_2017, item_2016, item_2015, item_2014, item_2013, item_2012, item_2011, item_2010, item_2009, item_2008, item_2007, item_2006, item_2005, item_2004, item_2003, item_2002, item_2001, item_2000, item_1999, item_1998, item_1997, item_1996, item_1995, item_1994, item_1993, item_1992, item_1991, item_1990, item_1989, item_1988, item_1987, item_1986, item_1985, item_1984, item_1983, item_1982, item_1981, item_1980, item_1979, item_1978, item_1977, item_1976, item_1975, item_1974, item_1973, item_1972, item_1971, item_1970, item_1969, item_1968, item_1967, item_1966, item_1965, item_1964, item_1963, item_1962, item_1961, item_1960, item_1959, item_1958, item_1957, item_1956, item_1955, item_1954, item_1953, item_1952, item_1951, item_1950, item_1949, item_1948, item_1947, item_1946, item_1945, item_1944, item_1943, item_1942, item_1941, item_1940, item_1939, item_1938, item_1937, item_1936, item_1935, item_1934, item_1933, item_1932, item_1931, item_1930, item_1929, item_1928, item_1927, item_1926, item_1925, item_1924, item_1923, item_1922)
years_keyboard.insert(item_back).add(item_2021, item_2020, item_2019, item_2018, item_2017, item_2016, item_2015, item_2014, item_2013, item_2012, item_2011, item_2010, item_2009, item_2008, item_2007, item_2006, item_2005, item_2004, item_2003, item_2002, item_2001, item_2000, item_1999, item_1998, item_1997, item_1996, item_1995, item_1994, item_1993, item_1992, item_1991, item_1990)



