'''
Use unittest.TestCase methods to confirm that the addition and subtraction of date and timedelta objects 
produce correct results'''

from datetime import date
from datetime import timedelta
import unittest

class date_obj(unittest.TestCase):
    
    def test_add(self):
        
        # print('Today is:', date.today)
        random_days = timedelta(days=6)

        add_day = random_days + date.today()
        self.assertEqual(add_day, date.today() + timedelta(days=6))

    def test_subtract(self): 
        # print('Today is:', date.today())
        christmas = date(2024,12,25)

        sub_day = christmas - date.today()
        self.assertEqual(sub_day, christmas - date.today())

# assignment = date_obj()
# print('After adding 6 days:', assignment.add())
# print('Days till Christmas:', assignment.subtract())

if __name__ == '__main__':
    unittest.main()


# must use date.today() with parentheses because we are calling a function
# must use unittest.TestCase inside class date_obj(unittest.TestCase) because need to inherit it to function in the class
