import queue

# Create a FIFO queue
q = queue.Queue()

# Enqueue elements
q.put(10)
q.put(20)
q.put(30)

# Check size of queue
print("Size of queue:", q.qsize())

# Peek at the front element (no direct method, but we can dequeue and put back)
# So instead, we demonstrate basic dequeue
print("Dequeued:", q.get())
print("Dequeued:", q.get())

# Check if queue is empty
print("Is queue empty?", q.empty())

# Enqueue more elements
q.put(40)
q.put(50)

# Dequeue remaining
while not q.empty():
    print("Dequeued:", q.get())
