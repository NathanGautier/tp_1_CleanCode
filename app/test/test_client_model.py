# import unittest
# import datetime

# from app.main.model.client import Client
# from app.test.base import BaseTestCase


# class TestUserModel(BaseTestCase):

#     def test_encode_auth_token(self):
#         user = User(
#             email='test@test.com',
#             password='test',
#             registered_on=datetime.datetime.utcnow()
#         )
#         db.session.add(user)
#         db.session.commit()
#         auth_token = user.encode_auth_token(user.id)
#         self.assertTrue(isinstance(auth_token, bytes))


# if __name__ == '__main__':
#     unittest.main()
