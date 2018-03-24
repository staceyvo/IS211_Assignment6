#function to convert celsius to kelvin, takes a float, returns kelvin temp
def convertCelsiusToKelvin(degrees):
    return degrees + 273.15


#function to convert celsius to fahrenheit, takes a float, returns fahrenheit temp
def convertCelsiusToFahrenheit(degrees):
    return (degrees * 1.8) + 32


#call function several times - test 5 cases against 0.0, use print statements
def test_convertCelsiusToKelvin():
    assert -99725.85 == convertCelsiusToKelvin(-99999)
    assert 273.1488 == convertCelsiusToKelvin(-.0012)
    assert 273.15 == convertCelsiusToKelvin(0)
    assert 273.174 == convertCelsiusToKelvin(.024)
    assert 2798.15 == convertCelsiusToKelvin(2525)


def test_convertCelsiusToFahrenheit():
    assert -142645 == convertCelsiusToFahrenheit(-79265)
    assert 31.9883 == convertCelsiusToFahrenheit(-.0065)
    assert 32 == convertCelsiusToFahrenheit(0)
    assert 32.045 == convertCelsiusToFahrenheit(.025)
    assert 15101.6 == convertCelsiusToFahrenheit(8372)


#implement functions correctly and run more tests


#repeat process creating 6 functions to test
def convertFahrenheitToCelsius(degrees):
    return (degrees - 32) * 5.0/9


def convertFahrenheitToKelvin(degrees):
    return (degrees + 459.67) * 5 / 9


def convertKelvinToFahrenheit(degrees):
    return (degrees * 9.0/5) - 459.67


def convertKelvinToCelsius(degrees):
    return degrees - 273.15


def test_convertFahrenheitToCelsius():
    assert -3559.4444444444443 == convertFahrenheitToCelsius(-6375)
    assert -17.78472222222222 == convertFahrenheitToCelsius(-.0125)
    assert -17.77777777777778 == convertFahrenheitToCelsius(0)
    assert -17.730555555555554 == convertFahrenheitToCelsius(.085)
    assert 1803.3333333333333 == convertFahrenheitToCelsius(3278)


def test_convertFahrenheitToKelvin():
    assert -4461.85 == convertFahrenheitToKelvin(-8491)
    assert 255.3178 == convertFahrenheitToKelvin(-.09796)
    assert 255.3722222222222 == convertFahrenheitToKelvin(0)
    assert 255.40722222222223 == convertFahrenheitToKelvin(.063)
    assert 4532.038888888888 == convertFahrenheitToKelvin(7698)


def test_convertKelvinToFahrenheit():
    assert -13927.27 == convertKelvinToFahrenheit(-7482)
    assert -459.8428 == convertKelvinToFahrenheit(-.096)
    assert -459.67 == convertKelvinToFahrenheit(0)
    assert -458.5396 == convertKelvinToFahrenheit(.628)
    assert 168236.33 == convertKelvinToFahrenheit(93720)


def test_convertKelvinToCelsius():
    assert -86571.15 == convertKelvinToCelsius(-86298)
    assert -273.2138 == convertKelvinToCelsius(-.0638)
    assert -273.15 == convertKelvinToCelsius(0)
    assert -273.0748 == convertKelvinToCelsius(.0752)
    assert 92099.85 == convertKelvinToCelsius(92373)


if __name__ == '__main__':
    test_convertCelsiusToKelvin()
    test_convertCelsiusToFahrenheit()
    test_convertFahrenheitToCelsius()
    test_convertFahrenheitToKelvin()
    test_convertKelvinToFahrenheit()
    test_convertKelvinToCelsius()
