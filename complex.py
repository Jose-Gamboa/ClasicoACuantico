def sum_complex(c1, c2):
    """
    It takes two complex numbers, adds them together, and returns the result
    :param c1: A complex number in the form of a list
    :param c2: A complex number in the form of a list
    :return: The sum of the two complex numbers.
    """
    return c1[0] + c2[0], c1[1] + c2[1]


def product_complex(c1, c2):
    """
    It takes two complex numbers, multiplies them, and returns the result
    :param c1: The first complex number
    :param c2: the complex number to be multiplied
    :return: The product of two complex numbers.
    """
    return c1[0] * c2[0] - c1[1] * c2[1], c1[0] * c2[1] + c1[1] * c1[0]


def mod_complex(c):
    """
    It takes a complex number than input and returns its modulus
    :param c: a complex number
    :return: The modulus of the complex number.
    """
    return (c[0] ** 2 + c[1] ** 2) ** (1 / 2)
