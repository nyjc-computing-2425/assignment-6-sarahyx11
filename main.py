from datetime import datetime
import time


# Part 1
def clock(n):
    '''
    take in integer n 
    prints out current time and updates it every second, for n number 
    of seconds in format of HH:MM:SS
    '''
    for i in range(n):
        convert = str(datetime.now().time())[:8]
        print(convert, end = "\r")
        time.sleep(1)
    return(convert)

# Part 2
def lcm(a, b):
    '''
    takes in integers a and b
    returns lowest common multiple of a and b
    '''
    valid = True
    a_original = a
    b_original = b
    while valid:
        if a < b:
            a += a_original
        elif b < a:
            b += b_original
        else:
            valid = False

    return(a)

#Part 3
def gcf(a, b):
    '''
    takes in integers a and b
    returns greatest common factor of a and b
    '''
    valid = True
    while valid:
        if b == 0:
            return(a)
            valid = False
        else:
            r = a % b
            a, b = b, r
