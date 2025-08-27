def calculate_gcd(a, b):
    """Calculate the Greatest Common Divisor using Euclidean algorithm."""
    while b:
        a, b = b, a % b
    return a

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
    print("Welcome to LCM Calculator!")
    
    while True:
        try:
            n = int(input("\nHow many numbers do you want to find LCM of? (Enter a number >= 2): "))
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
            
            result = calculate_multiple_lcm(numbers)
            print(f"\nThe LCM of {numbers} is: {result}")
            
            choice = input("\nDo you want to calculate another LCM? (yes/no): ").lower()
            if choice != 'yes':
                break
                
        except ValueError:
            print("Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    main()
