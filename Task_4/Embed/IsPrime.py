def isPrime(n):
    
    #Edge case
    if (n <= 1):
        return False;

    #Check from 2 to n-1 
    for i in range(2, n, 1):
        if (n % i == 0):
            return False;
    return True;
