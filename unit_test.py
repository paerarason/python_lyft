import unittest
from datetime import datetime
from Factory import carFactory
factory=carFactory()
class TestCalliope(unittest.TestCase):
    def test_battery_served(self):
        today=datetime.today().date()
        last_date=today.replace(year=today.year-3)
        current_mileage=0
        last_mileage=0
        car=factory.create_calliope(today,last_date,current_mileage,last_mileage)
        self.assertTrue(car.needs_service())
    
    def test_battery_shouldnot(self):
        today=datetime.today().date()
        last_date=today.replace(year=today.year-1)
        current_mileage=0
        last_mileage=0
        car=factory.create_calliope(today,last_date,current_mileage,last_mileage)
        self.assertFalse(car.needs_service())

    def test_engine_should(self):
        today=datetime.today().date()
        last_date=today.replace(year=today.year-1)
        current_mileage=30001
        last_mileage=0
        car=factory.create_calliope(today,last_date,current_mileage,last_mileage)
        self.assertTrue(car.needs_service())
  
    def test_engine_shouldnot(self):
        today=datetime.today().date()
        last_date=today.replace(year=today.year-1)
        current_mileage=30000
        last_mileage=0
        car=factory.create_calliope(today,last_date,current_mileage,last_mileage)
        self.assertFalse(car.needs_service())

#test class for Glissade car 
class TestGlissade(unittest.TestCase):
    def test_battery_served(self):
        today=datetime.today().date()
        last_date=today.replace(year=today.year-3)
        current_mileage=0
        last_mileage=0    
        car=factory.create_glissade(today,last_date,current_mileage,last_mileage)
        self.assertTrue(car.needs_service())
   
    def test_battery_shouldnot(self):
        today=datetime.today().date()
        last_date=today.replace(year=today.year-1)
        current_mileage=0
        last_mileage=0
        factory=carFactory()
        car=factory.create_glissade(today,last_date,current_mileage,last_mileage)
        self.assertFalse(car.needs_service())

    def test_engine_should(self):
        today=datetime.today().date()
        last_date=today.replace(year=today.year-1)
        current_mileage=60001
        last_mileage=0
        car=factory.create_glissade(today,last_date,current_mileage,last_mileage)
        self.assertTrue(car.needs_service())
  
    def test_engine_shouldnot(self):
        today=datetime.today().date()
        last_date=today.replace(year=today.year-1)
        current_mileage=60000
        last_mileage=0
        car=factory.create_glissade(today,last_date,current_mileage,last_mileage)
        self.assertFalse(car.needs_service())


#test cases for the Palindrome cars
class TestPalindrome(unittest.TestCase):
    def test_battery_served(self):
        today=datetime.today().date()
        last_date=today.replace(year=today.year-3)
        car=factory.create_palindrome(today, last_date,warning_light_is_on=False)
        self.assertTrue(car.needs_service())
   
    def test_battery_shouldnot(self):
        today=datetime.today().date()
        last_date=today.replace(year=today.year-1)
        factory=carFactory()
        car=factory.create_palindrome(today, last_date,warning_light_is_on=False)
        self.assertFalse(car.needs_service())

    def test_engine_should(self):
        today=datetime.today().date()
        last_date=today.replace(year=today.year-1)
        
        car=factory.create_palindrome(today, last_date,warning_light_is_on=True)
        self.assertTrue(car.needs_service())
   
    def test_engine_shouldnot(self):
        today=datetime.today().date()
        last_date=today.replace(year=today.year-1)       
        car=factory.create_palindrome(today, last_date,warning_light_is_on=False)
        self.assertFalse(car.needs_service())

#test the car for the RORSCHACH

class TestRorschach(unittest.TestCase):
    def test_battery_served(self):
        today=datetime.today().date()
        last_date=today.replace(year=today.year-5)
        current_mileage=0
        last_mileage=0 
        car=factory.create_rorschach(today,last_date,current_mileage,last_mileage)
        self.assertTrue(car.needs_service())
 
    def test_battery_shouldnot(self):
        today=datetime.today().date()
        last_date=today.replace(year=today.year-1)
        current_mileage=0
        last_mileage=0
        factory=carFactory()
        car=factory.create_rorschach(today,last_date,current_mileage,last_mileage)
        self.assertFalse(car.needs_service())
    def test_engine_should(self):
        today=datetime.today().date()
        last_date=today.replace(year=today.year-3)
        current_mileage=60001
        last_mileage=0
        car=factory.create_rorschach(today,last_date,current_mileage,last_mileage)
        self.assertTrue(car.needs_service())
    def test_engine_shouldnot(self):
        today=datetime.today().date()
        last_date=today.replace(year=today.year-3)
        current_mileage=60000
        last_mileage=0
        car=factory.create_rorschach(today,last_date,current_mileage,last_mileage)
        self.assertFalse(car.needs_service())


# test for the Thovex
class TestThovex(unittest.TestCase):
    def test_battery_served(self):
        today=datetime.today().date()
        last_date=today.replace(year=today.year-5)
        current_mileage=0
        last_mileage=0
        
        car=factory.create_thovex(today,last_date,current_mileage,last_mileage)
        self.assertTrue(car.needs_service())
    def test_battery_shouldnot(self):
        today=datetime.today().date()
        last_date=today.replace(year=today.year-3)
        current_mileage=0
        last_mileage=0
        car=factory.create_thovex(today,last_date,current_mileage,last_mileage)
        self.assertFalse(car.needs_service())

    def test_engine_should(self):
        today=datetime.today().date()
        last_date=today.replace(year=today.year-1)
        current_mileage=30001
        last_mileage=0
        car=factory.create_thovex(today,last_date,current_mileage,last_mileage)
        self.assertTrue(car.needs_service())
    def test_engine_shouldnot(self):
        today=datetime.today().date()
        last_date=today.replace(year=today.year-1)
        current_mileage=30000
        last_mileage=0
        car=factory.create_thovex(today,last_date,current_mileage,last_mileage)
        self.assertFalse(car.needs_service())
if __name__ == '__main__':
    unittest.main()