from asgiref.sync import sync_to_async


@sync_to_async
def get_list_len(list):
    return len(list)



@sync_to_async
def ret_list(vars):
    return list(vars)


def get_comments(list):
    new_list=[]
    for comment in list:
        new_list.append(comment.text)
    return new_list


def get_only_names2(list):
    new_list=[]
    for value in list:
        new_list.append(value.film_name)
    return new_list


@sync_to_async
def get_only_names(list):
    new_list=[]
    for value in list:
        new_list.append(value.film_name)
    return new_list


def do_with_3_10_8_film_info(film_info3, film_info10, film_info8):
    if film_info3 != '':
        film_info3 = do3(film_info3)
    if film_info10 != '':
        film_info10 = fo10(film_info10)
    if film_info8 != '':
        film_info8 = do8(film_info8)
    return {'film_info3': film_info3,
            'film_info10': film_info10,
            'film_info8': film_info8}


# genres
def do3(film3):
    film_info = [0, 1, 2,4]
    film_info[3] = film3

    len_f_l = len(film_info[3])
    if len_f_l > 2:
        film_info[3] = str(film_info[3][0]) + ', ' + str(film_info[3][1]) + ', ' + str(film_info[3][2])
    elif len_f_l == 2:
        film_info[3] = str(film_info[3][0]) + ', ' + str(film_info[3][1])
    elif len_f_l == 1:
        film_info[3] = str(film_info[3][0])
    else:
        film_info[3] = ''
    return film_info[3]


# description
def do8(film8):
    if len(film8) > 550:
        film8 = str(film8[0:550]) + '...'
    return film8


# stars
def fo10(film_info10):
    film_info = []

    if len(film_info10) > 2:
        film_info10 = str(film_info10[0]) + ', ' + str(film_info10[1]) + ', ' + str(film_info10[2])
    elif len(film_info[10]) == 2:
        film_info10 = str(film_info10[0]) + ', ' + str(film_info10[1])
    elif len(film_info[10]) == 1:
        film_info10 = str(film_info10[0])
    else:
        film_info10 = ''
    return film_info10
