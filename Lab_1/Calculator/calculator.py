#calculator.py

def sum(m,n):
    times = abs(n) # number of iterations
    inc = 1 if n > 0 else -1 # check if I need to sum or sub (if n is negative)
    for i in range(times): # loop 'times' for increment
        m += inc # increment
    return m # return result

def divide(m,n):
    if n == 0: raise ZeroDivisionError    
    times = 0 # result
    sign = 1 if ((n > 0) == (m > 0)) else -1 # if the sign is not equal, the sign is negative
    tmpM = abs(m) # ignore sign
    tmpN = abs(n) # ignore sign
    tmpM -= tmpN # first subtract tmpN
    while tmpM >= 0: # iterate while the tmpM var is positive, when is equal or less zero, exit while       
        times += 1 # accumulate which time the tmpN is subtracted from tmpM
        tmpM -= tmpN # subtract tmpN
    return times * sign # return result with sign

def main():
    print(f"Result is: {sum(10,3)}")

if __name__ == "__main__":
    main()
