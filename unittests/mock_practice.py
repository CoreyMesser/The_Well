import unittest

from mock import MagicMock, patch


class ProductionClass(object):

    def method(self):
        a = self.something(1, 2, 3)
        b = self.otherthing(1)

        return a, b

    def something(self, a, b, c):
        i = 0
        x = 1
        return 0

    def otherthing(self, a):
        x = 6
        return 0


class MyTest(unittest.TestCase):

    def some_return(self):
        return [1, 2, 3]

    def other_return(self):
        return [4, 5, 6]

    @patch('__main__.ProductionClass.something')
    @patch('__main__.ProductionClass.otherthing')
    def test_production_class(self, other_mock, some_mock):

        some_mock.return_value = self.some_return()
        other_mock.return_value = self.other_return()

        p = ProductionClass()

        z = p.method()
        print('done: {}'.format(str(z)))

if __name__ == '__main__':
    print('{}'.format(__name__))
    unittest.main()
