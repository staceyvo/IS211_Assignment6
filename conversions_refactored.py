import unittest


class ConversionNotPossible(Exception):
    pass



def convert(fromUnit, toUnit, value):
    #check conversion exception
    distance = ['meters', 'miles', 'feet', 'yards', 'inches']
    temperature = ['kelvin', 'fahrenheit', 'celsius']

    if fromUnit in distance and toUnit in temperature or fromUnit in temperature and toUnit in distance:
        raise ConversionNotPossible('Dimensions not compatible')


    #perform correct conversion
    if fromUnit == 'kelvin':
        if toUnit == 'kelvin':
            return value
        if toUnit == 'fahrenheit':
            return (value * 9.0/5) - 459.67
        #convert kelvin to celsius
        return value - 273.15

    if fromUnit == 'fahrenheit':
        if toUnit == 'fahrenheit':
            return value
        if toUnit == 'kelvin':
            return (value + 459.67) * 5 / 9
        #convert fahrenheit to celsius
        return (value - 32) * 5.0/9

    if fromUnit == 'celsius':
        if toUnit == 'celsius':
            return value
        if toUnit == 'fahrenheit':
            return (value * 1.8) + 32
        #convert celsius to kelvin
        return value + 273.15

    


if __name__ == '__main__':
    pass
