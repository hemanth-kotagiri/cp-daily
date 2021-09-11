# Implement stack and each method should run in constant time

class Stack:
    def __init__(self):
        self.max = None
        self.stack = []

    def push(self, item):
        if self.max == None or self.max < item:
            self.max = item
        self.stack.append(item)

    def pop(self):
        if self.stack:
            self.stack.pop()
        else:
            print("Underflow")

    def max_elem(self):
        return None if self.max == None else self.max


def main():

    obj = Stack()
    obj.pop()
    obj.pop()
    obj.pop()
    obj.pop()
    obj.push(-10)
    obj.push(-15)
    print(obj.max_elem())
    obj.push(-20)
    obj.push(-200)
    print(obj.max_elem())


if __name__ == "__main__":
    main()
