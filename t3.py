#!/bin/python3

def ping_pong(n):
    ''' return a for-loop solution '''
    res = []
    for i in range(1, n+1):
        print(check_value(i))
        res.append(check_value(i))    
    return res            

# def ping_pong(n):
#     ''' return a generator solution '''
#     value = get_value(n)
#     for _ in get_value(n):
#         print(next(value))

# def get_value(n):
#     ''' return a for-loop solution '''
#     i = 1
#     while i < n: 
#         yield check_value(i)  
#         i += 1  

def check_value(i):
    ''' return the int or the alternative string.  
    This is the engine of the script. '''
    if i%3 == 0: 
        if i%5 == 0:
            # If i is a multiple of both 3 and 5, print PingPong.
            # print('PingPong')
            return ('PingPong')
        else:
            # If i is a multiple of 3 (but not 5), print Ping.
            # print('Ping')
            return('Ping')
    else:         
        if i%5 == 0:
            # If i is a multiple of 5 (but not 3), print Pong.
            # print('Pong')
            return('Pong')
        else: 
            # If i is not a multiple of 3 or 5, print the value of i.
            # print(i)
            return(i)

if __name__ == '__main__':
    n = int(input('input a positive number: ').strip())
    ping_pong(n)

