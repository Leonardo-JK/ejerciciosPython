class Stack:
    def __init__(self):
        self.__stk = []
        

    def push(self, val):
        self.__stk.append(val)

    def pop(self):
        val = self.__stk[-1]
        del self.__stk[-1]
        return val


class CountingStack(Stack):
    def __init__(self):
        self.__popOp = 0
        Stack.__init__(self)
    # Llena el constructor con acciones apropiadas.
    #

    def get_counter(self):
        return self.__popOp
    #
    # Presenta el valor actual del contador al mundo.
    #

    def pop(self):
        self.__popOp += 1
        return Stack.pop(self)
    #
    # Haz un pop y actualiza el contador.
    #
	

stk = CountingStack()
for i in range(100):
    stk.push(i)
    stk.pop()
print(stk.get_counter())
