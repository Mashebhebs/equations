from get_numericial_value import *

def solve_equation(a,b):
    try:
        x = -1*b/a
        return f"The value of x = {round(x,2)}"
    except ZeroDivisionError:
        return f"Can not divide by Zero!"

if __name__ == "__main__":
    a = get_numeric_value("Enter the value of 'a' (The coefficient of x): ")
    b = get_numeric_value("Enter the value of 'b' (The constant value): ")
    print(solve_equation(a,b))