import unittest
from TSSCar import Car

class CarTest(unittest.TestCase):
    
    def test_turn_right_N_to_E(self):
        car = Car(0, 0, "N")
        car.go("R")
        self.assertEqual(car.facing, "E")

    def test_turn_right_E_to_S(self):
        car = Car(0, 0, "E")
        car.go("R")
        self.assertEqual(car.facing, "S")

    def test_turn_right_S_to_W(self):
        car = Car(0, 0, "S")
        car.go("R")
        self.assertEqual(car.facing, "W")

    def test_turn_right_W_to_N(self):
        car = Car(0, 0, "W")
        car.go("R")
        self.assertEqual(car.facing, "N")

    def test_turn_left_N_to_W(self):
        car = Car(0, 0, "N")
        car.go("L")
        self.assertEqual(car.facing, "W")

    def test_turn_left_W_to_S(self):
        car = Car(0, 0, "W")
        car.go("L")
        self.assertEqual(car.facing, "S")

    def test_turn_left_S_to_E(self):
        car = Car(0, 0, "S")
        car.go("L")
        self.assertEqual(car.facing, "E")

    def test_turn_left_E_to_N(self):
        car = Car(0, 0, "E")
        car.go("L")
        self.assertEqual(car.facing, "N")
        
    def test_move_North(self):
        car = Car(0, 0, "N")
        car.go("M")
        self.assertEqual(car.y, 0)
    
    def test_move_East(self):
        car = Car(0, 0, "E")
        car.go("M")
        self.assertEqual(car.x, 1)
    
    def test_move_South(self):
        car = Car(1, 1, "S")
        car.go("M")
        self.assertEqual(car.y, 2)
    
    def test_move_West(self):
        car = Car(1, 1, "W")
        car.go("M")
        self.assertEqual(car.x, 0)

if __name__ == '__main__':
    car = Car(1, 1, "N")
    car.print()
    car.go("R")
    car.go("M")
    car.print()
    car.go("RMRMMMRMMM")
    car.print()
    unittest.main()