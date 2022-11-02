def BilanganPrima(bilangan): 
    prima = True 
    for i in range(2, bilangan): 
        if (bilangan % i == 0): 
            prima = False 
            break 
    return prima
min = 1
max = 100
for i in range(min, max+1):
    if BilanganPrima(i):
        print(i, end=" ")
