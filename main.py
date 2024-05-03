class User():
    def __init__(self, user_id, name, access_level='user'):
        self.__user_id = user_id
        self.__name = name
        self.__access_ievel = access_level

    def get_ID(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_ievel

class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name, access_level='admin')
        self.__user_list = []

    def add_user(self, user):
        self.__user_list.append(user)
        print(f'Добавлен новый пользователь {user.get_name()}')

    def remove_user(self, user):
        if user in self.__user_list:
            self.__user_list.remove(user)
            print(f'Пользователь {user.get_name()} удален')
        else:
            print(f'Пользователь {user.get_name()} не найден')

    def get_user_list(self):
        return self.__user_list

    def print_user_list(self):
        print('Пользователи:')
        for user in self.__user_list:
            print(f"ID: {user.get_ID()}; Имя: {user.get_name()}; Уровень доступа: {user.get_access_level()}")

admin1 = Admin(1, "Анна")

user1 = User(11, "Ольга")
user2 = User(12, "Павел")
user3 = User(13, "Антон")

admin1.add_user(user1)
admin1.add_user(user2)
admin1.add_user(user3)

admin1.print_user_list()

admin1.remove_user(user2)
admin1.remove_user(user2)

admin1.print_user_list()