from linear_equations import *

def solve_equation():
    a = get_numeric_value("Enter the value of 'a' (The coefficient of x): ")
    b = get_numeric_value("Enter the value of 'b' (The constant value): ")
    
    x = -1*b/a
    return f"The value of x = {round(x,2)}"

if __name__ == "__main__":
    print(solve_equation())