from werkzeug.security import safe_str_cmp
from Login_SIgnUp.User import User

users = [
    User(843117002, 'Cyd Marie Rivera Rodriguez', 'abcxyz'),
    User(802118412, 'Yorkie Serrano Natal', 'abxyz'),
    User(802107409, 'Christian Lorenzo Muniz', 'abcxz'),
]

username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}

def authenticate(username, password):
    user = username_table.get(username, None)
    if user and safe_str_cmp(user.password, password): # depende de la version de python
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)