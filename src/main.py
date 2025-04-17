from calculator import Calculator
from string_utils import StringProcessor
from data_structures import CustomPriorityQueue
import random

def demonstrate_calculator():
    print("\n=== Calculator Demo ===")
    calc = Calculator(precision=2)
    
    # Basic operations
    result = calc.add(5.123, 3.789)
    print(f"5.123 + 3.789 = {result}")
    
    result = calc.divide(10, 3)
    print(f"10 / 3 = {result}")
    
    # Series calculation
    numbers = [1.1, 2.2, 3.3, 4.4, 5.5]
    result = calc.calculate_series_sum(numbers)
    print(f"Sum of {numbers} = {result}")
    
    # Compound interest
    result = calc.calculate_compound_interest(1000, 0.05, 3)
    print(f"Compound interest for $1000 at 5% for 3 years = ${result}")



def demonstrate_string_processor():
    print("\n=== String Processor Demo ===")
    processor = StringProcessor()
    
    # Reverse words
    text = "Hello World Python"
    result = processor.reverse_words(text)
    print(f"Original: {text}")
    print(f"Reversed words: {result}")
    
    # Word frequency
    text = "hello world hello python world world"
    result = processor.count_word_frequency(text)
    print(f"\nWord frequency in '{text}':")
    for word, count in result.items():
        print(f"  {word}: {count}")
    
    # Find palindromes
    text = "madam level python deed stats"
    result = processor.find_palindromes(text)
    print(f"\nPalindromes in '{text}': {result}")

def demonstrate_random_operations():
    print("\n=== Random Operations Demo ===")

    # Generate random integer
    rand_int = random.randint(1, 100)
    print(f"Random integer between 1 and 100: {rand_int}")

    # Choose random element from a list
    my_list = ['apple', 'banana', 'cherry', 'date']
    rand_choice = random.choice(my_list)
    print(f"Random choice from {my_list}: {rand_choice}")

    # Shuffle a list
    print(f"Original list: {my_list}")
    random.shuffle(my_list)
    print(f"Shuffled list: {my_list}")

    # Generate random float
    rand_float = random.random() # 0.0 <= x < 1.0
    print(f"Random float between 0.0 and 1.0: {rand_float:.2f}")

def demonstrate_priority_queue():
    print("\n=== Priority Queue Demo ===")
    pq = CustomPriorityQueue(max_size=5)
    
    # Add items with priorities
    items = [
        ("Task 1", 3),
        ("Task 2", 1),
        ("Task 3", 4),
        ("Task 4", 2),
        ("Task 5", 5)
    ]
    
    print("Adding items to priority queue:")
    for item, priority in items:
        success = pq.push(item, priority)
        print(f"  Added {item} with priority {priority}: {'Success' if success else 'Failed'}")
    
    print("\nProcessing items in priority order:")
    while not pq.is_empty():
        item = pq.pop()
        if item:
            print(f"  Processing: {item[0]} (Priority: {item[1]})")

def main():
    print("Welcome to the Python Examples Demo!")
    
    demonstrate_calculator()
    demonstrate_string_processor()
    demonstrate_priority_queue()
    demonstrate_random_operations()

if __name__ == "__main__":
    main()
