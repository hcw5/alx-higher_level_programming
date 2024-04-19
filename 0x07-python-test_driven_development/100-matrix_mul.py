#!/usr/bin/python3
"""A module thats contains a function that multiplies 2 matrices"""


def matrix_mul(m_a, m_b):
    """Multiples two matrices that are conformable"""
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    if not all((isinstance(row, list) for row in m_a)):
        raise TypeError("m_a must be a list of lists")
    if not all((isinstance(row, list) for row in m_b)):
        raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not all((type(x) in [int, float] for row in m_a for x in row)):
        raise TypeError("m_a should contain only integers or floats")
    if not all((type(x) in [int, float] for row in m_b for x in row)):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(m_a[0]) == len(row) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(m_b[0]) == len(row) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    return [[sum(a * b for a, b in zip(x_row, y_col)) for y_col in zip(*m_b)]
            for x_row in m_a]
