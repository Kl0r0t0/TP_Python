def factorial (n): 
    """En base al numero ingresado, se calcula el resultado de su factorial"""
    #El programa compara n con 0, y si n no es 0 se le va restando 1, mientras el n original se multiplica por el n-1
    if n == 0:
        return 1
    else: 
        return n * factorial(n - 1) 
    


print(factorial(4))

