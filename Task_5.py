'''class Stack():
    def __init__(self, stackSize):
        self.stackSize = stackSize
        self.buffer = [None] * self.stackSize * 3
        self.stackPointer = [0, 0, 0]

    def push(self, stackNum, value):
        if self.stackPointer[stackNum] >= self.stackSize:
            print(f'Недостаточно места в стеке {stackNum}.')
        else:
            index = stackNum * self.stackSize + self.stackPointer[stackNum] + 1
            self.stackPointer[stackNum] += 1
            self.buffer[index] = value


    def pop(self, stackNum):
        if self.stackPointer[stackNum] == 0:
            print(f'Стек {stackNum} пустой!')

        else:
            index = stackNum * self.stackSize + self.stackPointer[stackNum]
            self.stackPointer[stackNum] -= 1
            value = self.buffer[index]
            self.buffer[index] = None
            return value


    def peek(self):
        pass
'''