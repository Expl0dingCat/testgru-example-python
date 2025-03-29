from calculator import Calculator
from string_utils import StringProcessor
from data_structures import CustomPriorityQueue
import random
import time

def demonstrate_calculator():
    """
    Demonstrates the functionality of the Calculator class with various operations.
    Showcases basic arithmetic, series calculations, and financial functions.
    """
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
    
    # NEW: Statistical functions
    numbers = [4, 7, 2, 9, 3, 5, 8, 1, 6]
    mean = calc.calculate_mean(numbers)
    median = calc.calculate_median(numbers)
    std_dev = calc.calculate_standard_deviation(numbers)
    print(f"\nStatistical analysis of {numbers}:")
    print(f"  Mean: {mean}")
    print(f"  Median: {median}")
    print(f"  Standard Deviation: {std_dev}")

def demonstrate_string_processor():
    """
    Demonstrates the functionality of the StringProcessor class.
    Shows text manipulation capabilities including word reversal, 
    word frequency counting, and palindrome detection.
    """
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
    
    # NEW: Advanced text processing
    text = "The quick brown fox jumps over the lazy dog. It was the best of times, it was the worst of times."
    sentiment = processor.analyze_sentiment(text)
    print(f"\nSentiment analysis of '{text[:30]}...': {sentiment}")
    
    tokens = processor.tokenize_text(text)
    print(f"\nTokenized text (first 5 tokens): {tokens[:5]}")
    
    summarized = processor.summarize_text(text)
    print(f"\nText summary: '{summarized}'")

def demonstrate_priority_queue():
    """
    Demonstrates the functionality of the CustomPriorityQueue class.
    Shows how items are added with priorities and retrieved in priority order.
    """
    print("\n=== Priority Queue Demo ===")
    pq = CustomPriorityQueue(max_size=5)
    
    # Add items with priorities
    items = [
        ("Task 1", 3),  # Medium priority
        ("Task 2", 1),  # Lowest priority
        ("Task 3", 4),  # High priority
        ("Task 4", 2),  # Low priority
        ("Task 5", 5)   # Highest priority
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
    
    # NEW: Dynamic priority and batch operations
    print("\nDemonstrating dynamic priority queue:")
    dynamic_pq = CustomPriorityQueue(max_size=10, dynamic_priority=True)
    
    # Add items with initial priorities
    for i in range(1, 6):
        task_name = f"Dynamic Task {i}"
        priority = random.randint(1, 10)
        dynamic_pq.push(task_name, priority)
        print(f"  Added {task_name} with priority {priority}")
    
    # Update priorities
    dynamic_pq.update_priority("Dynamic Task 2", 12)
    dynamic_pq.update_priority("Dynamic Task 4", 15)
    print("\nAfter priority updates:")
    
    # Batch process top 3 items
    top_items = dynamic_pq.peek_batch(3)
    print(f"Top 3 items: {top_items}")
    
    # Process remaining items
    print("\nProcessing remaining items:")
    while not dynamic_pq.is_empty():
        item = dynamic_pq.pop()
        if item:
            print(f"  Processing: {item[0]} (Priority: {item[1]})")

def demonstrate_async_processing():
    """
    Demonstrates asynchronous task processing capabilities.
    Shows how tasks can be scheduled and executed with different priorities.
    """
    print("\n=== Async Processing Demo ===")
    
    # Create a task scheduler
    from task_scheduler import TaskScheduler
    scheduler = TaskScheduler()
    
    # Define some example tasks
    def task1():
        print("  Executing high priority task")
        time.sleep(0.1)
        return "High priority task complete"
    
    def task2():
        print("  Executing medium priority task")
        time.sleep(0.2)
        return "Medium priority task complete"
    
    def task3():
        print("  Executing low priority task")
        time.sleep(0.3)
        return "Low priority task complete"
    
    # Schedule tasks with different priorities
    scheduler.schedule(task1, priority=3)
    scheduler.schedule(task2, priority=2)
    scheduler.schedule(task3, priority=1)
    
    # Execute scheduled tasks
    print("\nExecuting scheduled tasks:")
    results = scheduler.execute_all()
    
    print("\nTask results:")
    for i, result in enumerate(results, 1):
        print(f"  Task {i}: {result}")

def main():
    """
    Main entry point for the demo application.
    Runs all demonstration functions to showcase various utility classes.
    """
    print("Welcome to the Python Examples Demo!")
    print("This program demonstrates several utility classes and their functionality.")
    
    demonstrate_calculator()
    demonstrate_string_processor()
    demonstrate_priority_queue()
    demonstrate_async_processing()

if __name__ == "__main__":
    main()
