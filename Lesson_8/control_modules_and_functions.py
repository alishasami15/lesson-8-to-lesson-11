# function
def functionname (name):
    return  f"Hello,{name}!"

# calling the function
message = functionname ("Alisha")
print(message)


# control flow with function
def check_even_odd (number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
print(check_even_odd(7))

