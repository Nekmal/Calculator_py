#!/usr/bin/env python3
"""
Simple Calculator
Main application file

This calculator performs basic arithmetic operations on two numbers.
"""

from calculator_functions import add, subtract, multiply, divide, get_operation_symbol
from utils import get_number_input, display_result, display_welcome, display_goodbye


def main():
    """Main calculator application loop"""
    display_welcome()
    
    while True:
        try:
            # Get first number
            print("\n" + "="*40)
            num1 = get_number_input("Enter the first number: ")
            
            # Get second number
            num2 = get_number_input("Enter the second number: ")
            
            # Display operation menu
            print("\nChoose an operation:")
            print("1. Addition (+)")
            print("2. Subtraction (-)")
            print("3. Multiplication (*)")
            print("4. Division (/)")
            
            # Get operation choice
            while True:
                choice = input("Enter your choice (1-4): ").strip()
                if choice in ['1', '2', '3', '4']:
                    break
                print("Invalid choice! Please enter 1, 2, 3, or 4.")
            
            # Perform calculation
            if choice == '1':
                result = add(num1, num2)
                operation = '+'
            elif choice == '2':
                result = subtract(num1, num2)
                operation = '-'
            elif choice == '3':
                result = multiply(num1, num2)
                operation = '*'
            elif choice == '4':
                result = divide(num1, num2)
                operation = '/'
            
            # Display result
            display_result(num1, num2, operation, result)
            
            # Ask if user wants to continue
            print("\n" + "-"*40)
            continue_choice = input("Do you want to perform another calculation? (y/n): ").strip().lower()
            if continue_choice not in ['y', 'yes']:
                break
                
        except KeyboardInterrupt:
            print("\n\nCalculation interrupted by user.")
            break
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}")
            continue_choice = input("Do you want to try again? (y/n): ").strip().lower()
            if continue_choice not in ['y', 'yes']:
                break
    
    display_goodbye()


if __name__ == "__main__":
    main()