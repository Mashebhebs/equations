from math import *
from get_numericial_value import *

def solution_exists(a,b,c):
    delta = pow(b,2) - 4*a*c

    if delta < 0:
        return False,"no solution"
    elif delta == 0:
        return True, "equal"
    return True, "unequal"

def solve(a,b,c):
    solutionExists = solution_exists(a,b,c)
    if (solutionExists[0] and solutionExists[1] == "equal"):
        x = (-b + sqrt(pow(b,2)-4*a*c))/(2*a)
        return f"The value of 𝑥: 𝑥 = {x}"
    elif (solutionExists[0] and solutionExists[1] == "unequal"):
        x = ( (-b - sqrt(pow(b,2)-4*a*c))/(2*a), (-b + sqrt(pow(b,2)-4*a*c))/(2*a))
        return f"The values of 𝑥: 𝑥 = {round(x[0],2)} or 𝑥 = {round(x[1],2)}."
    else:
        return f"There are no real roots for this equation."

if __name__ == "__main__":
    a = get_numeric_value("Enter the value of 'a' the coefficient of 𝑥²: ")
    b = get_numeric_value("Enter the value of 'b'(or 0 if it doesn't exist) the coefficient of 𝑥: ")
    c = get_numeric_value("Enter the value of 'c' the constant term: ")

    print(solve(a,b,c))