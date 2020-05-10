#Recursive function to calculate nth number of Fibonnacci series
#If input is wrong, returns -1
def NthNumberOfFibonacciSeries(n):
    if n <= 0:
        return -1
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return NthNumberOfFibonacciSeries(n - 1) + NthNumberOfFibonacciSeries(n - 2)
 
#Examples
if __name__ == '__main__':
    print('Enter n: ')
    n = int(input())
    print(n, ' nth number of Fibonnaci series is:')
    print(NthNumberOfFibonacciSeries(n))