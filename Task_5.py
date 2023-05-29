class Stack():
    def __init__(self, stackSize):
        self.stackSize = stackSize
        self.buffer = [None] * self.stackSize * 3
        self.stackPointer = [-1, -1, -1]

    def push(self, stackNum, value):
        if stackNum != 0 and stackNum != 1 and stackNum != 2:
            raise IndexError("Неверный номер стека")


        if self.stackPointer[stackNum] >= self.stackSize:
            print(f'Недостаточно места в стеке {stackNum}.')

        else:
            index = stackNum * self.stackSize + self.stackPointer[stackNum] + 1
            self.stackPointer[stackNum] += 1
            self.buffer[index] = value


    def pop(self, stackNum):

        if stackNum != 0 and stackNum != 1 and stackNum != 2:
            raise IndexError("Неверный номер стека")

        if self.stackPointer[stackNum] == -1:
            return f'Стек {stackNum} пустой!'

        else:
            index = stackNum * self.stackSize + self.stackPointer[stackNum]
            self.stackPointer[stackNum] -= 1
            value = self.buffer[index]
            self.buffer[index] = None
            return value


    def peek(self, stackNum):

        if stackNum != 0 and stackNum != 1 and stackNum != 2:
            raise IndexError("Неверный номер стека")

        if self.stackPointer[stackNum] == -1:
            return f'Стек {stackNum} пустой!'

        else:
            index = stackNum * self.stackSize + self.stackPointer[stackNum]

            return self.buffer[index]





stack = Stack(10)
stack.push(0, 3)
stack.push(1, 15)
stack.push(0, 2)
stack.push(2, 13)
stack.push(1, 3)
print(stack.buffer)
print(stack.pop(1))
print(stack.pop(2))
print(stack.pop(0))
print(stack.pop(0))
print(stack.peek(0))
print(stack.peek(1))
print(stack.peek(2))
print(stack.buffer)













