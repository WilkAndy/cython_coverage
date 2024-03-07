import cyApple, unittest
class APPLETests(unittest.TestCase):
    def test1(self):
            temp = 5
            apple1 = cyApple.pyApple(temp)
            self.assertEqual(25, apple1.getSquare())
suite = unittest.TestLoader().loadTestsFromTestCase(APPLETests)
unittest.TextTestRunner(verbosity=3).run(suite)
