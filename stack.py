# Stack using Python List

stack = []

# Push elements
stack.append(10)
stack.append(20)
stack.append(30)

print("Stack after pushing:", stack)

# Peek at top element
print("Top element:", stack[-1])

# Pop element
popped = stack.pop()
print("Popped element:", popped)
print("Stack after popping:", stack)

# Check if stack is empty
print("Is stack empty?", len(stack) == 0)

# Size of stack
print("Size of stack:", len(stack))
