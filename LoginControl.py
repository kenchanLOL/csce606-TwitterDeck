from User import User


def login(name, password, dataAdapter):
    user = dataAdapter.loadUser(name, password)
    if user is None:
        print('fail')
    else:
        print('succeed')
    return user
