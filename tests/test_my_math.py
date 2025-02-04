import pytest

from src.my_math import sum, multiply, difference,absolute_sum,calculate_birth_year

def test_sum():
    res = sum(1,1)
    assert res == 2

# Work together
## Test multiply
def test_multiply():
    res = multiply(2,2)
    assert res == 4

# Check for understanding
## Test difference
def test_difference():
    res = difference(1,1)
    assert res == 0

# Work together
## Test absolute sum

def test_absolutesum():
    res = absolute_sum (-1,2)
    assert res == 3
# Check for understanding
## Test calculate age
def test_birth_year():
    res = calculate_birth_year (2025,19,False)
    assert res == 2005
def test_age():
    res = calculate_birth_year