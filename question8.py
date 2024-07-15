
def compute_sum(numbers):
    return sum(numbers)


def compute_average(numbers):
    return sum(numbers) / len(numbers)


def compute_product(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product


def find_smallest(numbers):
    return min(numbers)


def find_largest(numbers):
    return max(numbers)


def main():
    
    numbers = []
    for i in range(4):
        num = int(input(f"Enter integer {i+1}: "))
        numbers.append(num)

    
    total_sum = compute_sum(numbers)
    average = compute_average(numbers)
    product = compute_product(numbers)
    smallest = find_smallest(numbers)
    largest = find_largest(numbers)

    print(f"Sum: {total_sum}")
    print(f"Average: {average}")
    print(f"Product: {product}")
    print(f"Smallest: {smallest}")
    print(f"Largest: {largest}")


if __name__ == "__main__":
    main()
