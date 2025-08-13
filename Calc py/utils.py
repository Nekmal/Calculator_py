"""
Utility Functions
Helper functions for input/output and display formatting
"""

from calculator_functions import is_integer


def get_number_input(prompt):
    """
    Get a valid number input from the user
    
    Args:
        prompt (str): Message to display to user
        
    Returns:
        float: Valid number entered by user
    """
    while True:
        try:
            user_input = input(prompt).strip()
            number = float(user_input)
            return number
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def format_number(number):
    """
    Format a number for display (remove unnecessary decimal places)
    
    Args:
        number (float): Number to format
        
    Returns:
        str: Formatted number as string
    """
    if is_integer(number):
        return str(int(number))
    else:
        # Round to 6 decimal places to avoid floating point precision issues
        return f"{number:.6f}".rstrip('0').rstrip('.')


def display_result(num1, num2, operation, result):
    """
    Display the calculation result in a formatted way
    
    Args:
        num1 (float): First number
        num2 (float): Second number
        operation (str): Operation symbol
        result (float): Calculation result
    """
    formatted_num1 = format_number(num1)
    formatted_num2 = format_number(num2)
    formatted_result = format_number(result)
    
    print(f"\n{'='*40}")
    print("CALCULATION RESULT")
    print(f"{'='*40}")
    print(f"{formatted_num1} {operation} {formatted_num2} = {formatted_result}")
    print(f"{'='*40}")


def display_welcome():
    """Display welcome message"""
    print("*" * 50)
    print("*" + " " * 48 + "*")
    print("*" + "        WELCOME TO SIMPLE CALCULATOR        ".center(48) + "*")
    print("*" + " " * 48 + "*")
    print("*" * 50)
    print("\nThis calculator can perform basic arithmetic operations:")
    print("• Addition")
    print("• Subtraction") 
    print("• Multiplication")
    print("• Division")


def display_goodbye():
    """Display goodbye message"""
    print("\n" + "*" * 50)
    print("*" + " " * 48 + "*")
    print("*" + "      THANK YOU FOR USING CALCULATOR!      ".center(48) + "*")
    print("*" + " " * 48 + "*")
    print("*" * 50)
    print("Goodbye! 👋")


def display_error(error_message):
    """
    Display error message in formatted way
    
    Args:
        error_message (str): Error message to display
    """
    print(f"\n❌ ERROR: {error_message}")