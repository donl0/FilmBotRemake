from asgiref.sync import sync_to_async


@sync_to_async
def ret_list(vars):
    return list(vars)

