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