limit = int(input("Enter a limit number: "))

prime_numbers = []

if limit <= 1:
    print(prime_numbers) 
else:
    for i in range(2, limit):
        for ii in range(2, i):
            if i % ii == 0:
               break
        else:
            prime_numbers.append(i)
    
    print(prime_numbers)
    