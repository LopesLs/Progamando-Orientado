LIFO = 'Last in first out, Último a entrar será o primeiro a sair'

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:

    def __init__(self):
        self.high = None
        self.size = 0

    def push(self, value) -> None:
        node = Node(value)
        node.next = self.high
        self.high = node
        self.size += 1

    def pop(self) -> Node:
        
        if self.high is None:
            return 'Lista vazia, não se pode usar o pop()'

        else:
            pass
        
        node = self.high
        self.high = self.high.next

        self.size -= 1
        
        return node.value

    def peek(self) -> Node:
        
        if self.high is None:
            return 'A lista está vazia, não se pode usar o peek()'
        
        else:
            return self.high.value
    
    def __len__(self) -> int:
        return self.size

    
    def __repr__(self) -> str:
        if self.high is None:
            return 'Lista Vazia'
        
        else:
            r = ''
            pointer = self.high
            
            while (pointer):
                r = r + str(pointer.value) + '\n'
                pointer = pointer.next
            
            return r


if __name__ == '__main__':
    pilha = Stack()

    pilha.push('Carlos')
    pilha.push(15)
    pilha.push(True)
    pilha.push('Sucesso!')
    pilha.push(1.70)

    print(pilha)

    pilha.pop()
    pilha.pop()

    print(pilha.peek())