class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight

def fractionalKnapsack(W, arr):
    arr.sort(key=lambda x: (x.profit / x.weight), reverse=True)
    finalvalue = 0.0

    for item in arr:
        if item.weight <= W:
            W -= item.weight
            finalvalue += item.profit
        else:
            finalvalue += item.profit * W / item.weight
            break

    return finalvalue

if __name__ == "__main__":
    # Take input for knapsack capacity
    W = float(input("Enter the knapsack capacity: "))

    # Take input for the number of items
    n = int(input("Enter the number of items: "))

    # Take input for each item's profit and weight
    arr = []
    for i in range(n):
        profit = float(input(f"Enter profit for item {i + 1}: "))
        weight = float(input(f"Enter weight for item {i + 1}: "))
        arr.append(Item(profit, weight))

    # Calculate the maximum value in the knapsack
    max_val = fractionalKnapsack(W, arr)
    print("Maximum value in Knapsack =", max_val)
