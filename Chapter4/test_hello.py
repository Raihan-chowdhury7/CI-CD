import unittest

from hello import say_hello

class TestHello(unittest.TestCase):
    self.assertEqual(say_hello(), "Hello World")