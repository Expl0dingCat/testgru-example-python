import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.data_structures import CustomPriorityQueue

def test_push_and_pop():
    pq = CustomPriorityQueue()
    assert pq.push("task1", 2)
    assert pq.push("task2", 1)
    assert pq.push("task3", 3)

    assert pq.pop() == ("task2", 1)
    assert pq.pop() == ("task1", 2)
    assert pq.pop() == ("task3", 3)
    assert pq.pop() is None

def test_peek():
    pq = CustomPriorityQueue()
    assert pq.peek() is None

    pq.push("task1", 2)
    pq.push("task2", 1)

    assert pq.peek() == ("task2", 1)
    assert pq.peek() == ("task2", 1)  # Verify peek doesn't remove item
    assert pq.size() == 2

def test_clear():
    pq = CustomPriorityQueue()
    pq.push("task1", 1)
    pq.push("task2", 2)

    assert pq.size() == 2
    pq.clear()
    assert pq.size() == 0
    assert pq.is_empty()

def test_is_empty():
    pq = CustomPriorityQueue()
    assert pq.is_empty()

    pq.push("task", 1)
    assert not pq.is_empty()

    pq.pop()
    assert pq.is_empty()

def test_size():
    pq = CustomPriorityQueue()
    assert pq.size() == 0

    pq.push("task1", 1)
    assert pq.size() == 1

    pq.push("task2", 2)
    assert pq.size() == 2

    pq.pop()
    assert pq.size() == 1

def test_max_size():
    pq = CustomPriorityQueue(max_size=2)

    assert pq.push("task1", 1)
    assert pq.push("task2", 2)
    assert not pq.push("task3", 3)  # Should fail as queue is full

    assert pq.size() == 2
    assert pq.is_full()

def test_priority_ordering():
    pq = CustomPriorityQueue()

    pq.push("task3", 3)
    pq.push("task1", 1)
    pq.push("task2", 2)

    assert pq.pop() == ("task1", 1)
    assert pq.pop() == ("task2", 2)
    assert pq.pop() == ("task3", 3)

def test_same_priority():
    pq = CustomPriorityQueue()

    pq.push("task1", 1)
    pq.push("task2", 1)

    result1 = pq.pop()
    result2 = pq.pop()

    assert result1[1] == result2[1] == 1
    assert {result1[0], result2[0]} == {"task1", "task2"}

def test_negative_priority():
    pq = CustomPriorityQueue()
    assert pq.push("task1", -1)
    assert pq.push("task2", -2)

    assert pq.pop() == ("task2", -2)
    assert pq.pop() == ("task1", -1)

def test_large_number_of_items():
    pq = CustomPriorityQueue()
    n = 1000

    for i in range(n-1, -1, -1):
        assert pq.push(f"task{i}", i)

    for i in range(n):
        assert pq.pop() == (f"task{i}", i)

def test_none_max_size():
    pq = CustomPriorityQueue(max_size=None)
    for i in range(100):
        assert pq.push(f"task{i}", i)
    assert pq.size() == 100
    assert not pq.is_full()

def test_push_and_peek_full_queue():
    pq = CustomPriorityQueue(max_size=1)
    assert pq.push("task1", 1)
    assert not pq.push("task2", 2)  # Queue is full, push should fail
    assert pq.peek() == ("task1", 1)

def test_push_when_full():
    pq = CustomPriorityQueue(max_size=3)
    assert pq.push("task1", 1)
    assert pq.push("task2", 2)
    assert pq.push("task3", 3)
    assert not pq.push("task4", 4)  # Queue is full
    assert pq.size() == 3
