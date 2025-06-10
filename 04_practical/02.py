stack = []
print(type(stack))  

print(f"Initial stack: {stack}")

stack.append(150)
stack.append(100)
stack.append(50)
stack.append(10)

print(f"After pushing: {stack}")

if stack:
    popped_item = stack.pop()
    print(f"Popped item: {popped_item}")
else:
    print("Cannot pop stack is empty.")

print(f"Stack after pop: {stack}")

if stack:
    print(f"Top of stack: {stack[-1]}")
else:
    print("Stack is empty")

if len(stack) == 0:
    print("Is stack empty? Yes")
else:
    print("Is stack empty? No")

print("Stack contents (top to bottom):")
for item in reversed(stack):
    print(item)
