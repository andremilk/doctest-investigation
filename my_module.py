#!/usr/env python

MY_DICT = {'key1': 'value1', 'key2': 'value2'}
MY_STRING = 'My keys are: {}'.format(MY_DICT.keys())

def my_method1():
    """
    >>> my_method1()
    Traceback (most recent call last):
            ...
    Exception: My keys are: ['key2', 'key1']
    """
    raise Exception(MY_STRING)


def my_method2():
    """
    >>> my_method1()
    Exception: {MY_STRING}
    """
    pass

if __name__ == '__main__':
    import doctest
    print doctest.__file__
    doctest.testmod()
