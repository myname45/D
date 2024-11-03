# Global counter for steps
COUNT = 0

# Recursive Fibonacci function with step count
def recur_fibo(n):
    global COUNT
    COUNT += 1  # Increment step count for each function call
    if n <= 1:
        return n
    else:
        return recur_fibo(n - 1) + recur_fibo(n - 2)

# Iterative Fibonacci function with step count
def fib_iterative(n):
    global COUNT
    COUNT = 0  # Reset count for iterative approach
    first, sec = 0, 1
    series = []
    if n <= 0:
        return "Please enter a positive integer.", COUNT
    elif n == 1:
        series = [0]
        COUNT += 1  # For first comparison
        return series, COUNT
    else:
        for _ in range(n):
            series.append(first)
            COUNT += 1  # For appending to series
            nth = first + sec
            first, sec = sec, nth
            COUNT += 3  # For addition and assignments

    return series, COUNT

# Main function to handle menu and user input
def main():
    while True:
        global COUNT
        print("\nMenu:")
        print("1. Fibonacci Series using Iterative approach")
        print("2. Fibonacci Series using Recursive approach")
        print("3. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1 or choice == 2:
            n = int(input("Enter the number of terms (n): "))
            
            if n <= 0:
                print("Please enter a positive integer.")
                continue

            COUNT = 0  # Reset count before each run

            if choice == 1:
                # Iterative Fibonacci
                series, steps = fib_iterative(n)
                print("Fibonacci Series:", series)
                print("Steps required using Counter:", steps)

            elif choice == 2:
                # Recursive Fibonacci
                series = []
                for i in range(n):
                    series.append(recur_fibo(i))
                print("Fibonacci Series:", series)
                print("Steps required using Counter:", COUNT)

        elif choice == 3:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
