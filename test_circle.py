import unittest
import math
from circle import area, perimeter


class TestCircle(unittest.TestCase):
    """Тесты для функций круга"""

    def test_area_positive_radius(self):
        """Тест площади круга с положительным радиусом"""
        self.assertAlmostEqual(area(5), math.pi * 5 * 5, places=10)
        self.assertAlmostEqual(area(1), math.pi, places=10)
        self.assertAlmostEqual(area(10), math.pi * 100, places=10)

    def test_area_zero_radius(self):
        """Тест площади круга с нулевым радиусом"""
        self.assertEqual(area(0), 0)

    def test_area_float_radius(self):
        """Тест площади круга с дробным радиусом"""
        self.assertAlmostEqual(area(2.5), math.pi * 2.5 * 2.5, places=10)
        self.assertAlmostEqual(area(0.5), math.pi * 0.25, places=10)

    def test_perimeter_positive_radius(self):
        """Тест периметра круга с положительным радиусом"""
        self.assertAlmostEqual(perimeter(5), 2 * math.pi * 5, places=10)
        self.assertAlmostEqual(perimeter(1), 2 * math.pi, places=10)
        self.assertAlmostEqual(perimeter(10), 2 * math.pi * 10, places=10)

    def test_perimeter_zero_radius(self):
        """Тест периметра круга с нулевым радиусом"""
        self.assertEqual(perimeter(0), 0)

    def test_perimeter_float_radius(self):
        """Тест периметра круга с дробным радиусом"""
        self.assertAlmostEqual(perimeter(2.5), 2 * math.pi * 2.5, places=10)
        self.assertAlmostEqual(perimeter(0.5), 2 * math.pi * 0.5, places=10)

    def test_area_negative_radius(self):
        """Тест площади круга с отрицательным радиусом (должно вернуть положительное значение)"""
        # Математически площадь всегда положительна, но функция может вернуть положительное значение
        result = area(-5)
        self.assertAlmostEqual(result, math.pi * 25, places=10)

    def test_perimeter_negative_radius(self):
        """Тест периметра круга с отрицательным радиусом (должно вернуть отрицательное значение)"""
        result = perimeter(-5)
        self.assertAlmostEqual(result, 2 * math.pi * (-5), places=10)


if __name__ == '__main__':
    unittest.main()

