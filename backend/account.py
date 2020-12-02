import sqlite3
from orm import ORM



DATABASE = "../data/nba.db"
where_clause = "SELECT * FROM {}"


class Account(ORM):
    dbpath = DATABASE
    tablename = "accounts"
    fields = ["username", "password_hash", "api_key"]

    def __init__(self, **kwargs):
        self.username = kwargs.get('username')
        self.password_hash = kwargs.get('password')
        self.pk = kwargs.get('pk')
        self.api_key = kwargs.get('api_key')


    def generate_api_key(self):
        letters = string.ascii_lowercase
        key = "".join(random.choice(letters) for i in range(20))
        self.api_key = key 

    def get_api_key(self):
        return self.api_key

    @classmethod
    def api_authenticate(cls, api_key):
        account = Account.one_from_where_clause("WHERE api_key=?",
                                            (api_key,))
        if account is None:
            return None
        return account

    @classmethod
    def login(self, username, password):
        return Account.one_from_where_clause("WHERE username=? AND password_hash=?",
                                            (username, hash_password(password)))
                                            
                                                                                            