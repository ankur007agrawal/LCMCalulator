def calculate_gcd(a, b):
    """Calculate the Greatest Common Divisor using Euclidean algorithm."""
    while b:
        a, b = b, a % b
    return a

def calculate_multiple_gcd(numbers):
    """Calculate the GCD (HCF) of multiple numbers."""
    result = numbers[0]
    for i in range(1, len(numbers)):
        result = calculate_gcd(result, numbers[i])
    return result

def calculate_lcm(a, b):
    """Calculate the Least Common Multiple of two numbers."""
    return abs(a * b) // calculate_gcd(a, b)

def calculate_multiple_lcm(numbers):
    """Calculate the LCM of multiple numbers."""
    lcm = numbers[0]
    for i in range(1, len(numbers)):
        lcm = calculate_lcm(lcm, numbers[i])
    return lcm

def main():
    print("Welcome to LCM and HCF Calculator!")
    
    while True:
        try:
            operation = input("\nWhat would you like to calculate? (lcm/hcf): ").lower()
            if operation not in ['lcm', 'hcf']:
                print("Please enter either 'lcm' or 'hcf'.")
                continue

            n = int(input(f"\nHow many numbers do you want to find {operation.upper()} of? (Enter a number >= 2): "))
            if n < 2:
                print("Please enter at least 2 numbers.")
                continue
            
            numbers = []
            for i in range(n):
                while True:
                    try:
                        num = int(input(f"Enter number {i+1}: "))
                        if num <= 0:
                            print("Please enter a positive number.")
                            continue
                        numbers.append(num)
                        break
                    except ValueError:
                        print("Invalid input! Please enter a valid positive integer.")
            
            if operation == 'lcm':
                result = calculate_multiple_lcm(numbers)
            else:
                result = calculate_multiple_gcd(numbers)
            
            print(f"\nThe {operation.upper()} of {numbers} is: {result}")
            
            choice = input(f"\nDo you want to calculate another {operation.upper()}? (yes/no): ").lower()
            if choice != 'yes':
                break
                
        except ValueError:
            print("Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    main()
