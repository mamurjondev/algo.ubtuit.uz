n = int(input())
def PrintFibonacci(length):
    #Initial variable for the base case. 
    first = 1
    second = 1
    length -= 2
    while length > 0:
        temp = second
        second = first + second
        first = temp
        length -= 1
    print(second)

if __name__ == "__main__":
    PrintFibonacci(n)    
