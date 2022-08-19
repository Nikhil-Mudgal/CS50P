import pytest

from calculator import squared

def test_postive():
    assert squared(2) == 4
    assert squared(3) == 9

def test_negative():
    assert squared(-2) == 4
    assert squared(-3) == 9

def test_zero():
    assert squared(0) == 0

def test_str():
    with pytest.raises(TypeError):
        squared("cat")



















# import randoms
# from calculator import squared

# def main():
#     test_squared()


# def test_square():
#     if squared() != 4: # even though squared function is broken this is a corner case 
#         print("2 squared was not 4")
#     if squared(3) != 9: 
#         print("3 sqaured was not 9")

# def test_squared():
#     try:
#         assert squared(2) == 4
#     except AssertionError:
#         print("2 sqaured was not 4")
#     try:
#         assert squared(3) == 9
#     except AssertionError:
#         print("3 sqaured was not 9")
#     try:
#         assert squared(-3) == 9
#     except AssertionError:
#         print("-3 sqaured was not 9")
#     try:
#         assert squared(-2) == 4
#     except AssertionError:
#         print("-2 sqaured was not 4")
#     try:
#         assert squared(0) == 0
#     except AssertionError:
#         print("0 sqaured was not 0")

# if __name__ == "__main__" :
#     main()