import queue

# Create a priority queue
pq = queue.PriorityQueue()

# Enqueue items with priorities (priority, value)
pq.put((2, "Low Priority Task"))
pq.put((1, "High Priority Task"))
pq.put((3, "Very Low Priority Task"))

# Dequeue all items
while not pq.empty():
    priority, task = pq.get()
    print(f"Dequeued: {task} with priority {priority}")
