import unittest
import thompsons


class TestThompsons(unittest.TestCase):
    def test_match(self):
        self.assertEqual(thompsons.match("a.b|b*", "bbb"), True)
        self.assertEqual(thompsons.match("a.b|b*", "bbx"), False)
        self.assertEqual(thompsons.match("b**", "b"), True)
        self.assertEqual(thompsons.match("b*", ""), True)
        self.assertEqual(thompsons.match("a?b", "b"), True)
        self.assertEqual(thompsons.match("a+", "a"), True)
        self.assertEqual(thompsons.match("a?|b", "a"), True)
        self.assertEqual(thompsons.match("a+|b", "a"), True)
        self.assertEqual(thompsons.match("a+|b", "b"), True)
        self.assertEqual(thompsons.match("a+|b*", "bbb"), True)


if __name__ == '__main__':
    unittest.main(exit=False)
