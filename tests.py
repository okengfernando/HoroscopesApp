import unittest
import daily_horoscope


  
class Test_Horoscope_Methods(unittest.TestCase): 
      
    def setUp(self): 
        pass
    
    def testSuite(self):
        pass

    def test_check_sign(self):
        self.assertTrue(type(daily_horoscope.check_sign(13,12)) == str)

    def test_date_selector(self):
        self.assertTrue(daily_horoscope.date_selector() == 'yesterday' or 'today' or 'tomorrow')
    
    def test_Horoscope_dipslay(self):
        self.assertTrue(type(daily_horoscope.horoscope(9,'today')) == str)
    
    
  
if __name__ == '__main__': 
    unittest.main() 
