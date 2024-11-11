fibonacci = [1, 1]

while True:
    next_number = fibonacci[-1] + fibonacci[-2]

    if next_number > 55:  
        break
    fibonacci.append(next_number)    

    
print(fibonacci)