import unittest
from conversions import *
from conversions_refactored import *


class TestCelsiusCase(unittest.TestCase):
    """Tests the conversions from celsius"""

    def test_convertCelsiusToKelvin(self):
        self.assertTrue(-99725.85 == convertCelsiusToKelvin(-99999))
        self.assertTrue(273.1488 == convertCelsiusToKelvin(-.0012))
        self.assertTrue(273.15 == convertCelsiusToKelvin(0))
        self.assertTrue(273.174 == convertCelsiusToKelvin(.024))
        self.assertTrue(2798.15 == convertCelsiusToKelvin(2525))

    def test_convertCelsiusToFahrenheit(self):
        self.assertTrue(-142645 == convertCelsiusToFahrenheit(-79265))
        self.assertTrue(31.9883 == convertCelsiusToFahrenheit(-.0065))
        self.assertTrue(32 == convertCelsiusToFahrenheit(0))
        self.assertTrue(32.045 == convertCelsiusToFahrenheit(.025))
        self.assertTrue(15101.6 == convertCelsiusToFahrenheit(8372))


class TestFahrenheitCase(unittest.TestCase):
    """Tests the conversions from fahrenheit"""

    def test_convertFahrenheitToCelsius(self):
        self.assertTrue(-3559.4444444444443 == convertFahrenheitToCelsius(-6375))
        self.assertTrue(-17.78472222222222 == convertFahrenheitToCelsius(-.0125))
        self.assertTrue(-17.77777777777778 == convertFahrenheitToCelsius(0))
        self.assertTrue(-17.730555555555554 == convertFahrenheitToCelsius(.085))
        self.assertTrue(1803.3333333333333 == convertFahrenheitToCelsius(3278))

    def test_convertFahrenheitToKelvin(self):
        self.assertTrue(-4461.85 == convertFahrenheitToKelvin(-8491))
        self.assertTrue(255.3178 == convertFahrenheitToKelvin(-.09796))
        self.assertTrue(255.3722222222222 == convertFahrenheitToKelvin(0))
        self.assertTrue(255.40722222222223 == convertFahrenheitToKelvin(.063))
        self.assertTrue(4532.038888888888 == convertFahrenheitToKelvin(7698))


class TestKelvinCase(unittest.TestCase):
    """Tests the conversions from kelvin"""

    def test_convertKelvinToFahrenheit(self):
        self.assertTrue(-13927.27 == convertKelvinToFahrenheit(-7482))
        self.assertTrue(-459.8428 == convertKelvinToFahrenheit(-.096))
        self.assertTrue(-459.67 == convertKelvinToFahrenheit(0))
        self.assertTrue(-458.5396 == convertKelvinToFahrenheit(.628))
        self.assertTrue(168236.33 == convertKelvinToFahrenheit(93720))

    def test_convertKelvinToCelsius(self):
        self.assertTrue(-86571.15 == convertKelvinToCelsius(-86298))
        self.assertTrue(-273.2138 == convertKelvinToCelsius(-.0638))
        self.assertTrue(-273.15 == convertKelvinToCelsius(0))
        self.assertTrue(-273.0748 == convertKelvinToCelsius(.0752))
        self.assertTrue(92099.85 == convertKelvinToCelsius(92373))

class TestConvert(unittest.TestCase):
    """Tests the conversions from distance to temperature"""

    def test_convert_exception(self):
        self.assertRaises(ConversionNotPossible, convert('meter', 'kelvin', 15))
        self.assertRaises(ConversionNotPossible, convert('miles', 'fahrenheit', 123))
        self.assertRaises(ConversionNotPossible, convert('celsius', 'meters', 834))
        self.assertRaises(ConversionNotPossible, convert('kelvin', 'meters', 369))

    def test_convert_miles_and_yards(self):
        self.assertTrue(15 == convert('miles', 'yards', 65))
        self.assertTrue(15 == convert('yards', 'miles', 65))

if __name__ == '__main__':
    unittest.main()
