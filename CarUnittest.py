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
        
        
    ###Bogdan
    def test_statementCoverage(self):
        car = Car(0, 0, "N")
        car.go("R")
        self.assertEqual(car.facing, "E")
        car = Car(0, 0, "E")
        car.go("R")
        self.assertEqual(car.facing, "S")
        car = Car(0, 0, "S")
        car.go("R")
        self.assertEqual(car.facing, "W")
        car = Car(0, 0, "W")
        car.go("R")
        self.assertEqual(car.facing, "N")
        car = Car(0, 0, "N")
        car.go("L")
        self.assertEqual(car.facing, "W")
        car = Car(0, 0, "W")
        car.go("L")
        self.assertEqual(car.facing, "S")
        car = Car(0, 0, "S")
        car.go("L")
        self.assertEqual(car.facing, "E")
        car = Car(0, 0, "E")
        car.go("L")
        self.assertEqual(car.facing, "N")
        car = Car(-1, -1, "N")
        car.go("M")
        self.assertEqual(car.y, 0)
        car = Car(100, 100, "E")
        car.go("M")
        self.assertEqual(car.x, 7)
        car = Car(1, 1, "S")
        car.go("M")
        self.assertEqual(car.y, 2)
        car = Car(1, 1, "W")
        car.go("M")
        self.assertEqual(car.x, 0)

    def test_branchCoverage(self):
        car = Car(0, 0, "N")
        car.go("R")
        self.assertEqual(car.facing, "E")
        car = Car(0, 0, "E")
        car.go("R")
        self.assertEqual(car.facing, "S")
        car = Car(0, 0, "S")
        car.go("R")
        self.assertEqual(car.facing, "W")
        car = Car(0, 0, "W")
        car.go("R")
        self.assertEqual(car.facing, "N")
        car = Car(0, 0, "N")
        car.go("L")
        self.assertEqual(car.facing, "W")
        car = Car(0, 0, "W")
        car.go("L")
        self.assertEqual(car.facing, "S")
        car = Car(0, 0, "S")
        car.go("L")
        self.assertEqual(car.facing, "E")
        car = Car(0, 0, "E")
        car.go("L")
        self.assertEqual(car.facing, "N")
        car = Car(-1, -1, "N")
        car.go("M")
        self.assertEqual(car.y, 0)
        car = Car(100, 100, "E")
        car.go("M")
        self.assertEqual(car.x, 7)
        car = Car(1, 1, "S")
        car.go("M")
        self.assertEqual(car.y, 2)
        car = Car(1, 1, "W")
        car.go("M")
        self.assertEqual(car.x, 0)
        
    def test_conditioinCoverage(self):
        car = Car(0, 0, "N")
        car.go("R")
        self.assertEqual(car.facing, "E")
        car = Car(0, 0, "E")
        car.go("R")
        self.assertEqual(car.facing, "S")
        car = Car(0, 0, "S")
        car.go("R")
        self.assertEqual(car.facing, "W")
        car = Car(0, 0, "W")
        car.go("R")
        self.assertEqual(car.facing, "N")
        car = Car(0, 0, "N")
        car.go("L")
        self.assertEqual(car.facing, "W")
        car = Car(0, 0, "W")
        car.go("L")
        self.assertEqual(car.facing, "S")
        car = Car(0, 0, "S")
        car.go("L")
        self.assertEqual(car.facing, "E")
        car = Car(0, 0, "E")
        car.go("L")
        self.assertEqual(car.facing, "N")
        car = Car(-1, -1, "N")
        car.go("M")
        self.assertEqual(car.y, 0)
        car = Car(100, 100, "E")
        car.go("M")
        self.assertEqual(car.x, 7)
        car = Car(1, 1, "S")
        car.go("M")
        self.assertEqual(car.y, 2)
        car = Car(1, 1, "W")
        car.go("M")
        self.assertEqual(car.x, 0)
        car = Car(1, 1, "E")
        car.go("")
        self.assertEqual(car.x, 1)
        self.assertEqual(car.y, 1)
        self.assertEqual(car.facing, "E")

    def test_pathCoverage(self):
        return
    
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


# 7. Test pentru a verifica n valid pentru functia execute
    def test_execute_valid_n(self):
        # Test with a valid positive integer
        car = Car(3, 3, "N")
        car.execute("R", 5)
        self.assertEqual(car.facing, "E")

# 8. Test pentru a verifica n zero pentru functia execute
    def test_execute_zero_n(self):
        car = Car(3, 3, "N")
        # Test with zero
        with self.assertRaises(ValueError):
            car.execute("R", 0)

# 9. Test pentru a verifica n negativ pentru functia execute
    def test_execute_negative_n(self):
        car = Car(3, 3, "N")
        # Test with a negative integer
        with self.assertRaises(ValueError):
            car.execute("R", -5)

# 10. Test pentru a verifica n string pentru functia execute
    def test_execute_string_n(self):
        car = Car(3, 3, "N")
        # Test with a string
        with self.assertRaises(ValueError):
            car.execute("R", "5")

# Analiza valorilor de frontiera
    def test_move_north_at_top_edge(self):
        car = Car(3, 0, "N")
        car.go("M")
        self.assertEqual((car.x, car.y), (3, 0))

    def test_move_south_at_bottom_edge(self):
        car = Car(3, 7, "S")
        car.go("M")
        self.assertEqual((car.x, car.y), (3, 7))

    def test_move_east_at_right_edge(self):
        car = Car(7, 3, "E")
        car.go("M")
        self.assertEqual((car.x, car.y), (7, 3))

    def test_move_west_at_left_edge(self):
        car = Car(0, 3, "W")
        car.go("M")
        self.assertEqual((car.x, car.y), (0, 3))

    def test_long_move_from_corner_to_corner(self):
        car = Car(0, 0, "E")
        car.go("MMMMMMMRRMMMMMMM")
        self.assertEqual((car.x, car.y), (7, 7))
    def test_turn_right_in_northeast_corner(self):
        car = Car(7, 0, "N")
        car.go("R")
        self.assertEqual(car.facing, "E")
        self.assertEqual((car.x, car.y), (7, 0))

    def test_turn_left_in_southwest_corner(self):
        car = Car(0, 7, "S")
        car.go("L")
        self.assertEqual(car.facing, "E")
        self.assertEqual((car.x, car.y), (0, 7))

    def test_sequence_moves_in_northeast_corner(self):
        car = Car(7, 0, "S")
        car.go("LLM")
        self.assertEqual((car.x, car.y), (7, 0))

    def test_sequence_moves_in_southwest_corner(self):
        car = Car(0, 7, "E")
        car.go("RRM")
        self.assertEqual((car.x, car.y), (0, 7))

    def test_complex_path_around_edges(self):
        car = Car(0, 0, "E")
        car.go("MMMMMMMRRMMMMMMMLLMMMMMMMRRMMMMMMM")
        self.assertEqual((car.x, car.y), (0, 0))

if __name__ == '__main__':
    car = Car(1, 1, "N")
    car.print()
    car.go("R")
    car.go("M")
    car.print()
    car.go("RMRMMMRMMM")
    car.print()

    unittest.main()