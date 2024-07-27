def get_numeric_value(prompt):
    while True:
        value = input(prompt)
        if "'a'" in prompt and value.isdigit():
            if int(value) == 0:
                print("The value of 'a' can not be equal to zero!!")
                continue
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

   
