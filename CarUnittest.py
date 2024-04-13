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

# Partitionare de echivalenta
# 1. Test pentru a verifica coordonate valide
    def test_valid_coordinates(self):
        car = Car(3, 3, "N")
        self.assertEqual(car.x, 3)
        self.assertEqual(car.y, 3)

# 2. Test pentru a verifica coordonate invalide
    def test_invalid_coordinates(self):
        with self.assertRaises(ValueError):
            Car(-1, 3, "N")
        with self.assertRaises(ValueError):
            Car(3, 8, "N")

# 3. Test pentru a verifica directie valida
    def test_valid_direction(self):
        car = Car(3, 3, "N")
        self.assertEqual(car.facing, "N")

# 4. Test pentru a verifica directie invalida
    def test_invalid_direction(self):
        with self.assertRaises(ValueError):
            Car(3, 3, "X")

# 5. Test pentru verifica instructiune valida
    def test_valid_instruction(self):
            car = Car(3, 3, "N")
            car.go("LR")
            self.assertEqual(car.facing, "N")

# 6. Test pentru verifica instructiune invalida
    def test_invalid_instruction(self):
        with self.assertRaises(ValueError):
            car = Car(3, 3, "N")
            car.go("X") 

if __name__ == '__main__':
    car = Car(1, 1, "N")
    car.print()
    car.go("R")
    car.go("M")
    car.print()
    car.go("RMRMMMRMMM")
    car.print()

    unittest.main()