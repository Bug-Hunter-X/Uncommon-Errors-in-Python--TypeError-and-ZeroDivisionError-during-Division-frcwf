def function_with_uncommon_error(x, y):
    try:
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Operands must be numeric")
        if y == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        result = x / y
        return result
    except TypeError as e:
        print(f"TypeError: {e}")
        return None
    except ZeroDivisionError as e:
        print(f"ZeroDivisionError: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None