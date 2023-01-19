def checker(var_1):
    if type(var_1) != float:
        raise TypeError(f"What are you doing????? It is calculator!! We can’t work with {type(var_1)}! "
        f"We need class float.")
    else:
        return var_1

def checker2(var_2):
    if type(var_2) != float:
        raise TypeError(f"What are you doing????? It is calculator!! We can’t work with {type(var_2)}! "
        f"We need class float.")
    else:
        return var_2
first_number=input("First number: ") # Має бути float(input("First number: "))
second_number=input("Second number: ") # Має бути float(input("Second number: "))
checker(first_number)
checker2(second_number)
print(f"{first_number} + {second_number} = {first_number+second_number}")