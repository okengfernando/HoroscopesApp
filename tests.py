import unittest
import daily_horoscope


  
class Test_Horoscope_Methods(unittest.TestCase): 

    def test_pass(self):
        pass

    def test_check_sign(self):
        self.assertTrue(type(daily_horoscope.check_sign(13,12)) == str)

    def test_date_selector(self):
        self.assertTrue(daily_horoscope.date_selector() == 'yesterday' or 'today' or 'tomorrow')
    
    def test_Horoscope_dipslay(self):
        self.assertTrue(type(daily_horoscope.horoscope(9,'today')) == str)
    
    def test_Horoscope_dipslay(self):
        self.assertTrue(type(daily_horoscope.horoscope(9,'tomorrow')) == str)
    
    def test_Horoscope_dipslay(self):
        self.assertTrue(type(daily_horoscope.horoscope(9,'yesterday')) == str)
    
    def test_Horoscope_dipslay(self):
        self.assertTrue(type(daily_horoscope.horoscope(9,'yesterday')) == str)
    
    def test_Horoscope_dipslay(self):
        self.assertTrue(type(daily_horoscope.horoscope(9,'yesterday')) == str)
    
    def test_Horoscope_dipslay(self):
        self.assertTrue(type(daily_horoscope.horoscope(9,'yesterday')) == str)
    
    def test_Horoscope_dipslay(self):
        self.assertTrue(type(daily_horoscope.horoscope(9,'yesterday')) == str)
    
    def test_Horoscope_dipslay(self):
        self.assertTrue(type(daily_horoscope.horoscope(9,'yesterday')) == str)
    
    def test_Horoscope_dipslay(self):
        self.assertTrue(type(daily_horoscope.horoscope(9,'yesterday')) == str)
   
    
    def test_ignore(self):
        pass
    
    def test_mode(self):
        pass
    
  
if __name__ == '__main__': 
    unittest.main() 
