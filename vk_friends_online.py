from argparse import ArgumentParser
from getpass import getpass
import vk


APP_ID = 5830124


def get_vk_api_via_auth(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends'
    )
    api = vk.API(session)
    return api


def get_users_names_by_ids(vk_handler, dict_of_ids):
    list_of_users_names = vk_handler.users.get(order='hints', user_ids=dict_of_ids['online_mobile'])
    for name in list_of_users_names:
        name['mobile'] = 1
    list_of_users_names.extend(vk_handler.users.get(user_ids=dict_of_ids['online']))
    return list_of_users_names


def get_online_friends(vk_handler):
    dict_of_ids = vk_handler.friends.getOnline(online_mobile=1)
    list_of_users_names = get_users_names_by_ids(vk_handler, dict_of_ids)
    return list_of_users_names


def output_friends_to_console(friends_online, sort=False):
    if sort:
        friends_online_for_listing = sorted(friends_online, key=lambda f: '{} {}'.format(f['last_name'], f['first_name']))
    else:
    	friends_online_for_listing = friends_online.copy()
    for user in friends_online_for_listing:
        if 'mobile' in user:
            template = '{} {} [m]'
        else:
            template = '{} {}'
        print(template.format(user['last_name'], user['first_name']))
    print('---')
    print('Total friends online: {}'.format(len(friends_online)))

def get_user_password():
    password = getpass()
    return password


if __name__ == '__main__':
    parser = ArgumentParser(description='List your friends that online in vk.com right now')
    parser.add_argument('login', help='Your vk login')
    parser.add_argument('password', nargs='?', default=None, help='Your vk password')
    parser.add_argument('-s', '--sort', action='store_true', default=False, help='Sort your mates by name, not by vk hints')
    args = parser.parse_args()
    
    if args.password is None:
        password = get_user_password()
    else:
        password = args.password

    vk_handler = get_vk_api_via_auth(args.login, password)
    friends_online = get_online_friends(vk_handler)
    output_friends_to_console(friends_online, args.sort)
