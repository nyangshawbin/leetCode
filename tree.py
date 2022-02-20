import sys
# class

class Node:
    def __init__(self, item):
        self.left = None
        self.right = None
        self.val = item

def inorder(root):

    if root:
        # Traverse left
        inorder(root.left)
        # Traverse root
        print(str(root.val) + "->", end='')
        # Traverse right
        inorder(root.right)

# Code execution starts here
if __name__=='__main__':


    #               1
    #              / \
    #             2   3
    #            / \
    #           4   5

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print("Inorder traversal ")
    inorder(root)


    sys.exit() #replace return in main function