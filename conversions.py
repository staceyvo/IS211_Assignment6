

#function to convert celsius to kelvin, takes a float, returns kelvin temp
def convertCelsiusToKelvin(degrees):
    return degrees + 273.15


#function to convert celsius to fahrenheit, takes a float, returns fahrenheit temp
def convertCelsiusToFahrenheit(degrees):
    return (degrees * 1.8) + 32


#repeat process creating 6 functions to test
def convertFahrenheitToCelsius(degrees):
    return (degrees - 32) * 5.0/9


def convertFahrenheitToKelvin(degrees):
    return (degrees + 459.67) * 5 / 9


def convertKelvinToFahrenheit(degrees):
    return (degrees * 9.0/5) - 459.67


def convertKelvinToCelsius(degrees):
    return degrees - 273.15


if __name__ == '__main__':
    print convertCelsiusToKelvin(10)
    print convertCelsiusToFahrenheit(10)
    print convertFahrenheitToCelsius(10)
    print convertFahrenheitToKelvin(10)
    print convertKelvinToFahrenheit(10)
    print convertKelvinToCelsius(10)
