if __name__=="__main__":
    main()

def main():
    caculate_factorial()
    fibonacci()

def caculate_factorial(n):
    if n < 0:
        return -1
    elif n < 2:
        return 1
    else:
        return n * caculate_factorial (n-1) 
    print(caculate_factorial(5))

    def fibonacci(n):
        if n <= 1:
            return n
        else:
            return(fibonacci(n-1) + fibonacci(n-2) )
        n = 8
        for i in range():
            print(fibonacci(i)) 
            