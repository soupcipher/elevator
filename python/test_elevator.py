from elevator import *

def test_given_ex():
    assert elevator([12, 2, 9, 1, 32]) == "560 12, 2, 9, 1, 32"

def test_no_travel():
    assert elevator([12]) == "0 12"

def test_no_start():
    assert elevator([]) == "0 "

def test_large_travel_time():
    assert elevator([999, 2, 0, 13, 14]) == "10130 999, 2, 0, 13, 14"

def test_repeat_floors():
    assert elevator([44, 44, 45, 44, 44]) == "20 44, 45, 44"

def test_consecutive():
    assert elevator([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == "140 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15"

def test_negative():
    assert elevator([-4, 4]) == "80 -4, 4"

def test_ground_to_basement():
    assert elevator([0, -3]) == "30 0, -3"

def test_superstitous():
    assert elevator([1, 3, 4, 5, 6, 7, 9, 10, 11, 12, 14, 15, 16, 17]) == "160 1, 3, 4, 5, 6, 7, 9, 10, 11, 12, 14, 15, 16, 17"

def test_china():
    assert elevator([-1, 2, 3, 5, 10, 13]) == "140 -1, 2, 3, 5, 10, 13"

# Floors 1 to 99
def test_elevator_to_sky():
    long_list = list(range(1, 100))
    expected = "980 " + ", ".join(str(num) for num in long_list)
    assert elevator(long_list) == expected

# Floors 1 to 9999
def test_elevator_to_heaven():
    long_list = list(range(1, 10000))
    expected = "99980 " + ", ".join(str(num) for num in long_list)
    assert elevator(long_list) == expected