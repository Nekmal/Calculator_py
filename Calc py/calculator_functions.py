"""
Calculator Functions
Contains all arithmetic operations for the simple calculator
"""


def add(a, b):
    """
    Add two numbers together
    
    Args:
        a (float): First number
        b (float): Second number
        
    Returns:
        float: Sum of a and b
    """
    return a + b


def subtract(a, b):
    """
    Subtract second number from first number
    
    Args:
        a (float): First number (minuend)
        b (float): Second number (subtrahend)
        
    Returns:
        float: Difference of a and b
    """
    return a - b


def multiply(a, b):
    """
    Multiply two numbers together
    
    Args:
        a (float): First number
        b (float): Second number
        
    Returns:
        float: Product of a and b
    """
    return a * b


def divide(a, b):
    """
    Divide first number by second number
    
    Args:
        a (float): Dividend
        b (float): Divisor
        
    Returns:
        float: Quotient of a divided by b
        
    Raises:
        ValueError: If divisor (b) is zero
    """
    if b == 0:
        raise ValueError("Error: Division by zero is not allowed!")
    return a / b


def get_operation_symbol(operation_number):
    """
    Get the mathematical symbol for an operation
    
    Args:
        operation_number (str): Operation choice ('1', '2', '3', or '4')
        
    Returns:
        str: Mathematical symbol (+, -, *, /)
    """
    symbols = {
        '1': '+',
        '2': '-',
        '3': '*',
        '4': '/'
    }
    return symbols.get(operation_number, '?')


def is_integer(number):
    """
    Check if a float is actually an integer value
    
    Args:
        number (float): Number to check
        
    Returns:
        bool: True if number is an integer, False otherwise
    """
    return number == int(number)