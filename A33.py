class Item:
    def __init__(self, profit, weight):  # Corrected to __init__
        self.profit = profit
        self.weight = weight

def fractionalKnapsack(W, arr):
    # Sort items by profit-to-weight ratio in descending order
    arr.sort(key=lambda x: (x.profit / x.weight), reverse=True)
    finalvalue = 0.0

    # Iterate through items
    for item in arr:
        if item.weight <= W:
            # If the item can be added in full
            W -= item.weight
            finalvalue += item.profit
        else:
            # If only part of the item can be added
            finalvalue += item.profit * W / item.weight
            break

    return finalvalue

if __name__ == "__main__":
    W = 50
    arr = [Item(60, 10), Item(100, 20), Item(120, 30)]
    max_val = fractionalKnapsack(W, arr)
    print("Maximum value in Knapsack =", max_val)
