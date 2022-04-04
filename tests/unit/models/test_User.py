from src.models.User import User
from tests.BaseTest import BaseTest


class TestUser(BaseTest):

    def test_new_users_must_be_initialized(self):
        new_user = User('Juan Luis', 'Guerra', '44', 'juan@email.com')

        new_user.first_name = 'Juan Luis'
        new_user.last_name  = 'Guerra'
        new_user.age        = '44'
        new_user.email      = 'juan@email.com'
