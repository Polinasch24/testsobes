class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0


    def push(self, stack):
        self.stack.append(stack)

    def pop(self):
        if len(self.stack) == 0:
            return None
        removed = self.stack.pop()
        return removed

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

def balance_bracketes(expr):
    s=Stack()
    for i in range(len(expr)):
        if (expr[i] == '(' or
            expr[i] == '[' or
            expr[i] == '{'):
            s.push(expr[i])
            continue

        if s.isEmpty():
            return False

        if expr[i] == ')':
           x = s.pop();
           if (x == '{' or x == '['):
              return False
        elif expr[i] == '}':
           x = s.pop();
           if (x == '(' or x == '['):
                return False
        elif expr[i] == ']':
            x = s.pop();
            if (x == '(' or x == '{'):
                return False

    if s.isEmpty():
        return True
    else:
        return False

if __name__ == "__main__":
    expr = "{{[(])]}}";
    if (balance_bracketes(expr)):
        print("Balanced");
    else:
        print("Not Balanced")