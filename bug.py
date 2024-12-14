def function_with_uncommon_error(x, y):
    try:
        result = x / y
        return result
    except TypeError:
        print("TypeError: Cannot divide by non-numeric type")
        return None
    except ZeroDivisionError:
        print("ZeroDivisionError: Cannot divide by zero")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None