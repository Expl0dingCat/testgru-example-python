from typing import Any, List, Optional, Tuple
from dataclasses import dataclass
import heapq

@dataclass
class PriorityQueueItem:
    priority: int
    data: Any
    
    def __lt__(self, other: 'PriorityQueueItem') -> bool:
        return self.priority < other.priority

class CustomPriorityQueue:
    """A priority queue implementation that maintains items with priorities."""
    
    def __init__(self, max_size: Optional[int] = None):
        self._items: List[PriorityQueueItem] = []
        self._max_size = max_size
        
    def push(self, item: Any, priority: int) -> bool:
        """
        Add an item with a priority to the queue.
        
        Returns:
            bool: True if the item was added, False if queue is full
        """
        if self._max_size and len(self._items) >= self._max_size:
            return False
            
        heapq.heappush(self._items, PriorityQueueItem(priority, item))
        return True
        
    def pop(self) -> Optional[Tuple[Any, int]]:
        """
        Remove and return the item with lowest priority.
        
        Returns:
            Tuple of (item, priority) or None if queue is empty
        """
        if not self._items:
            return None
            
        item = heapq.heappop(self._items)
        return (item.data, item.priority)
        
    def peek(self) -> Optional[Tuple[Any, int]]:
        """
        Return the item with lowest priority without removing it.
        
        Returns:
            Tuple of (item, priority) or None if queue is empty
        """
        if not self._items:
            return None
            
        item = self._items[0]
        return (item.data, item.priority)
        
    def clear(self) -> None:
        """Remove all items from the queue."""
        self._items.clear()
        
    def is_empty(self) -> bool:
        """Check if the queue is empty."""
        return len(self._items) == 0
        
    def size(self) -> int:
        """Return the current number of items in the queue."""
        return len(self._items)
        
    def is_full(self) -> bool:
        """Check if the queue is full (if max_size is set)."""
        return self._max_size is not None and len(self._items) >= self._max_size 