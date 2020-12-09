import unittest
import datetime
from app.main.service.client_service import calculate_letter, is_int, calculate_id, verify_id, response_object, first_int, creation_id


# classe de test pour le service Client
class TestClientService(unittest.TestCase):
    # GIVEN
    def setUp(self):
        self.client_id = 'J123456789'
        self.key = 'J'
        self.id = '123456789'
        self.first = 1
        self.status = 'success'
        self.result = 1
        self.object = {
            'status': self.status,
            'request': self.client_id,
            'result': self.result
        }
        self.object_creation = {
            'status': self.status,
            'request': self.id,
            'result': self.client_id
        }

    def test_calculate_letter(self):
        res = calculate_letter(45)
        self.assertEqual(res, self.key)

    def test_is_int(self):
        res = is_int(self.id)
        self.assertTrue(res)

    def test_first_int(self):
        res = first_int(self.id)
        self.assertTrue(res is False)

    def test_calculate_id(self):
        data = list(self.id)
        res = calculate_id(data)
        self.assertEqual(res, 45)

    def test_response_object(self):
        res = response_object(self.status, self.client_id, self.result)
        self.assertEqual(res, self.object)

    def test_verify_id(self):
        res = verify_id(self.key, self.id)
        self.assertEqual(res, self.object)

    def test_creation_id(self):
        res = creation_id(self.id)
        self.assertEqual(res, self.object_creation)


if __name__ == '__main__':
    unittest.main()
