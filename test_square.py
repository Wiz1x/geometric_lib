import unittest
from square import area, perimeter


class TestSquare(unittest.TestCase):
    """Тесты для функций квадрата"""

    def test_area_positive_side(self):
        """Тест площади квадрата с положительной стороной"""
        self.assertEqual(area(4), 16)
        self.assertEqual(area(1), 1)
        self.assertEqual(area(10), 100)
        self.assertEqual(area(5), 25)

    def test_area_zero_side(self):
        """Тест площади квадрата с нулевой стороной"""
        self.assertEqual(area(0), 0)

    def test_area_float_side(self):
        """Тест площади квадрата с дробной стороной"""
        self.assertEqual(area(2.5), 6.25)
        self.assertEqual(area(0.5), 0.25)
        self.assertAlmostEqual(area(1.5), 2.25, places=10)

    def test_perimeter_positive_side(self):
        """Тест периметра квадрата с положительной стороной"""
        self.assertEqual(perimeter(4), 16)
        self.assertEqual(perimeter(1), 4)
        self.assertEqual(perimeter(10), 40)
        self.assertEqual(perimeter(5), 20)

    def test_perimeter_zero_side(self):
        """Тест периметра квадрата с нулевой стороной"""
        self.assertEqual(perimeter(0), 0)

    def test_perimeter_float_side(self):
        """Тест периметра квадрата с дробной стороной"""
        self.assertEqual(perimeter(2.5), 10.0)
        self.assertEqual(perimeter(0.5), 2.0)
        self.assertAlmostEqual(perimeter(1.5), 6.0, places=10)

    def test_area_negative_side(self):
        """Тест площади квадрата с отрицательной стороной (должно вернуть положительное значение)"""
        # Математически площадь всегда положительна, но функция может вернуть положительное значение
        self.assertEqual(area(-5), 25)

    def test_perimeter_negative_side(self):
        """Тест периметра квадрата с отрицательной стороной (должно вернуть отрицательное значение)"""
        self.assertEqual(perimeter(-5), -20)


if __name__ == '__main__':
    unittest.main()

