from project.user import User
from project.library import Library


class Registration:
    # def __init__(self):

    def add_user(self, user: User, library: Library):
        if user not in library.user_records:
            library.user_records.append(user)
        else:
            return f"User with id = {user.user_id} already registered in the library!"

    def remove_user(self, user: User, library: Library):
        if user in library.user_records:
            library.user_records.remove(user)
        else:
            return f"We could not find such user to remove!"

    def change_username(self, user_id: int, new_username: str, library: Library):
        found_user = [u for u in library.user_records if u.user_id == user_id]
        if not found_user:
            return f"There is no user with id = {user_id}!"
        user = found_user[0]
        if user.username == new_username:
            return f"Please check again the provided username - it should be different than the username used so far!"

        user.username = new_username
        for user_name, books in library.rented_books.items():
            if user_name == user.username:
                library.rented_books[new_username] = library.rented_books[new_username].pop(user_name)

        return f"Username successfully changed to: {new_username} for user id: {user_id}"



