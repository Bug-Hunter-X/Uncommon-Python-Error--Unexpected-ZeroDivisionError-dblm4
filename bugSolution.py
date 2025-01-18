def function_with_uncommon_error(a, b):
    if a == 0:
        return float('inf') # Handle division by zero by returning infinity or a suitable alternative
    return a + b

result = function_with_uncommon_error(0,10)
print(result) # Output: inf

#Alternative solution using try-except block
def function_with_uncommon_error(a, b):
    try:
        return b / a
    except ZeroDivisionError:
        return float('inf') # Handle division by zero by returning infinity or a suitable alternative
result = function_with_uncommon_error(0, 10)
print(result) #Output: inf