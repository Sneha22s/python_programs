radius = 26.0
print(f'Radius is {radius}')

my_int = 22
my_float = 10.0
my_bool = True
my_str = "My name is Sneha"

print(f'The datatype of my_int is {type(my_int)}')
print(f'The datatype of my_float is {type(my_float)}')
print(f'The datatype of my_bool is {type(my_bool)}')
print(f'The datatype of my_str is {type(my_str)}')


def calculator():
    print('inside the calculator method')
    a = input('Enter the first number: ')
    b = input('Enter the second number: ')
    #if type(a) is not int:
    a = int(a)
    #if type(b) is not int:
    b = int(b)
    while b == 0:
        print("Second number cannot be zero . Please enter one more time")
        new_b = input('Enter the second number again: ')
        new_b = int(new_b)
        if new_b != 0:
            b = new_b
            break
    add_numbers = a + b
    sub_numbers = a - b
    multiply_numbers = a * b
    divide_numbers = a/b
    print(f"The addition of {a} and {b} is {add_numbers}")
    print(f"The subtraction of {a} and {b} is {sub_numbers}")
    print(f"The multiplication of {a} and {b} is {multiply_numbers}")
    print(f"The Division of {a} and {b} is {divide_numbers}")

if __name__ == "__main__":
    print("Inside the main method..")
    calculator()
