#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Refactoring a module"""


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
            return float(value)
        if toUnit == 'fahrenheit':
            return float((value * 9.0/5) - 459.67)
        #convert kelvin to celsius
        return float(value - 273.15)

    if fromUnit == 'fahrenheit':
        if toUnit == 'fahrenheit':
            return float(value)
        if toUnit == 'kelvin':
            return float((value + 459.67) * 5 / 9)
        #convert fahrenheit to celsius
        return float((value - 32) * 5.0/9)

    if fromUnit == 'celsius':
        if toUnit == 'celsius':
            return float(value)
        if toUnit == 'fahrenheit':
            return float((value * 1.8) + 32)
        #convert celsius to kelvin
        return float(value + 273.15)

    if fromUnit == 'meters':
        if toUnit == 'meters':
            return float(value)
        if toUnit == 'miles':
            return float(value / 1609.344)
        if toUnit == 'feet':
            return float(value * 3.28)
        if toUnit == 'yards':
            return float(value / 0.9144)
        #convert meters to inches
        return float(value * 39.37007874)

    if fromUnit == 'miles':
        if toUnit == 'meters':
            return float(value * 1609.344)
        if toUnit == 'miles':
            return float(value)
        if toUnit == 'feet':
            return float(value * 5280)
        if toUnit == 'yards':
            return float(value * 1760)
        #convert miles to inches
        return float(value * 63360)

    if fromUnit == 'feet':
        if toUnit == 'meters':
            return float(value / 3.28)
        if toUnit == 'miles':
            return float(value * 0.00018939)
        if toUnit == 'feet':
            return float(value)
        if toUnit == 'yards':
            return float(value * 0.333333333333)
        #convert feet to inches
        return float(value * 12)

    if fromUnit == 'yards':
        if toUnit == 'meters':
            return float(value / 0.9144)
        if toUnit == 'miles':
            return float(value * 1.0/1760)
        if toUnit == 'feet':
            return float(value * 3)
        if toUnit == 'yards':
            return float(value)
        #convert yards to inches
        return float(value * 36)

    if fromUnit == 'inches':
        if toUnit == 'meters':
            return float(value * 0.0254)
        if toUnit == 'miles':
            return float(value * 0.0000157828283)
        if toUnit == 'feet':
            return float(value * 12)
        if toUnit == 'yards':
            return float(value * 0.027778)
        #convert inches to inches
        return float(value)



if __name__ == '__main__':
    pass
