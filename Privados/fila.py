# Fifo

# Criando um tipo de estrutura abstrada de dados.

class Node:
    
    def __init__(self, value) -> None:
        self.value = value
        self.next: Node

    def __repr__(self) -> str:
        return f'{self.value}'

class Queue:
    
    def __init__(self) -> None:
        self.first = None
        self.last = None
        self._count = 0

    def push(self, node_value) -> None:
        new_node = Node(node_value)

        if self.first is None:
            self.first = new_node
        
        else:
            pass

        if self.last is None:
            self.last = new_node
        
        else:
            self.last.next = new_node
            self.last = new_node

        self._count += 1

    def pop(self) -> Node:
        
        if self.first is None:
            return 'Lista vazia!!!'
        
        else:
            first = self.first
            self.first = self.first.next
            self._count -= 1
        
        return first

    def peek(self) -> Node:
        
        if self.first is None:
            return 'Lista Vazia!!!'
        
        else:
            return self.first

    def __len__(self) -> int:
        return self._count

    def __repr__(self) -> str:
        
        if self.first is None:
            
            return 'Lista Vazia!!!'
        
        else:
            pass
        
        return f'Valores = ({self.first}, {self.last})'
    
if __name__ == '__main__':
    fila = Queue()

    fila.push(10)
    fila.push(15)
    fila.push(30)

    print(fila)

    print(fila.pop())

    print(fila.__repr__())
