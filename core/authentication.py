import bcrypt
from database.user_model import User

def register_user(email, password, firstname, lastname):
    """Registers a new user."""
    password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    user = User()
    user = user.create_user(first_name=firstname, last_name=lastname, username=email, email=email, password_hash=password_hash.decode())
    if (user):
        return True
    return False

def authenticate_user(username, password):
    """Authenticates an existing user."""
    user = User.get_user_by_username(username)

    if user:
        if bcrypt.checkpw(password.encode(), user.password_hash.encode()):
            return True
        else:
            return False
    else:
        return False
