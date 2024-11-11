user_input = input("Enter a positive integer: ")

if user_input.isdigit():
    number = int(user_input)
    number_str = str(number)
    num_digits = len(number_str)
    
    total = 0

    for digit in number_str:
        total += int(digit) ** num_digits

    if number == total:
        print(f"{number} is an Armstrong Number")
    else:
        print(f"{number} is not an Armstrong Number")

else:
    print("It is an invalid entry. Don't use non-numeric, float, or negative values!")