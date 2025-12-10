# app.py
from fastapi import FastAPI, Form
from priority_queue import PriorityMessageQueue, Message  # <-- your module
import threading, time

app = FastAPI()
q = PriorityMessageQueue()

@app.post("/enqueue")
def enqueue(priority: int = Form(...), payload: str = Form(...)):
    q.enqueue(Message(priority, payload))
    return {"status": "enqueued", "priority": priority, "payload": payload}

@app.get("/dequeue")
def dequeue():
    msg = q.dequeue()
    if msg:
        return {"priority": msg.priority, "payload": msg.payload}
    return {"status": "queue empty"}


@app.get("/size")
def size():
    return {"size": q.size()}

def worker_loop():
    while True:
        msg = q.dequeue()
        if msg:
            print("Processing:", msg.payload)
        else:
            time.sleep(0.5)

# start background worker (daemon so process exits cleanly)
t = threading.Thread(target=worker_loop, daemon=True)
t.start()

