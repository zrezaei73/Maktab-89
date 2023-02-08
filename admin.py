import pickle

class User:
    def __init__(self, name, unique_id, is_admin=False):
        self.name = name
        self.unique_id = unique_id
        self.is_admin = is_admin

    def __repr__(self):
        return f"User(name={self.name}, unique_id={self.unique_id}, is_admin={self.is_admin})"

class Manager(User):
    def __init__(self, name, unique_id):
        super().__init__(name, unique_id, is_admin=True)

def create_user(name):
    unique_id = generate_unique_id()
    user = User(name, unique_id)
    with open("users.pickle", "ab") as f:
        pickle.dump(user, f)
    return user

def create_manager(name):
    unique_id = generate_unique_id()
    manager = Manager(name, unique_id)
    with open("users.pickle", "ab") as f:
        pickle.dump(manager, f)
    return manager

def generate_unique_id():
    # code to generate unique id
    return 123456789

def get_users():
    users = []
    with open("users.pickle", "rb") as f:
        try:
            while True:
                users.append(pickle.load(f))
        except EOFError:
            pass
    return users

def get_managers():
    managers = [user for user in get_users() if user.is_admin]
    return managers