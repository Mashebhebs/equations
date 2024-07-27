def get_numeric_value(prompt):
    while True:
        value = input(prompt)
        if is_valid_number(value):
            return float(value)

        else:
            print("Enter a valid number!!")
            continue
    
def is_valid_number(value):
    if value.replace(".","",1).replace("/","",1).replace("-","",1).isdigit():
        if "/" in value:
           denominator = value.split("/")[1]
           if int(denominator) == 0:
               return False
        return True
    return False

   
