import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.data_structures import CustomPriorityQueue, PriorityQueueItem

def test_priority_queue_push():
    pq = CustomPriorityQueue()
    assert pq.push("item1", 1) == True
    assert pq.size() == 1
    assert pq.peek() == ("item1", 1)

def test_priority_queue_push_multiple():
    pq = CustomPriorityQueue()
    pq.push("item1", 3)
    pq.push("item2", 1)
    pq.push("item3", 2)
    assert pq.size() == 3
    assert pq.peek() == ("item2", 1)

def test_priority_queue_pop():
    pq = CustomPriorityQueue()
    pq.push("item1", 2)
    pq.push("item2", 1)
    assert pq.pop() == ("item2", 1)
    assert pq.pop() == ("item1", 2)
    assert pq.pop() is None

def test_priority_queue_peek():
    pq = CustomPriorityQueue()
    assert pq.peek() is None
    pq.push("item1", 1)
    assert pq.peek() == ("item1", 1)
    pq.push("item2", 2)
    assert pq.peek() == ("item1", 1)

def test_priority_queue_clear():
    pq = CustomPriorityQueue()
    pq.push("item1", 1)
    pq.push("item2", 2)
    assert pq.size() == 2
    pq.clear()
    assert pq.size() == 0
    assert pq.is_empty()

def test_priority_queue_is_empty():
    pq = CustomPriorityQueue()
    assert pq.is_empty()
    pq.push("item", 1)
    assert not pq.is_empty()
    pq.pop()
    assert pq.is_empty()

def test_priority_queue_size():
    pq = CustomPriorityQueue()
    assert pq.size() == 0
    pq.push("item1", 1)
    assert pq.size() == 1
    pq.push("item2", 2)
    assert pq.size() == 2
    pq.pop()
    assert pq.size() == 1

def test_priority_queue_is_full():
    pq = CustomPriorityQueue(max_size=2)
    assert not pq.is_full()
    pq.push("item1", 1)
    assert not pq.is_full()
    pq.push("item2", 2)
    assert pq.is_full()
    assert not pq.push("item3", 3)

def test_priority_queue_with_max_size():
    pq = CustomPriorityQueue(max_size=2)
    assert pq.push("item1", 1)
    assert pq.push("item2", 2)
    assert not pq.push("item3", 3)
    assert pq.size() == 2
    assert pq.pop() == ("item1", 1)
    assert pq.push("item3", 3)
    assert pq.size() == 2

def test_priority_queue_same_priority():
    pq = CustomPriorityQueue()
    pq.push("item1", 1)
    pq.push("item2", 1)
    assert pq.size() == 2
    item1 = pq.pop()
    item2 = pq.pop()
    assert item1[1] == item2[1] == 1
