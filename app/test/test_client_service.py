import unittest
import datetime

from app.main.service.client_service import calculate_letter, is_int, calculate_id, verify_id, response_object, first_int

# classe de test pour le service Client
class TestClientService(unittest.TestCase):
    # GIVEN
    def setUp(self):
        self.client_id = 'E123456789'
        self.key = 'E'
        self.id = '123456789'
        self.first = 1
        self.status = 'success'
        self.result = 1
        self.object = {
            'status': self.status,
            'request': self.client_id,
            'result': self.result
        }

    def test_calculate_letter(self):
        # WHEN
        res = calculate_letter(45)
        # THEN
        self.assertEqual(res, self.key)

    def test_is_int(self):
        # WHEN
        res = is_int(self.id)
        # THEN
        self.assertTrue(res)

    def first_int(self):
        # WHEN
        res = first_int(self.id)
        # THEN
        self.assertEqual(res, self.first)

    def test_calculate_id(self):
        # WHEN
        data = list(self.id)
        res = calculate_id(data)
        # THEN
        self.assertEqual(res, 45)

    def test_response_object(self):
        # WHEN
        res = response_object(self.status, self.client_id, self.result)
        # THEN
        self.assertEqual(res, self.object)

    def test_verify_id(self):
        # WHEN
        res = verify_id(self.key, self.id)
        # THEN
        self.assertEqual(res, self.object)


if __name__ == '__main__':
    unittest.main()
