import vk


APP_ID = 4592955


def get_user_login():
    pass


def get_user_password():
    pass


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
    )
    api = vk.API(session)
    # например, api.friends.get()


def output_friends_to_console(friends_online):
    pass

if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
