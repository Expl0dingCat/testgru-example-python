import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from src.data_structures import CustomPriorityQueue

def test_priority_queue_push():
    pq = CustomPriorityQueue()
    assert pq.push("item1", 1) == True
    assert pq.push("item2", 2) == True
    assert pq.size() == 2

def test_priority_queue_max_size():
    pq = CustomPriorityQueue(max_size=2)
    assert pq.push("item1", 1) == True
    assert pq.push("item2", 2) == True
    assert pq.push("item3", 3) == False
    assert pq.size() == 2

def test_priority_queue_pop():
    pq = CustomPriorityQueue()
    pq.push("item1", 2)
    pq.push("item2", 1)
    pq.push("item3", 3)

    assert pq.pop() == ("item2", 1)
    assert pq.pop() == ("item1", 2)
    assert pq.pop() == ("item3", 3)
    assert pq.pop() is None

def test_priority_queue_peek():
    pq = CustomPriorityQueue()
    assert pq.peek() is None

    pq.push("item1", 2)
    pq.push("item2", 1)
    assert pq.peek() == ("item2", 1)
    assert pq.size() == 2  # Verify peek doesn't remove item

def test_priority_queue_clear():
    pq = CustomPriorityQueue()
    pq.push("item1", 1)
    pq.push("item2", 2)

    pq.clear()
    assert pq.size() == 0
    assert pq.is_empty() == True

def test_priority_queue_is_empty():
    pq = CustomPriorityQueue()
    assert pq.is_empty() == True

    pq.push("item", 1)
    assert pq.is_empty() == False

    pq.pop()
    assert pq.is_empty() == True

def test_priority_queue_size():
    pq = CustomPriorityQueue()
    assert pq.size() == 0

    pq.push("item1", 1)
    pq.push("item2", 2)
    assert pq.size() == 2

    pq.pop()
    assert pq.size() == 1

def test_priority_queue_is_full():
    pq = CustomPriorityQueue()  # No max size
    assert pq.is_full() == False

    pq2 = CustomPriorityQueue(max_size=2)
    assert pq2.is_full() == False

    pq2.push("item1", 1)
    pq2.push("item2", 2)
    assert pq2.is_full() == True

def test_priority_queue_ordering():
    pq = CustomPriorityQueue()
    items = [(5, "e"), (3, "c"), (1, "a"), (4, "d"), (2, "b")]

    for priority, item in items:
        pq.push(item, priority)

    expected = sorted(items, key=lambda x: x[0])
    result = []
    while not pq.is_empty():
        item = pq.pop()
        result.append((item[1], item[0]))

    assert result == expected

def test_priority_queue_with_duplicate_priorities():
    pq = CustomPriorityQueue()
    pq.push("item1", 1)
    pq.push("item2", 1)
    pq.push("item3", 1)

    assert pq.size() == 3
    assert pq.pop()[0] in ["item1", "item2", "item3"]

def test_priority_queue_with_negative_priorities():
    pq = CustomPriorityQueue()
    pq.push("item1", -5)
    pq.push("item2", -3)
    pq.push("item3", -1)

    assert pq.pop() == ("item1", -5)
    assert pq.pop() == ("item2", -3)
    assert pq.pop() == ("item3", -1)

def test_priority_queue_with_different_data_types():
    pq = CustomPriorityQueue()
    pq.push(42, 1)  # integer
    pq.push(3.14, 2)  # float
    pq.push(["list"], 3)  # list
    pq.push({"dict": 1}, 4)  # dict

    assert pq.size() == 4
    assert pq.pop()[0] == 42
