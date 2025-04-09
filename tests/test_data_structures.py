import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.data_structures import CustomPriorityQueue

# Test push and pop functionality
def test_push_pop():
    pq = CustomPriorityQueue()
    assert pq.push("item1", 2)
    assert pq.push("item2", 1)
    assert pq.push("item3", 3)

    assert pq.pop() == ("item2", 1)
    assert pq.pop() == ("item1", 2)
    assert pq.pop() == ("item3", 3)
    assert pq.pop() is None


# Test the peek method
def test_peek():
    pq = CustomPriorityQueue()
    assert pq.peek() is None

    pq.push("item1", 2)
    pq.push("item2", 1)

    assert pq.peek() == ("item2", 1)
    assert pq.peek() == ("item2", 1)  # Peek again to verify item not removed
    assert pq.size() == 2


# Test clearing the queue
def test_clear():
    pq = CustomPriorityQueue()
    pq.push("item1", 1)
    pq.push("item2", 2)

    assert pq.size() == 2
    pq.clear()
    assert pq.size() == 0
    assert pq.is_empty()


# Test is_empty method
def test_is_empty():
    pq = CustomPriorityQueue()
    assert pq.is_empty()

    pq.push("item", 1)
    assert not pq.is_empty()

    pq.pop()
    assert pq.is_empty()


# Test the queue size method
def test_size():
    pq = CustomPriorityQueue()
    assert pq.size() == 0

    pq.push("item1", 1)
    assert pq.size() == 1

    pq.push("item2", 2)
    assert pq.size() == 2

    pq.pop()
    assert pq.size() == 1


# Test the maximum size constraint
def test_max_size():
    pq = CustomPriorityQueue(max_size=2)

    assert pq.push("item1", 1)
    assert pq.push("item2", 2)
    assert not pq.push("item3", 3)  # Should fail as queue is full

    assert pq.size() == 2
    assert pq.is_full()


# Test priority ordering in the queue
def test_priority_ordering():
    pq = CustomPriorityQueue()

    pq.push("low", 1)
    pq.push("high", 3)
    pq.push("medium", 2)

    assert pq.pop() == ("low", 1)
    assert pq.pop() == ("medium", 2)
    assert pq.pop() == ("high", 3)


# Test handling items with the same priority
def test_same_priority():
    pq = CustomPriorityQueue()

    pq.push("first", 1)
    pq.push("second", 1)

    item1 = pq.pop()
    item2 = pq.pop()

    assert item1[1] == item2[1] == 1
    assert {item1[0], item2[0]} == {"first", "second"}


# Test handling different data types in the queue
def test_different_data_types():
    pq = CustomPriorityQueue()

    pq.push(42, 1)
    pq.push("string", 2)
    pq.push([1, 2, 3], 3)
    pq.push({"key": "value"}, 4)

    assert pq.pop() == (42, 1)
    assert pq.pop() == ("string", 2)
    assert pq.pop() == ([1, 2, 3], 3)
    assert pq.pop() == ({"key": "value"}, 4)


# Test the is_full method when no max size is set
def test_is_full_no_max_size():
    pq = CustomPriorityQueue()
    assert not pq.is_full()

    pq.push("item", 1)
    assert not pq.is_full()


# Test handling negative max size constraints
def test_negative_max_size():
    pq = CustomPriorityQueue(max_size=-1)
    assert not pq.push("item", 1)
    assert pq.is_full()
    assert pq.pop() is None
    assert pq.is_empty()


# Test pushing None as an item
def test_push_none():
    pq = CustomPriorityQueue()
    assert pq.push(None, 1)
    assert pq.pop() == (None, 1)


# Test max size edge cases
def test_max_size_edge_cases():
    pq = CustomPriorityQueue(max_size=1)
    assert pq.push("item1", 1)
    assert not pq.push("item2", 2)
    assert pq.pop() == ("item1", 1)
    assert pq.push("item2", 2)
