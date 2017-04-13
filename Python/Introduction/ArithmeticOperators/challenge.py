
class ArithmeticOperator(object):
    def __init__(self):
        pass

    def sum(self, a, b):
        a = int(a)
        b = int(b)
        return a + b

    def subtract(self, a, b):
        a = int(a)
        b = int(b)
        return a - b

    def multiply(self, a, b):
        a = int(a)
        b = int(b)
        return a * b

if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())
    mathMachine = ArithmeticOperator()
    print mathMachine.sum(a,b)
    print mathMachine.subtract(a,b)
    print mathMachine.multiply(a,b)