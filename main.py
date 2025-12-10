# main.py
import time
from priority_queue import PriorityMessageQueue, Message

def process_message(msg: Message):
    # Replace this with real processing
    print(f"[PROCESS] priority={msg.priority} payload={msg.payload}")

if __name__ == "__main__":
    q = PriorityMessageQueue()

    # enqueue some messages (lower number = higher priority)
    q.enqueue(Message(4, "Not important task"))
    q.enqueue(Message(2, "urgent task"))
    q.enqueue(Message(3, "normal task"))
    q.enqueue(Message(1, "very urgent task"))

    while not q.is_empty():
        msg = q.dequeue()
        process_message(msg)
        time.sleep(0.3)

    print("All messages have been processed.")
