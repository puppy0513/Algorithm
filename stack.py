stack =[]

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(4)
stack.append(6)
stack.append(7)
stack.append(8)
stack.append(9)

stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack)
print(stack[::-1])