import unittest


class ConversionNotPossible(Exception):
    pass



def convert(fromUnit, toUnit, value):
    #check conversion exception
    distance = ['millimeters', 'centimeters', 'meters', 'kilometers']
    temperature = ['kelvin', 'fahrenheit', 'celsius']

    if fromUnit in distance and toUnit in temperature or fromUnit in temperature and toUnit in distance:
        raise ConversionNotPossible('Dimensions not compatible')

    #perform correct conversion



if __name__ == '__main__':
    pass
