# Alyssa Feagans 7/6/2023 - Outside Analytics Elevator Problem

## Python solution
    Input is an integer array with the first value being the starting floor
    Returns a string in format = "TOTAL_TRAVEL_TIME FLOOR, FLOOR, FLOOR"

    Script ignores duplicate floors back to back (can only visit a floor once without leaving)
    Assumes elevator has "infinite" positive and negative floors and there are no gaps in numbers in the elevator.
    Infinite being restricted to the available memory on the system being used to run.

    Dependencies: python >= 3.0
    Runtime: O(n) where n is length of input array (num of floors to visit)

    To run python script:
    $ python3 python/elevator.py 

    TESTS:
    Dependencies to run tests: Python 3.7+ or PyPy3

    Install pytest:
    $ pip install -U pytest

    Validate install: 
    $ pytest --version

    To run all tests:
    $ pytest python/test_elevator.py

    To get more info on a test:     
    $ pytest python/test_elevator.py -vv

### TODOS:
- ~~Python - return output instead of printing~~
- Python - allow user to input example through command line
- ~~Write tests for python solution~~
- Write a solution as a bash script
- Write a solution in Java
- Write a solution in C
- Test in parallels on windows machine