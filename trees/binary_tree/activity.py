class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
    
    def __str__(self):
        return str(self.data)
    
class BinaryTree:
    def __init__(self, data=None):
        if data:
            node = Node(data)
            self.root = node
        else:
            self.root = None
    
    def simetric_traversal(self, node = None):
        if node is None:
            node = self.root
        if node.left:
            print('(', end="")
            self.simetric_traversal(node.left)
        print(node, end = '')
        if node.right:
            self.simetric_traversal(node.right)
            print(')', end="")
    
n = int(input())
root = input()

lista =[]
for i in range(n-1):
    lista.append(input().split())
    lista[i][0] = Node(lista[i][0])

print(lista)

tree = BinaryTree(root)

for i in range(n-1):
    

    if lista[i][2] == 'e':
        tree.root.left = lista[1]
        
    if lista[i][2] == 'd':
        tree.root.right = lista[1]