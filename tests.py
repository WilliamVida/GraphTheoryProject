import unittest
import thompsons


class TestThompsons(unittest.TestCase):
    def test_match_equal(self):
        self.assertEqual(thompsons.match("a.b|b*", "bbb"), True)
        self.assertEqual(thompsons.match("b**", "b"), True)
        self.assertEqual(thompsons.match("b*", ""), True)
        self.assertEqual(thompsons.match("a?b", "b"), True)
        self.assertEqual(thompsons.match("a+|b", "a"), True)
        self.assertEqual(thompsons.match("a+|b", "b"), True)

    def test_match_true(self):
        self.assertTrue(thompsons.match("b*", "b"))
        self.assertTrue(thompsons.match("a+|b*", "bbb"))
        self.assertTrue(thompsons.match("a+", "a"))
        self.assertTrue(thompsons.match("a?|b", "a"))

    def test_match_false(self):
        self.assertFalse(thompsons.match("b*", "bx"))
        self.assertFalse(thompsons.match("a.b|b*", "bbx"))
        self.assertFalse(thompsons.match("a?b", "bx"))
        self.assertFalse(thompsons.match("a+b?", "aabb"))
        self.assertFalse(thompsons.match("a+|b", "abx"))


if __name__ == '__main__':
    unittest.main(exit=False)
