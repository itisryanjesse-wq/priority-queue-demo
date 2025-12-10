# priority_queue.py
import heapq
import itertools
from typing import Any

_counter = itertools.count()  # tie-breaker to preserve FIFO for same-priority

class Message:
    def __init__(self, priority: int, payload: Any):
        self.priority = int(priority)
        self.payload = payload

    def __repr__(self):
        return f"Message(priority={self.priority}, payload={self.payload!r})"

class PriorityMessageQueue:
    def __init__(self):
        self._heap = []

    def enqueue(self, message: Message):
        # Use (priority, tie-breaker, message) so that:
        # - smaller priority is popped first
        # - messages with same priority are FIFO by insertion order
        entry = (message.priority, next(_counter), message)
        heapq.heappush(self._heap, entry)

    def dequeue(self) -> Message | None:
        if not self._heap:
            return None
        _, _, message = heapq.heappop(self._heap)
        return message

    def peek(self) -> Message | None:
        if not self._heap:
            return None
        return self._heap[0][2]

    def is_empty(self) -> bool:
        return len(self._heap) == 0

    def size(self) -> int:
        return len(self._heap)
