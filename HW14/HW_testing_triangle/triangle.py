def get_triangle_side(s_value: str) -> float:
    """
    Value error. The value must be a float type.
    >>> get_triangle_side('asd')
    Traceback (most recent call last):
    ...
    ValueError: could not convert string to float: 'asd'

    Work with float.
    >>> get_triangle_side('2.25')
    5.25

    Work with integer.
    >>> get_triangle_side('2')
    2.0

    Negative value exception
    >>> get_triangle_side('0')
    Traceback (most recent call last):
    ...
    ValueError: The value must be positive
    """
    number = float(s_value)

    if number <= 0:
        raise ValueError('The value must be positive')
    else:
        return number


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)