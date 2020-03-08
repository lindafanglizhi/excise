try:
    import mock
except ImportError:
    from unittest import mock

import unittest

from day1.square import Square


class TestClass(unittest.TestCase):

    @mock.patch('test_class.Square')
    def test_mocking_instance(self, mocked_instance):
        mocked_instance = mocked_instance.return_value
        mocked_instance.calculate_area.return_value = 1
        sq = Square(100)
        self.assertEqual(sq.calculate_area(), 1)

    def test_mocking_classes(self):
        sq = Square(2)
        print(sq.calculate_area())
        sq.calculate_area = mock.MagicMock(return_value=1)
        self.assertEqual(sq.calculate_area(), 1)

    @mock.patch.object(Square, 'calculate_area')
    def test_mocking_class_methods(self, mocked_method):
        mocked_method.return_value = 20
        self.assertEqual(Square.calculate_area(), 20)


if __name__ == '__main__':
    unittest.main()
