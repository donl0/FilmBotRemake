from ..models.trending import TrendingFilms
from ..models.messageEditor import Message
from ..models.filmInfo import Films, Genres
from ..models.star import Stars
from ..models.director import Directors
from ..models.admindb import Admins
from ..models.generalHistory import GeneralHistory
from ..models.userInfo import Users
#from .. import models
from asgiref.sync import sync_to_async
from django.db.models import F


@sync_to_async
def add_new_favourite_film_user(film_name, user_id):
    Users.objects.get(id_tele=user_id).favourite.add(Films.objects.get(film_name=film_name))


@sync_to_async
def get_favourite_user(user_id):
    favourite_list = Users.objects.get(id_tele=user_id).favourite.all()
    favourite_list = list(favourite_list)
    return favourite_list


@sync_to_async
def remove_liked_film_user(film_name, user_id):
    Users.objects.get(id_tele=user_id).liked_films.remove(Films.objects.get(film_name=film_name))


@sync_to_async
def remove_disliked_film_user(film_name, user_id):
    Users.objects.get(id_tele=user_id).disliked_films.remove(Films.objects.get(film_name=film_name))


@sync_to_async
def add_new_liked_film_user(film_name, user_id):
    Users.objects.get(id_tele=user_id).liked_films.add(Films.objects.get(film_name=film_name))


@sync_to_async
def add_new_disliked_film_user(film_name, user_id):
    Users.objects.get(id_tele=user_id).disliked_films.add(Films.objects.get(film_name=film_name))


@sync_to_async
def decrease_film_likes(film_name):
    Films.objects.get(film_name=film_name).update(likes=F('likes') - 1)


@sync_to_async
def decrease_film_dislikes(film_name):
    Films.objects.get(film_name=film_name).update(likes=F('dislikes') - 1)


@sync_to_async
def increase_film_likes(film_name):
    Films.objects.get(film_name=film_name).update(likes=F('likes') + 1)


@sync_to_async
def increase_film_dislikes(film_name):
    Films.objects.get(film_name=film_name).update(likes=F('dislikes') + 1)


@sync_to_async
def get_dislikes_from_user(user_id):
    dislikes = Users.objects.get(id_tele=user_id).id_dislikes
    dislikes = list(dislikes.disliked_films.all())
    return dislikes


@sync_to_async
def get_likes_from_user(user_id):
    likes = Users.objects.get(id_tele=user_id).id_likes
    likes = list(likes.liked_films.all())
    return likes


@sync_to_async
def get_all_by_film_name(film_name):
    film_info = Films.objects.get(film_name=film_name)
   # film_info = list(film_info)
    return film_info


@sync_to_async
def get_genres_by_film_name(film_name):
    genres = Films.objects.get(film_name=film_name)
    genres = genres.genres.all()
    genres = list(genres)
    return genres


@sync_to_async
def push_video_link(film_name, link):
    Films.objects.filter(film_name=film_name).update(video_link=link)


@sync_to_async
def get_paper_count(user_id):
    paper_counter = Users.objects.get(id_tele=user_id).paper_count
    return paper_counter


@sync_to_async
def get_trending_films():
    trending = TrendingFilms.objects.filter()
    print(trending)
    print(len(trending))
    trending = list(trending)
    print(len(trending))
    return trending

@sync_to_async
def get_all_general_history():
    all_g_history = GeneralHistory.objects.filter()
    all_g_history = list(all_g_history)
    return all_g_history


@sync_to_async
def get_all_info():
    info = Films.objects.filter()
    info = list(info)
    return info[0]


@sync_to_async
def get_message(msg_id):
    text = Message.objects.filter(msg_id=msg_id)
    return text[0].text


@sync_to_async
def genre_create(genres):
    for genre in genres:
        Genres.objects.get_or_create(genre_name=genre)


@sync_to_async
def stars_create(stars):
    for star in stars:
        Stars.objects.get_or_create(name=star)


@sync_to_async
def directors_create(director):
    Directors.objects.get_or_create(name=director)


@sync_to_async
def film_create(info, genres, stars, director):
#def film_create(info):
    film = Films.objects.get_or_create(**info)
   # film = Films.objects.create(**info)
    #film_name
    #film = Films.objects.get_or_create(film_name=info['film_name'])
   # film = Films.objects.get_or_create(film_name='1')
    print(film)
  #  print(film[0])
    for genre in genres:
        #film[0].objects.update(genres=Genres.objects.filter(genre_name=genre))
        #film2 = Films.objects.filter(film_name=film[0].film_name)
       # for film_ in film2:
     #       film_.genres.add(Genres.objects.get(genre_name=genre))
        film[0].genres.add(Genres.objects.get(genre_name=genre))
    for star in stars:
        film[0].stars.add(Stars.objects.get(name=star))

    film[0].director.add(Directors.objects.get(name=director))

       # film[0].genres.add(genres=Genres.objects.filter(genre_name=genre))


@sync_to_async
def get_admin():
    admins = Admins.objects.filter()
    mass_admins = []
    for admin in admins:
        mass_admins.append(admin.admin_id)
    print(mass_admins)
   # admins = list(admins)
   # print(admins)
    return mass_admins
