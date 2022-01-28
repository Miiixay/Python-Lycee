class Tree(object):
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None

    def getDepth(self, root, depth=0):
        if root == None:
            return depth
        return max(self.getDepth(root.left, depth + 1), self.getDepth(root.right, depth + 1))

    def size(self):
        leftSize = self.left.size() if self.left else 0
        rightSize = self.right.size() if self.right else 0
        return leftSize + 1 + rightSize

    def getSousArbre(self, treeWanted):
        rightTree = treeWanted.right.data if treeWanted.right != None else "None"
        leftTree = treeWanted.left.data if treeWanted.left != None else "None"
        return treeWanted.data + " = " + rightTree + " " + leftTree

    def parcourir(self, tree):
        trees = []
        if tree:
            trees = self.parcourir(tree.left)
            trees.append(tree.data)
            trees = trees + self.parcourir(tree.right)
        return trees

    def find(self, tree, value, pos=[]):
        if tree == None:
            return

        pos.append(tree.data)

        if tree.data == value:
            return pos, pos.index(value)

        return list(filter(None, (self.find(tree.right, value, pos), self.find(tree.left, value, pos))))


root = Tree()
root.data = "root"
root.left = Tree()
root.left.data = "left"
root.right = Tree()
root.right.data = "right"
root.right.right = Tree()
root.right.right.data = "a"

print(f'''
          {root.data}
        /      \      
      {root.left.data}    {root.right.data}
      / \       / \ 
  {root.left.left} {root.left.right}  {root.right.left} {root.right.right.data}
''')

print(root.getDepth(root))
print(root.size())
print(root.getSousArbre(root.right))
print(root.parcourir(root))
print(root.find(root, "a"))